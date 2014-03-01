# class Parent(object):
#     """docstring for Parent"""
#     def implicit(self):
#         print "PARENT implicit()"

# class Child(Parent):
#     """docstring for Child"""
#     pass    

# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()


# class Parent(object):
#     """docstring for Parent"""
#     def override(self):
#         print "PARENT override()"

# class Child(Parent):
#     """docstring for Child"""
#     def override(self):
#         print "CHILD override()"

# dad = Parent()
# son = Child()

# dad.override()
# son.override()


# class Parent(object):
#     """docstring for Parent"""
#     def altered(self):
#         print "PARENT altered()"

# class Child(Parent):
#     """docstring for Child"""
    
#     def altered(self):
#         print "CHILD, BEFORE PARENT altered()"
#         super(Child, self).altered()
#         print "CHILD, AFTER PARENT altered()"

# dad = Parent()
# son = Child()

# dad.altered()
# son.altered()




# class Parent(object):
#     """docstring for Parent"""
#     def override(self):
#         print "PARENT override()"

#     def implicit(self):
#         print "PARENT implicit()"

#     def altered(self):
#         print "PARENT altered"

# class Child(Parent):
#     """docstring for Child"""
#     def override(self):
#         print "CHILD override"

#     def altered(self):
#         print "CHILD , BEFORE PARENT altered()"
#         super(Child, self).altered()
#         print "CHILD, AFTER PARENT altered()"

# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()

# dad.override()
# son.override()

# dad.altered()
# son.altered()

# print "-" *30

# print "PARENT implicit()"
# print "PARENT implicit()"
# print "PARENT override()"
# print "CHILD override"
# print "PARENT altered"
# print "CHILD , BEFORE PARENT altered()"
# print "PARENT altered"
# print "CHILD, AFTER PARENT altered()"




class Other(object):
    """docstring for Other"""
    def override(self):
        print "OTHER override"

    def implicit(self):
        print "OTHER implicit"

    def altered(self):
        print "OTHER altered"


class Child(object):
    """docstring for Child"""
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()

print "-" *40

print "OTHER implicit"
print "CHILD override"
print "CHILD, BEFORE OTHER altered()"
print "OTHER altered"
print "CHILD, AFTER OTHER altered()"

a = "abadslkfjaldskjflksajdflkjadl"
print list(a)