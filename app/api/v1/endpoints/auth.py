from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import create_access_token, verify_password, hash_password
from app.schemas.token import Token

router = APIRouter()


PUBLISHER_USERNAME = "publisher"
PUBLISHER_HASH = hash_password("secret")  

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != PUBLISHER_USERNAME or not verify_password(form_data.password, PUBLISHER_HASH):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": create_access_token(PUBLISHER_USERNAME), "token_type": "bearer"}