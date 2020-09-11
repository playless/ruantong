
import json

import xlrd
from commont.public import Public
from commont.log import logger

body = '{"adress": {"city": "changsha"},"httpstatus": 200,"info": {"age": 18,"name": "admin"},"msg": "success","token": "23657DGYUSGD126731638712GE18271H"}'
body=json.loads(body)


class OpreationExcel:
    public = Public()

    def __init__(self, filedir, filename):
        filepath = self.public.filepath(filedir, filename)
        self.wb = xlrd.open_workbook(filepath)

    def rows_value(self):
        '''

        :return: 返回单个sheet的行数据
        '''
        sheet = self.wb.sheet_by_index(0)
        rows = sheet.nrows
        rows_value = []
        for row in range(1, rows):
            rows_value.append(sheet.row_values(row))
        logger.debug("读取excel每行的数据是{}".format(rows_value))
        return rows_value
    def sheets_values(self):
        '''

        :return: 返回表格中所有sheet的行的数据
        '''
        m=self.wb.nsheets
        # print(m)
        sheets_value = []
        for i in range(m):
            print(i)
            sheet = self.wb.sheet_by_index(i)
            rows = sheet.nrows
            for row in range(1, rows):
                sheets_value.append(sheet.row_values(row))
        # logger.debug("读取excel,sheet编号是{}，每行的数据是{},"
        #              "总长度是{}".format(i,sheets_value),len(sheets_value))
        return sheets_value
    def excels_value(self):
        '''

        :return: 返回多个excel表中的数据
        '''
        pass

# if __name__ == '__main__':
#     oe = OpreationExcel("data", "case.xlsx")
#     print(len(oe.sheets_values()))
