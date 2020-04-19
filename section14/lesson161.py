"""
dectest

document + test
説明文に簡単なサンプルをつけたい時に有効
複雑なテストには使わない
"""


class Cal(object):
    def add_and_double(self, x, y):
        # 以下のdocumentを書く場所を利用して、testを書く
        # その際に対話型shellで用いる、>>>を使う
        """Add and double

        >>> c = Cal()
        >>> c.add_and_double(1, 1)
        5

        >>> c.add_and_double('1', '1')
        Traceback (most recent call last):
        ...
        ValueError
        """
        # ...は間を省略するという意味
        if type(x) is not int or type(y) is not int:
            raise ValueError

        result = x + y
        result *= 2
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
