import json
user=int(input("Press 1 for login or Press 2 for signup:"))
# Signup:-
if user==2:
    name=input("Enter username:")
    password =input("Enter strong password:")
    upper,lower,digit,special=0,0,0,0
    if len(password)>=6:
        for i in password:
            if (i.isupper()):
                upper=1
            if (i.isdigit()):
                digit=1
            if (i.islower()):
                lower=1
            if(i=='@'or i=='$' or i=='_' or i=='#' or i=="!" or i=="%" or i=="^" or i=="&" or i=="*" or i=="(" or i==")"):

                special=1
        total=upper+digit+lower+special 
        if total!=4:
            print("Please use  atleast one capital letter , Smalll letter, Digit and Special character!! ")
        else:
            confirm=input("Confirm Password:")
            if password!=confirm:
                print("Please enter correct pasword!")
            else:
                hobby=input("Enter your Hobbies:")
                Designation=input("Enter your Designation:")
                Birth=input("enter your Date of Birth:")
                Gender=input("Enter your Gender:")
        
                d={}
                d["Password"]=password
                d['Hobbies']=hobby
                d["Gender"]=Gender
                d["Designation"]=Designation
                d["Date of Birth"]=Birth
                k=json.dumps(d,indent=1)
                f1=open("neha.json","a")
                f1.writelines(k)
                f1.write("\n")
                f1.write("\n")
                f1.close()
                print() 
                
                print("**Congrats",name,"You are signed up successfully**")
    else:
        print("Password is too short!")   
# login:-
elif user==1:
    name1=input("Enter your name: ")
    passw=input("Enter your Password: ")
    r=open("neha.json","r")
    j=r.read()
    if name1 in j:
        if passw in j:
            print("**You are login Successfully!**")
            print("---------------")
            print(j)

        else:
            print("Please enter correct password!!")
    else:
        print()
        print("**Please first log in your Account!**")
