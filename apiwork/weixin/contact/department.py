import requests


class DepartMent:
    def creatDpa(self, token, data=None, json=None, **kwargs):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                             params={"access_token": token},
                             json=json,
                             # proxies={"https": "http://127.0.0.1:8080",
                             #          "http": "http://127.0.0.1:8080"},
                             # verify=False
                             ).json()

    def list(self, token,params=None, **kwargs):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                     params={"access_token": token}
                     ).json()

