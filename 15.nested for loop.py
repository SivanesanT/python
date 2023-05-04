# 15.nested for loop
"""
*
**
***
****
*****



*****
****
***
**
*

ABCDE
ABCDE
ABCDE
ABCDE
ABCDE
"""

for i in range(6):
    for j in range(i):
        print("*", end=" ")
    print(" ")
print("______________")
for i in range(6, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print(" ")
print("______________")
for i in range(65, 70, 1):
    for j in range(65, 70, 1):
        print(chr(j), end="")
    print(" ")
