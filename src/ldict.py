##!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import display


def main():
    if len(sys.argv) < 2:
        display.help()
        sys.exit()
        
    is_speak = False # 是否发音
    is_forms = False # 是否查询格式变形
    is_web_translatation = False 
    is_example_sentences = False # 是否查询双语例句
    is_web_explains = False # 是否查询网络词组
    word = "" # 请求查询单词
    
    for x in sys.argv[1:]:
        if x == "--speak" or x == "-s":
            is_speak = True
        elif x == "--forms" or x == "-f":
            is_forms = True
        elif x == "--web-translation" or x == "-w":
            is_web_translatation = True
        elif x == "--example-sentences" or x == "-e":
            is_example_sentences = True
        elif x == "--web-explains" or x == "-c":
            is_web_explains = True
        else:
            if x[0] == "-":
                print "ldict: 未知操作, 别乱来啊... -________-'' "
                display.help()
                sys.exit()
            else:
                word = x

    display.lookup(word, is_speak, is_forms, is_web_translatation,
                   is_example_sentences, is_web_explains)
    
if __name__ == "__main__":
    main()
