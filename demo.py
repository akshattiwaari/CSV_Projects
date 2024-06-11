import csv
def add():
    File=open('Record.csv','w',newline="")
    Data=csv.writer(File)
    Data.writerow(['Name','City','Profession','MobileNo'])
    while True:
        Name=input('Enter Your Name :')
        City=input('Enter Your City :')
        Profession=input('Enter Your Profession :')
        MobileNo=int(input('Enter Your Mobile no :'))
        List=[Name,City,Profession,MobileNo]
        Data.writerow(List)
        Ch=input('Are you want to enter more data Y/y ? ')
        if Ch not in 'Yy':
            break
    File.close()

def read():
    File=open('Record.csv','r',newline='')
    Data=csv.reader(File)
    for i in Data:
        print(i)
    File.close()

def search_count():
    File=open('Record.csv','r',newline='')
    Data=csv.reader(File)
    Ch=input('Enter City :')
    Count=0
    next(Data)
    for i in Data:
        if i[1]==Ch:
            print(i)
            Count+=1
    print('Peoples who are from this city :',Count)
    File.close()

#add()
#read()
#search_count()

