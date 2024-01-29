from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.db import ALL_COLUMNS, addresses
from src.models.address_models import Address, AddressResponse, AddressResponseList

router = APIRouter()


@router.post('/addresses',
             response_model=Address,
             summary="Creates a new address and returns inserted row.",
             tags=["addresses"])
def create_address(address: Address) -> JSONResponse:
    result = addresses.insert().values(**address.dict()).returning(ALL_COLUMNS).execute().first()
    return JSONResponse(status_code=status.HTTP_201_CREATED,
                        content=f"Added address successfully: {result}")


@router.patch('/addresses/{address_id}',
              response_model=AddressResponse,
              summary="Updates row where UUID equals address_id provided, if it exists.",
              tags=["addresses"])
def update_address(address_id: UUID, address: Address) -> JSONResponse:
    updated_address = addresses.update().\
        where(addresses.c.address_id == address_id).\
        values(**address.dict(exclude_none=True)).\
        returning(ALL_COLUMNS).execute().first()

    if not updated_address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No address was found with input id: {address_id}.")

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=f"Updated address: {updated_address}")


@router.get('/addresses/{address_id}',
            response_model=AddressResponse,
            summary="Return address information by providing an existing address ID.",
            tags=["addresses"])
def get_address(address_id) -> JSONResponse:
    address = addresses.select().where(addresses.c.address_id == address_id).execute().first()
    if not address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with id: {address_id} not found.")
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=jsonable_encoder(AddressResponse(**dict(address))))


@router.get('/addresses',
            response_model=AddressResponseList,
            summary="Returns list of AddressResponse.",
            tags=["addresses"])
def get_addresses() -> JSONResponse:
    result = addresses.select().execute().fetchall()

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Was not able to retrieve addresses.")

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=jsonable_encoder(AddressResponseList(addresses=result)))


@router.delete('/addresses/{address_id}',
               response_model=UUID,
               summary="Deletes row where UUID equals address_id provided, if it exists.",
               tags=["addresses"])
def delete_address(address_id: UUID) -> JSONResponse:
    result = addresses.delete().where(addresses.c.address_id == address_id).execute().rowcount
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No address was found with input id: {address_id}.")

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=f"Deleted address with id: {address_id}")
