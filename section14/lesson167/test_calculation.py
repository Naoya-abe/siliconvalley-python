import pytest

import calculation


def test_add_and_double():  # test_を先頭につければOK
    cal = calculation.Cal()
    assert cal.add_and_double(1, 1) == 4


class TestCal(object):  # classで書く場合は「Test」を先頭につける
    def test_add_and_double(self):
        cal = calculation.Cal()
        assert cal.add_and_double(1, 1) == 4

    def test_add_and_double_raise(self):
        with pytest.raises(ValueError):
            cal = calculation.Cal()
            cal.add_and_double('1', '1')

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
