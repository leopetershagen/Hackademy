import os

for root, dirs, files in os.walk("C:\\Users\\LeoPetershagen\\Desktop\\Pictures\\"):  
    for filename in files:
        print(filename)