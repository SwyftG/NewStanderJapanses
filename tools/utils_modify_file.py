# encoding: utf-8
__author__ = 'lianggao'
__date__ = '2019/7/16 11:23 PM'

import os

PWD_PATH = os.getcwd()
FATHER_PATH = os.path.abspath(os.path.dirname(PWD_PATH) + os.path.sep + ".")


LEVEL_ONE = "LevelOne"
CLASS_NAME = "lesson_01_01"
LEVEL_ONE_PATH = FATHER_PATH + "/" + LEVEL_ONE
LEVEL_ONE_CLASS = os.listdir(LEVEL_ONE_PATH)


def add_splash_in_file(file_name):
    operate_splash_in_file(file_name, True)


def remove_splash_in_file(file_name):
    operate_splash_in_file(file_name, False)


def operate_splash_in_file(file_name, add_or_remove):
    file_str = ""
    with open(file_name, 'r') as file_to_read:
        for line in file_to_read:
            new_line = (line[:-1] + "::\n") if add_or_remove else (line[:-3] + line[-1:])
            file_str += new_line
    with open(file_name, 'w') as file_to_write:
        file_to_write.write(file_str)



if __name__ == '__main__':
    file_dir = LEVEL_ONE_PATH + "/" + CLASS_NAME
    add_splash_in_file(file_dir)
    # remove_splash_in_file(file_dir)