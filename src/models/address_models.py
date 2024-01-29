from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, constr


class Address(BaseModel):
    zip_code: constr(regex=r"^(\d{5}|\d{5}[-]\d{4})$") = None
    state: int = None
    street: str = None
    house_num: int = None


class AddressResponse(BaseModel):
    address_id: UUID
    zip_code: str
    state: int
    street: str
    house_num: int
    created_at: datetime
    updated_at: datetime


class AddressResponseList(BaseModel):
    addresses: List[AddressResponse]
