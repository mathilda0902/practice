# anagram_palindrome 


# input: str
# output: bool 


# palindromes: racecar, mom, dad, sis 
# anagrams: bat, tab

# racecar, carerac, aaccrre 


# mmo --> return true omm, mmo, mom 

# tips: 
# 1. Please communicate 
# 2. Syntax? Ask me, or google 
# 3. Settings 
# 4. Test your code throughout 


# "carrace" 

# 7 6 5 4 3 2 1 
# _ * _ * _ * _ * _ * _ *__ 


# charCount = {}

# i 
# carraceee


# { 
# 'c': 1, 
# 'a': 1, 
# 'r': 1
#
#
# }


# valid_palindrome 


defanagram_palidrome(some_string):
string_dict = dict(list())

forletter insome_string:
ifletter notinstring_dict:
string_dict[letter]= 1
else:
string_dict[letter]+= 1

odd_counter = 0
fork,v instring_dict.items():
ifv % 2!= 0:
odd_counter += 1
# else:

ifodd_counter == 1:
returnTrue
elifodd_counter == 0:
returnTrue
else:
returnFalse


# print(anagram_palindrome("carraceee")) # True 
# print(anagram_palindrome("cutoo")) # False 


# O(N) --> 1 pass 
# O(1) --> Constant space 

# a --> paal
# ab --> not a pal
# aba --> pal 
# abac --> not aa pal

# aabaa


# b 
# f 
# abctbua


# skips = 1

# Problems to practice 
# 1. isValidPalindrome 
# 2. Reverse A string
# 3. Given two words, figure out if they're anagrams 
# 4. Print a string backwards in constant space. [::-1]

defvalid_palindrome(some_string):
skips = 0
front = 0
back = len(some_string)- 1
whilefront < back:
# if chars are not equal 
ifsome_string[front]!= some_string[back]:
# if skips is equal to or greater than 1, return False
ifskips >= 1:
returnFalse
# try skipping from the back
back -= 1
# if skipping from back doesn't work, try skipping from the front
ifsome_string[front]!= some_string[back]:
back -= 1
front += 1
# if skipping from the back and skipping from the front doesn't work, return false
ifsome_string[front]!= some_string[back]:
returnFalse
# otherwise, skipping from the front worked, increment skips
else:
skips += 1
# if skipping from back works 
else:
skips += 1
else:
front += 1
back -= 1
returnTrue

print(valid_palindrome("carraceee"))# False
print(valid_palindrome("rawr"))# True 
print(valid_palindrome("abctbua"))# False 
print(valid_palindrome("racecar"))# True 

# rraacce 


# raceeecar 

# carraccareee

# for a string to return True:
# case 1. this word same as spelled backward
# case 2. 
