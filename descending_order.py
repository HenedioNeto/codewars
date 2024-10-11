#Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    #create a list with the numbers
    split_num = [int(single_num) for single_num in str(num)]
    #create a definitive list
    descendig_list = []
    higher_num = 0
    while len(split_num) > 0:
         higher_num = max(split_num)
         descendig_list.append(higher_num)
         split_num.remove(higher_num)

    result = int(''.join(map(str, descendig_list)))
    print(result)

descending_order(123456789) #987654321
descending_order(15) #51
descending_order(123456789) #987654321

"""
def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))
"""