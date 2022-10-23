a = 5
class A:
      a = 7
      pass

class B(A):
      pass

class C(B):
      pass

c = C()
print(c.a)

class A:
      def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   pass

class D(C, A, B):
   pass

d = D()
print(d.a)

