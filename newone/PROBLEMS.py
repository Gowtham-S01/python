

# class Solution:
#     def removeDuplicates(self, nums):
#         i = 1
#         while i != len(nums):
#             if nums[i] == nums[i - 1]:
#                 nums.pop(i)
#                 continue
#             i = i + 1
#         return len(nums)
#
#
# print(Solution().removeDuplicates([1, 1, 2]))

#
# class Solution:
#     def fizzBuzz(self, n: int):
#         l = []
#         for i in range(1, n + 1):
#             if i % 3 != 0 and i % 5 != 0:
#                 l.append(i)
#             elif i % 3 == 0:
#                 l.append('Fizz')
#             elif i % 5 == 0:
#                 l.append('Buzz')
#             elif i % 3 == 0 and i % 5 == 0:
#                 l.append('FizzBuzz')
#             else:
#                 l.append('i')
#         return l
#
#
# print(Solution().fizzBuzz(3))




# def ans(n):
#     if n<1:
#         print('DONE')
#     else:
#         ans(n-1)
#         print(n)
# ans(4)



# def fact(n):
#     assert n>=0 and int(n)==n , 'integer must be positive only'
#     if n==0:
#         return 1
#     else:
#         return n * fact(n-1)

# print(fact(-3))


# def fibo(n):
#     assert n >= 0 and int(n) == n, 'integer must be positive only'
#     if n in [0,1]:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)
# print(fibo(-7))


#
# def sum(n):
#     assert n >= 0 and int(n) == n, 'integer must be positive only'
#     if n==0:
#         return 0
#     else:
#         return (sum(int(n/10)))+int(n%10)
# print(sum(-10))



# def pow(x,n):
#     assert n >= 0 and int(n) == n, 'integer must be positive only'
#     if n==1:
#         return x    #also n==0 => ret 1
#     else:
#         return x*pow(x,n-1)
# print(pow(3,4.1))
#


# def gcd(a,b):
#     assert int(a)==a and int(b)==b , 'no neg no'
#     if a<0:
#         a=-1*a
#     if b<0:
#         b=-1*b
#     if b==0:
#         return a
#     else:
#         return gcd(b,int(a%b))
# print(gcd(48,18))



# def dectobin(x):
#     assert x >= 0 and int(x) == x, 'integer must be positive only'
#     if x==0:
#         return 0
#     else:
#         return x%2 + 10*dectobin(int(x/2))
# print(dectobin(1.3))




# def productOfArray(arr):
#     prod=1
#     for i in arr:
#         prod=prod*i
#     return prod
# print(productOfArray([1,2,3,4,6]))




# def recursiveRange(num):
#     sum=0
#     for i in range(num):
#         sum=sum+i
#     return sum
# print(recursiveRange(6))




# def flatten(arr):
#     new=[]
#     for item in arr:
#         if type(item) is list:
#             new.extend(flatten(item))
#         else:
#             new.append(item)
#     return new
# print(flatten([1,2,3,[4,5]]))
#
#
#
#
# str='hi'
# for i in str:
#     if i==str[0]:
#         str=i.upper()
# print(str)





#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# nestedEvenSum Solution

# obj1 = {
#   "outer": 2,
#   "obj": {
#     "inner": 2,
#     "otherObj": {
#       "superInner": 2,
#       "notANumber": True,
#       "alsoNotANumber": "yup"
#     }
#   }
# }

# obj2 = {
#   "a": 2,
#   "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
#   "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
#   "d": 1,
#   "e": {"e": {"e": 2}, "ee": 'car'}
# }

# def nestedEvenSum(obj, sum=0):
#     for key in obj:
#         if type(obj[key]) is dict:
#             sum += nestedEvenSum(obj[key])
#         elif type(obj[key]) is int and obj[key]%2==0:
#             sum+=obj[key]
#     return sum
# print(nestedEvenSum(obj1))



# def capitalizeWords(arr):
#     result = []
#     if len(arr) == 0:
#         return result
#     result.append(arr[0].upper())
#     return result + capitalizeWords(arr[1:])
# print(capitalizeWords(['bye mame']))




#
# def stingify(obj):
#
#     for key in obj:
#         if type(obj[key]) is int:
#             obj[key]=str(obj[key])
#         elif type(obj[key]) is dict:
#             obj[key]=str(stingify(obj[key]))
#
#     return obj
# print(stingify(obj2))
#
# #   Created by Elshad Karimov
# #   Copyright © AppMillers. All rights reserved.
#
# obj1 = {"outer": 2,"obj": {"inner": 2,"otherObj": {"superInner": 2,"notANumber": True,"alsoNotANumber": "yup"}}}
#
# def stringifyNumbers(obj):
#     # TODO
#     for key in obj:
#         if type(obj[key]) is int:
#             obj[key]=str(obj[key])
#         elif type(obj[key]) is dict:
#             obj[key]=(stringifyNumbers(obj[key]))
#
#     return obj
# print(stringifyNumbers(obj1))



# def collectStrings(obj):
#     # TODO
#     l=[]
#     for key in obj:
#         if type(obj[key]) is dict:
#             l=l+collectStrings(obj[key])
#         if type(obj[key]) is str:
#             l.append(obj[key])
#     return l


# def someRecursive(arr, cb):
#     if len(arr) == 0:
#         return False
#     if not (cb(arr[0])):
#         return someRecursive(arr[1:], cb)
#     return True
#
#
# def isOdd(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True
#
# print(someRecursive([2,4,6,8],isOdd))
# import random
#
# l=[1,2,3,4,5,6]
# random.shuffle(l)
# print(l)


# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
#
#
# def fun(m):
#     v = m[0][0]
#
#     for row in m:
#         for element in row:
#             if v < element: v = element
#
#     return v
#
#
# print(fun(data[0]))






# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     arr[i - 1] = arr[i]
# for i in range(0, 6):
#     print(arr[i], end = " ")





# def f(i, values = []):
#     values.append(i)
#     print (values)
#     return values
# f(1)
# f(2)
# f(3)
#
#
# l=[3,3,2,4]
# l.sort()
# print(l)




# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))


#
# a = {'a':1,'b':2,'c':3}
# print (a['a','b'])


# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# print(my_dict)
#
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
#
# print(sum)


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#
#         opening = '({['
#
#         pairdict = {
#             '(': ')',
#             '{': '}',
#             '[': ']'
#         }
#
#         for parenthesis in s:
#             if parenthesis in opening:
#                 stack.append(pairdict[parenthesis])
#             elif len(stack) == 0:
#                 return False
#             elif parenthesis != stack.pop():
#                 return False
#         return len(stack) == 0
# print(Solution().isValid('()[]{}'))



