from django.urls import path
from .views import LessonDetail, AllLessons
from . import views


urlpatterns = [
    path('lesson/<int:pk>/', LessonDetail.as_view(), name='lesson_detail'),
    path('lesson/<int:pk>/questions', views.view_lesson_exercises, name='lesson_exercises'),
    path('progress/', views.grades_view, name='progress_page'),
    path('', AllLessons.as_view(), name="all_lessons"),
    path('lesson/<int:pk>/grade/', views.grade_exercises, name='grade_exercises'),

]
