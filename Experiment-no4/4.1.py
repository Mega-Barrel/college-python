# Write a python program to implement different file handling operations.

# Opening a file:
try:
    file = open('Experiment-no4/test.txt') 
    for i in file:
        print(file.read())

except Exception as e:
    print('Something went wrong \n', e)

finally:
    file.close()
