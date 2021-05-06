import pytest
from appserver import app as flask_app

@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_slash(app, client):
    tryassert = client.get("/")
    assert tryassert.status_code == 302


def test_cowsay(app, client):
    collect = "Complete!!"
    tryassert = client.get("/cowsay/%s/" % collect)
    assert tryassert.status_code == 200
    realconnect = tryassert.get_data(as_text=True)
    assert collect in realconnect


def test_fortune(app, client):
    tryassert = client.get("/fortune/")
    assert tryassert.status_code == 200
    realconnect = tryassert.get_data(as_text=True)
    assert realconnect.startswith("<pre>")
    assert realconnect.endswith("</pre>")
    assert len(realconnect.lstrip("<pre>").rstrip("</pre>")) > 0

def test_cowfortune(app, client):
    tryassert = client.get("/cowfortune/")
    assert tryassert.status_code == 200
    realconnect = tryassert.get_data(as_text=True)
    assert realconnect.startswith("<pre>")
    assert realconnect.endswith("</pre>")
    assert len(realconnect.lstrip("<pre>").rstrip("</pre>")) > 0
