# -*- coding: utf-8 -*-
from enum import Enum

__author__ = 'g_trofimov'


class Rout:
    def __init__(self, name, id):
        self.id = id
        self.name = name
        # self.region = region
        # self.sector = sector

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
