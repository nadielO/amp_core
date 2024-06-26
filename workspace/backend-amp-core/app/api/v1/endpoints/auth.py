from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.jwt import create_access_token
from app.schemas.user import User, UserInDB
from app.services.crud_user import get_user_by_email
from app.api.deps import get_db
from app.core.security import verify_password
from pydantic import BaseModel
import logging

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

class Login(BaseModel):
    username: str
    password: str

@router.post("/login", response_model=Token)
def login_for_access_token(form_data: Login, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        logging.error(f"Login failed for user: {form_data.username}")
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    logging.info(f"Token generated for user: {user.username}")
    return {"access_token": access_token, "token_type": "bearer"}