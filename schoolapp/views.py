from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import redirect, render



def new(request):

    return render(request,"index.html")


