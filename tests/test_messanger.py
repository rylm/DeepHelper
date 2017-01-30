import pytest
from deephelper.messangers import Messangers
from deephelper.messangers.backend import TeleBot

def send_message(self, token, message):
    print("{}:{}".format(token, message))

@pytest.yield_fixture
def work_settings():
    settings = {"telegram": {
                            "token": "tr4t334g5y343h435h4",
                            "chat_id": [343, 2342424]
                                },
                "message_template": "Hello, {name}, {question}",
                "input_pattern": ["name", "question"]}
    yield settings

@pytest.yield_fixture
def fail_settings():
    settings = {"ex_messanger": {
                            "token": "tr4t334g5y343h435h4",
                            "chat_id": [343, 2342424]
                                }
                }
    yield settings

@pytest.yield_fixture
def work_messanger(work_settings, monkeypatch):
    monkeypatch.setattr(TeleBot, "send_message", send_message)
    yield Messangers(work_settings)






def test_build_messangers(work_messanger):
    assert len(work_messanger._messagers_list) == 1

def test_message_template(work_messanger):
    assert work_messanger._message_template == "Hello, {name}, {question}"

def test_exception_build_messangers(fail_settings):
    with pytest.raises(NotImplementedError) as ex_info:
        Messangers(fail_settings)

def test_send_messages_one_str(work_messanger, capsys):
    work_messanger.send_messages("Ron", "how are you?")
    out, err = capsys.readouterr()
    msg = "Hello, Ron, how are you?"
    assert out == "343:{0}\n2342424:{0}\n".format(msg)

