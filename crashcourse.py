# brute force (largest sum number)
def arrange():
    arr = []
    for i in range(5):
        arradd=int(input('Please Input number: '))
        arr.append(arradd)
    max_sum = float('-inf')

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            s = sum(arr[i:j+1])
            max_sum = max(max_sum, s)
    return max_sum

# print (arrange())

# brute force (max sum)

def maxsum():
    numarray=[]
    result=[]
    targetnum=int(input('Please enter target number: '))
    numofdata=int(input('Please enter how many number in array: '))

    for i in range(numofdata):
        numadd=int(input('Please enter a number for the array: '))
        numarray.append(numadd)
    
    numarray.sort(reverse=True)

    for num in numarray:
        while sum(result)+num <= targetnum:
            result.append(num)
    return result

# print (maxsum())

# hahsmap

def two_sum(nums, target):
    hashmap = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

# print(two_sum([2, 7, 11, 15], 9))

from collections import Counter

def all_non_repeating(s):
    cnt = Counter(s)
    result = [ch for ch in s if cnt[ch] == 1]
    return result if result else None

# print(all_non_repeating("pizza")) 
# print(all_non_repeating("swiss"))   
# print(all_non_repeating("aabb"))  

def coin_change_greedy(amount, coins=[25,10,5,1]):
    coins = sorted(coins, reverse=True)
    used = []
    for c in coins:
        count = amount // c
        if count:
            used.append((c, count))
            amount -= c * count
    return used

print(coin_change_greedy(63))  # [(25,2),(10,1),(1,3)]



