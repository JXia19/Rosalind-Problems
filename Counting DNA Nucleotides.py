# Author: Jing Xia
# Date: June 13th, 2022
# This program determines the numbers of A, C, G, and Ts from a sequence.

test_str = input("Enter your sequence here:")

count_A = 0
count_T = 0
count_C = 0
count_G = 0

for i in test_str:
    if i == 'A':
        count_A = count_A + 1
    elif i == 'G':
        count_G = count_G +1
    elif i == 'C':
        count_C = count_C +1
    elif i == 'T':
        count_T = count_T + 1

result = "There are {A} 'A's, {C} 'C's, {G} 'G's, and {T} 'T's."\
         .format(A = count_A, C = count_C, G = count_G, T = count_T)

print (result)
