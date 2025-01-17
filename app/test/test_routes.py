import os
import pytest
from app.main import app
from fastapi.testclient import TestClient
from dotenv import load_dotenv


load_dotenv()
client = TestClient(app)

AUTH_MATRICULA = os.getenv("AUTH_MATRICULA")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD")



# v2 - /activities
@pytest.mark.v2
def test_v2_activities_group_7_error_message():
    response = client.get("/api/v2/activities?group=7")
    assert response.status_code == 200
    assert response.json() == [{"error": "O parâmetro (group) deve ser de 1 á 4"}]

@pytest.mark.v2
def test_v2_activities_group_4_without_activities():
    group = 4
    response = client.get(f"/api/v2/activities?group={group}")
    assert response.status_code == 200
    assert response.json() == [{"error": f"Não há atividades para o grupo {group}"}]

@pytest.mark.v2
def test_v2_activities_group_1_return_values():
    group = 1
    response = client.get(f"/api/v2/activities?group={group}")
    assert response.status_code == 200
    assert response.json() != [{"error": f"Não há atividades para o grupo {group}"}]
    assert response.json() != [{"error": "O parâmetro (group) deve ser de 1 á 4"}]
    assert isinstance(response.json(), list)



# v2 - /activities/auth
@pytest.mark.v2
def test_v2_activities_auth_doesnt_pass_parameters():
    response = client.get("/api/v2/activities/auth")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}

@pytest.mark.v2
def test_v2_activities_auth_error_message():
    response = client.get("/api/v2/activities/auth", auth=("123456", "123456"))
    assert response.status_code == 200
    assert response.json() == [{"error": "Matricula ou senha incorretos"}]

@pytest.mark.v2
def test_v2_activities_auth_return_values():
    response = client.get("/api/v2/activities/auth", auth=(AUTH_MATRICULA, AUTH_PASSWORD))
    assert response.status_code == 200
    assert response.json() != [{"error": "Matricula ou senha incorretos"}]
    assert isinstance(response.json(), list)