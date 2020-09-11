
import json

import requests


class Requests:
    def run(self, method, url, header, type, params=None, data=None, **kwargs):
        method = method.lower()
        if header == '':
            pass
        else:
            header = json.loads(header)
        if params == '':
            pass
        else:
            params = json.loads(params)
        if data == '':
            pass
        else:
            data = json.loads(data)

        if method == "get":
            if type == '':
                return self.get(url, params=params, headers=header, **kwargs)
        if method == "post":
            if type == "form":
                return self.post(url, params=params, data=data, headers=header, **kwargs)
            elif type == "json":
                return self.post(url, params=params, json=data, headers=header, **kwargs)
            elif type == '':
                print("找不到对应的type")

    def get(self, url, params=None, **kwargs):
        try:
            return requests.get(url, params=params, **kwargs)
        except:
            print("get请求参有误，请检查")

    def post(self, url, data=None, **kwargs):
        try:
            return requests.post(url, data=data, **kwargs)
        except:
            print("post请求参有误，请检查")
