"""
serial_dictatorship Library
---------------------
setumei ryaku
usage:
   >>> import serial_dictatorship
   >>> serial_dictatorship.run(["ACDEBF","BDCFAE","CADFBE","ABCDFE"])
Full documentation is got by sphinx .
:copyright: (c) 2019 by kkiyama117.
:license: MIT, see LICENSE for more details.
"""

from .api import run
from .core import serial_dictatorship

from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import __build__, __author__, __author_email__, __license__
from .__version__ import __maintainer__, __maintainer_email__