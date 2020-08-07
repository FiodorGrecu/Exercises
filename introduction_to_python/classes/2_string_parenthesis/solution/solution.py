class py_solution:

   def is_valid_parenthese(self, str1):
      sparantese = []
      par_char = {"(": ")", "{": "}", "[": "]"}
      for i in str1:
         if i in par_char:
            sparantese.append(i)
         elif len(sparantese) == 0 or par_char[sparantese.pop()] != i:
            return False
      return len(sparantese) == 0
print(py_solution().is_valid_parenthese("([{}])"))

      

                          