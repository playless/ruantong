

import pytest
from commont.log import logger
from base.requests import Requests
from commont.change import *
from commont.opreationExcel import OpreationExcel


class TestRunTong:
    re = Requests()
    oe = OpreationExcel("data", "case.xlsx")
    exceldata = oe.sheets_values()
    # print(exceldata)
    change = Change()

    @pytest.mark.parametrize(("apiname",'method', 'url', 'header', 'params', 'data', 'type', 'expect', 'dependency'), exceldata)
    def test_run(self, apiname,method, url, header, params, data,type, dependency, expect):
        header = '' if header is None else header
        params = '' if params is None else params
        data = '' if data is None else data
        header = self.change.change(header) if header.find("$") >= 0 else header
        params = self.change.change(params) if header.find("$") >= 0 else params
        data = self.change.change(data) if data.find("$") >= 0 else data
        type = '' if type is None else type

        res = self.re.run(method, url, header, type, params=params, data=data)
        if len(dependency) > 0 and dependency.find("/") < 0:
            append[dependency] = res.json()
            # print(append)
        resjson:dict=res.json()
        logger.info("resjson{}".format(json.dumps(resjson,indent=4,ensure_ascii=False)))
        expect_value = eval(expect)
        expect_value: dict
        # print(expect_value)
        for k, v in expect_value.items():
                slist=k.split('.',1)
                logger.info("slist为{}".format(slist))
                if len(slist)==1:
                    s = jsonpath.jsonpath(resjson, "$." + k)[0]
                    logger.info("s{}".format(s))
                    assert s == v
                else:
                    value=jsonpath.jsonpath(resjson,"$."+slist[0])[0]
                    logger.info("value{}".format(value))
                    if isinstance(value,dict):
                        s=jsonpath.jsonpath(value,"$."+slist[1])[0]
                        assert s==v
                    elif isinstance(value,str):
                        value=json.loads(value)
                        s = jsonpath.jsonpath(value, "$." + slist[1])[0]
                        logger.info("s{}".format(s))
                        assert s == v








        print(res.text)





if __name__ == '__main__':
    pytest.main(['-s', '-v','test_ruantong.py'])
