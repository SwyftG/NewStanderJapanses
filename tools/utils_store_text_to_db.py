# encoding: utf-8
__author__ = 'lianggao'
__date__ = '2019/9/24 11:23 AM'

import os
import pymongo
from dbModel import NSJModel
from config_utils import read_config_from_configfile


PWD_PATH = os.getcwd()
FATHER_PATH = os.path.abspath(os.path.dirname(PWD_PATH) + os.path.sep + ".")
LEVEL_ONE = "LevelOne"
CLASS_NAME = "lesson_01_01"
LEVEL_ONE_PATH = FATHER_PATH + "/" + LEVEL_ONE
LEVEL_ONE_CLASS = os.listdir(LEVEL_ONE_PATH)


IS_NEED_TO_UPDATE = False

def run():
    for item in LEVEL_ONE_CLASS:
        show_detail(LEVEL_ONE_PATH, item)


def show_detail(folder_dir, filename):
    level_num_text = folder_dir.split('/')[-1]
    level_num = str()
    if level_num_text == "LevelOne":
        level_num = "01"

    lession_num = filename.split('_')[1]
    file_dir = folder_dir + '/' + filename
    insert_list = []
    with open(file_dir, 'r') as file_to_read:
        for line in file_to_read:
            work_list = line.split('::')
            chinese = work_list[0]
            jp_only = work_list[1]
            jp_chinese = str()
            if '\n' in jp_only:
                jp_only = jp_only[:-1]
            if '\n' in jp_chinese:
                jp_chinese = jp_chinese[:-1]
            change = get_change_from_word(chinese, jp_only)
            if len(work_list) == 3:
                jp_chinese = work_list[2]
            nsj_model = NSJModel(level_num, lession_num, chinese, jp_only, jp_chinese, change)
            insert_list.append(nsj_model)
            print(nsj_model)

    if len(insert_list) != 0:
        insert_into_db(insert_list)

def get_change_from_word(chinese, japanese):
    if '[动' not in chinese:
        return str()
    ver_type = chinese[-2:-1]
    original = get_original(ver_type, japanese)
    tei = get_tei(ver_type, japanese)
    ta = get_ta(ver_type, japanese)
    nayi = get_nayi(ver_type, japanese)
    print('type:', ver_type, '-----',japanese)
    print(original)
    print(tei)
    print(ta)
    print(nayi)
    return original + "::" + tei + "::" + ta + "::" + nayi

def get_original(type, japanese):
    if type == "1":
        last_letter = japanese[-3]
        if last_letter == 'あ' or last_letter == 'い' or last_letter == 'う' or last_letter == 'え' or last_letter == 'お':
            return japanese[:-3] + 'う'
        elif last_letter == 'か' or last_letter == 'き' or last_letter == 'く' or last_letter == 'け' or last_letter == 'こ':
            return japanese[:-3] + 'く'
        elif last_letter == 'さ' or last_letter == 'し' or last_letter == 'す' or last_letter == 'せ' or last_letter == 'そ':
            return japanese[:-3] + 'す'
        elif last_letter == 'た' or last_letter == 'ち' or last_letter == 'つ' or last_letter == 'て' or last_letter == 'と':
            return japanese[:-3] + 'つ'
        elif last_letter == 'な' or last_letter == 'に' or last_letter == 'ぬ' or last_letter == 'ね' or last_letter == 'の':
            return japanese[:-3] + 'ぬ'
        elif last_letter == 'は' or last_letter == 'ひ' or last_letter == 'ふ' or last_letter == 'へ' or last_letter == 'ほ':
            return japanese[:-3] + 'ふ'
        elif last_letter == 'ま' or last_letter == 'み' or last_letter == 'む' or last_letter == 'め' or last_letter == 'も':
            return japanese[:-3] + 'む'
        elif last_letter == 'や' or last_letter == 'ゆ' or last_letter == 'よ':
            return japanese[:-3] + 'ゆ'
        elif last_letter == 'ら' or last_letter == 'り' or last_letter == 'る' or last_letter == 'れ' or last_letter == 'ろ':
            return japanese[:-3] + 'る'
        elif last_letter == 'が' or last_letter == 'ぎ' or last_letter == 'ぐ' or last_letter == 'げ' or last_letter == 'ご':
            return japanese[:-3] + 'ぐ'
        elif last_letter == 'ざ' or last_letter == 'じ' or last_letter == 'ず' or last_letter == 'ぜ' or last_letter == 'ぞ':
            return japanese[:-3] + 'ず'
        elif last_letter == 'だ' or last_letter == 'ぢ' or last_letter == 'づ' or last_letter == 'で' or last_letter == 'ど':
            return japanese[:-3] + 'づ'
        elif last_letter == 'ば' or last_letter == 'び' or last_letter == 'ぶ' or last_letter == 'べ' or last_letter == 'ぼ':
            return japanese[:-3] + 'ぶ'
        elif last_letter == 'ぱ' or last_letter == 'ぴ' or last_letter == 'ぷ' or last_letter == 'ぺ' or last_letter == 'ぽ':
            return japanese[:-3] + 'ぷ'
    if type == "2":
        return japanese[:-2] + 'る'
    if type == "3":
        if japanese == 'きます':
            return 'くる'
        if japanese == 'します':
            return 'する'
        return japanese[:-3] + 'る'


