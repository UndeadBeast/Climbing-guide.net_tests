# -*- coding: utf-8 -*-
from enum import Enum

__author__ = 'g_trofimov'


class AscendType(Enum):
    onsight = 1
    flash = 2
    redpoint = 3


class Ascend:
    def __init__(self, ascend_type: AscendType, category, ascend_date, like, comment):
        self.ascend_type = ascend_type
        self.category = category
        self.ascend_date = ascend_date
        self.like = like
        self.comment = comment
