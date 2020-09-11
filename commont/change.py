
# append = {"uc1002":'{"C-Response-Desc":"success","C-API-Status":"00","C-Response-Body":"{\"createtime\":\"2020-07-28 16:54:51\",\"fingerInfo\":{},\"isSign\":0,\"token\":\"4a1eec977aac4459840ebd5ebd1cff41\",\"txnCommCom\":{\"tCurrTotalPage\":1,\"tCurrTotalRec\":1,\"totalPage\":1,\"totalRec\":1},\"userInfo\":{\"accFlag\":\"01\",\"acctType\":\"10\",\"centNum\":3,\"contactMobile\":\"18337634500\",\"loginAccountId\":\"8c98a97476f44ab287ae560e54755b04\",\"loginNo\":\"fp_1595926491251_3148\",\"nickname\":\"fp_1595926491251_3148\",\"pvtAccIdr\":\"0\",\"pvtRdcCadrIdr\":\"0\",\"registerTime\":\"2020-07-28 16:54:51\",\"userRealLvl\":\"RC02\"}}","C-Response-Code":"000000000000"}'}

# import jsonpath
# ''
# data = '{"Content-Type ":"application/json;charset=utf-8",\n"C-Tenancy-Id":"009900000000",\n"C-Timestamp":"20200518101752326"...APP_001",\n"C-Dynamic-Password-Foruser":"$uc1002.C-Response-Body.token$",\n"referer":"https://xffp.zgshfp.com.cn"\n\n}'
import json
from commont.log import  logger
import jsonpath

append={}
class Change:


    def change(self, data):
        '''
        把excel中读取到 的值解析，切片，然后把参数关联的值进行替换返回
        :param data: excel读取到的值
        :return: 替换后的值
        '''
        splitlist = data.split("$")
        logger.info("切片后的列表为{}".format(splitlist))
        num = 0
        for split in splitlist:
            if num % 2 == 1:
                var = split
                logger.info("需要提取的 变量名var的值为{}".format(var))
                app = var.split('.', 1)[0]
                logger.info("提取的接口返回变量名为{}".format(app))
                appvalue = append[app]
                logger.info("把提取的 变量名放到append字典中的值为{}".format(append))
                # print(appvalue)
                # print(type(appvalue))
                varjsonpath = var.split(".")
                # print(varjsonpath)
                if len(varjsonpath) <= 2:
                    # print(appvalue)
                    path=varjsonpath[1]
                    changvalue = jsonpath.jsonpath(appvalue,"$."+path)
                    # print(changvalue)
                    splitlist[num] = str(changvalue[0])
                elif len(varjsonpath) > 2:
                    varjsonpath1 = var.split(".", 2)[2]
                    print(varjsonpath1)
                    path=varjsonpath[1]
                    # print(path)
                    chang = jsonpath.jsonpath(appvalue,"$."+path)[0]
                    # print(chang)
                    # print(type(chang))
                    if isinstance(chang, dict):
                        changvalue = jsonpath.jsonpath(chang, "$." + str(varjsonpath1))
                        # print("changevalue是{}".format(changvalue))
                        splitlist[num]=str(changvalue[0])

                    elif isinstance(chang, str):
                        chang = json.loads(chang)
                        # print(chang)
                        # print(type(chang))
                        changvalue = jsonpath.jsonpath(chang, "$." + str(varjsonpath1))
                        # print(changvalue)
                        splitlist[num] = str(changvalue[0])
            num = num + 1

        strsplitvar = ''.join(splitlist)
        # print(strsplitvar)
        return strsplitvar



#
# if __name__ == '__main__':
#     c = Change()
#     c.change(data)