def get_tei(type, japanese):
    if type == "1":
        if japanese == 'いきます':
            return 'いって'
        last_letter = japanese[-3]
        if last_letter == 'き':
            return japanese[:-3] + 'いて'
        elif last_letter == 'ぎ':
            return japanese[:-3] + 'いで'
        elif last_letter == 'び' or last_letter == 'み' or last_letter == 'に':
            return japanese[:-3] + 'んで'
        elif last_letter == 'ち' or last_letter == 'り' or last_letter == 'い':
            return japanese[:-3] + 'って'
        elif last_letter == 'し':
            return japanese[:-2] + 'て'
    if type == "2":
        return japanese[:-2] + 'て'
    if type == "3":
        return japanese[:-3] + 'て'

def get_ta(type, japanese):
    if type == "1":
        if japanese == 'いきます':
            return 'いった'
        last_letter = japanese[-3]
        if last_letter == 'き':
            return japanese[:-3] + 'いた'
        elif last_letter == 'ぎ':
            return japanese[:-3] + 'いだ'
        elif last_letter == 'び' or last_letter == 'み' or last_letter == 'に':
            return japanese[:-3] + 'んだ'
        elif last_letter == 'ち' or last_letter == 'り' or last_letter == 'い':
            return japanese[:-3] + 'った'
        elif last_letter == 'し':
            return japanese[:-2] + 'た'
    if type == "2":
        return japanese[:-2] + 'た'
    if type == "3":
        return japanese[:-3] + 'た'

def get_nayi(type, japanese):
    if type == "1":
        last_letter = japanese[-3]
        if last_letter == 'あ' or last_letter == 'い' or last_letter == 'う' or last_letter == 'え' or last_letter == 'お':
            return japanese[:-3] + 'わない'
        elif last_letter == 'か' or last_letter == 'き' or last_letter == 'く' or last_letter == 'け' or last_letter == 'こ':
            return japanese[:-3] + 'かない'
        elif last_letter == 'さ' or last_letter == 'し' or last_letter == 'す' or last_letter == 'せ' or last_letter == 'そ':
            return japanese[:-3] + 'さない'
        elif last_letter == 'た' or last_letter == 'ち' or last_letter == 'つ' or last_letter == 'て' or last_letter == 'と':
            return japanese[:-3] + 'たない'
        elif last_letter == 'な' or last_letter == 'に' or last_letter == 'ぬ' or last_letter == 'ね' or last_letter == 'の':
            return japanese[:-3] + 'なない'
        elif last_letter == 'は' or last_letter == 'ひ' or last_letter == 'ふ' or last_letter == 'へ' or last_letter == 'ほ':
            return japanese[:-3] + 'はない'
        elif last_letter == 'ま' or last_letter == 'み' or last_letter == 'む' or last_letter == 'め' or last_letter == 'も':
            return japanese[:-3] + 'まない'
        elif last_letter == 'や' or last_letter == 'ゆ' or last_letter == 'よ':
            return japanese[:-3] + 'やない'
        elif last_letter == 'ら' or last_letter == 'り' or last_letter == 'る' or last_letter == 'れ' or last_letter == 'ろ':
            return japanese[:-3] + 'らない'
        elif last_letter == 'が' or last_letter == 'ぎ' or last_letter == 'ぐ' or last_letter == 'げ' or last_letter == 'ご':
            return japanese[:-3] + 'がない'
        elif last_letter == 'ざ' or last_letter == 'じ' or last_letter == 'ず' or last_letter == 'ぜ' or last_letter == 'ぞ':
            return japanese[:-3] + 'ざない'
        elif last_letter == 'だ' or last_letter == 'ぢ' or last_letter == 'づ' or last_letter == 'で' or last_letter == 'ど':
            return japanese[:-3] + 'だない'
        elif last_letter == 'ば' or last_letter == 'び' or last_letter == 'ぶ' or last_letter == 'べ' or last_letter == 'ぼ':
            return japanese[:-3] + 'ばない'
        elif last_letter == 'ぱ' or last_letter == 'ぴ' or last_letter == 'ぷ' or last_letter == 'ぺ' or last_letter == 'ぽ':
            return japanese[:-3] + 'ぱない'
    if type == "2":
        return japanese[:-2] + 'ない'
    if type == "3":
        if japanese == 'きます':
            return 'こない'
        return japanese[:-2] + 'ない'


def insert_into_db(model_list):
    client = pymongo.MongoClient(read_config_from_configfile().get('mongodb_url'), read_config_from_configfile().get('mongodb_port'))
    db = client["DailyProject"]
    collection = db["JPN"]
    for item in model_list:
        temp_result = collection.find_one({'chinese': item.chinese})
        if temp_result is None:
            collection.insert(item.__dict__)
            print('success insert: {}'.format(item))
        # else:
            # if IS_NEED_TO_UPDATE:
            #     collection.update()




if __name__ == '__main__':
    run()