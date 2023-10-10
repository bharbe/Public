student = {}
student =  {}
print("enter the keys abd values " , "Q for Quit")

while ( False):
    k = input("Key:")
    v = input("values:")
    if k == 'Q' and v == 'Q':
        break
    else :
        student[k] = v
print("stud dict :" , student)
