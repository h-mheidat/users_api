from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from src.routers import addresses_controllers, users_controllers

app = FastAPI()
app.include_router(users_controllers.router)
app.include_router(addresses_controllers.router)


@app.exception_handler(IntegrityError)
def integrity_error_handler(request: Request, exc: IntegrityError) -> JSONResponse:
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                        content={"Message": f"{base_error_message}.", "Detail": f"{exc.args}"})
