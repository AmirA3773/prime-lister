from math import *

def prime_lister(count):
    if count < 1:
        print("Invalid input! try again.")
        prime_lister(int(input("Please enter a positive integer: ")))
    else:
        i = 1
        j = 2
        primes_list = []
        while i <= count:
            j_list = []
            for x in range(2,floor(sqrt(j))+1):
                if j % x == 0:
                    j_list.append(x)
            if j_list == []:
                primes_list.append(j) 
                i += 1
            j += 1
        count_str = str(count)
        if count_str[-1] == "1" and count_str[-2:] != "11":
            phrase = "st"
        elif count_str[-1] == "2" and count_str[-2:] != "12":
            phrase = "nd"
        elif count_str[-1] == "3" and count_str[-2:] != "13":
            phrase = "rd"
        elif count_str[-2:] == "11" or count_str[-2:] == "12" or count_str[-2:] == "13":
            phrase = "th"
        else:
            phrase = "th"
        print("Here's a list from the 1st to the "+count_str+phrase+" prime number:")
        print(primes_list)
    
prime_lister(int(input("Please enter a positive integer: ")))

while 1:
    retry = input("Would you like to try again?\n1.Yes 2.No :")
    if retry == "2" or retry.lower() == "no":
        print("cya.")
        break
    elif retry == "1" or retry.lower() == "yes":
        prime_lister(int(input("Please enter a positive integer: ")))
    else:
        print("Wrong answer!")