import unittest

import calculation


class CalTest(unittest.TestCase):
    # unittest.TestCaseを継承
    # testを行う場合、[test_]は必須[_]以降は何をテストしているのかわかりやすいように記述
    def test_add_and_double(self):
        cal = calculation.Cal()
        # unittest.TestCaseを継承しているので、assertEqualが使える
        # assertEqual(テストしたい関数, 予想する値)
        # 他のメソッドは随時検索する。
        self.assertEqual(cal.add_and_double(1, 1), 5)


if __name__ == "__main__":
    unittest.main()
