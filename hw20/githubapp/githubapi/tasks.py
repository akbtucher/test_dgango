import requests
from celery import shared_task
from .models import Repository

@shared_task
def fetch_github_repos(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            name = repo['name']
            stars = repo['stargazers_count']
            Repository.objects.create(name=name, stars=stars)
    else:
        raise Exception('Failed to fetch Github repos')
