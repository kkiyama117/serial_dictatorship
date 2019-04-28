#!python3
# -*- coding: utf-8 -*-

"""serial dictatorship test with python

serial dictatorship の解決をさせる
"""
import serial_dictatorship.factories as sdf
from serial_dictatorship.utils import format_output


def serial_dictatorship(method, priorities):
    """hook to call event list factory

    call any function

    Args:
        method (str): 取得の仕方. 'run'
        priorities(list): kwargs for priorities

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
        return priorities
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
    print(format_output(serial_dictatorship('run', format_kwargs(**kwargs))))


if __name__ == '__main__':
    main()
