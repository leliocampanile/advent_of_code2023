with open('input_day1.txt','r') as input_text:
    input_list = input_text.readlines()

numbers = []
for word in input_list:
    number = [int(x) for x in word if x.isdigit()]
    if (len(number)>1):
        numbers.append(int(''.join(map(str,number[::len(number)-1])))) # get first and last
    else:
        numbers.append(int(str(number[0])*2))

print(sum(numbers))
    
