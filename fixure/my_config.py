import lya
import os

__author__ = 'g_trofimov'


script_path = os.path.dirname(os.path.dirname(__file__))
config_path = os.path.join(script_path, 'common.yaml')
config_file = lya.AttrDict.from_yaml(config_path)

CGN_URL = config_file.cgn.host
CGN_LANGUAGE = config_file.cgn.language
CGN_MY_ROUTES = CGN_URL + '/' + CGN_LANGUAGE + '/climb/user-routes/my-routes'
