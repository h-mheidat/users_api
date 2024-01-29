
from typing import Optional
from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.sql import select

from src.db import ALL_COLUMNS, addresses, users
from src.models.user_models import User, UserResponse, UserResponseList

router = APIRouter()


@router.get('/users/{user_id}',
            response_model=UserResponse,
            summary="Return user information by providing an existing user ID.",
            tags=["users"])
def get_user(user_id: UUID) -> JSONResponse:
    clmns = [
        users,
        addresses.c.zip_code,
        addresses.c.state,
        addresses.c.street,
        addresses.c.house_num,
        addresses.c.created_at.label("adr_created"),
        addresses.c.updated_at.label("adr_updated")
    ]
    user = select(clmns).select_from(users.join(addresses, isouter=True)
                                     ).where(users.c.user_id == user_id).execute().first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {user_id} not found.")

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=jsonable_encoder(UserResponse(**user)))


@router.get('/users',
            response_model=UserResponseList,
            summary="Returns list of UserResponse. Returns all users if 'name' param equals None.",
            tags=["users"])
def get_users(name: Optional[str] = None) -> JSONResponse:
    clmns = [
        users,
        addresses.c.zip_code,
        addresses.c.state,
        addresses.c.street,
        addresses.c.house_num,
        addresses.c.created_at.label("adr_created"),
        addresses.c.updated_at.label("adr_updated")
    ]
    result = None
    if name:
        result = select(clmns).select_from(users.join(addresses, isouter=True))\
            .where(users.c.name.ilike(f"%{name}%")).execute().fetchall()
    else:
        result = select(clmns).select_from(users.join(addresses, isouter=True))\
            .execute().fetchall()

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Was not able to retrieve users.")

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=jsonable_encoder(UserResponseList(users=result)))


@router.post('/users',
             response_model=User,
             summary="Creates a new user and returns inserted row.",
             tags=["users"])
def create_user(user: User) -> JSONResponse:
    result = users.insert().values(**user.dict()).returning(ALL_COLUMNS).execute().first()
    return JSONResponse(status_code=status.HTTP_201_CREATED,
                        content=f"Added user successfully: {result}")


@router.delete('/users/{user_id}',
               response_model=UUID,
               summary="Deletes row where UUID equals user_id provided, if it exists.",
               tags=["users"])
def delete_user(user_id: UUID) -> JSONResponse:
    result = users.delete().where(users.c.user_id == user_id).execute().rowcount
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No user was found with input id: {user_id}.")

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=f"Deleted user with id: {user_id}")


@router.patch('/users/{user_id}',
              response_model=UserResponse,
              summary="Updates row where UUID equals user_id provided, if it exists.",
              tags=["users"])
def update_user(user_id: UUID, user: User) -> JSONResponse:
    updated_user = users.update().\
        where(users.c.user_id == user_id).\
        values(**user.dict(exclude_none=True)).\
        returning(ALL_COLUMNS).execute().first()
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No user was found with input id: {user_id}.")

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=f"Updated user: {updated_user}")
