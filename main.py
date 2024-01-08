# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

import flet as ft
from flet.auth.providers import GitHubOAuthProvider

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
assert GITHUB_CLIENT_ID, "set GITHUB_CLIENT_ID environment variable"
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
assert GITHUB_CLIENT_SECRET, "set GITHUB_CLIENT_SECRET environment variable"


def main(page: ft.Page):
    provider = GitHubOAuthProvider(
        client_id=GITHUB_CLIENT_ID,
        client_secret=GITHUB_CLIENT_SECRET,
        redirect_url="http://localhost:8550/api/oauth/redirect",
    )

    def login_click(e):
        page.login(provider)

    def on_login(e):
        print("Login error:", e.error)
        print("Access token:", page.auth.token.access_token)
        print("User ID:", page.auth.user.id)

    page.on_login = on_login
    page.add(ft.ElevatedButton("Login with GitHub", on_click=login_click))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ft.app(target=main, port=8550, view=ft.WEB_BROWSER)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
