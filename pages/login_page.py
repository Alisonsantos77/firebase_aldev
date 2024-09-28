import asyncio

import flet as ft
from auth.firebase_auth import sign_in_email_password
from auth.provider_auth import login_github
from loguru import logger


def LoginPage(page: ft.Page):
    new_avatar = ft.Ref[ft.CircleAvatar]()

    def generator_avatar(e):
        if not input_username.value:
            new_avatar.current.foreground_image_src = "https://robohash.org/userdefault.png"
            new_avatar.current.content = ft.Text("", size=30, weight=ft.FontWeight.BOLD)
        else:
            new_avatar.current.foreground_image_src = f"https://robohash.org/{input_username.value}.png"
            new_avatar.current.content = ft.Text(input_username.value[0].upper(), size=30, weight=ft.FontWeight.BOLD)
        new_avatar.current.update()

    # Função de login
    def login_user(e):
        email = input_username.value
        password = input_senha.value
        result = sign_in_email_password(email, password)
        if isinstance(result, dict):
            print("Login realizado com sucesso!")
            page.go("/home")
            for key, value in result.items():
                print(f"{key}: {value}")
            return result
        else:
            logger.error(f"Erro ao realizar login: {result}")
            return None

    async def loading():
        loading_icon = ft.AlertDialog(
            content=ft.Container(
                content=ft.ProgressRing(),
                alignment=ft.alignment.center,
            ),
            bgcolor=ft.colors.TRANSPARENT,
            modal=True,
            disabled=True,
        )
        page.open(loading_icon)
        await asyncio.sleep(3)
        page.close(loading_icon)

    async def acess_github(e):
        try:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Entrando com Github..."),
                bgcolor=ft.colors.BLUE,
                action="OK",
            )
            page.snack_bar.open = True
            page.update()

            login_github(page)

            page.snack_bar.content = ft.Text("Login com Github bem-sucedido! Redirecionando...")
            page.snack_bar.bgcolor = ft.colors.GREEN
            page.snack_bar.update()

            await loading()
            page.go("/home")

        except Exception as error:
            page.snack_bar.content = ft.Text(f"Erro ao acessar Github: {error}")
            page.snack_bar.bgcolor = ft.colors.RED
            page.snack_bar.open = True
            page.update()
            logger.error(f"Erro ao acessar Github: {error}")

    avatar = ft.Container(
        content=ft.Row(
            controls=[
                ft.CircleAvatar(
                    foreground_image_src="https://robohash.org/userdefault.png",
                    content=ft.Text("FF"),
                    width=100,
                    height=100,
                    ref=new_avatar
                )
            ]
        ),
        col={"sm": 5, "md": 4, "xl": 12},
    )

    # Campos de entrada de dados
    input_username = ft.TextField(
        hint_text='Insira seu email',
        col={"sm": 8, "md": 12, "xl": 5},
        on_change=generator_avatar,
        border=ft.InputBorder.UNDERLINE,
    )

    input_senha = ft.TextField(
        hint_text='Insira sua senha',
        password=True,
        border=ft.InputBorder.UNDERLINE,
        max_lines=1,
        max_length=20,
        can_reveal_password=True,
        col={"sm": 8, "md": 12, "xl": 5},
    )

    login_button = ft.ElevatedButton(
        text="Acessar conta",
        style=ft.ButtonStyle(
            padding=ft.padding.all(10),
            bgcolor={ft.ControlState.HOVERED: ft.colors.WHITE},
            color={
                ft.ControlState.DEFAULT: ft.colors.WHITE,
                ft.ControlState.HOVERED: ft.colors.BLACK,
            },
            elevation={"pressed": 0, "": 1},
            animation_duration=500,
            shape=ft.RoundedRectangleBorder(radius=6),
        ),
        col={"sm": 8, "md": 10, "xl": 6},
        on_click=login_user,
    )

    github_btn = ft.ElevatedButton(
        text="Entrar com Github",
        style=ft.ButtonStyle(
            padding=ft.padding.all(10),
            bgcolor={ft.ControlState.HOVERED: ft.colors.WHITE},
            color={
                ft.ControlState.DEFAULT: ft.colors.WHITE,
                ft.ControlState.HOVERED: ft.colors.BLACK,
            },
            elevation={"pressed": 0, "": 1},
            animation_duration=500,
            shape=ft.RoundedRectangleBorder(radius=6),
        ),
        col={"sm": 8, "md": 10, "xl": 6},
        on_click=acess_github
    )

    google_btn = ft.ElevatedButton(
        text="Entrar com Google",
        style=ft.ButtonStyle(
            padding=ft.padding.all(10),
            bgcolor={ft.ControlState.HOVERED: ft.colors.WHITE},
            color={
                ft.ControlState.DEFAULT: ft.colors.WHITE,
                ft.ControlState.HOVERED: ft.colors.BLACK,
            },
            elevation={"pressed": 0, "": 1},
            animation_duration=500,
            shape=ft.RoundedRectangleBorder(radius=6),
        ),
        col={"sm": 8, "md": 10, "xl": 6},
        on_click=lambda _: print('Entrar com Google')
    )

    return ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                ft.ResponsiveRow(
                    col={"sm": 10, "md": 4, "xl": 12},
                    controls=[
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[avatar]
                                ),
                                ft.Text(
                                    value="Bem-vindo de volta!",
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                    size=20,
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                    col={"sm": 5, "md": 4, "xl": 12},
                                ),
                            ]
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    col={"sm": 10, "md": 12, "xl": 12},
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        input_username,
                        input_senha,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=[ft.TextButton(
                                text='Esqueceu sua senha?',
                                icon_color=ft.colors.BLACK12,
                                col={"sm": 8, "md": 12, "xl": 12},
                                on_click=lambda _: print('Resetar senha')
                            )]
                        ),
                        login_button,
                        github_btn,
                        google_btn
                    ],
                    run_spacing={"xs": 10},
                ),
            ],
            spacing=20
        )
    )
