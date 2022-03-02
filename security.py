import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from config import FASTAPI_USERNAME, FASTAPI_PASSWORD

security = HTTPBasic()


def get_current_username(
    credentials: HTTPBasicCredentials = Depends(security),
):
    correct_username = secrets.compare_digest(
        credentials.username, FASTAPI_USERNAME
    )
    correct_password = secrets.compare_digest(
        credentials.password, FASTAPI_PASSWORD
    )
    if not (correct_username and correct_password):

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username