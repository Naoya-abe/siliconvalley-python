import pytest

import calculation


class TestCal(object):
    @classmethod
    def setup_class(cls):
        cls.cal = calculation.Cal()

    def test_add_and_double(self, request):  # requestを使うのは、pytestのルールなので覚える
        # terminalからの引数はrequestから受け取る
        os_name = request.config.getoption('--os-name')
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_and_double(1, 1) == 4
