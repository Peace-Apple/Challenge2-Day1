#defining the dictionary function
def dictionary(lower, upper):
    myDictionary=dict()                           #initialising a new dictionary
    for y in range(lower,upper):
        myDictionary[y]=y**2
    return myDictionary
#the main
if __name__ == '__main__':
    print(dictionary(2,15))