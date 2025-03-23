from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView,
)
from .forms import UserCreationForm, UpdateUserForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "blog/register.html"


@login_required(login_url="/blog/login/")
def profile_view(request):
    # This view can only be accessed by authenticated users
    return render(request, "blog/profile.html")


def logout_view(request):
    logout(request)
    return render(request, "blog/logout.html")


def update_profile(request, pk):

    user = get_object_or_404(User, id=pk)
    user = User.objects.get(id=pk)
    form = UpdateUserForm(request.POST, instance=user)
    if request.method == "POST":
        user.email = request.POST.get("email")
        user.username = request.POST.get("username")
        user.save()
        return HttpResponseRedirect("/blog/profile/")
    else:
        form = UpdateUserForm(instance=user)
    context = {"form": form, "user": user}
    return render(request, "blog/update_profile.html", context)


class UpdateProfileView(UpdateView):
    model = User
    template_name = "blog/update_profile.html"
    fields = ["first_name", "last_name", "username", "email"]
    success_url = reverse_lazy("profile")


# Use Django’s class-based views to handle CRUD operations:


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    paginate_by = 10
    template_name = "blog/post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_details.html"


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_update_form.html"

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse_lazy("posts-details", args=[self.get_object().id])


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("posts")

    def test_func(self):
        return self.get_object().author == self.request.user


class CommentCreateView(LoginRequiredMixin, CreateView):
    pass


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.get_object().author == self.request.user


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    def test_func(self):
        return self.get_object().author == self.request.user
