import datetime
import json
import os

import allure
import pytest
import requests

from weixin.contact.department import *
from weixin.contact.token import Weixin
import logging

from weixin.contact.utils import Utils

@allure.feature("部门")
class TestDepartment:
    @allure.story()
    def test_create_depth(self,token):
        parentid = 7

        for i in range(13):
            json = {
                "name": "_开发部门_" + str(parentid)+ str(datetime.datetime.now().timestamp()),
                "parentid": parentid,
            }

            r = DepartMent().creatDpa(token,json)
            logging.debug(r)
            parentid = r["id"]
            assert r["errcode"]==0

    def test_create_name(self, token):
        json = {
            "name": "第九期_seveniruby",
            "parentid": 1,
        }

        logging.debug(json)
        r = DepartMent().creatDpa(token,json)
        logging.debug(r)

    @pytest.mark.parametrize("name", [
        "运维部门",
        "東京アニメーション研究所",
        "도쿄 애니메이션 연구소",
        "معهد طوكيو للرسوم المتحركة",
        "東京動漫研究所"
    ])
    def test_create_order(self, name,token):
        data = {
            "name": name+Utils.udid(),
            "parentid": 1,
            "order": 1,
        }

        r = DepartMent().creatDpa(token,json)

        #解密
        logging.debug(r)
        assert r["errcode"]==0

    def test_get(self, token):
        r =DepartMent().list(token,params={"id":2})

        logging.debug(json.dumps(r, indent=4))
