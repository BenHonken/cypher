import random
masterstring="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz`~1!2@3#4$5%6^7&8*9(0)-_=+,<.>?:;\"\'{[}]\\| "
cypherkey=[]
while len(cypherkey)<len(masterstring):
        num=random.randint(0, len(masterstring)-1)
        cypherkey.append(num)
print(cypherkey)
input('Here is your key.  This program will close with further input. ')
