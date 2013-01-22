##!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from en_engine import en_dictionary

def help():
    print """
ldict - dictionary for Linux! o(*≧▽≦)ツ 

Usage: ldict [option1] [option2]... [word]

Option		GNU long option		Meaning
-f              --forms                 查询单词其他格式
-s              --speak                 发音
-e              --example-sentences     双语例句
"""

def lookup(word, is_speak, is_forms, is_web_translatation, is_example_sentences):
    if word == "":
        print u"ldict: 要输入单词的哦！"
        sys.exit()
    mydictionary = en_dictionary(word)
    if mydictionary.return_phrase == "":
        print "ldict: 呃！真的有这个词？(⊙o⊙)"
    else:
        print "\033[1;34;40m%s\033[0m" %mydictionary.return_phrase
        if mydictionary.phonetic_symbol != None:
            print  "\033[1;31;40m[%s]\033[0m" %mydictionary.phonetic_symbol
        for x in mydictionary.cn_translation:
            print  "\033[1;36;40m%s\033[0m" %x
        if is_forms:
            word_forms = mydictionary.word_forms()
            print "\t"
            for x in word_forms.keys():
                print x + ":" + word_forms[x]
        if is_example_sentences:
            print "\t"
            print  "\033[22;36;40m双语例句:\033[0m" 
            example_sentences = mydictionary.example_sentence()
            for x in example_sentences:
                for key in x.keys():
                    print  "\033[1;36;40m%s\033[0m" %key.text
                    print x[key].text + "\n"
        if is_speak:
            mydictionary.speak()


def main():
    if len(sys.argv) < 2:
        help()
        sys.exit()
        
    is_speak = False
    is_forms = False
    is_web_translatation = False
    is_example_sentences = False
    word = ""
    
    for x in sys.argv[1:]:
        if x == "--speak" or x == "-s":
            is_speak = True
        elif x == "--forms" or x == "-f":
            is_forms = True
        elif x == "--web-translation" or x == "-w":
            is_web_translatation = True
        elif x == "--example-sentences" or x == "-e":
            is_example_sentences = True
        else:
            if x[0] == "-":
                print "ldict: 未知操作, 别乱来啊... -________-'' "
                help()
                sys.exit()
            else:
                word = x

    lookup(word, is_speak, is_forms, is_web_translatation, is_example_sentences)
    
if __name__ == "__main__":
    main()
