import os

number = int(os.environ['REACT_APP_NUMBER'])
for num in range(1,100):
    print(num * number // number)