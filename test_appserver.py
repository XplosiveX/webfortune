import pytest
from appserver import app as flask_app
intropre = '<pre style="border:black solid 4px; border-radius: 12.5px; background:silver; opacity: 0.65; margin-left:auto; margin-right:auto;height:100%;height:65%;overflow:auto; text-align:center; font-size:16px;">'

@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


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
    assert realconnect.startswith(intropre)
    assert realconnect.endswith("</pre>")
    assert len(realconnect.lstrip(intropre).rstrip("</pre>")) > 0

def test_cowfortune(app, client):
    tryassert = client.get("/cowfortune/")
    assert tryassert.status_code == 200
    realconnect = tryassert.get_data(as_text=True)
    assert realconnect.startswith(intropre)
    assert realconnect.endswith("</pre>")
    assert len(realconnect.lstrip(intropre).rstrip("</pre>")) > 0
