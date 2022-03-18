# Gabriel Solomon, 2020

import json

#
# this is a relative path to the .json data file
# you can also use a "full" or "absolute path" to the file
# windows and mac paths are different.  You should google and youttube to learn about paths if you are
# not familiar with them.  They are important fundamental computer concepts.
#
# this is a full windows path, note the forward slashes "/" used in python
# pathToFile = "E:/Users/jerome/GitHub/evc-cit134a-python/birthday/birthday.json"
#
# mac (which is built on linux) and linux paths are like this: "a/b/c/d/e/f.json"
#



#Function which takes the user name as input and find the name in the json file
def Finder(name):
    #Here i added the direct name of the file you can use the relative path as per your given code
    try:
        jsonFile = open("birthday.json", 'r')
    except OSError:
        exit(-1)

    # read the whole json file into a variable
    birthdayList = json.load(jsonFile)

    #Main loop for the finding the name
    for elem in birthdayList:
        if(name == elem["name"]):
            birthday = elem["birthday"]
            print("name = " + name)
            print("birthday = " + birthday)
            exit(0)

    print("Lupita does not have any friends that match this name")




# to get user input
name = input("Enter a name:")
Finder(name)
