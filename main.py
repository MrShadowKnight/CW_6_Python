import json

def filterLetter(letter, data):
    filter_arr = []
    for item in data:
        title = item["title"]
        if title[0].upper() == letter:
            filter_arr.append(item)
    return filter_arr

with open("products.json", "r", encoding="utf-8") as file :
    products = json.load(file)

print(filterLetter("F", products))
print(filterLetter("K", products))
print(filterLetter("M", products))


# new_arr = []
# for i in products:
#     if len(i["title"]) != 0:
#         new_arr.append(i)

# with open("products.json", "w", encoding="utf-8")as file:
#     json.dump(new_arr, file)