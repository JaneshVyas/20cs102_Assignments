class one:
   def newprint(self):
      print('one')
 
class two(one):
   def newprint(self):
      one.newprint(self)
      print('two')
 
o = two()
o.newprint()
