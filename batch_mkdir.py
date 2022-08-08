#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

# 创建的目录
path = "H:/documents/"
fruits = [
    '000 Generalities',
    '100 Philosophy & psychology',
    '200 Religion',
    '300 Social sciences',
    '400 Language',
    '500 Natural sciences & mathematics',
    '600 Technology (Applied sciences)',
    '700 The arts',
    '800 Literature & rhetoric',
    '900 Geography & history']
for fruit in fruits:  # 第二个实例
    #os.mkdir('%s%s' % (path, fruit), 0o755);
    print('path: %s%s' % (path, fruit))
