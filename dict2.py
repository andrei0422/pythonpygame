#
"""


sample_dict ={"food" : "burger",  "drink" : "water", "phone" : "android"}
print(sample_dict.keys()  )
print(sample_dict.values())


for key in sample_dict.keys():
    print(key,sample_dict [key])
if "city" in sample_dict:
    print(sample_dict["city"])

else:
    print("key does not exist")



if "drink" in sample_dict:
    print(sample_dict["drink"])

else:
    print("key does not exist")



#delete a key-value pairs

del(sample_dict["drink"])
print(sample_dict)

sample_dict ={"numbers" : "2", "library" : "book", "money" : "5$"}
print(sample_dict.keys())
print(sample_dict.values())


sample_dict["sports"]=["soccer", "basketball", "tennis", "table tennis", "icehockey"]
print(sample_dict["sports"][3])
print(sample_dict["sports"][4])


gym = {
    "jack":{
        "age":34.
        "marks": [90,85,25]}
    "andrew":{"age":39,"marks":
    [90,85]
 print(gym.keys())
print(gym.values())
 print(gym)(andrew)("marks"
"""



textbook = {"physics":400, "diary":200, "scary":450}

textbook["physics"] = 200
print(textbook)
textbook["english"] = 250
textbook["computer"] = 300
print(textbook)

bookname = input("you want a book?")
cost = textbook.get(bookname)
if cost:
    print(f"the cost of book{bookname} is {cost}")
else:
    print("we dont have that book")
     
print(textbook)