# encoding: utf-8
__author__ = 'lianggao'
__date__ = '2019/10/16 4:22 PM'
import json
import os

PWD_PATH = os.getcwd()
FATHER_PATH = os.path.abspath(os.path.dirname(PWD_PATH) + os.path.sep + ".")
FILE_PATH = FATHER_PATH + '/config'

def read_config_from_configfile():
    file_path = FILE_PATH
    with open(file_path + '/config.json', 'r') as load_f:
        load_json = json.load(load_f)
        print("Config_utils_read_config_from_configfile:::")
        print(load_json)
    return load_json