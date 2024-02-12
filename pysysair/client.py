from .graphql import Client
from .auth import oidc_password_auth, get_env_credentials
from .consts import GRAPHQL_URL


class SystemairClient(Client):
    def __init__(self, credentials=None):
        self.credentials = credentials or get_env_credentials()
        super(SystemairClient, self).__init__(GRAPHQL_URL)

    async def authenticate(self):
        return await oidc_password_auth(*self.credentials)

    async def _execute_json(self, *args, **kwargs):
        tokens = await self.authenticate()
        return await super(SystemairClient, self)._execute_json(
            *args,
            headers={"x-access-token": tokens["access_token"]},
            **kwargs
        )

    async def get_devices(self):
        for _, item in await self.get_all_devices():
            yield item
