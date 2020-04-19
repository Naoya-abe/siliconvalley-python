import pytest

import calculation


class TestCal(object):
    @classmethod
    def setup_class(cls):  # テストするクラスの前後に行いたい処理
        print('start')
        cls.cal = calculation.Cal()

    @classmethod
    def teardown_class(cls):  # テストするクラスの前後に行いたい処理
        print('end')
        cls.cal = calculation.Cal()

    def setup_method(self, method):
        # テストされるmethodの名前を出力可能
        print('method={}'.format(method.__name__))
        self.cal = calculation.Cal()

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        del self.cal

    def test_add_and_double(self):
        assert self.cal.add_and_double(1, 1) == 4

    def test_add_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_and_double('1', '1')

    # class CalTest(unittest.TestCase):
    #     def setUp(self):
    #         print('setup')
    #         self.cal = calculation.Cal()

    #     def tearDown(self):
    #         print('clean up')
    #         del self.cal

    #     # 単純なスキップ
    #     # @unittest.skip('skip!')

    #     # 条件付きのスキップ
    #     @unittest.skipIf(release_name == "lesson2", 'skip!!')
    #     def test_add_and_double(self):
    #         self.assertEqual(self.cal.add_and_double(1, 1), 4)

    #     def test_add_and_double_raise(self):
    #         with self.assertRaises(ValueError):
    #             self.cal.add_and_double('1', '1')

    # if __name__ == "__main__":
    #     unittest.main()
