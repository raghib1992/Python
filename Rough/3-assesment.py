

from ast import AnnAssign
from random import shuffle
import string


def number_list(num):
    numb = [x for x in num if x % 2 == 0]
    return numb

y = number_list([1,2,3,4,5,6,7,8,9,10])
# print(y)

#*******************#
# Guess_number = int(input("Kinldy guess the number: "))


MyList= ['','O','']

def shuffle_cup(redBall):
    shuffle(redBall)
    print(redBall)
    return redBall

def check_guess(shuffle_list, position):
    if position in [1,2,0]:
        if shuffle_list[position] == 'O':
            print("You guess correct input")
        else:
            print("Better Luck Next Time")
    else:
        print("kinldy enter your number 0,1 or 2")

# list = shuffle_cup(MyList)
# check_guess(list, Guess_number)

#*************************
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            print(b)
            return b
        else:
            print(a)
            return a
    else:
        if a < b:
            print(b)
            return b
        else:
            print(a)
            return a

# lesser_of_two_evens(3,5)
#*******************
def animal_crackers(text):
    comp = text.split()
    print(comp)
    for head, *tail in comp:
        print(head)
# animal_crackers('sam san')
#***************************

def old_macdonald(name):
    if len(name) > 3:
        print(name[:3].capitalize() + name[3:].capitalize())
    else:
        print(f"The lenght od name {name} is too short")
# old_macdonald('macdonald')
#*****************************

text = 'Hi, Am I doing good?'
# print('-'.join(text))
new_text = list(text.split())
# print(' '.join(new_text[::-1]))
#*************

def master_yoda(text):
    new_text = text.split()[::-1]
    print(" ".join(new_text))
    return " ".join(new_text)

# master_yoda('I am home')
#******************************************

list = [3, 1, 3]


# print(list.index(3))
# print(list[-1]==3)
#************************
def paper_doll(text):
    result = ''
    for char in text:
        result += char*3
    print(result)

# paper_doll('Helo')

#************************

def blackjack(a,b,c):
    if a + b + c <= 21:
        print(sum((a,b,c)))
    elif a + b +c > 21 and 11 in (a,b,c):
        print(sum((a,b,c,-10)))
    else:
        print('BUST')

# blackjack(5,7,8)

#*******************

def summer_69(arr):
    total = 0
    add = True
    for n in arr:
        while add:
            if n != 6:
                total += n
                break
            else:
                add = False
        while not add:
            if n != 9:
                break
            else:
                add = True
    print(total)

# summer_69([4, 5, 6, 7, 8, 9])
#****************
def spy_game(nums):
    for x in range(0, len(nums) -1):
        if nums[x:x+3] == [0,0,7]:
            print(True)
        else:
            pass

# spy_game([1,0,2,4,0,5,7])
#***************************

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        print(f"nums is {num} which is less than 2")
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    # return len(primes)


# count_primes(2)

#***************

def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

# print_big('b')
#**********************************************
def sqr(nums):
    print(nums**2)

# myList= [1,2,3,4,5]
# map(sqr,myList)

#**********************************************
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(s):
    x = 0
    y = 0
    for l in s: 
        if l.isupper():
            print("Upper")
            x += 1
        else:
            print("Lower")
            y += 1
    print(f"No. of Upper case characters : {x}\nNo. of Lower case Characters : {y}")


# up_low(s)
#******************



# def ispangram(str1, alphabet=string.ascii_lowercase): 
#     # Create a set of the alphabet
#     print(alphabet)
#     alphaset = set(alphabet)  
#     print(alphaset)

#     # Remove spaces from str1
#     str1 = str1.replace(" ",'')
    
#     # Lowercase all strings in the passed in string
#     # Recall we assume no punctuation 
#     str1 = str1.lower()
    
#     # Grab all unique letters in the string as a set
#     str1 = set(str1)
    
#     # Now check that the alpahbet set is same as string set
#     return str1 == alphaset

# ispangram("The quick brown fox jumps over the lazy dog")

#****************************
