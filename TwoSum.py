def twoSum():
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums = [2,7,11,15]
    #nums = [3,2,4]
    #nums = [3,3]
    target = 9
    done_flg = 0

    for locout, valout in enumerate(nums):
        for locin, valin in enumerate(nums):
            if (locout != locin) & ((valout + valin ) == target):
                #print(valout, valin)
                print(locout, locin)
                done_flg = 1
                break
        if done_flg == 1:    
            break    

twoSum()


        