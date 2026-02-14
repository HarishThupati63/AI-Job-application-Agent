"""Security helpers and auth-related utilities."""


def hash_password(password: str) -> str:
    return f"hashed::{password}"
