import pytest
from jsonpath import jsonpath

from api.tag import Tag


class TestDemo:

    def setup(self):
        self.tag = Tag()

    def test_add(self):
        self.tag.get()

    @pytest.mark.parametrize("name", [
        "专业1","demo1",
        "专业2","demo2",
        "专业3","demo3",
        "专业4","demo4",
    ])
    def test_delete(self,name):
        r1 = self.tag.get()
        a_name = jsonpath(r1, "$..name")
        assert name not in a_name

        self.tag.add(name)
        r2 = self.tag.get()
        b_name = jsonpath(r2, "$..name")
        assert name in b_name

        path = f"$..tag[?(@.name=='{name}')]"
        tag_id = jsonpath(r2, path)[0]["id"]
        print(tag_id)
        self.tag.delete(tag_id)
        r3 = self.tag.get()
        c_name = jsonpath(r3, "$..name")
        assert name not in c_name


