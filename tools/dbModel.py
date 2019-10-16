# encoding: utf-8
__author__ = 'lianggao'
__date__ = '2019/10/8 11:05 AM'


class NSJModel(object):
    levelNum = str()
    classNum = str()
    chinese = str()
    jp_only = str()
    jp_chinese = str()
    change = str()

    def __init__(self, level_num, class_num, chinese, jp_only, jp_chinese, changed):
        self.levelNum = level_num
        self.classNum = class_num
        self.chinese = chinese
        self.jp_only = jp_only
        self.jp_chinese = jp_chinese
        self.change = changed

    def __str__(self):
        return "Level: %s\n" \
               "Class: %s\n" \
               "Chi: %s\n" \
               "Jap1: %s\n" \
               "Jap2: %s\n" \
               "Change: %s\n" % (self.levelNum, self.classNum, self.chinese, self.jp_only, self.jp_chinese, self.change)
