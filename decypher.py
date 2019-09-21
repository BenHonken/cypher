masterstring="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz`~1!2@3#4$5%6^7&8*9(0)-_=+,<.>?:;\"\'{[}]\\| "
cypherkey=[47, 34, 38, 84, 0, 39, 67, 33, 44, 51, 20, 13, 20, 35, 66, 39, 52, 94, 56, 57, 31, 10, 4, 87, 63, 19, 38, 46, 81, 57, 6, 64, 31, 50, 83, 52, 72, 18, 46, 25, 32, 25, 67, 40, 8, 72, 70, 53, 19, 11, 61, 25, 13, 81, 19, 32, 84, 28, 67, 4, 21, 6, 21, 34, 46, 2, 67, 11, 2, 50, 77, 42, 88, 27, 55, 55, 5, 5, 64, 5, 67, 10, 72, 5, 35, 69, 38, 89, 13, 60, 89, 89, 46, 38]
def cypher(string):
	cypherstring=""
	n=0
	for char in string:
		num=masterstring.index(char)
		num-=cypherkey[n]
		if num>len(masterstring):
			num+=len(masterstring)
		cypherstring+=(masterstring[num])
		n+=1
	return cypherstring
string=input('Please input the string you would like to decode.  ')
str(string)
code=cypher(string)
print (code)
close=input('This program will close with further input. ')
