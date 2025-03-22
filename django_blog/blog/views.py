from django.views.generic import CreateView
from .forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


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
