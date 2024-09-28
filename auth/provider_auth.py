import flet as ft
from flet.auth.providers import GoogleOAuthProvider, GitHubOAuthProvider
import os
from loguru import logger

GITHUB_CLIENT_ID = os.getenv("githubClientId")
GITHUB_CLIENT_SECRET = os.getenv("githubClientSecret")
GITHUB_URL = os.getenv("redirectUrlGithub")
GOOGLE_URL = os.getenv("redirecUrltGoogle")


def login_google(page: ft.Page):
    pass


def login_github(page: ft.Page):
    provider = GitHubOAuthProvider(
        client_id=GITHUB_CLIENT_ID,
        client_secret=GITHUB_CLIENT_SECRET,
        redirect_url=GOOGLE_URL
    )
    page.login(provider)
