#importing the datetime module
from datetime import datetime

#defining the function that will calculate the age
def calculate_age(yob):
    current=datetime.now().year
    age=current-int(yob)
    if (age<0):
        return "Your age cannot be negative"
    elif(age<18):
        return "You are a minor"
    elif(18<=age<=36):
        return "You are a youth"
    else:
        return "You are an elder"
    
 
if __name__=='__main__':
    
    yob = int(input("Enter year of birth:"))

    print (calculate_age(yob))
    

   
     
    