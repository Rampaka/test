import os

for num in range(1,1000):
    print(num * int(os.environ['REACT_APP_NUMBER']))