
def find_flames(name1, name2):
    flames = ['Friends', 'Lovers', 'Arranged Marriage', 'Marriage', 'Enemies', 'Siblings']
    count = 0
    str1_dict = {}
    str2_dict = {}
    for s in name1:
        if ord(s) > 96 and ord(s) < 123:
            if s in str1_dict:
                str1_dict[s] +=1
            else:
                str1_dict[s] = 1

    for s in name2:
        if ord(s) > 96 and ord(s) < 123:
            if s in str2_dict:
                str2_dict[s] +=1
            else:
                str2_dict[s] = 1
    arr = [ 0 for i in range(6)]

    c = 0
    for key in str1_dict:
        if key in str2_dict:
            c = c + str1_dict[key] + str2_dict[key]
        
    return flames[findfinalind(arr, count, 0)]



def findfinalind(arr, count, pos):
    count_copy = count
    c = 0
    ind = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            c+=1
        else:
            ind = i
    if(c==(len(arr) - 1)):
        return ind
    
    else:
        count = count_copy % (len(arr) - c)
        if(count == 0):
            count = len(arr) - c
        j = pos
        if ( j >= len(arr)):
            j =0
        while(count > 0):
            if( j >= len(arr)):
                j = 0
                continue
            
            if arr[j] == 0 and count == 1:
                print(j)
                arr[j] = 1
                break

            if arr[j] == 0:
                count -=1 
            j = j + 1
        return findfinalind(arr, count_copy , j+1)
