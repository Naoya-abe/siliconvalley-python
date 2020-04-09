"""Utils to display to be returned to the user on the console."""
import os
import string

import termcolor


def get_template_dir_path():
    """Return the path of the template's directory.

    Returns:
        str: The template dir path.
    """
    template_dir_path = None
    try:
        import settings
        # settingsディレクトリが存在したら、そこのtemplateファイルを取得する
        if settings.TEMPLATE_PATH:
            template_dir_path = settings.TEMPLATE_PATH
    except ImportError:
        pass

    if not template_dir_path:
        # ユーザーから指定がなければ、パッケージの中のtemplateを使う
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir, 'templates')

    return template_dir_path


class NoTemplateError(Exception):
    """No Template Error"""


def find_template(temp_file):
    """Find for template file in the given location.

    Returns:
        str: The template file path

    Raises:
        NoTemplateError: If the file does not exists.
    """
    # templateが入っているディレクトリがわからないので、ディレクトリのパスを取得していく
    template_dir_path = get_template_dir_path()
    temp_file_path = os.path.join(template_dir_path, temp_file)
    if not os.path.exists(temp_file_path):
        raise NoTemplateError('Could not find {}'.format(temp_file))
    # templateファイルのpathを返す。名前を見ただけでわかる
    return temp_file_path


def get_template(template_file_path, color=None):
    """Return the path of the template.

    Args:
        template_file_path (str): The template file path
        color: (str): Color formatting for output in terminal
            See in more details: https://pypi.python.org/pypi/termcolor

    Returns:
        string.Template: Return templates with characters in templates.
    """
    # 引数で指定されたテンプレートファイルを探しに行く
    template = find_template(template_file_path)
    with open(template, 'r', encoding='utf-8') as template_file:
        contents = template_file.read()
        # 改行コードを削除
        contents = contents.rstrip(os.linesep)
        # テキストの整形
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
            contents=contents, splitter="=" * 60, sep=os.linesep)
        # テキストに色を付ける
        contents = termcolor.colored(contents, color)
        # str型にしてテキストを返す
        return string.Template(contents)
