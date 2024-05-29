#!/usr/bin/env python3
"""filter data"""


import re


def filter_datum(fields, redaction, message, separator) -> None:
    """
    filter_datum returns the log message obfuscated
    """
    return re.sub(separator.join(fields), redaction, message)
