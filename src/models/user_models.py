from datetime import date, datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, EmailStr, confloat, validator


class User(BaseModel):
    name: str = None
    date_of_birth: date = None
    email: EmailStr = None
    height: confloat(gt=140.0, le=200) = None
    weight: confloat(gt=40, le=250) = None
    address_id: UUID = None
    favourite_color: int = None

    @validator('name')
    def name_must_be_capital(cls, value: str):
        return value.strip().upper()

    @validator('email')
    def email_must_be_capital(cls, value):
        return value.strip().upper()


class UserResponse(BaseModel):
    user_id: UUID
    name: str
    date_of_birth: date
    email: str
    height: float
    weight: float
    address_id: UUID
    created_at: datetime
    updated_at: datetime
    favourite_color: int
    zip_code: str
    state: int
    street: str
    house_num: int
    adr_created: datetime
    adr_updated: datetime


class UserResponseList(BaseModel):
    users: List[UserResponse]
