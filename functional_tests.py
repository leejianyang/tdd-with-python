#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
"""

from selenium import webdriver

browser = webdriver.Chrome(executable_path='./chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
