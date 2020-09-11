import pytest

from weixin.contact.token import Weixin


@pytest.fixture(scope="session", autouse=True)
def token():
    print(Weixin.get_token_new())
    return Weixin.get_token_new()
