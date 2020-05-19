#a problem I saw where you have a list of values and you want to figure out if a pair of numbers in that list equals a particular sum

def find_pairs(sum, listofnumbers):
    left = 0
    right = len(listofnumbers) - 1
    pairs = []
    while(left != right):
        if(listofnumbers[left] + listofnumbers[right] > sum):
            right-=1
        elif(listofnumbers[left] + listofnumbers[right] == sum):
            temp = listofnumbers[left],listofnumbers[right]
            pairs.append(list(temp))
            left+=1
        else:
            left+=1
    return pairs

checking = find_pairs(8, [1,2,3,4,4,5,7])

print(checking)

