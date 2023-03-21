#1
def is_two (num):
    if num == (2 or '2'):
        print('True')
    else:
        print('False')
    return num

#2
def is_vowel (ch):
    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
     or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        print('True')
    else:
        print('False')
    return ch
#3
def is_consonant (con):
    if con == ("a" or "e" or "i" or "o" or "u"):
        print ("False")
    else:
        print ("True")
    return
#4
def capitalize_consonant(word):
    vowel = ["a","e",'i','o','u']
    if word[0].lower() not in vowel:
        return word.capitalize()
    else:
        return word
#5
def calculate_tip(tip_perc, bl_total):
    tip_amount = tip_perc * bl_total
    return (tip_amount)

#6
def apply_discount(original_price, discount_percentage):
    discount_amount = original_price * (discount_percentage/100)
    discounted_price = original_price - discount_amount
    return discounted_price
#7
def handle_commas(number_string):
    number_string= number_string.replace(',',"")
    number = float(number_string)
    return number

#8
def get_letter_grade(number):
    if number >= 90:
        return 'A'
    elif number >= 80:
        return 'B'
    elif number >= 70:
        return 'C'
    elif number >= 60:
        return 'D'
    else:
        return 'F'

#9
def remove_vowels(string):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string

#10
def normalize_name(string):
    string = ''.join(i for i in string if i.isalnum() or i ==' ')
    string = string.strip()
    string = string.lower()
    string = string.replace(' ','_')
    return string

#11
from itertools import accumulate
def cumulative_sum(input_list):
    return list(accumulate(input_list))

#or

def cumulative_sum(numbers):
    cumulative_sum = []
    sum_so_far = 0
    for number in numbers:
        sum_so_far += number
        cumulative_sum.append(sum_so_far)
    return cumulative_sum