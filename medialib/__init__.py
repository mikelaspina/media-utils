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
"""

import re

from datetime import date

class TvParser(object):
    def __init__(self):
        self.date_aired_patterns = [
            re.compile(r'''
                        (?P<year>(?:19|20)[0-9]{2})
                        [\.\-_]
                        (?P<month>[0-9]{2})
                        [\.\-_]
                        (?P<day>[0-9]{2})
                        ''', re.VERBOSE),
            re.compile(r'''
                        (?P<month>[0-9]{2})
                        [\.\-_]
                        (?P<day>[0-9]{2})
                        [\.\-_]
                        (?P<year>(?:19|20)[0-9]{2})
                        ''', re.VERBOSE)
        ]

    def parse(self, name):
        r = self._try_date_aired(name)
        if r:
            return r

        return {}

    def _try_date_aired(self, name):
        for pat in self.date_aired_patterns:
            m = pat.search(name)
            if m:
                year = int(m.group('year'))
                month = int(m.group('month'))
                day = int(m.group('day'))
                
                return { 'DateAired': date(year, month, day) }

        return None
