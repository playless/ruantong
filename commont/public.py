
import os

from commont.log import logger


class Public:
    def filepath(self,filedir,filename):
       filepath=os.path.join(os.path.dirname(os.path.dirname(__file__)),filedir,filename)
       logger.debug("文件路径是{}".format(filepath))
       return filepath


# if __name__ == '__main__':
#     Public().filepath("data", "case.xlsx")