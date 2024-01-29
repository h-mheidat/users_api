import pytest

from src.models.address_models import Address
from src.models.user_models import User


@pytest.fixture
def return_id():
    return "75c5180c-c214-11eb-8529-0242ac130003"  # random UUID generated online


@pytest.fixture
def return_user_json_response():
    return {
        "user_id": "75c5180c-c214-11eb-8529-0242ac130003",
        "name": "TEST USER",
        "date_of_birth": "2021-05-31",
        "email": "TEST@USER.COM",
        "height": 156,
        "weight": 250,
        "address_id": "f8de1993-d056-42c5-bb3b-5b58c3efd1a0",
        "created_at": "2021-05-31T13:25:32.307285",
        "updated_at": "2021-06-01T10:05:16.424223",
        "favourite_color": 1,
        "zip_code": "12345-1234",
        "state": 1,
        "street": "st-12345",
        "house_num": 123,
        "adr_created": "2021-05-31T13:24:51.417367",
        "adr_updated": "2021-05-31T13:24:51.417375"}


@pytest.fixture
def return_user_json_response_list():
    return [{
        "user_id": "75c5180c-c214-11eb-8529-0242ac130003",
        "name": "NAME",
                "date_of_birth": "2021-06-02",
                "email": "TEST@USER.COM",
                "height": 170,
                "weight": 180,
                "address_id": "75c5180c-c214-11eb-8529-0242ac130003",
                "created_at": "2021-06-02T11:39:34.051Z",
                "updated_at": "2021-06-02T11:39:34.051Z",
                "favourite_color": 1,
                "zip_code": "11111-1111",
                "state": 2,
                "street": "string",
                "house_num": 1,
                "adr_created": "2021-06-02T11:39:34.051Z",
                "adr_updated": "2021-06-02T11:39:34.051Z"
    }]


@pytest.fixture
def return_new_user():
    user = User(
        name="Test User 1",
        email="Test1@User.com",
        date_of_birth="2021-06-01",
        height=200,
        weight=250,
        address_id="f8de1993-d056-42c5-bb3b-5b58c3efd1a0",
        favourite_color=1
    )
    return user


@pytest.fixture
def return_user_to_update():
    user = User(
        height=170
    )
    return user.dict(exclude_none=True)


@pytest.fixture
def return_address_json_response():
    return {
        "address_id": "75c5180c-c214-11eb-8529-0242ac130003",
        "zip_code": "12345-1234",
        "state": 1,
        "street": "st-12345",
        "house_num": 123,
        "created_at": "2021-05-31T13:24:51.417367",
        "updated_at": "2021-05-31T13:24:51.417375"}


@pytest.fixture
def return_address_json_response_list():
    return [
        {
            "address_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "zip_code": "string",
            "state": 0,
            "street": "string",
            "house_num": 0,
            "created_at": "2021-06-02T10:09:05.729Z",
            "updated_at": "2021-06-02T10:09:05.729Z"
        }
    ]


@pytest.fixture
def return_new_address():
    return Address(
        zip_code="12345-1234",
        state=1,
        street="st-1",
        house_num=3
    )


@pytest.fixture
def return_address_to_update():
    address = Address(
        house_num=1
    )
    return address.dict(exclude_none=True)
