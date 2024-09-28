from auth.firebase_config import auth


def sign_in_email_password(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user
    except Exception as e:
        return str(e)


def sign_up_email_password(email, password):
    try:
        auth.create_user_with_email_and_password(email, password)
        return "Usuário criado com sucesso!"
    except Exception as e:
        return str(e)


def send_password_reset(email):
    try:
        auth.send_password_reset_email(email)
        return "Instruções de redefinição de senha enviadas por email!"
    except Exception as e:
        return str(e)


def confirm_password_reset(oob_code, new_password):
    try:
        auth.confirm_password_reset(oob_code, new_password)
        return "Senha redefinida com sucesso!"
    except Exception as e:
        return str(e)


def sign_out():
    try:
        auth.current_user = None
        return "Logout realizado com sucesso"
    except Exception as e:
        return str(e)
