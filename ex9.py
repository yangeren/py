
# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months
print "*" * 20
print "Here are the days: %r " % days
print "Here are the months: %r" % months
print "list\\" #双反斜杠可以打印出一个\，但如果一个的话，会报错。
 
print """
There's something going on here. 
With the three double-quotes. 
We'll be able to type as much as we like. 
Even 4 lines if we want, or 5, or6.
"""