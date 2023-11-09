import  collections

# with open('C:\code\lki.xml') as file:
#     s:str = file.read()
#     d:dict[str, int] = {}
#     for key in s:
#         if d.get(key):
#             d[key] += 1
#         else:
#             d[key] = 1
#
#     print(d)

# with open('C:\code\lki.xml') as file:
#     s:str = file.read()
#     d:dict[str, int] = collections.defaultdict(int)
#     for key in s:
#         d[key]+=1
#     keys_sorted:list[str] = sorted(d, key=d.get, reverse=True)
#     d_sorted:dict[str, int] = {}
#     for key in keys_sorted:
#         d_sorted[key] = d.get(key)


    #print(d_sorted, type(d_sorted))

with open('C:\code\lki.xml') as file:
    s:str = file.read()
    d:dict[str, int] = collections.defaultdict(int)
    for key in s:
        d[key] +=1

    #print(key, "=", d[key])
    keys_sorted:list[str] = sorted(d, key=d.get)
    #print( "=", keys_sorted)
    d_sorted:dict[str, int] = {}
    for key in keys_sorted:
        d_sorted[key] = d.get(key)

    for key in d_sorted:
        print(key, '=', d_sorted[key])

    #print(d_sorted, type(d_sorted))





