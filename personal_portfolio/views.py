from django.shortcuts import render, redirect
from personal_portfolio.forms import LoginForm


def login(request):
    context = {'form': LoginForm()}
    return render(request, "project_index.html", context)

