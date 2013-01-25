#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import httplib2
import urllib

def login():
    username = ""
    password = ""
    filename = os.getenv("HOME") + "/.ldict/user"
    if os.path.exists(filename) == True:
        f = open(filename, 'r')
        username = f.readline().strip()
        password = f.readline().strip()
        f.close()
    else:
        username = raw_input(u"用户名:")
        password = raw_input(u"密码:")

        f = open(filename, 'w')
        f.write(username + "\n")
        f.write(password + "\n")
        f.close()
        
    url = "https://reg.163.com/logins.jsp"
    body = {
        "url":"http://account.youdao.com/login?service=dict&back_url=http%3A%2F%2Fdict.youdao.com&success=1",
        "product":"search",
        "type":"1",
        "username":username,
        "password":password,
        "savelogin":"1"
    }

    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4",
        "Content-Type":"application/x-www-form-urlencoded"
    }

    h = httplib2.Http()
    resp, content = h.request(url, method='POST', body=urllib.urlencode(body), headers=headers)
    # print resp
    cookie = resp['set-cookie']
    return cookie

def add_to_wordbook(word):
    word = urllib.quote(word)
    cookie = login()
    # 添加单词，会自动添加单词信息
    add_word_url = 'http://dict.youdao.com/wordbook/ajax?action=addword&q=' + word

    headers = {
        "Cookie":cookie,
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4",
        "X-Requested-With":"XMLHttpRequest"
    }

    h = httplib2.Http()
    resp, content = h.request(add_word_url, headers=headers)

    if content == '{"message":"adddone"}':
        print u"\n已添加 %s 到单词本 ^_^" % word
    else:
        print u"\n添加失败... ::>.<::" % word
        print content
