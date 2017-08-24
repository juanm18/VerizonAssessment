def permute(str):
    #checks to see if there is a string
    if len(str) == 0:
        return ['']
    prev_list = permute(str[1:len(str)])
    new_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            #checks to for repeats
            if new_str not in new_list:
                new_list.append(new_str)
    return new_list

print(permute('ABC'));
