# -*- coding: utf-8 -*-
from fixure import my_config

__author__ = 'g_trofimov'


class UserAccount(object):
    def __init__(self):
        self.username = None
        self.email = None
        self.password = None
        self.ip = None
        self.read_default_settings_from_config()

    def read_default_settings_from_config(self):
        self.username = my_config.config_file.account.username
        self.email = my_config.config_file.account.email
        self.password = my_config.config_file.account.password
