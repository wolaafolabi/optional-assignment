#Printing number_list in reverse

number_list = [7,15,68,2,19,30,15,11,29,4]

index = 0
while number_list[index:]:
    index += 1

    number_index = index - 1

for number in range(number_index, -1, -1):

    print(number_list[number])

