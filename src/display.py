#!/usr/bin/env python
# -*- coding: utf-8 -*-

from en_engine import en_dictionary
from fanyi_engine import fanyi_dictionary

def help():
    print '''
ldict - dictionary for Linux! o(*≧▽≦)ツ 

Usage: ldict [option1] [option2]... [word]

Option		GNU long option		Meaning
-f              --forms                 查询单词其他格式
-s              --speak                 发音
-e              --example-sentences     双语例句
-c              --web-explains          网络词组
'''

def fanyi_lookup(word):
    mydictionary = fanyi_dictionary(word)
    if mydictionary.errorCode == "0":
        if mydictionary.translation == "":
            print "ldict: 呃！真的有这个词？(⊙o⊙)"
        else:
            print "\033[1;34;40m%s\033[0m" %word
            if mydictionary.phonetic != "":
                print  "\033[1;31;40m[%s]\033[0m" %mydictionary.phonetic
            print "\n有道翻译:"
            print  "\033[1;36;40m%s\033[0m" %mydictionary.translation

def display_forms(dictionary):
    word_forms = dictionary.word_forms()
    print "\t"
    for x in word_forms.keys():
        print x + ":" + word_forms[x]

def display_web_explains(word):
    myfanyi = fanyi_dictionary(word)
    if myfanyi.errorCode == "0":
        web_explains = myfanyi.web_explains()
        print "\n\033[22;36;40m网络词组:\033[0m"
        for explain in web_explains.keys():
            print  "\033[1;36;40m%s\033[0m" %explain
            for value in web_explains[explain]:
                print value
def display_web_sencences(dictionary):
    print "\t"
    print  "\033[22;36;40m双语例句:\033[0m"
    example_sentences = dictionary.example_sentence()
    for x in example_sentences.keys():
        print  "\033[1;36;40m%s\033[0m" %x
        print example_sentences[x]
        
def en_lookup(word, is_speak, is_forms, is_web_translatation,
              is_example_sentences, is_web_explains):
    mydictionary = en_dictionary(word)
    if mydictionary.return_phrase == "":
        fanyi_lookup(word)
    else:
        print "\033[1;34;40m%s\033[0m" %mydictionary.return_phrase
        if mydictionary.phonetic_symbol != None:
            print  "\033[1;31;40m[%s]\033[0m" %mydictionary.phonetic_symbol
        for x in mydictionary.cn_translation:
            print  "\033[1;36;40m%s\033[0m" %x
        if is_forms:
            display_forms(mydictionary)
        if is_web_explains:
            display_web_explains(word)
        if is_example_sentences:
            display_web_sencences(mydictionary)
        if is_speak:
            mydictionary.speak()


def lookup(word, is_speak, is_forms, is_web_translatation, is_example_sentences, is_web_explains):
    if word == "":
        print u"ldict: 要输入单词的哦！"
        sys.exit()
    if len(word) > 255:
        fanyi_lookup(word)
    else:
        en_lookup(word, is_speak, is_forms, is_web_translatation, is_example_sentences, is_web_explains)
