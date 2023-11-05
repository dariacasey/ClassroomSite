from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .models import Lesson, Exercise, ExerciseSet, StudentScore
from classes.models import Class
from accounts.models import Profile


def get_user_type(user):
    try:
        user_profile = user.profile
        if user_profile.is_student:
            return 'student'
        elif user_profile.is_teacher:
            return 'teacher'
    except Profile.DoesNotExist:
        return 'unknown'  # Handle cases where the user has no profile
    return 'unknown'


# Displays list of lessons to pick from
class AllLessons(ListView):
    model = Lesson
    template_name = "lessons/all_lessons.html"


# Pull up page with individual Lesson on it. Not questions
class LessonDetail(DetailView):
    model = Lesson
    template_name = 'lessons/lesson_detail.html'


# Displays questions
def view_lesson_exercises(request, pk):
    lesson = Lesson.objects.get(pk=pk)
    exercises = Exercise.objects.filter(lesson=lesson)
    user = request.user

    if StudentScore.objects.filter(student=user, exercise_set=lesson.exerciseset_set.first()).count() >= 3:
        message = "Quiz attempt limit reached. You cannot attempt this quiz again."
        context = {'lesson': lesson, 'message': message}
        return render(request, 'lessons/exercises.html', context)

    context = {'lesson': lesson, 'exercises': exercises}
    return render(request, 'lessons/exercises.html', context)


def grade_exercises(request, pk):
    if request.method == 'POST':
        lesson = Lesson.objects.get(pk=pk)
        user = request.user
        exercise_set = lesson.exerciseset_set.first()

        if StudentScore.objects.filter(student=user, exercise_set=exercise_set).count() >= 3:
            message = "Quiz attempt limit reached. You cannot attempt this quiz again."
            context = {'lesson': lesson, 'message': message}
            return render(request, 'lessons/exercises.html', context)

        exercises = Exercise.objects.filter(lesson=lesson)
        total_score = 0

        for exercise in exercises:
            answer_key = str(exercise.correct_answer)
            user_answer = request.POST.get(f'exercise_{exercise.id}')

            if user_answer == answer_key:
                total_score += 1

        percentage_score = (total_score / len(exercises)) * 100

        student_score = StudentScore.objects.create(
            student=request.user, exercise_set=lesson.exerciseset_set.first(), score=percentage_score, final_score=percentage_score
        )

        return redirect('progress_page')

    return redirect('lessons/lesson_detail', lesson_id=pk)


# Initially had two different views for teacher and student grades. Decided to have one "grades" link and to just call
# different views based on user type
def grades_view(request):
    user = request.user
    user_type = get_user_type(user)
    print(user_type)
    if user_type == 'teacher':
        # Call the teacher-specific view
        return teacher_progress(request)
    else:
        # Call the student-specific view
        return progress_page(request)


def progress_page(request):
    user = request.user
    exercise_sets = ExerciseSet.objects.filter(lesson__exerciseset__studentscore__student=user).distinct()

    lesson_scores = []

    for exercise_set in exercise_sets:
        lesson = exercise_set.lesson
        # ordered in reverse to show first attempts
        scores = StudentScore.objects.filter(exercise_set=exercise_set, student=user)

        final_score = scores.last().final_score if scores else 0
        lesson_scores.append({
            'lesson': lesson,
            'final_score': final_score,
            'scores': scores,
        })

    context = {'lesson_scores': lesson_scores}
    return render(request, 'lessons/progress_page.html', context)


def teacher_progress(request):
    teacher_classes = Class.objects.filter(teacher=request.user)
    lessons = Lesson.objects.filter(lesson_class__in=teacher_classes)
    class_students = User.objects.filter(classes__in=teacher_classes).distinct()

    lesson_scores = []

    for lesson in lessons:
        exercise_set = ExerciseSet.objects.filter(lesson=lesson).first()

        student_scores = []
        final_scores = []

        for student in class_students:
            scores = StudentScore.objects.filter(
                student=student,
                exercise_set=exercise_set,
            ).order_by('id')

            if scores:
                # Get the final score from the last attempt
                final_score = scores.last().final_score
                final_scores.append({
                    'student': student,
                    'final_score': final_score,
                })

            student_scores.append({
                'student': student,
                'scores': scores,
            })

        lesson_scores.append({
            'lesson': lesson,
            'student_scores': student_scores,
            'final_scores': final_scores,
        })

    context = {'lesson_scores': lesson_scores}
    return render(request, 'lessons/teacher_progress.html', context)
