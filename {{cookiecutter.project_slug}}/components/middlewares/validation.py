from itertools import zip_longest
from typing import Optional

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from interfaces.responses import UNAUTHORIZED


class AuthorizedHeaderTokenMiddleware(BaseHTTPMiddleware):

    def __init__(self, app, secret_token: str):
        super(AuthorizedHeaderTokenMiddleware, self).__init__(app)
        self.secret_token = secret_token

    def __constant_time_string_compare(self, source: str, target: str) -> bool:
        res: bool = True
        for x, y in zip_longest(source, target, fillvalue=None):
            res = res and (x == y)
        return res

    async def dispatch(self, request: Request, call_next):
        # do something with the request object, for example
        provided_token: Optional[str] = request.headers.get('Token')
        assert provided_token is not None
        assert isinstance(provided_token, str)
        if self.__constant_time_string_compare(
                source=provided_token, target=self.secret_token) is False:
            return UNAUTHORIZED
        # process the request and get the response
        response = await call_next(request)
        return response
