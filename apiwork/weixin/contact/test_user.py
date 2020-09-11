import json
import logging
import time

import pystache

from weixin.contact.user import *
from weixin.contact.utils import Utils

class TestUser:
    depart_id = 65

    def test_create(self, token):
        uid = "seveniruby_" + str(time.time())
        params = {"access_token": token}
        data = {
            "userid": uid,
            "name": uid,
            "department": [self.depart_id],
            "email": uid + "@testerhome.com"
        }
        UserCreate().set_querystring(params).set_body(data).run().get_header()


       ## assert r['errcode'] == 0

    def test_create_by_real(self, token):
        uid = "seveniruby_" + str(time.time())
        mobile = str(time.time()).replace(".", "")[0:11]
        data = str(Utils.parse("user_create.json", {
            "name": uid,
            "title": "校长",
            "email": mobile + "@qq.com",
            "mobile": mobile
        }))
        data = data.encode("UTF-8")

        r = self.user.create(token, data=data)
        logging.debug(r)
        assert r['errcode'] == 0

    def test_list(self, token):
        r = self.user.list(token)
        logging.debug(json.dumps(r, indent=4))

        r = self.user.list(token, department_id=65)
        logging.debug(r)
