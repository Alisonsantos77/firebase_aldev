import flet as ft
from loguru import logger


def RegisterPage(page: ft.Page):
    new_avatar = ft.Ref[ft.CircleAvatar]()

    def generator_avatar(e):
        if not input_username.value:
            new_avatar.current.foreground_image_src = "https://robohash.org/userdefault.png"
            new_avatar.current.content = ft.Text("A", size=30, weight=ft.FontWeight.BOLD)
        else:
            new_avatar.current.foreground_image_src = f"https://robohash.org/{input_username.value}.png"
            new_avatar.current.content = ft.Text(input_username.value[0].upper(), size=30, weight=ft.FontWeight.BOLD)
        new_avatar.current.update()

    avatar = ft.Container(
        content=ft.Row(
            controls=[
                ft.CircleAvatar(
                    foreground_image_src="https://robohash.org/userdefault.png",
                    content=ft.Text("A", size=30, weight=ft.FontWeight.BOLD),
                    width=100,
                    height=100,
                    ref=new_avatar
                )
            ]
        ),
        col={"sm": 5, "md": 4, "xl": 12},
    )

    def login_redirect(e):
        page.go('/login')

    input_username = ft.TextField(
        hint_text='Insira seu nome de usuário',
        col={"sm": 12, "md": 10, "xl": 8},
        on_change=generator_avatar,
        border=ft.InputBorder.UNDERLINE,
        max_lines=1,
        max_length=20,
    )
    input_email = ft.TextField(
        hint_text='Insira seu email',
        col={"sm": 12, "md": 10, "xl": 8},
        border=ft.InputBorder.UNDERLINE,
        max_lines=1,
        max_length=35,
    )

    input_senha = ft.TextField(
        hint_text='Crie uma senha',
        password=True,
        border=ft.InputBorder.UNDERLINE,
        max_lines=1,
        max_length=20,
        can_reveal_password=True,
        col={"sm": 12, "md": 10, "xl": 8},
    )
    input_senha_confirm = ft.TextField(
        hint_text='Confirme sua senha',
        password=True,
        border=ft.InputBorder.UNDERLINE,
        max_lines=1,
        max_length=20,
        can_reveal_password=True,
        col={"sm": 12, "md": 10, "xl": 8},
    )

    have_account = ft.TextButton(
        text='Já possui uma conta?',
        col={"sm": 8, "md": 12, "xl": 12},
        style=ft.ButtonStyle(
            color={
                ft.ControlState.DEFAULT: ft.colors.WHITE,
                ft.ControlState.HOVERED: ft.colors.BLACK,
            },
            elevation=2,
            overlay_color=ft.colors.TRANSPARENT,

        ),
        on_click=login_redirect
    )

    async def validate_input(e):
        if len(input_senha.value) < 6:
            input_senha.border_color = ft.colors.RED
            input_senha.color = ft.colors.RED
            input_senha.error_text = "A senha deve ter no mínimo 6 caracteres"
        else:
            input_senha.border_color = ft.colors.GREEN
            input_senha.color = ft.colors.GREEN
            input_senha.error_text = ""

        input_senha.update()

        # Verificar se as senhas coincidem
        if input_senha_confirm.value != input_senha.value:
            input_senha_confirm.border_color = ft.colors.RED
            input_senha_confirm.color = ft.colors.RED
            input_senha_confirm.error_text = "As senhas não coincidem"
        else:
            input_senha_confirm.border_color = ft.colors.GREEN
            input_senha_confirm.color = ft.colors.GREEN
            input_senha_confirm.error_text = ""

        input_senha_confirm.update()

    submit_btn = ft.ElevatedButton(
        text="Cadastrar",
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
    )

    return ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Container(
            padding=ft.padding.symmetric(vertical=10, horizontal=40),
            border_radius=ft.border_radius.all(10),
            blur=ft.Blur(sigma_x=8, sigma_y=8),
            margin=5,
            bgcolor=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            border=ft.Border(
                top=ft.BorderSide(width=2, color=ft.colors.WHITE30),
                right=ft.BorderSide(width=2, color=ft.colors.WHITE30),
            ),
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
                                    ft.ResponsiveRow(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                alignment=ft.alignment.center,
                                                content=ft.Text(
                                                    value="Crie sua conta AlDev",
                                                    size=22,
                                                    color=ft.colors.WHITE,
                                                    weight=ft.FontWeight.BOLD,
                                                ),
                                                padding=5,
                                                col={"sm": 5, "md": 4, "xl": 12},
                                            ),
                                            ft.Container(
                                                alignment=ft.alignment.center,
                                                content=ft.Text(
                                                    value="Acesse todos os apps AlDev com uma única conta.",
                                                    size=16,
                                                    color=ft.colors.GREY_300,
                                                    weight=ft.FontWeight.NORMAL,
                                                    overflow=ft.TextOverflow.ELLIPSIS,
                                                ),
                                                padding=5,
                                                col={"sm": 6, "md": 4, "xl": 12},
                                            ),
                                        ],
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
                            input_email,
                            input_senha,
                            input_senha_confirm,
                            submit_btn,
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[have_account]
                            ),
                        ],
                        run_spacing={"xs": 5},
                    ),
                ],
                spacing=5
            )
        )
    )
