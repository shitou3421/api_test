import json
import logging

import requests
import yaml
from jsonpath import jsonpath

from utils.utils import format_data

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class BaseApi():
    params = {}

    @staticmethod
    def load_yaml(path):
        '''加载接口文件的数据'''
        with open(path) as f:
            data = yaml.safe_load(f)
            return data

    def send_api(self, data: dict):
        '''发送接口文件的指定接口数据'''
        raw = yaml.safe_dump(data)

        for k, v in self.params.items():
            raw = raw.replace(f"${{{k}}}", repr(v))
        data = yaml.safe_load(raw)

        url = data.get("url")
        method = data.get("method")
        params = data.get("params")
        jsons = data.get("json")

        raw = json.dumps(data, indent=2, ensure_ascii=False)
        logger.info("本次加载的数据为:\n{raw}".format(raw=raw))

        r = requests.request(url=url, method=method, params=params, json=jsons)
        return format_data(r)

    # def steps_run(self, steps):
    #     '''接口的数据驱动，用例的数据驱动, 待完善'''
    #     for step in steps:
    #         raw = yaml.dump(step)
    #         for k, v in self.params.items():
    #             raw = raw.replace(f"{{{k}}}", repr(v))
    #         step = yaml.load(raw)
    #         if "method" in step.keys():
    #             method = step["method"].split(".")[-1]
    #             getattr(self, method)(**step)
    #         if "extract" in step.keys():
    #             self.data[step["extract"]] = self.json_path(**step)
    #         if "assert" in step.keys():
    #             assert eval(step["assert"])

    def json_path(self, path, r):
        return jsonpath(path, r)


if __name__ == '__main__':
    print(BaseApi().load_yaml("../testcase/test_demo.yaml"))
