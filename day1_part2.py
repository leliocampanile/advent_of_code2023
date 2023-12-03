'''
number_words = {'one': '1', 
                'two': '2', 
                'three': '3', 
                'four': '4', 
                'five': '5', 
                'six': '6', 
                'seven': '7', 
                'eight': '8', 
                'nine':'9'
                }
'''
# using this trick to avoid issues with last letter overlap - not best solution but quickest one
number_words = {'one' : 'on1e', 
                'two' : 'tw2o', 
                'three' : 'thr3e',
                'four': 'fo4ur', 
                'five':'fi5ve',
                'six': 'si6x',
                'seven': 'sev7en',
                'eight':'ei8ght',
                'nine':'ni9ne'}

with open('input_day1.txt','r') as input_text:
    input_list = input_text.readlines()


for i in range(len(input_list)):
    for str_number, str_digit in number_words.items():
        input_list[i] = input_list[i].replace(str_number, str_digit)

numbers = []
for word in input_list:
    number = [int(x) for x in word if x.isdigit()]
    #print(number)
    if (len(number)>1):
        numbers.append(int(''.join(map(str,number[::len(number)-1])))) # get first and last
    else:
        numbers.append(int(str(number[0])*2))

print(sum(numbers))