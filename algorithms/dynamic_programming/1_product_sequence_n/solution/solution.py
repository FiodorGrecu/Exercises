def product_sequence_n(n):
     if n <= 1:
         return 1
     else:
         return n * product_sequence_n(n-2)
  
print(product_sequence_n(5))