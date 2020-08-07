class py_solution:
    def roman_to_int(self, s):
        rom_val = { "I" : 1, 
                    "V" : 5,
                    "X" : 10,
                    "L" : 50,
                    "C" : 100,
                    "D" : 500,
                    "M" : 1000
        }
        ints = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                ints += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                ints += rom_val[s[i]]
        return ints 

                
