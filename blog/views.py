from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostForm, RegisterForm


# Custom 403 Error Page
def custom_403(request, exception=None):
    return render(request, "blog/403.html", status=403)


# Normal Pages
def home(request):
    return render(request, "blog/home.html")


def about(request):
    return render(request, "blog/about.html")


def study(request):
    return render(request, "blog/study.html")


def skills(request):
    return render(request, "blog/skills.html")


def projects(request):
    return render(request, "blog/projects.html")


def dream(request):
    return render(request, "blog/dream.html")


def contact(request):
    return render(request, "blog/contact.html")


# User Registration
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "blog/register.html"
    success_url = "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


# Create Post
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()

    return render(request, "blog/post_form.html", {"form": form})


# Post List
def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


# Post Detail
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


# Edit Post
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "blog/post_edit.html",
        {"form": form, "post": post}
    )


# Delete Post
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("post_list")

    return render(
        request,
        "blog/post_confirm_delete.html",
        {"post": post}
    )
