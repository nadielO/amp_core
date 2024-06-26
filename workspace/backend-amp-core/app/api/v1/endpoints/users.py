from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user import User, UserCreate, UserUpdate
from app.services.crud_user import create_user, get_user, update_user, delete_user, get_user_by_email
from app.api.deps import get_db
from fastapi.security import OAuth2PasswordBearer
from app.core.jwt import verify_token

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED, dependencies=[Depends(oauth2_scheme)])
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

@router.get("/{user_id}", response_model=User, dependencies=[Depends(oauth2_scheme)])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=User, dependencies=[Depends(oauth2_scheme)])
def update_user_endpoint(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db=db, user_id=user_id, user=user)

@router.delete("/{user_id}", response_model=User, dependencies=[Depends(oauth2_scheme)])
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db=db, user_id=user_id)