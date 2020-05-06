import json
import logging

import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def format_data(f: requests.Response):
    '''格式化显示响应的数据'''
    data = json.dumps(json.loads(f.text), indent=2, ensure_ascii=False)
    logger.info("本次响应的数据为:\n{data}".format(data=data))
    return f.json()


def json_path():
    '''封装对'''
    pass


def schema_diff():
    '''封装schema校验'''
    pass


class Mysql():

    def connect(self):
        '''连接数据库'''
        pass

    def get(self):
        '''获取指定数据库的指定表的指定字段'''
        pass

    def set(self):
        '''预置指定数据库的指定表的数据'''
        pass
