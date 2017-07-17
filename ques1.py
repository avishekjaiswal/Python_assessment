class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg

try:
   raise Networkerror("Run Time Error")
except Networkerror,e:
   print e.args