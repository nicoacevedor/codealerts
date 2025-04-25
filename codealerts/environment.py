from getpass import getpass
from pathlib import Path
from typing import Dict

from dotenv import dotenv_values, set_key


def check_env() -> None:
    env_file = Path().resolve() / ".notification_credentials"
    if not env_file.exists():
        create_env(env_file)
    print(f"Using credentials from {env_file}")


def load_env() -> Dict[str, str]:
    env_file = Path().resolve() / ".notification_credentials"
    env_values = dotenv_values(env_file)
    return env_values


def create_env(env_file: Path) -> None:
    email, password = '', ''
    while email == '' or password == '':
        print("Credentials setting:")
        email = input("Email: ")
        password_user = getpass()
        confirm_password = getpass("Confirm password: ")
        while password_user != confirm_password:
            print("Incorrect password")
            password_user = getpass()
            confirm_password = getpass("Confirm password: ")
        password = password_user
    env_file.touch(mode=0o600, exist_ok=False)
    set_key(
        dotenv_path=env_file,
        key_to_set="EMAIL",
        value_to_set=email
    )
    set_key(
        dotenv_path=env_file,
        key_to_set="PASSWORD",
        value_to_set=password
    )
    print("Credentials set!")
