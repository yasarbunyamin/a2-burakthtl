from hashlib import sha256


def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

PASSWORDHASH = "983589f68a61012b2fda3650f4de287b194ba5bfa64a0028dc97a12bdadfee03"
a: int=1
b: int=1
command=[]
while b>0 :

    command.append(str( input("Enter your comment:")))
    psw=input("enter your password:")
    if create_hash(psw)==PASSWORDHASH:
        mylist=list(command)
        print("Previously entered command:")
        a=1
        for i in mylist:

            print(a,i,".")
            a=a+1
    else:
        print("I am sorry I can’t let you do that.")