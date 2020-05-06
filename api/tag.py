import os

from jsonpath import jsonpath

from api.work import Work

class Tag(Work):

    def __init__(self):
        corpsecret = "i6hRZ7g5N9hA8BPYpa9H_8agPcHJKsxbtFOBm7KiqZA"
        self.params["access_token"] = self.get_token(corpsecret)

        locd = os.path.abspath(os.path.dirname(__file__))
        case_path = os.path.join(locd, "tag.yaml")

        self.data = self.load_yaml(case_path)

    def get(self):
        return self.send_api(self.data.get("get"))

    def add(self, name):
        self.params["group_id"] = "etjIywCwAAY_H3Mi4n1KGatPFGP-TMwA"
        self.params["name"] = name
        return self.send_api(self.data.get("add"))

    def delete(self, tag_id):
        self.params["tag_id"] = tag_id
        return self.send_api(self.data.get("delete"))

