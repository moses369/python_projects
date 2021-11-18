#Replace a particular item in a Python list using a list comprehension
a_list = [['aple', 'orange'],[ 'aple', 'banana'],[ 'grape', 'aple']]
a_list[0][0] = 'juice'
a_list[1][0] = 'grey'
print(a_list)
# Returns: ['apple', 'orange', 'apple', 'banana', 'grape', 'apple']