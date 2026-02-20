def check_key(dict, key):
    if(key in dict):
        print("key exists")
    else:
        print("key is not exists")

my_dict = {"FRN": 140, "Batch": "SEPT"}
result = check_key(my_dict, "Batch")
print(result)