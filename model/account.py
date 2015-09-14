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
        self.username = my_config.my_config.account_name
        self.email = my_config.my_config.account_e_mail
        self.password = my_config.my_config.account_password
