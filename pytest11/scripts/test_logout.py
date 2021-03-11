import pytest


class TestLogout:

    @pytest.mark.parametrize(["username", "pwd"],[("zhangsan", "lisi")])
    def test_logout(self, username, pwd):
        print(username)
        print(pwd)











    # @pytest.mark.xfail(conditon=True, reason="xxx")
    # def test_logout1(self):
    #     print("登出1")
    #     assert 1
    #
    # @pytest.mark.xfail(conditon=True, reason="xxx")
    # def test_logout2(self):
    #     print("登出2")
    #     assert 0


















    # # @pytest.mark.skip
    # @pytest.mark.skipif(condition=True, reason="xxx")
    # def test_logout1(self):
    #     print("登出1")
    #
    # def test_logout2(self):
    #     print("登出2")