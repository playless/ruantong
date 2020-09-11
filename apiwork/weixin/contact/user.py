import requests
import pytest

##from weixin.contact.token import Weixin
from weixin.http import HttpRequest


class UserCreate(HttpRequest):
    method = HttpRequest.HttpMethod.POST
    url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
    ##self.params={"access_token": token}

    ##return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
    ## params={"access_token": token},
    ##json=dict,
    ## data=data
    ## ).json()


def list(self, token, department_id=1, fetch_child=0, **kwargs):
    return requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                        params={"access_token": token,
                                "department_id": department_id,
                                "fetch_child": fetch_child
                                }
                        ).json()


