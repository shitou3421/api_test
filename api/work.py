from api.baseapi import BaseApi


class Work(BaseApi):


    def get_token(self, corpsecret):
        '''具体项目， 具体接口'''
        self.params["corpsecret"] = corpsecret
        wework_data = self.load_yaml("../api/work.yaml")
        data = self.send_api(wework_data.get("get_token"))
        return data["access_token"]

