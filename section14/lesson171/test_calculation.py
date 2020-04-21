# pytestのfixture
import os
import pytest

import calculation


class TestCal(object):

    @classmethod
    def setup_class(cls):
        cls.cal = calculation.Cal()
        cls.test_file_name = 'test.txt'

    def test_add_and_double(self):
        assert self.cal.add_and_double(1, 1) == 4

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(
            tmpdir, self.test_file_name
        )
        assert os.path.exists(test_file_path) is True
