import os

import httpx

from .consts import OIDC_TOKEN_ENDPOINT


def get_env_credentials():
    email, password = os.environ.get("SYSTEMAIR_AUTH_EMAIL"), os.environ.get("SYSTEMAIR_AUTH_PASSWORD")

    if not (email and password):
        raise EnvironmentError("`SYSTEMAIR_AUTH_EMAIL` and `SYSTEMAIR_AUTH_PASSWORD` environment variables must be set")

    return email, password


async def oidc_password_auth(email, password):
    api_endpoint = OIDC_TOKEN_ENDPOINT

    data = {
        "grant_type": "password",
        "username": email,
        "password": password,
        "client_id": "iot-application",
        "scope": "openid email profile"
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = httpx.post(api_endpoint, data=data, headers=headers)
    tokens = response.json()
    return tokens
