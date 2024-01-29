from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from src.main import app

client = TestClient(app)


def test_get_user(mocker: MockerFixture, return_id, return_user_json_response):
    mock_sel = mocker.patch('src.routers.users_controllers.select')
    mock_sel.return_value.select_from.return_value.where.return_value.\
        execute.return_value.first.return_value = return_user_json_response

    response = client.get(f'/users/{return_id}')
    assert response.status_code == 200
    assert mock_sel.called


def test_get_user_bad_id(mocker: MockerFixture, return_id):
    mock_sel = mocker.patch('src.routers.users_controllers.select')
    mock_sel.return_value.select_from.return_value.where.return_value.\
        execute.return_value.first.return_value = None

    response = client.get(f'/users/{return_id}')
    assert response.status_code == 404
    assert mock_sel.called


def test_get_users(mocker: MockerFixture, return_user_json_response_list):
    mock_sel = mocker.patch('src.routers.users_controllers.select')
    mock_sel.return_value.select_from.return_value.execute.return_value.\
        fetchall.return_value = return_user_json_response_list

    response = client.get('/users')
    assert response.status_code == 200
    assert mock_sel.called


def test_create_user(mocker: MockerFixture, return_new_user):
    mock_user = mocker.patch('src.routers.users_controllers.users')
    mock_user.insert.return_value.values.return_value.returning.return_value.\
        execute.return_value.first.return_value = return_new_user

    response = client.post('/users', json=jsonable_encoder(return_new_user))
    assert response.status_code == 201
    assert mock_user.insert.called


def test_delete_user(mocker: MockerFixture, return_id):
    mock_user = mocker.patch('src.routers.users_controllers.users')
    mock_user.delete.return_value.where.return_value.execute.return_value.rowcount = 1

    response = client.delete(f'/users/{return_id}')
    assert response.status_code == 200
    assert mock_user.delete.called


def test_delete_bad_user(mocker: MockerFixture, return_id):
    mock_user = mocker.patch('src.routers.users_controllers.users')
    mock_user.delete.return_value.where.return_value.execute.return_value.rowcount = 0

    response = client.delete(f'/users/{return_id}')
    assert response.status_code == 404
    assert mock_user.delete.called


def test_update_user(mocker: MockerFixture, return_id, return_user_to_update):
    mock_user = mocker.patch('src.routers.users_controllers.users')
    mock_user.update.return_value.where.return_value.values.return_value.returning.return_value.\
        execute.return_value.first.return_value = return_user_to_update

    response = client.patch(f'/users/{return_id}', json=jsonable_encoder(return_user_to_update))
    assert response.status_code == 200
    assert mock_user.update.called


def test_update_bad_user(mocker: MockerFixture, return_id, return_user_to_update):
    mock_user = mocker.patch('src.routers.users_controllers.users')
    mock_user.update.return_value.where.return_value.values.return_value.returning.return_value.\
        execute.return_value.first.return_value = None

    response = client.patch(f'/users/{return_id}', json=return_user_to_update)
    assert response.status_code == 404
    assert mock_user.update.called
