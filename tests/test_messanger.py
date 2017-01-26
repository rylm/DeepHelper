import pytest
from deephelper.messangers import Messangers

@pytest.yield_fixture
def work_settings():
    settings = {"telegram": {
                            "token": "tr4t334g5y343h435h4",
                            "chat_id": [343, 2342424]
                                },
                "message_template": "Hello, Ron, how are you?"}
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
def work_messanger(work_settings):
    yield Messangers(work_settings)

def test_build_messangers(work_messanger):
    assert len(work_messanger._messagers_list) == 1

def test_message_template(work_messanger):
    assert work_messanger._message_template == "Hello, Ron, how are you?"

def test_exception_build_messangers(fail_settings):
    with pytest.raises(NotImplementedError) as ex_info:
        Messangers(fail_settings)

