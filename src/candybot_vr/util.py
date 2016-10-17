#!/usr/bin/env python3

def rus_ascii_filter(string, additional_symbols=None):
	'''Deletes non-ascii non-russian symbols. Usefull where unicode can not be used
	Args:
		string: filtered string
		additional_symbols: additional symbol group that will be included into output_string
	Returns:
		filtered_string: string without non-ascii non-russian symbols (with considering additional symbols)
	'''
	
	russian_symbols = set("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789., ")
	if not additional_symbols is None:
		russian_symbols.update(additional_symbols)
	filtered_string = ''
	for char in string:
		if char in russian_symbols:
			filtered_string += char
	return filtered_string		

	
