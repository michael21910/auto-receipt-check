import requests
import pandas as pd
from bs4 import BeautifulSoup

true = True
false = False

# the dataframe storing the receipt
info = []

# function here, read the txt file, it includes the user's receipt numbers
user_list = []
def read_file():
    with open('materials/receipt.txt') as file:
        user = file.read().split('\n')
    return user

# function here, get the prize number first
def find_prize_number():
    html = requests.get('https://invoice.etax.nat.gov.tw/')
    html.encoding = "utf-8"
    sp = BeautifulSoup(html.text, 'lxml')
    numbers_list = sp.find_all('p', 'etw-tbiggest')
    for i in range(len(numbers_list)):
        numbers_list[i] = numbers_list[i].text.strip('\n')
    numbers_list = numbers_list[0:6]
    # print(numbers_list)
    return numbers_list

# function here, detect the user's input to determine if there is a winning
def isCorrect_input(user_list):
    for string in user_list:
        isCorrect = true
        if (len(string) == 8):
            for i in range(len(string)):
                if(not('0' <= string[i] and string[i] <= '9')):
                    isCorrect = false
                    continue
        else:
            isCorrect = false
        if(isCorrect):
            prize_detect(string)
                
# function here, detect the user's input to determine if there is a winning
def prize_detect(string):
    # 判斷特別獎
    if(string == numbers_list[0]):
        info.append([string, int('10000000')])
        return
    
    # 判斷特獎
    elif(string == numbers_list[1]):
        info.append([string, int('2000000')])
        return
    
    # 判斷增開六獎
    elif(string[5:8] == numbers_list[5][0:3]):
        info.append([string, int('200')])
        return
    
    # 判斷頭獎到六獎
    else:
        for i in range(2, 5):
            if(string[0:8] == numbers_list[i][0:8]):
                info.append([string, int('200000')])
                return
            if(string[1:8] == numbers_list[i][1:8]):
                info.append([string, int('40000')])
                return
            if(string[2:8] == numbers_list[i][2:8]):
                info.append([string, int('10000')])
                return
            if(string[3:8] == numbers_list[i][3:8]):
                info.append([string, int('4000')])
                return
            if(string[4:8] == numbers_list[i][4:8]):
                info.append([string, int('1000')])
                return
            if(string[5:8] == numbers_list[i][5:8]):
                info.append([string, int('200')])
                return
    info.append([string, int('0')])
        
# input, main function
numbers_list = find_prize_number()
user_list = read_file()
isCorrect_input(user_list)

output = pd.DataFrame(info, columns = ['Your receipt number', 'The price you get'])
output = output.sort_values(['The price you get'], ascending = false)
output.index = [i + 1 for i in range(len(output))]
display(output)