
# -*- coding: utf-8 -*-

def returnRcmlFunction(x,i,j):
	dictionary={
		u'A': "@fr->draw_A(",
		u'B': "@fr->draw_B(",
		u'C': "@fr->draw_C(",
		u'D': "@fr->draw_D(",
		u'E': "@fr->draw_E(",
		u'F': "@fr->draw_F(",
		u'G': "@fr->draw_G(",
		u'H': "@fr->draw_H(",
		u'I': "@fr->draw_I(",
		u'J': "@fr->draw_J(",
		u'K': "@fr->draw_K(",
		u'L': "@fr->draw_L(",
		u'M': "@fr->draw_M(",
		u'N': "@fr->draw_N(",
		u'O': "@fr->draw_O(",
		u'P': "@fr->draw_P(",
		u'Q': "@fr->draw_Q(",
		u'R': "@fr->draw_R(",
		u'S': "@fr->draw_S(",
		u'T': "@fr->draw_T(",
		u'U': "@fr->draw_U(",
		u'V': "@fr->draw_V(",
		u'W': "@fr->draw_W(",
		u'X': "@fr->draw_X(",
		u'Y': "@fr->draw_Y(",
		u'Z': "@fr->draw_Z(",

        u'А': "@fr->draw_A(",
		u'Б': "@fr->draw_r_B(",
		u'В': "@fr->draw_B(",
		u'Г': "@fr->draw_r_Ge(",
		u'Д': "@fr->draw_r_D(",
		u'Е': "@fr->draw_E(",
		u'Ж': "@fr->draw_r_Je(",
		u'З': "@fr->draw_r_Z(",
		u'И': "@fr->draw_r_I(",
		u'Й': "@fr->draw_r_Ii(",
		u'К': "@fr->draw_K(",
		u'Л': "@fr->draw_r_L(",
		u'М': "@fr->draw_M(",
		u'Н': "@fr->draw_H(",
		u'О': "@fr->draw_O(",
		u'П': "@fr->draw_r_P(",
		u'Р': "@fr->draw_P(",
		u'С': "@fr->draw_C(",
		u'Т': "@fr->draw_T(",
		u'У': "@fr->draw_r_U(",
		u'Ф': "@fr->draw_r_F(",
		u'Х': "@fr->draw_X(",
		u'Ц': "@fr->draw_r_Ce(",
		u'Ч': "@fr->draw_r_Che(",
		u'Ш': "@fr->draw_r_Sha(",
		u'Щ': "@fr->draw_r_Shya(",
		u'Ь': "@fr->draw_soft_sign(",
		u'Ы': "@fr->draw_r_y(",
		u'Ъ': "@fr->draw_hard_sign(",
		u'Э': "@fr->draw_r_aE(",
		u'Ю': "@fr->draw_r_Yu(",
		u'Я': "@fr->draw_r_Ya(",
		u'.': "@fr->draw_Dot(",
		u',': "@fr->draw_Comm(",
		u':': "@fr->draw_two_dots(",
		u'!': "@fr->draw_Exclamation(",
		u'=': "@fr->draw_Equal(",
		u'-': "@fr->draw_Minus(",
		u'^': "@fr->draw_Roof(",
		u'/': "@fr->draw_Slash(",
		u' ': " ",
		u'\n': " "
	};
	res_string = "\n"
	if dictionary[x] != " ":
		res_string = dictionary[x] + str(i) + "," + str(j) + ");\n"
		pass
	return res_string;

def parse_line(_line, _file, j):
	for letter in xrange(0,len(_line)):
		function_string = returnRcmlFunction(_line[letter], letter, j);
		print function_string
		_file.write(function_string)
		pass
	pass


input_file = open('input_text.txt', 'r');
_file = open('text.txt', 'w')
row_num = 0
for line in input_file:
	parse_line(line.decode('utf-8'), _file, row_num)
	row_num = row_num + 1
	pass

