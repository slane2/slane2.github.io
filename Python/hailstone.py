import random

#return # of values in hailstone sequence, given n to start
#pass in maximum value and call hailstone for 1... max n value
#return value w/ longest hailstone sequence

def maxHailStone (maxNum):
    nums=[]
    for n in range (1, maxNum+1):
        count = hailStone(n)
        nums.append(count)
    maxValue = max(nums)
    return maxValue, nums.index(maxValue)
#calculate sequence of #s in hailstone sequence down to 1
#do not count n itself
def hailStone():
    return random.randint(1,1000)
#for i in range (10):
#    print(hailStone(0))

print(maxHailStone(100))

#maxHailStone(100)
# x, y = 10, 9 ------ x, y = foo()
