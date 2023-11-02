from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy
from .forms import CommentForm, PostForm
from accounts.models import Profile
from lessons.models import Lesson


class HomePage(ListView):
    model = Post
    template_name = 'home/home_page.html'

    # Passes post count
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get anonymous user error if not
        if self.request.user.is_authenticated:
            user = self.request.user

            # Passes post count in context
            post_count_context = self.get_post_count(user)
            context.update(post_count_context)

        return context

    # gets post count (might be able to combine both functions in future if there's time)
    def get_post_count(self, user):
        try:
            user_profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            user_profile = None

        if user_profile and user_profile.is_student:
            post_count = Post.objects.filter(class_field__students=user).count()
        elif user_profile and user_profile.is_teacher:
            post_count = Post.objects.filter(class_field__teacher=user).count()
        else:
            post_count = 0

        return {'post_count': post_count}

    # Only display posts from classmates/teacher
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            user_profile = user.profile
        else:
            user_profile = None

        if user_profile and user_profile.is_student:
            return Post.objects.filter(class_field__students=user).order_by('-date_created')
        elif user_profile and user_profile.is_teacher:
            return Post.objects.filter(class_field__teacher=user).order_by('-date_created')
        else:
            return Post.objects.none()


class ArticleDetail(DetailView):
    model = Post
    template_name = 'home/article_detail.html'

    # Does post views
    def get_object(self, queryset=None):
        post = super().get_object(queryset=queryset)

        post.views += 1
        post.save()

        return post


class AddPostView(CreateView):
    model = Post
    template_name = "home/add_post.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user

        # Fixed Anonymous User error
        try:
            user_profile = self.request.user.profile
        except AttributeError:
            user_profile = None

        if user_profile:
            form.instance.class_field = user_profile.class_field

        return super().form_valid(form)


class EditPostView(UpdateView):
    model = Post
    template_name = "home/edit_post.html"
    fields = ['title', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = "home/delete_post.html"
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "home/add_comment.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


def search_view(request):
    user = request.user
    user_type = get_user_type(user)

    if request.method == "POST":
        searched = request.POST['searched']
        if user_type == 'student':
            post = Post.objects.filter(class_field__students=user, title__contains=searched)
            comment = Comment.objects.filter(body__contains=searched)
            lesson = Lesson.objects.filter(title__contains=searched)
            results = []
            for post in post:
                post.type = 'post'
                results.append(post)

            for comment in comment:
                comment.type = 'comment'
                results.append(comment)

            for lesson in lesson:
                lesson.type = 'lesson'
                results.append(lesson)
        elif user_type == 'teacher':
            post = Post.objects.filter(class_field__teacher=user, title__contains=searched)
            comment = Comment.objects.filter(body__contains=searched)
            lesson = Lesson.objects.filter(title__contains=searched)
            results = list(post) + list(comment) + list(lesson)
            print(results)
        return render(request, 'home/search.html', {'searched': searched, 'results': results})
    else:
        return render(request, 'home/search.html', {})


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