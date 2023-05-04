"""16.while  else & for else.py
while else and for else not use for break
it use for continue lalso but not use for break
"""
print("while else")
i=1
while i<=5:
    print(i)
    i+=1
else:
    print("loop completed")
print("--------------------------")

#but
i=1
while i<=5:
    if(i==4):
        break
    print(i)
    i+=1
else:
    print("loop completed")
print("--------------------------")


print("For else")
for i in range (1,21):
    print(i)
else:
    print("for loop completed")
print("--------------------------")


for i in range(1,8):
    if i==5:
        continue
    print(i)
else:
    print("for loop completed")
print("--------------------------")