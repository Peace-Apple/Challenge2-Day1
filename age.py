#importing the datetime module
from datetime import datetime

#defining the function that will calculate the age
def calculate_age(yob):

    if (age<0):
        return "Your age cannot be negative"
    elif(age<18):
        return "You are a minor"
    elif(18<=age<=36):
        return "You are a youth"
    else:
        return "You are an elder"
    
 
current=datetime.now().year
yob = int(input("Enter year of birth:"))
age = current-int(yob)
print (calculate_age(yob))
    

   
     
    