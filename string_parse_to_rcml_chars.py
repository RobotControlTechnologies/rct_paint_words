
# -*- coding: utf-8 -*-

eng_letters = u'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

def returnSymbolName(letter,i,j):
	if letter in eng_letters:
		return letter;
	else :
		dictionary={
	        u'А': "A",
			u'Б': "r_B",
			u'В': "B",
			u'Г': "r_Ge",
			u'Д': "r_D",
			u'Е': "E",
			u'Ж': "r_Je",
			u'З': "r_Z",
			u'И': "r_I",
			u'Й': "r_Ii",
			u'К': "K",
			u'Л': "r_L",
			u'М': "M",
			u'Н': "H",
			u'О': "O",
			u'П': "r_P",
			u'Р': "P",
			u'С': "C",
			u'Т': "T",
			u'У': "r_U",
			u'Ф': "r_F",
			u'Х': "X",
			u'Ц': "r_Ce",
			u'Ч': "r_Che",
			u'Ш': "r_Sha",
			u'Щ': "r_Shya",
			u'Ь': "soft_sign",
			u'Ы': "r_y",
			u'Ъ': "hard_sign",
			u'Э': "r_aE",
			u'Ю': "r_Yu",
			u'Я': "r_Ya",

			u'.': "Dot",
			u',': "Comm",
			u':': "two_dots",
			u'!': "Exclamation",
			u'=': "Equal",
			u'-': "Minus",
			u'^': "Roof",
			u'/': "Slash",
			u' ': " ",
			u'\n': " "
		};
		return dictionary[letter];


def writeRCMLFunction(_line, _file, row_number):
	for letter in xrange(0,len(_line)):
		res_string = "\n";
		symbol = returnSymbolName(_line[letter], letter, row_number);
		if symbol != " ":
			res_string = "@fr->draw_" + symbol + "(" + str(letter) + ", " + str(row_number) + ");\n";
		_file.write(res_string);
		pass
	pass


input_file = open('input_text.txt', 'r');
_file = open('text.txt', 'w');
row_num = 0
for line in input_file:
	writeRCMLFunction(line.decode('utf-8'), _file, row_num);
	row_num = row_num + 1;
	pass

