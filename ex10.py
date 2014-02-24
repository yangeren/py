#-*- coding:utf-8 -*-
#python 中的单双引号转义

print "I am 6'2\" tall." #将字符串中的双引号转义
print 'I am 6\'2" tall.'



tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."


fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

fat_cat1 = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print fat_cat1

#以下句子会无法运行，一直在转~
#while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" %i,
#
#print "/\n-\n|\n\\\n|\n"