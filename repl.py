a: int=1
b: int=1
command=[]
while b>0 :
    command.append(str( input("Enter your comment:")))
    mylist=list(command)
    print("Previously entered command:")
    a=1
    for i in mylist:

        print(a,i,".")
        a=a+1
