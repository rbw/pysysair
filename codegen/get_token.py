import asyncio
import sys

from pysysair.auth import oidc_password_auth, get_env_credentials


async def get_access_token():
    credentials = get_env_credentials()
    tokens = await oidc_password_auth(*credentials)
    return tokens["access_token"]


if __name__ == '__main__':
    token = asyncio.run(get_access_token())
    sys.stdout.write(token)
    sys.exit(0)
