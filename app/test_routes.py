from fastapi.testclient import TestClient
import pytest
from .main import app


client = TestClient(app)


# V1 - /activities
@pytest.mark.v1
def test_v1_route_activities_group_7_error_message():
    response = client.get("/api/v1/activities?group=7")
    assert response.status_code == 200
    assert response.json() == [{"error": "O parâmetro (group) deve ser de 1 á 4"}]

@pytest.mark.v1
def test_v1_route_activities_group_4_without_activities():
    group = 4
    response = client.get(f"/api/v1/activities?group={group}")
    assert response.status_code == 200
    assert response.json() == [{"error": f"Não há atividades para o grupo {group}"}]

@pytest.mark.v1
def test_v1_route_activites_group_1_return_values():
    group = 1
    response = client.get(f"/api/v1/activities?group={group}")
    assert response.status_code == 200
    assert response.json() != [{"error": f"Não há atividades para o grupo {group}"}]
    assert response.json() != [{"error": "O parâmetro (group) deve ser de 1 á 4"}]
    assert isinstance(response.json(), list)



# V2 - /activities
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



# V2 - /activities/auth
@pytest.mark.v2
def test_v2_activities_auth_doesnt_pass_parameters():
    response = client.get("/api/v2/activities/auth")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}

@pytest.mark.v2
def test_v2_activities_auth_error_message():
    response = client.get("/api/v2/activities/auth", auth=("010620005", "123456"))
    assert response.status_code == 200
    assert response.json() == [{"error": "Matricula ou senha incorretos"}]

@pytest.mark.v2
def test_v2_activities_auth_return_values():
    response = client.get("/api/v2/activities/auth", auth=("010620005", "7946852"))	    
    assert response.status_code == 200
    assert response.json() != [{"error": "Matricula ou senha incorretos"}]
    assert isinstance(response.json(), list)