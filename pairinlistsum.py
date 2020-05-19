#a problem I saw where you have a list of values and you want to figure out if a pair of numbers in that list equals a particular sum
#Need a way to track the last move made and not to repeat that once I find a match

def find_pairs(sum, listofnumbers):
    left = 0
    right = len(listofnumbers) - 1
    left_move = False
    pairs = []
    while(left != right):
        if(listofnumbers[left] + listofnumbers[right] > sum):
            right-=1
            left_move = False
        elif(listofnumbers[left] + listofnumbers[right] == sum):
            temp = listofnumbers[left],listofnumbers[right]
            pairs.append(list(temp))
            if(left_move):
                right-=1
                left_move = False
            else:
                left+=1
                left_move = True
        else:
            left+=1
            left_move = True
    return pairs

checking = find_pairs(8, [-1,-1,0,0,1,2,3,4,4,5,7,7,8,8,8,9,9,9])
print(checking)





