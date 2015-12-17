#!/usr/bin/env python
#coding: utf-8
import string
import re


def removePunctuation(text):
	puctuation = '!,;?:"\''
	#1.除了－意外的标点符号用空格代替。
	#2.去掉－标点，英文中可能出现xxx-xxx的单词。编程xxxxxx来保证该列表成员的内容全是数字
	text = re.sub(r'[^a-zA-Z0-9\-]',' ',text)
	text = re.sub(r'[\-]', '',text)
	print text
	return text

def statisic_words_in_file():
	filename = "/Users/yefei/Program/python/0004/en.txt"
	count = 0
	fd = open(filename, 'r')
	content = fd.read()
	content = removePunctuation(content)
	words_list = content.split()
	print words_list
	for word in words_list:
		if word.isalpha():
			count = count + 1
	return count 



if __name__ == '__main__':
	print statisic_words_in_file()