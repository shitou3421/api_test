import os

from api.baseapi import BaseApi


class Work(BaseApi):


    def get_token(self, corpsecret):
        '''具体项目， 具体接口'''
        self.params["corpsecret"] = corpsecret

        locd = os.path.abspath(os.path.dirname(__file__))
        case_path = os.path.join(locd, "work.yaml")

        wework_data = self.load_yaml(case_path)
        data = self.send_api(wework_data.get("get_token"))
        return data["access_token"]

