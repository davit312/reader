#!/bin/python
# -*- coding: utf-8 -*-

import os,re
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description='sum the integers at the command line')
    parser.add_argument(
        '-g', '--gtts',  help='If present, use googel tts online engine' ,action='store_true')
    return parser.parse_args()

def getLang(cptx):
    am = 0
    en = 0
    ru = 0
    count = 0
    for i in cptx:
        c = ord(i)
        if c<63:
            continue
        elif c < 255:
            en += 1
        elif c<1300:
            ru +=1
        else:
            am += 1
        if count<64:
            count +=1
        else:
            break
    
    if am>ru and am>en:
        return 'am'
    elif ru>en and ru>am:
        return 'ru'
    else :
        return 'en' 
    return '0'        


def killspeach():
    os.system("touch /tmp/stoptts")
    os.system("pkill espeak ")
    os.system("pkill aplay -f")
    os.system("pkill mplayer -f")

def russianfix(text):
    text = re.sub(r'\«', "\n ", text,flags=re.MULTILINE)
    text = re.sub(r'\»', "\n ", text,flags=re.MULTILINE)
    text = text.replace('"', "\n ")
    text = text.replace("'", "\n ")
    text = text.replace('—', "\n ")
    text = text.replace('–', "\n ")
    text = text.replace('.', "\n ")
    text = text.replace('…', " ")
    text = text.replace(',', "\n ")
    text = text.replace(';', "\n ")
    text = text.replace(':', "\n ")
    text = text.replace('(', "\n ")
    text = text.replace(')', "\n ")
    text = text.replace('[', "\n ")
    text = text.replace(']', "\n ")
    text = text.replace('!', "\n ")
    text = text.replace('№', "номер ")
    text = text.replace('%', 'процент')
    text = text.replace('*', 'звездочка')
    text = text.replace('+', 'добавить')
    text = text.replace('>', 'больше чем')
    text = text.replace('<', 'меньше  чем')
    text = text.replace('=', 'равно')
    return text
