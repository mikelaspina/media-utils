# -*- coding: utf-8 -*- 

# Copyright 2013 Mike LaSpina

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Unit tests for parsing tv show file names.
"""

import medialib
import unittest

from datetime import date
from nose.tools import *

# class Foo(unittest.TestCase):
#     SAMPLES = [
#         'Show_Name_S01E02.mp4',
#         'Show-Name-S01E02.mp4',
#         'Show.Name.S01E02.mp4',
#         'Show Name S01E02.mp4',

#         'Show_Name_S01_E02.mp4',
#         'Show-Name-S01-E02.mp4',
#         'Show.Name.S01.E02.mp4',
#         'Show Name S01 E02.mp4'
#     ]

#     def test_s00e00_format():
#         pass


class TestDateAired(object):
    SAMPLES = [
        # YYYY-MM-DD
        #   With dash separator
        'Show_Name_1900-01-02',
        'Show_Name-1900-01-02',
        'Show_Name.1900-01-02',
        'Show_Name 1900-01-02',
        #   With dash separator
        'Show_Name_1900_01_02',
        'Show_Name-1900_01_02',
        'Show_Name.1900_01_02',
        'Show_Name 1900_01_02',
        #   With dot separator
        'Show_Name_1900.01.02',
        'Show_Name-1900.01.02',
        'Show_Name.1900.01.02',
        'Show_Name 1900.01.02',
        # MM-DD-YYYY
        #   With dash separator
        'Show_Name_01-02-1900',
        'Show_Name-01-02-1900',
        'Show_Name.01-02-1900',
        'Show_Name 01-02-1900',
        #   With dash separator
        'Show_Name_01_02-1900',
        'Show_Name-01_02-1900',
        'Show_Name.01_02-1900',
        'Show_Name 01_02-1900',
        #   With dot separator
        'Show_Name_01.02-1900',
        'Show_Name-01.02-1900',
        'Show_Name.01.02-1900',
        'Show_Name 01.02-1900'
    ]

    def setUp(self):
        self.parser = medialib.TvParser()

    def test_date_aired(self):
        for name in self.SAMPLES:
            yield self.check_date_aired, name
        
    def check_date_aired(self, name):
        result = self.parser.parse(name)

        assert_in('DateAired', result)
        assert_equal(result['DateAired'], date(1900, 1, 2))
