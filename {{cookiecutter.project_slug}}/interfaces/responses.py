from fastapi import status
from fastapi.responses import JSONResponse

UNAUTHORIZED = JSONResponse(content="Unauthorized",
                            status_code=status.HTTP_401_UNAUTHORIZED)

BAD_REQUEST = JSONResponse(content="Bad Request",
                           status_code=status.HTTP_400_BAD_REQUEST)

NOT_FOUND = JSONResponse(content="Error: Not found!",
                         status_code=status.HTTP_404_NOT_FOUND)

INTERNAL_SERVER_ERROR = JSONResponse(
    content="Error: Internal error",
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

HELLO_WORLD = JSONResponse(content={"message": "Hello, World!"},
                           status_code=status.HTTP_200_OK)
