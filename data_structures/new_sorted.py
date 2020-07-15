from functools import cmp_to_key 
  
def customComparator(a, b): 
      
    octetsA = a.address.strip().split(".") 
    octetsB = b.address.strip().split(".") 
    # print(octetsA)
    # print(octetsB)
    if octetsA == octetsB: 
        return 0
    elif int(octetsA[0]) > int(octetsB[0]): 
        return 1
    elif int(octetsA[0]) < int(octetsB[0]): 
        return -1
    elif int(octetsA[1]) > int(octetsB[1]): 
        return 1
    elif int(octetsA[1]) < int(octetsB[1]): 
        return -1
    elif int(octetsA[2]) > int(octetsB[2]): 
        return 1
    elif int(octetsA[2]) < int(octetsB[2]): 
        return -1
    elif int(octetsA[3]) > int(octetsB[3]): 
        return 1
    elif int(octetsA[3]) < int(octetsB[3]): 
        return -1

def my_sorted(list_entries):

    list_entries = sorted(list_entries, key = cmp_to_key(customComparator)) 
    # print(*list_entries)
    return list_entries 