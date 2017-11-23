#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function, absolute_import

import unittest

from ibotcloud import ask

APP_KEY = 'mjjmBCLHyjeo'
SECRET = '5OI4lJr5zwgQFHuZhWXR'


class TestAsk(unittest.TestCase):

    def test_execute(self):
        req = ask.Request(APP_KEY, SECRET)
        question = '北京周末天气'
        print('Q:', question)
        answer = req.execute(question, platform='web', response_type=ask.ResponseType.advanced)
        print('A:', answer)
        self.assertTrue(answer)
