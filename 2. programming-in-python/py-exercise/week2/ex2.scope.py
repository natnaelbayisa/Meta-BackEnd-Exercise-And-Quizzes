# Global_Scope

my_global = 5
 
def fn1():
     enclosed_v = 8
     
     def fn2():
         local_v = 6
         
         print("Access to global", my_global)
         print("Access to local", enclosed_v)
         
     fn2()
     
fn1()  
print("Access to global", my_global)

