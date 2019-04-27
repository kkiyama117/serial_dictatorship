# -*- coding: utf-8 -*-
"""event-parser api

APIを規定.
各APIは他のAPIまたは `core` の関数を呼び出す.
api.pyをスクリプトとして利用すると今月のイベント名一覧が得られる.
eventそのものを得たい場合,以下の関数を利用する.

Example:

    >>> from serial_dictatorship import api
    >>> api.run()
    []

詳細は各関数のdocstringを参照.
"""

from serial_dictatorship import core


def serial_dictatorship(method, **kwargs):
    return core.serial_dictatorship(method, **kwargs)


def run(**kwargs):
    """Construct and return an list of Class `Event`.

    hookを呼び出す.

    Args:


    Returns:
        generator of assignment
    """
    return serial_dictatorship(method='run', **kwargs)
