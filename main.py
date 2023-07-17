import json

# def moneyExchang(hryvnia):
#     dolar = 0.027
#     dolar = hryvnia * dolar
#     dolar = round(dolar, 2)
    
#     return dolar
# print(moneyExchang(1))

# def helloWorld():
#     print ("Hello World")

# helloWorld()

# def filterLetter(letter, data):
#     filter_arr = []
#     for item in data:
#         title = item["title"]
#         if title[0].upper() == letter:
#             filter_arr.append(item)
#     return filter_arr

# with open("products.json", "r", encoding="utf-8") as file :
#     products = json.load(file)

# print(filterLetter("F", products))
# print(filterLetter("K", products))
# print(filterLetter("M", products))


# new_arr = []
# for i in products:
#     if len(i["title"]) != 0:
#         new_arr.append(i)

# with open("products.json", "w", encoding="utf-8")as file:
#     json.dump(new_arr, file)

# def square_list(numbers):
#     squared_numbers = []

#     for num in numbers:
#         squared_numbers.append(num * num)
    
#     return squared_numbers

# main_list = [1, 4, 7, 65, 34, 56, 78, 9]
# print(square_list(main_list))

# n = int(input("Введіть факторіал: "))
# factorial_number = 1
# def factorial(n):
#     while n > 1:
#         n = n -1
#         factorial_number = factorial_number * n
#     return factorial_number
    
# print(factorial(factorial_number))

# def isPolidrom(word):
#     revers_word = word[::-1]
#     if revers_word == word:
#         return True
#     else:
#         return False
    
# input("Введіть слово для перевірки (поліглоту): ")
# print(isPolidrom(velue))

# def casarCode(txt, key=3):
#     with open("alphabet.json", "r") as file:
#         alphabet_data = json.load(file)
#     code_in_number = []
#     for letter in txt:
#         for l in alphabet_data:
#             if alphabet_data[f"{l}"] == letter.lower():
#                 code_in_number.append(int(l) + int(key))
         
#     code_word = ''
#     for num in code_in_number:
#         if num <= 26:    
#             code_word += alphabet_data[f"{num}"]
#         else:
#             code_word += alphabet_data[f"{num - 26}"]
#     return code_word.capitalize



# enter_txt = "Python"
# print(enter_txt)
# print(casarCode(enter_txt))