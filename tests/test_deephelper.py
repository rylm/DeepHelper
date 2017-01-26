import pytest
from deephelper import DeepHelper

class dropbox_test:
    def __init__(self, token=444):
        self.token = token

    def put_file(self, path, data):
        return data.decode("utf-8")

def test_dropbox(monkeypatch, tmpdir):
    #monkeypatch.setenv("dropbox.client.DropboxClient", dropbox_test)
    n = DeepHelper({"dropbox": {"token": "geettty"}})
    monkeypatch.setattr(n, "dropbox", dropbox_test())
    p = tmpdir.join("test.txt")
    p.write("hello")
    message = n.to_dropbox(p.strpath)
    assert message == "hello"
