from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Repository
from .tasks import fetch_github_repos

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fetch_github_repos.delay(username)
        return redirect('result')
    return render(request, 'githubapi/index.html')


def result(request):
    repos = Repository.objects.all()
    processing = repos.count() == 0
    return render(request, 'githubapi/result.html', {'repos': repos, 'processing': processing})


