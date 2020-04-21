#  conftestでは必ずconftest.pyを用意する


def pytest_addoption(parser):
    # parserが引数
    parser.addoption('--os-name', default='linux', help='os name')
