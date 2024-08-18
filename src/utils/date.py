"""
The MIT License (MIT)

Copyright (c) 2024-present Paillat-dev <me@paillat.dev>

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import datetime


def parse_date(filename: str) -> datetime.datetime:
    """
    Parse a date from a bereal-created filename.

    :param filename:
    :return: The datetime object
    :rtype: datetime.datetime
    """
    # format is bereal-yyyy-mm-dd-hhmm.ext
    date_str = filename.split("-")[1:5]
    date_str = "-".join(date_str)
    return datetime.datetime.strptime(date_str, "%Y-%m-%d-%H%M").replace(tzinfo=datetime.UTC)
