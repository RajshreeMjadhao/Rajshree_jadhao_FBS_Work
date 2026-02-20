def merge_dict(d1,d2):
    d1.update(d2)
    return d1

dict1 = {"Raji": 15, "Shree": 14}
dict2 = {"Jadhao": 12, "Gadu": 3}

print(f'Merge Dictionary: {merge_dict(dict1,dict2)}')