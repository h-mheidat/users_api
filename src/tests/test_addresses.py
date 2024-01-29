from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from src.main import app

client = TestClient(app)


def test_get_address(mocker: MockerFixture, return_id, return_address_json_response):
    mock_address = mocker.patch('src.routers.addresses_controllers.addresses')
    mock_address.select.return_value.where.return_value.execute.return_value\
        .first.return_value = return_address_json_response

    response = client.get(f'/addresses/{return_id}')
    assert response.status_code == 200
    assert response.json() == return_address_json_response
    assert mock_address.select.called


def test_get_address_bad_id(mocker: MockerFixture, return_id):
    mock_address = mocker.patch('src.routers.addresses_controllers.addresses')
    mock_address.select.return_value.where.return_value.execute\
        .return_value.first.return_value = None

    response = client.get(f'/addresses/{return_id}')
    assert response.status_code == 404
    assert mock_address.select.called


def test_get_addresses(mocker: MockerFixture, return_address_json_response_list):
    mock_address = \
        mocker.patch('src.routers.addresses_controllers.addresses')
    mock_address.select.return_value.execute.return_value\
        .fetchall.return_value = return_address_json_response_list

    response = client.get('/addresses')
    assert response.status_code == 200
    assert mock_address.select.called


def test_create_address(mocker: MockerFixture, return_new_address):
    mock_address = mocker.patch('src.routers.addresses_controllers.addresses')
    mock_address.insert.return_value.values.return_value.returning.return_value\
        .execute.return_value.first.return_value = return_new_address

    response = client.post('/addresses', json=jsonable_encoder(return_new_address))
    assert response.status_code == 201
    assert mock_address.insert.called


def test_delete_address(mocker: MockerFixture, return_id):
    mock_address = mocker.patch('src.routers.addresses_controllers.addresses')
    mock_address.delete.return_value.where.return_value.execute.return_value.rowcount = 1

    response = client.delete(f'/addresses/{return_id}')
    assert response.status_code == 200
    assert mock_address.delete.called


def test_delete_bad_address(mocker: MockerFixture, return_id):
    mock_address = mocker.patch('src.routers.addresses_controllers.addresses')
    mock_address.delete.return_value.where.return_value.execute.return_value.rowcount = 0

    response = client.delete(f'/addresses/{return_id}')
    assert response.status_code == 404
    assert mock_address.delete.called


def test_update_address(mocker: MockerFixture, return_id, return_address_to_update):
    mock_address = mocker.patch('src.routers.addresses_controllers.addresses')
    mock_address.update.return_value.values.return_value.returning.return_value\
        .execute.return_value.first.return_value = return_address_to_update

    response = client.patch(f'/addresses/{return_id}',
                            json=jsonable_encoder(return_address_to_update))
    assert response.status_code == 200
    assert mock_address.update.called


def test_update_address_not_found(mocker: MockerFixture, return_id, return_address_to_update):
    mock_address = mocker.patch('src.routers.addresses_controllers.addresses')
    mock_address.update.return_value.where.return_value.values.return_value\
        .returning.return_value.execute.return_value.first.return_value = None

    response = client.patch(f'/addresses/{return_id}', json=return_address_to_update)
    assert response.status_code == 404
    assert mock_address.update.called
