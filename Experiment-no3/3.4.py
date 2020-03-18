# Write a python program to implement different types of exception.
a = 10
b = 2
try:
    print('Resource opened')
    print(a / b)
    z = int(input('Enter a number: '))
    l1 = [0, 1, 2, 3]
    print(l1[5])
# Zero divide exception.
except ZeroDivisionError as e:
    print('Hey, you cannto divide a number by Zero.', e)

# Value exception.
except ValueError as e:
    print('Enter interger number only.', e)

# Index Exception.
except IndexError as e:
    print('Errr.. , array index is out of bound.')

# Global exception, it will catch all other exception.
except Exception as e:
    print('Something went wrong \n', e)

# The finally block will execute no matter if the try block raises a error or not.
finally:
    print('Resource closed')


# How to use Exception inside a class.
class DefaultError(Exception):
    def __init__(self):
        print('Your Marks and Attendance are less than 75... Get Serious')

class student:
    def __init__(self, name, Attendance, Marks):
        self.name = name
        self.Attendance = Attendance
        self.Marks = Marks

    def findDefaulter(self):
        try:
            if self.Attendance<75 and self.Marks<75:
                raise DefaultError()
        except DefaultError:
            print("DefaulterError")
        finally:
            print('Well done, You are doing great')

s1 = student("Saurabh", 90, 80)
s1.findDefaulter()


