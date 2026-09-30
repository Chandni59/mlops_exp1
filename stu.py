details=[]
def student():
    id=int(input("enter student id:"))
    n=input("Enter student name")
    m1=int(input("enter mark"))
    m2=int(input("enter mark"))
    m3=int(input("enter mark"))
    dob_id=input("enter dob")
    details.append([id,n,m1,m2,m3,dob_id])
def search(id):
    for i in details:
        if id in i:
            print(i)
def display():
    for i in details:
        print(i)
#search
while(True):
    q=input("enterr")
    if(q=="1"):
        student()
    elif(q=="2"):
        display()
    elif(q=="3"):
        id=int(input("Enter id"))
        search(id)
    else:
        break