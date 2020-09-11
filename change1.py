import ast
import json

import ask as ask
import jsonpath
append = {"uc1002":{"C-Response-Desc":"success","C-API-Status":"00","C-Response-Body":"{\"createtime\":\"2020-07-28 16:54:51\",\"fingerInfo\":{},\"isSign\":0,\"token\":\"4a1eec977aac4459840ebd5ebd1cff41\",\"txnCommCom\":{\"tCurrTotalPage\":1,\"tCurrTotalRec\":1,\"totalPage\":1,\"totalRec\":1},\"userInfo\":{\"accFlag\":\"01\",\"acctType\":\"10\",\"centNum\":3,\"contactMobile\":\"18337634500\",\"loginAccountId\":\"8c98a97476f44ab287ae560e54755b04\",\"loginNo\":\"fp_1595926491251_3148\",\"nickname\":\"fp_1595926491251_3148\",\"pvtAccIdr\":\"0\",\"pvtRdcCadrIdr\":\"0\",\"registerTime\":\"2020-07-28 16:54:51\",\"userRealLvl\":\"RC02\"}}","C-Response-Code":"000000000000"}}

# import jsonpath
# ''
data = '{"Content-Type ":"application/json;charset=utf-8",\n"C-Tenancy-Id":"009900000000",\n"C-Timestamp":"20200518101752326"...APP_001",\n"C-Dynamic-Password-Foruser":"$uc1002.C-Response-Body.txnCommCom.tCurrTotalPage$",\n"referer":"https://xffp.zgshfp.com.cn"\n\n}'

# append={}
class Change1:


    def change1(self, data):

        splitlist = data.split("$")
        # print("切片后的列表为{}".format(splitlist))
        num = 0
        for split in splitlist:
            if num % 2 == 1:
                var = split
                # print("需要提取的 变量名var的值为{}".format(var))
                app = var.split('.', 1)[0]
                # print("提取的接口返回变量名为{}".format(app))
                appvalue = append[app]
                # print("把提取的 变量名放到append字典中的值为{}".format(append))
                # print(appvalue)
                print(type(appvalue))
                varjsonpath = var.split(".")
                # print(varjsonpath)
                if len(varjsonpath)<=2:
                    path = varjsonpath[1]
                    changvalue=jsonpath.jsonpath(appvalue,"$."+path)
                    print(changvalue)
                    print(type(changvalue))
                    splitlist[num] = str(changvalue[0])
                elif len(varjsonpath)>2:
                    varjsonpath1=var.split(".",2)[2]
                    print(varjsonpath1)
                    chang=appvalue[varjsonpath[1]]
                    print(chang)
                    print(type(chang))
                    if isinstance(chang,dict):
                        changvalue=jsonpath.jsonpath(chang,"$."+str(varjsonpath1))
                        splitlist[num]=str(changvalue[0])
                        # print(changvalue)
                    elif isinstance(chang,str):
                        chang=json.loads(chang)
                        # print(chang)
                        # print(type(chang))
                        changvalue=jsonpath.jsonpath(chang,"$."+str(varjsonpath1))
                        # print(changvalue)
                        splitlist[num]=str(changvalue[0])
            num = num + 1

        strsplitvar = ''.join(splitlist)
        print(strsplitvar)
        return strsplitvar




if __name__ == '__main__':
    c = Change1()
    c.change1(data)
    # a={"createtime":"2020-07-28 16:54:51","fingerInfo":{},"isSign":0,"token":"4a1eec977aac4459840ebd5ebd1cff41","txnCommCom":{"tCurrTotalPage":1,"tCurrTotalRec":1,"totalPage":1,"totalRec":1},"userInfo":{"accFlag":"01","acctType":"10","centNum":3,"contactMobile":"18337634500","loginAccountId":"8c98a97476f44ab287ae560e54755b04","loginNo":"fp_1595926491251_3148","nickname":"fp_1595926491251_3148","pvtAccIdr":"0","pvtRdcCadrIdr":"0","registerTime":"2020-07-28 16:54:51","userRealLvl":"RC02"}}
    # print(a["token"])
    # a={"C-Response-Desc":"success","C-API-Status":"00","C-Response-Body":"{\"createtime\":\"2020-07-28 16:54:51\",\"fingerInfo\":{},\"isSign\":0,\"token\":\"4a1eec977aac4459840ebd5ebd1cff41\",\"txnCommCom\":{\"tCurrTotalPage\":1,\"tCurrTotalRec\":1,\"totalPage\":1,\"totalRec\":1},\"userInfo\":{\"accFlag\":\"01\",\"acctType\":\"10\",\"centNum\":3,\"contactMobile\":\"18337634500\",\"loginAccountId\":\"8c98a97476f44ab287ae560e54755b04\",\"loginNo\":\"fp_1595926491251_3148\",\"nickname\":\"fp_1595926491251_3148\",\"pvtAccIdr\":\"0\",\"pvtRdcCadrIdr\":\"0\",\"registerTime\":\"2020-07-28 16:54:51\",\"userRealLvl\":\"RC02\"}}","C-Response-Code":"000000000000"}
    #
    # print(a)
    # # a=json.dumps(a)
    # # print(a)
    # # print(type(a))
    # # c=json.loads(a)
    # # print(a)
    # # print(type(a))
    # #
    s="w.o"
    list1=s.split('.',1)
    print("".join(list1))
