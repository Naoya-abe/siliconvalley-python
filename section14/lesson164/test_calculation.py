import unittest

import calculation


class CalTest(unittest.TestCase):
    # テストを行う前に必ず実行したいこと
    def setUp(self):
        print('setup')
        # ここで宣言してしまえば、これ以降
        # cal = calculation.Cal()がいらない
        self.cal = calculation.Cal()

    # キャメルケースで書く
    def tearDown(self):
        print('clean up')
        del self.cal

    def test_add_and_double(self):
        self.assertEqual(self.cal.add_and_double(1, 1), 4)

    def test_add_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_and_double('1', '1')


if __name__ == "__main__":
    unittest.main()
