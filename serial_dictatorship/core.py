#!python3
# -*- coding: utf-8 -*-

"""serial dictatorship test with python

serial dictatorship の解決をさせる
"""
from serial_dictatorship.utils import format_priorities
import serial_dictatorship.factories as sdf


def serial_dictatorship(method, priorities):
    """hook to call event list factory

    call any function

    Args:
        method (str): 取得の仕方. 'get' or 'get_all'
        priorities(list): kwargs for method selected by args
            date or (year and month) ... get_all method
            url ... get

    Returns:
        method selected by args
    """
    return getattr(sdf, method)(priorities)


def format_kwargs(**kwargs) -> list:
    """select args from kwargs

    Args:

    Returns:
        dict:  (HTML取得に失敗した時はStopIteration例外)
    """
    priorities: list = kwargs.get('priorities', None)
    if priorities is not None and type(priorities) is list:
        return format_priorities(priorities)
    else:
        raise ValueError("please set priorities")


def main():
    """スクリプトとして実行したとき,実際に実行される関数

    `argparse` を用いた.
    """
    import argparse

    # templates
    parser = argparse.ArgumentParser(
        description='Run the factory to solve serial dictatorship.',
        epilog="For detail, see github, sphinx and source code",
    )
    parser.add_argument('priorities', nargs='+',
                        help="set strings like 'ACDBE, BDEAC, ABCDE'.",
                        metavar=None)
    # main parser
    args = parser.parse_args()
    kwargs = vars(args)
    # call event_parser
    # print(kwargs)
    print(serial_dictatorship('run', format_kwargs(**kwargs)))


if __name__ == '__main__':
    main()
