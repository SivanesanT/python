# input with list in python
para=[]
print("enter the para:")

while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
print(para)
output="\n".join(para)
print(output)