from fastapi.testclient import TestClient
from app.main import app
from fastapi.templating import Jinja2Templates

import pathlib


BASE_DIR = pathlib.Path(__file__).parent

client = TestClient(app)

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


def test_get_home():
    response = client.get("/")

    # tests
    assert response.status_code == 200

    assert "<!DOCTYPE html>" in response.text
    assert "<html" in response.text  # This will match <html lang="en">
