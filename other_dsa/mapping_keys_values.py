arr = ["viv", "takleya", "viv", "somi", "somi", "takleya", "lulu"]

obj={}
for i in range(len(arr)):
    if(arr[i] in obj):
        obj[arr[i]] = obj[arr[i]] + 1
    else:
        obj[arr[i]] = 1
print(obj)