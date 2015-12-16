#!/usr/bin/env python
#coding: utf-8
import string
import random


def generate_key():
	filed = string.uppercase + string.digits
	strkey = ()
	for i in range(4):
		strkey = strkey + ("".join(random.sample(filed, 4)),)
	key = "-".join(strkey)
	return key

def create_key_list(count):
	key_list = []
	for i in range(count):
		key_list.append(generate_key())

	return key_list

def write_key_to_file(count):
	filename = "/Users/yefei/Program/python/cd-key.txt"
	fp = open(filename, 'w')
	for i in create_key_list(count):
		fp.write(i)
		fp.write('\n')
	#fp.write("\n".join(create_key_list(count)))
	fp.close()
	return 

def read_key_from_file():
	filename = "/Users/yefei/Program/python/cd-key.txt"
	key_list = []
	fp = open(filename, 'r')
	strl = fp.read()
	key_list = strl.split('\n')
	del key_list[-1]
	fp.close()
	return key_list

if __name__ == '__main__':
    write_key_to_file(20)
    print read_key_from_file()
