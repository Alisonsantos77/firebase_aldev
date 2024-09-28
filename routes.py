import flet as ft
from pages.login_page import LoginPage
from loguru import logger
from pages.register_page import RegisterPage


def setup_routes(page: ft.Page):
    logger.info("Configurando rotas")
    page.theme = ft.Theme(
        page_transitions={'windows': ft.PageTransitionTheme.FADE_UPWARDS}
    )

    def route_change(route):
        logger.info(f"Rota alterada: {route}")
        page.views.append(
            ft.View(
                route="/login",
                appbar=ft.AppBar(),

                controls=[
                    LoginPage(page)
                ],
            )
        )
        logger.info("Página de Login do Usuário carregada")
        if page.route == '/register':
            page.views.append(
                ft.View(
                    route="/register",
                    appbar=ft.AppBar(),
                    controls=[
                        RegisterPage(page)
                    ],
                )
            )
            # Página Home
        elif page.route == "/home":
            page.views.append(
                ft.View(
                    route="/home",
                    appbar=ft.AppBar(),
                    controls=[
                        ft.Text("Bem-vindo à página Home!"),
                    ],
                )
            )
            logger.info("Página Home carregada")

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        logger.info(f"Retornando para a rota anterior: {top_view.route}")
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
