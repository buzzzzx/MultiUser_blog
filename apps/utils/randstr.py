# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/11/9 下午9:03'

import random
import string


def generate_code():
    letters = string.ascii_letters
    digits = string.digits
    chars = letters + digits
    length = len(chars)

    code = ""
    for i in range(8):
        code += chars[random.randint(0, length - 1)]
    return code
