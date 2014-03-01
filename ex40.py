# mystuff = {'apple': "I AM APPLES"}
# print mystuff['apple']

# #this goes in mystuff.py

# def apple():
# 	print "I AM APPLES!"


# import mystuff
# mystuff.apple()

# def apple():
# 	print "I AM APPLES"

# #this is just a variable

# mystuff.apple()

# print mystuff.tangerine

# print mystuff
# print 1
# #mystuff['apple'] # get appple from dict
# mystuff.apple() #get apple from the module
# mystuff.tangerine # same thing, it's just a variable


# class MyStuff(object):
# 	"""docstring for MyStuff"""
# 	def __init__(self):
# 		self.tangerine = "And now a thousand years between"

# 	def apple(self):
# 		print "I AM CLASSY APPLES"

# thing = MyStuff()
# thing.apple()
# print thing.tangerine


# #dict style
# mystuff['apple']

# #module style
# mystuff.apples()
# print mystuff.tangerine

# #class style
# thing = MyStuff()
# thing.apples()
# print thing.tangerine


class Song(object):
	"""docstring for Song"""
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line  in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
				"I don't want to get sued",
				"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
	"With pockets full of shells",])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
	