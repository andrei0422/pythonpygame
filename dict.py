#



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


