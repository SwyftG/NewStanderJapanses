# encoding: utf-8
__author__ = 'lianggao'
__date__ = '2019/7/17 10:44 AM'

if __name__ == '__main__':
    ss = "东京大学::::"
    flag = True
    res = (ss[:-4] if flag else ss[:-1]) + "??"
    print(res)