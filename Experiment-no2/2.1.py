# Write a program to implement control statement.

''' Note
1. Decision statement: if, else-if, if-else ladder.
2. Control statement: continue, break, pass.
3. loop statement: for loop, nested-for-loop, while loop, do-while loop.
'''

# 1. Continue Statement:
for letter in 'saurabhJoshi':  
    if letter == 'h' or letter == 'i': 
         continue
    print ('Current Letter :', letter) 
    var = 10

print('------------/------------')

# 2. Break Statement:
for letter in 'saurabhJoshi':  
    if letter == 'J': 
        break
    print ('Current Letter :', letter) 


print('------------/------------')

# 3. Pass Statement:
for letter in 'saurabh': 
    pass
print('Last Letter :', letter)
