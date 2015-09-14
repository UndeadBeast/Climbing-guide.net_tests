import lya
import os

__author__ = 'g_trofimov'


scriptpath = os.path.dirname(__file__)
config_path = os.path.join(scriptpath, 'common.yaml')
my_config = lya.AttrDict.from_yaml(config_path)

CGN_URL = my_config.cgn.host
CGN_LANGUAGE = my_config.cgn.language
CGN_MY_ROUTES = CGN_URL + '/' + CGN_LANGUAGE + '/climb/user-routes/my-routes'
