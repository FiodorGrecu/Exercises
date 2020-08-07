class py_solution:

   # def __init__(self, fnc):
   #    self.fnc = fnc
   #    self.result = result
   #    self.result = []
   

   # def __call__(self):
   #    return_result = self.fnc()
   #    self.result.append(return_result)
   #    return return_result
   
   # def result(self):
   #    return self.result
      

   def pow(self,x, n):
      if n == 0:
         return 1
      elif x == 0:
         return 0
      else:
         return x * pow(x, n-1)
print(pow(2,-3))  
# print(py_solution().pow.result(3,4))