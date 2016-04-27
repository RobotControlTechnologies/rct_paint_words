
# -*- coding: utf-8 -*-
import sys

eng_letters = u'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

def returnSymbolName(letter):
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
	for letter_position in xrange(0,len(_line)):
		res_string = "\n";
		symbol = returnSymbolName(_line[letter_position]);
		if symbol != " ":
			res_string = "    @fr->draw_" + symbol + "(" + str(letter_position) + ", " + str(row_number) + ");\n";
		_file.write(res_string);
		pass
	pass

def printUseMessage():
	print "Use: string_parse_to_rcml_chars.py input_file output_file"
	pass

if len(sys.argv) < 3:
	printUseMessage();
	raise SystemExit;
if sys.argv[1] == "" or sys.argv[2] == "":
	print "Error: Wrong argument";
	printUseMessage();
	raise SystemExit;

input_file = open(sys.argv[1], 'r');
output_file = open(sys.argv[2], 'w');

rcml_include = "include \"chars_config.rcml\"\n\
include \"chars.rcml\"\n"

rcml_function_main = "function main(){\n\
  try {\n\
    @fr = robot_fanuc;\n\
    @fr->set_integer_di(\"uframe\", UFRAME);\n\
    @fr->set_integer_di(\"tool\", UTOOL);\n\
    @fr->set_integer_di(\"payload\", PAYLOAD);\n\
    @fr->set_real_di(\"speed\", SPEED);\n\
    system.echo(\"prepare\\n\");\n\
  	@fr->prepare();\n\
	system.echo(\"Start move program\\n\");\n\
	@fr->run_program_soft(UNIVERSAL_MOVE_PNS);\n\
    system.echo(\"start draw\\n\");\n\n" 

output_file.write(rcml_include + rcml_function_main);

row_number = 0
for line in input_file:
	writeRCMLFunction(line.decode('utf-8'), output_file, row_number);
	row_number = row_number + 1;
	pass

rcml_function_main_end = "\n    @fr->stop_soft_program();\n\
    @fr->go_home();\n\
  } catch(E){\n\
    system.echo(\"Exception catched!\");\n\
    return E;\n\
  }\n\
  return 0;\n\
}\n";
output_file.write(rcml_function_main_end);
