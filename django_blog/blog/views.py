from django.views.generic import CreateView, UpdateView
from .forms import UserCreationForm, UpdateUserForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


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
