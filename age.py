#importing the datetime module
from datetime import datetime
#defining the function that will calculate the age
def calculate_age(yob):

    current=datetime.now().year
    age =current-int(yob)
    
    if (age<0):
        y="Your age cannot be negative"
    elif(age<18):
        y="You are a minor"
    elif(18<=age<=36):
        y="You are a youth"
    else:
        y="You are an elder"
    return(y)    

yob = int(input("Enter year of birth:"))
print (calculate_age(yob))