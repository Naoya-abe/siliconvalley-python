import os


class Cal(object):

    def add_and_double(self, x, y):
        # if文の中がテストされていない
        if type(x) is not int or type(y) is not int:
            raise ValueError

        result = x + y
        result *= 2
        return result

    def save(self, dir_path, file_name):
        print(dir_path)
        # if文の中がテストされていない
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'w') as f:
            f.write('test')
