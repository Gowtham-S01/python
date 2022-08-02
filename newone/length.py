# lst=[1,2,3]
# print(len(lst))

# lst1=[6,69,79,100]
# print(max(lst1))
# print(min(lst1))

# lst2=['A','B','C']
# n=input('Enter var')
# if n in lst2:
#     print (True)
# else:
#     print (False)

# lst=[1,2,3,4]
# lst.reverse()
# print(lst)

#
# lst=[3,5,7,9,8]
# x=0
# for i in range(len(lst)):
#    x=x+lst[i]
# avg=x/len(lst)
# print(x)
# print(avg)

# lst=[1,2,3,4,1,3,5]
# d={}
# for i in range(len(lst)):
#     x=lst[i]
#     c=0
#     for j in range(i,len(lst)):
#         c=lst.count(x)
#     count=dict({x:c})
#     if x not in d.keys():
#         d.update(count)
# print(d)


# lst=[1,2,3,4,5,6]
# m=1
# for i in range(len(lst)):
#     m=m*lst[i]
#
# print('mul',m)

# lst=[1,3,-5,4,-7]
# pos=[]
# neg=[]
# for i in range(len(lst)):
#     if lst[i]>=0:
#         pos.append(lst[i])
#     else:
#         neg.append(lst[i])
# print(pos)
# print(neg)


# lst=[1,2,3,4,2,6]
# o=0
# e=0
# for i in range(len(lst)):
#     if lst[i]%2==0:
#         e+=1
#     else:
#         o+=1
# print("odd",o)
# print("even",e)


# l=[1,2,3]
# m=[2,3,4]
# for i in range(len(l)):
#
#     l.append(m[i])
# print(l)


# lst=[1,2,3,3,4,5]
# lst1=[]
# c=0
# for i in lst:
#     if i not in lst1:
#
#         lst1.append(i)
# print(lst1)


# 10


# lst=["Kousik","Gowtham","Dhaaru"]
# for i in lst:
#         if i[0]=='K':
#             print(i)


# sentences = "I love my country . My country is the best in the world . We have the best athletes in the world ."
# sen_map = {}
# sentences = sentences.lower()
# sentences=sentences.split()
# print(sentences)
# for i in sentences:
#     if i not in sen_map:
#         sen_map[i] = 0
#     sen_map[i] += 1
# print(sen_map)


# students = [{'Name': 'John Smith', 'Age': 12, 'Score': 90},
#            {'Name': 'Laila Jones', 'Age': 11, 'Score': 82},
#            {'Name': 'Omar Martinez', 'Age': 10, 'Score': 70},
#            {'Name': 'Romana Raha', 'Age': 13, 'Score': 71}]
#
# temp=[]
# for i in range(len(students)):
#     temp.append(students[i]['Score'])
# print(temp)
# temp.sort()
# temp.reverse()
# print(temp)
# final_list=[]
# for e in temp:
#
#     for i in range(len(students)):
#
#
#         if e==students[i]['Score']:
#             final_list.append(students[i])
#             break
#
# print(final_list)
#
#


#
# d={'a':5 , 'b':4,'c':3,'d':2}
# d1={}
# for e in sorted(d.keys()):
#     d1[e]=d[e]
#
# print(d1)

# d={'a':5,'b':4,'c':3,'d':2}
# p=d.values()
# s=0
# for e in p:
#    s+=e
# print(s)


# import sys
#
# d={'a':5 , 'b':4,'c':3,'d':2}
# print(sys.getsizeof(d)/1024,'kbytes')


#
# students = [{'Name': 'John Smith', 'Age': 12, 'Score': 90},
#            {'Name': 'Laila Jones', 'Age': 11, 'Score': 82},
#            {'Name': 'Omar Martinez', 'Age': 10, 'Score': 70},
#            {'Name': 'Romana Raha', 'Age': 13, 'Score': 71}]
#
# from operator import *
# print (sorted(students,key=itemgetter("Age")))


# d1={'a':1 , 'b':2 ,'c':3}
# d2={'d':4 ,'e':5 ,'f':6}
# d1.update(d2)
# print(d1)
# d1.clear()
# print(d1)


# students = [{'Name': 'John Smith', 'Age': 12, 'Score': 90},
#            {'Name': 'Laila Jones', 'Age': 11, 'Score': 82},
#            {'Name': 'Omar Martinez', 'Age': 10, 'Score': 70},
#            {'Name': 'Romana Raha', 'Age': 13, 'Score': 71}]
#

# A={'Grade': 'A'}
# B={'Grade':'B'}
# C={'Grade':'C'}
# for i in range(len(students)):
#     if students[i]['Score']>=90:
#         students[i].update(A)
#     elif students[i]['Score']>=80:
#         students[i].update(B)
#     elif students[i]['Score']>=70:
#         students[i].update(C)
#
#
# print(students)
# s=0
# for e in range(len(students)):
#     s=s+students[e]['Score']
#
# print("avg",s/len(students))
# if s>=90:
#     print("Total Grade",A)
# elif s>=80:
#     print("Total Grade",B)
# elif s>=70:
#     print("Total Grade",C)


# #[i]
# from collections import OrderedDict
#
# iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])
#
# # inserting items in starting of dict
# iniordered_dict.update({'manjeet': '3'})
# iniordered_dict.move_to_end('manjeet', last=True)
#
# # print result
# print("Resultant Dictionary : "+str(iniordered_dict))
#
#
#
#
#
# #[ii]
#
# from collections import OrderedDict
#
# # initialising ordered_dict
# ini_dict1 = OrderedDict([('akshat', '1'), ('nikhil', '2')])
# ini_dict2 = OrderedDict([("manjeet", '4'), ("akash", '4')])
#
# # adding in beginning of dict
# both = OrderedDict(list(ini_dict2.items()) + list(ini_dict1.items()))
#
# # print result
# print("Resultant Dictionary :" + str(both))
#
#
#


# d={'a':1,'b':2}
# print(d.items())


# Function to check if string follows order of
# characters defined by a pattern
# from collections import OrderedDict
#
#
# def checkOrder(input, pattern):
#     # create empty OrderedDict
#     # output will be like {'a': None,'b': None, 'c': None}
#     dict = OrderedDict.fromkeys(input)
#
#     # traverse generated OrderedDict parallel with
#     # pattern string to check if order of characters
#     # are same or not
#     ptrlen = 0
#     for key, value in dict.items():
#         if (key == pattern[ptrlen]):
#             ptrlen = ptrlen + 1
#
#         # check if we have traverse complete
#         # pattern string
#         if (ptrlen == (len(pattern))):
#             return True
#
#     # if we come out from for loop that means
#     # order was mismatched
#     return False
#
#
# if __name__=="__main__":
#     input = 'kousic'
#     pattern = 'kcs'
#     print(checkOrder(input, pattern))

# import array as ar
# ar1 = ar.array('i',[1, 120, 10, 20, 40, 80])
# ar2 = ar.array('i',[6, 7, 20, 80, 120])
# ar3 = ar.array('i',[3, 4, 15, 20, 30, 70, 80, 120])
# arr=ar.array('i',[])
# for i in ar1:
#     for e in ar2:
#         for t in ar3:
#             if i==e==t:
#                 arr.append((i))
# print(arr)
#
#
from collections import Counter

#
# votes = ["john", "johnny", "jackie",
#          "johnny", "john", "jackie",
#          "jamie", "jamie", "john",
#          "johnny", "jamie",
#          "john"]
#
# c=Counter(votes)
# print(c)
#
# s=max(c.values())
# print(s)
#
# for key,values in c.items() :
#     if values==s:
#         print(key)


# dic = {'Gfg':[5, 7, 9, 4, 0], 'is': [6, 7, 4, 3, 3],'Best': [9, 9, 6, 5, 5,7,7,3,3,4,4]}
#
# max=0
# mkey=None
# for i in dic:
#     if len(set(dic[i]))>max:
#         max=len(set(dic[i]))
#         mkey=i
# print(mkey)


#
# from collections import Counter
# d='kousikmuthukumar'
# c=Counter(d)
# print(c)
#
# for key,values in c.items():
#
#     if values >1:
#         print(key)
#
# from collections import Counter
#
#
# def find_dup_char(input):
#     # now create dictionary using counter method
#     # which will have strings as key and their
#     # frequencies as value
#     WC = Counter(input)
#     j = -1
#
#     # Finding no. of occurrence of a character
#     # and get the index of it.
#     for i in WC.values():
#         j = j + 1
#         if (i > 1):
#             print
#             WC.keys()[j],
#
#
# # Driver program
# if __name__ == "__main__":
#     input = 'geeksforgeeks'
#     find_dup_char(input)


# test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
# import collections
# m=Counter(test_list)
# print(m)
# l=[]
# for key,values in m.items():
#     m[key]=list(values*str(key))
#     sorted(m)
# print(str(dict(m)))


#
# # Python3 code to demonstrate working of
# # Group Similar items to Dictionary Values List
# # Using defaultdict + loop
# from collections import defaultdict
#
# # initializing list
# test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
#
# # printing original list
# print("The original list : " + str(test_list))
#
# # using defaultdict for default list
# res = defaultdict(list)
# for ele in test_list:
#     # appending Similar values
#     res[ele].append(ele)
#
# # printing result
# print("Similar grouped dictionary : "+str (dict(res)))


# str = "geeksforgeeks"
# k=int(input())
# l=list(str)
# n=Counter(l)
# #print(n)
# #print(l)
# l1=[]
# for key, values in n.items():
#     if values==1:
#         l1.append(key)
# #print(l1)
# print("kth time non repeating ele ",l1[k-1])
# #else can be used


#
# l=['Gfg','is','best']
# subs_dict = {'best' : [5, 6, 7], 'is' : [7, 4, 2]}
# k=int(input("e"))
#
# l1=[]
# for e in  l:
#     if e in subs_dict.keys():
#         l1.append(subs_dict[e][k])
#     else:
#         l1.append(e)
# print(l1)


#
# test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
# del test_dict['Arushi']
# print(test_dict)


# Python3 code to demonstrate working of
# Replace words from Dictionary
# Using split() + join() + get()

# # initializing string
# test_str = 'geekforgeeks best for geeks'
#
# # printing original string
# print("The original string is : " + str(test_str))
#
# # lookup Dictionary
# lookp_dict = {"best": "good and better", "geeks": "all CS aspirants"}
#
# # performing split()
# temp = test_str.split()
# res = []
# for wrd in temp:
#     # searching from lookp_dict
#     res.append(lookp_dict.get(wrd, wrd))
#
# res = ' '.join(res)
#
# # printing result
# print("Replaced Strings : " + str(res))


# l=[12, 35, 9, 56, 24]
# t=l[0]
# l[0]=l[len(l)-1]
# l[len(l)-1]=t
#
# print(l)


# l =['Gfg', 'is', 'best', 'for', 'Geeks']
# # p1=1
# # p2=3
# # l[p1-1],l[p2-1]=l[p2-1],l[p1-1]
# l1=[ s.replace('G',' ').replace('e','G').replace(' ','e')for s in l]
# print(l1)
#

# # Python3 program to swap elements
# # at given positions
#
# # Swap function
# def swapPositions(list, pos1, pos2):
#     # popping both the elements from list
#     first_ele = list.pop(pos1)
#     second_ele = list.pop(pos2 - 1)
#
#     # inserting in each others positions
#     list.insert(pos1, second_ele)
#     list.insert(pos2, first_ele)
#
#     return list
#
#
# # Driver function
# List = [23, 65, 19, 90]
# pos1, pos2 = 1, 3
#
# print(swapPositions(List, pos1 - 1, pos2 - 1))


# from collections import Counter
#
# l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
# d = Counter(l1)
# print(d)
#
# new_list = list([item for item in d if d[item]>1])
# print(new_list)


# d={'a':1,'b':2}
# for item in d :
#     if d[item]=='b':
#         print(print(d[item])


# l=[1,2,3,4]
# del l[0]
# print(l)


# test_list = [5, 6, [], 3, [], [], 9]
# for i in test_list:
#         if i!=[]:
#             pass
#         else:
#             del i
# print(test_list)


# test_list = ['Gfg', 3, 'is' , 8]
# key_list = ['name', 'id']
#
# final_list = []
# for i in range(0, len(test_list), 2):
#     print(i)
#     d = {}
#     d[key_list[0]] = test_list[i]
#     d[key_list[1]] = test_list[i+1]
#     print(d)
#     final_list.append(d)

# print(final_list)


# [{"name": "Gfg", "id": 3}, {"name": "is", "id": 8}]


# Python 3 code to demonstrate
# Uncommon elements in List
# using naive method

# # initializing lists
# test_list1 = [[1, 2], [3, 4], [5, 6]]
# test_list2 = [[3, 4], [5, 7], [1, 2]]
#
# # printing both lists
# print("The original list 1 : " + str(test_list1))
# print("The original list 2 : " + str(test_list2))
#
# # using naive method
# # Uncommon elements in List
# res_list = []
# for i in test_list1:
#     if i not in test_list2:
#         res_list.append(i)
# for i in test_list2:
#     if i not in test_list1:
#         res_list.append(i)
#
# # printing the uncommon
# print("The uncommon of two lists is : " + str(res_list))


# # Python 3 code to demonstrate
# # Uncommon elements in Lists of List
# # using map() + set() + ^
#
# # initializing lists
# test_list1 = [ [1, 2], [3, 4], [5, 6] ]
# test_list2 = [ [3, 4], [5, 7], [1, 2] ]
#
# # printing both lists
# print ("The original list 1 : " + str(test_list1))
# print ("The original list 2 : " + str(test_list2))
#
# # using map() + set() + ^
# # Uncommon elements in Lists of List
# res_set = set(map(tuple, test_list1)) ^ set(map(tuple, test_list2))
# res_list = list(map(list, res_set))
#
# # printing the uncommon
# print ("The uncommon of two lists is : " + str(res_list))


# str = 'geeks quiz practice code'
# w=str.split(' ')
# print(w)
# c=reversed(w)
# m=' '.join(c)
# print(m)


# str ='GeeksForGeeks'
# i=5
# print(len(str))
# new=str.replace('s','',1)
#
# print(new)


# #without spaces
# test_str = 'geeksforgeeks 33 is   best'
# r=sum(map(len,test_str.split(' ')))
# print(r)


# s="I am Kousik"
# s = s.split(' ')
# for w in s:
#
#     if len(w)%2==0:
#         print(w)
#


# str = 'geeksforgeek'
#
# h=len(str) // 2
# print(h)
# res=''.join([str[i].upper() if i >=h else str[i] for i in range(len(str))])    #''.join([test_str[idx].upper() if idx >= hlf_idx else test_str[idx] for idx in range(len(test_str))])
#
# print('result',res)
#
#
#
#
#
#
# # Python3 code to demonstrate working of
# # Uppercase Half String
# # Using list comprehension + join() + upper()
#
# # initializing string
# test_str = 'geeksforgeeks'
#
# # printing original string
# print("The original string is : ",(test_str))
#
# # computing half index
# hlf_idx = len(test_str) // 2
#
# # join() used to create result string
# res = ''.join([test_str[idx].upper() if idx >= hlf_idx else test_str[idx]
#                for idx in range(len(test_str))])
#
# # printing result
# print("The resultant string" ,res)


# str = 'geeksforgeeks'
# g = ''
# for w in str :
#     if w==str[0]:
#         g = g + str[0].upper()
#     elif w==str[-1]:
#         g =  g + str[-1].upper()
#     else:
#         g = g + w
# print(g)


# print(s[:-1] + s[-1].upper(), s.title())

# print(type(r))
# print( s[0].upper()+ s[1:-1]+ s[-1].upper())


#
# s='welcomeourco89untry'
#
# def check():
#     c1 = False
#     c2 = False
#     for i in range(len(s)):
#         # print(type(s[i]), s[i])
#         if s[i].isdigit():
#             c1=True
#         if s[i].isalpha():
#             c2= True
#     return c1 and c2
#
# print(check())


#
# s='BeeIaaghiObhkl'
# v=set('aeiou')
# str=s.lower()
# s1=set({})
#
# for i in str:
#
#     if i in v :
#         s1.add(i)   #update()
#
# if len(v)==len(s1):
#     print("true")
# else:
#     print("f")
#
# #
# # s1.update(v)
# # print(s1)


# str1='abcdef'
# str2='defghai'
# l=[]
#
# for i in str1:
#     for j in str2:
#         if i == j :
#             l.append(i)
# print(l)
# print(len(l))
#
# s1=set(str1)
# s2=set(str2)
# m=s1 & s2
# print(m)
# print(len(m))
#
#


#
# str1='Hello World'
# str2='aeiou'
# str1=str1.lower()
# l=[]
#
# for i in str1:
#     for j in str2:
#         if i == j :
#             l.append(i)
# print(l)
# print(len(l))


# from collections import Counter
# str1='womennn'
# str1=str1.lower()
# d=Counter(str1)
# print(d)
# s=[]
# for key,values in d.items():
#     if values==1:
#         s.append(key)
# print(s[0])
# s.sort()
# print(s[0])


# from collections import Counter
# str1='womenn'
# str1=str1.lower()
# d=Counter(str1)
# print(d)
# s=[]
# for key,values in d.items():
#     if values%2!=0:
#         s.append(key)
# print(s)


# # Python3 code to demonstrate working of
# # Odd Frequency Characters
# # Using list comprehension + Counter()
# from collections import Counter
#
# # initializing string
# test_str = 'geekforgeeks is best for geeks'
#
# # printing original string
# print("The original string is : " + str(test_str))
#
# # Odd Frequency Characters
# # Using list comprehension + Counter()
# res = [ chr for chr, count in Counter(test_str).items() if count &  ]
#
# # printing result
# print("The Odd Frequency Characters are : " + str(res))


# from collections import Counter
#
# l = 'geeksforgeeks is best for geeks'
# # l1=str(l[0])
# # print(l1)
# chr= ['e','b','g','f']
# dic=Counter(l)
# s={}
# for key,values in dic.items():
#     for i in chr:
#         if i == key:
#             s[key] = values
# print(s)


# #
# str='''The above code gives the starting index and the ending index of the string portal. \n3
#
# # Note: Here r character (r’portal’) stands for raw, not regex. The raw string is slightly different from a regular string, it won’t interpret the \ character as an escape character. This is because the regular expression engine uses \ character for its own escaping purpose.
# #
# # Before starting with the Python regex module let’s see how to actually write regex using metacharacters or special sequences. '''
# count=0
# for i in str:
#     if i.isdigit():
#         count+=1
# print(count)
#


# import re
#
# pattern = '^a...s$'
# test_string = 'abyss'
# res=re.match(pattern,test_string)
#
# if res:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")


# str='Geeks$For$Geeks'
# count=0
# for i in str :
#     print(i)
#     if i.isalpha() or i.isdigit():
#         pass
#     else:
#         count=count+1
#     print(count)
# if count>1:
#     print('spec char present')
# else:
#     print('no spec char')


# import re
#
# txt='GeeksFor_!@#$%^&*()Geeks'
# pattern='[@_!#$%^&*()<>?/\|}{~:]'
#
# result=re.search(pattern,txt)
# if result:
#     print('yes spec')
# else:
#     print('no spec')


#
# help_dict = {
#     'one': '1',
#     'two': '2',
#     'three': '3',
#     'four': '4',
#     'five': '5',
#     'six': '6',
#     'seven': '7',
#     'eight': '8',
#     'nine': '9',
#     'zero' : '0'
# }
# num=""
# test_str = "zero four zero one"
# test_str=test_str.split(' ')
# for i in test_str:
#     for key,values in help_dict.items():
#
#         if i==key:
#             num=num+values
# print(num)


# import re
# str='geeksforgeeks is best for geeks'
#
# print(str)
# wor='best'
# str=str.split()
# res = str.index(wor) + 1
#
# print(res)


# str='geekksforgggeeks'
# l=[]
# print(len(str))
# for i in range(len(str)):
#     print(i)
#     c=1
#     if i<len(str)-1:
#         if str[i]==str[i+1]:
#             c+=1
#             l.append(c)
#             i = i+1
#             print(i)
#         else:
#             l.append(c)
#
#     else:
#         pass
#
# print(l)

# def _check(str, i, count):
#     if str[i] == str[i + 1]:
#         count = count + 1
#         l.append(count)
#         i = i + 1
#         print("$$$$$$$$$$$$",str[i])
#         _check(str, i, count)
#
#     return i
#
#
# str = 'geekkksf'
# print(len(str))
# l = []
# i = 0
# while i < len(str):
#     print(i)
#     count = 1
#     if i < len(str) - 1:
#         print("@@@@@", i, str[i])
#         if str[i] == str[i + 1]:
#             count = count + 1
#             l.append(count)
#             i = i + 1
#             i = _check(str, i, count)
#             # print(i)
#         else:
#             l.append(count)
#     else:
#         l.append(count)
#     i = i + 1
#
# print(l)

# import re
# st='geekksforgggeeks'
# s=re.finditer(r'(.)\1*',st)
# for i in s:
#     print(len(i.group()))

# import re
#
# # initializing string
# test_str = "geekksforgggeeks"
#
# # printing original string
# print("The original string is : " + test_str)
#
# # Consecutive characters frequency
# # Using regex
# res = [len(sub.group()) for sub in re.finditer(r'(.)\1*', test_str)]
#
# # printing result
# print("The Consecutive characters frequency : " + str(res))


# s = "GeeksforGeeks"
# d=2
#
# l=[]
# for i in s:
#     l.append(i)
# print(l)
# print(s)
# sre=''
# for i in range(d):
#     li=l.pop(i)
#     sre=sre+li
# print(sre)
# print(l)
# n=''
# for j in l:
#     n=n+j
#
# n=n+sre
# print(n)


# s = "GeeksforGeeks"
# d=2
# l1st=s[0:d]
# l2nd=s[d:]
# r1st=s[0:len(s)-d]
# r2nd=s[len(s)-d:]
# print(l2nd+l1st)
# print(r2nd+r1st)

#
# def check(s, i, count):
#     if i < (len(s) - 1):
#         if s[i] == s[i + 1]:
#
#             count += 1
#             i += 1
#             print(i)
#         else:
#             _list.append(count)
#
#             print(i, s[i], count)
#             i+=1
#             count = 1
#
#     else:
#         print(i,s[i],count)
#         _list.append(count)
#         return _list
#
#     return check(s, i, count)
#
#
# s = "gggkkksfftttt"
# i = 0
# count = 1
# _list = []
# _list= check(s, i, count)
# print(_list)


########    SETS  #########


# import sys
# Set1 = {"A", 1, "B", 2, "C", 3}
# Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
# Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}
# s=sys.getsizeof(Set3)
# print(s,'kb')

# s=Set3.__sizeof__()
# print(s)


# s=set((12, 10, 13, 15, 8, 9))
# v=s.copy()
# print(v)
# # print(s[0])
# for i in s:
#
#     v.remove(i)
#     print(set(v))


# a = [1, 2, 3, 4, 5]
# b = [5,6, 7, 8, 9]
# def eq():
#     for i in a:
#         for j in b:
#             if i==j:
#                 return True
#     return False
#
# print(eq())


# Python program to check
# if two lists have at-least
# one element common
# using set and property

# def common_member(a, b):
#     a_set = set(a)
#     b_set = set(b)
#     if (a_set & b_set):
#         return True
#     else:
#         return False
#
#
# a = [1, 2, 3, 4, 5]
# b = [5, 6, 7, 8, 9]
# print(common_member(a, b))
#
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9]
# print(common_member(a, b))


# s = {'a', 'b', 'c', 'd'}
# print(type(s))
# v=str(s)
# print(v)
# print(s)
# print(type(v))
# s.update()
# v.up

#
# set = {1, 2, 3, 4, 5}
# d=dict.fromkeys(set,5)
# print(d)


# arr = [[1, 2, 2, 4, 3, 6],
#               [5, 1, 3, 4],
#               [9, 5, 7, 1],
#               [2, 4, 1, 3]]
# d=set()
# for i in arr:
#     s=set(i)
#     d.update(s)
# print(d)


# a = [1, 2, 3, 4, 5]
# b = [5,6, 7, 8, 9]
#
# for i in a:
#     for j in b:
#         if i==j:
#             print(i)


# # Python program to illustrate the intersection
# # of two lists using set() method
# def intersection(lst1, lst2):
# 	return list(set(lst1) & set(lst2))
#
# # Driver Code
# lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
# lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
# print(intersection(lst1, lst2))


# Python program to print Even Numbers in given range

# start, end = 4, 19
#
# # iterating each number in list
# for num in range(start, end + 1):
#
#     # checking condition
#     if num % 2 == 0:
#         print(num, end=',')
#
#
# # Python program to print Positive Numbers in a List
#
# # list of numbers
# list1 = [-10, -21, -4, 45, -66, 93]
#
# # using list comprehension
# pos_nos = [num for num in list1 if num >= 0]
#
# print("Positive numbers in the list: ", *pos_nos)


# tup = (3, 7, 1, 18, 9)
# t=list(tup)
# print(t)
# t.sort()
# print(t)
# tu=tuple(t)
# print(tu)


# l=[1, 2, 3]
# t=[]
# for i in l:
#     s=i**3
#     t.append(i)
#     t.append(s)
#
# li=[]
#
# print(t)
# for j in range(0,len(t)-1,2):
#     c=(t[j],t[j+1])
#     li.append(c)
# print(li)


# l=[1, 2, 3]
# t=(4,5)
# li=tuple(list(t)+l)
# print(li)


# t1=(10, 4, 5, 6)
#
# t2=(5, 6, 7, 5)
# l=[]
#
# for i in range(len(t1)):
#     for j in range(len(t2)):
#         if i==j:
#             a=(t1[i]%t2[j])
#             l.append(a)
# print(tuple(l))
# # print(d)


# from math import pi
# x=int(input('enter radian angle'))
# deg=x*180/pi
# print('degree=',deg)


# li=[1,3,9,7,10]
# ordr=input('enter order')
# if ordr=='asc':
#     li.sort()
#     print('list in asc',li)
# elif ordr=='desc':
#     li.sort()
#     li.reverse()
#     print('list in desc',li)
# elif ordr=='None':
#     print(li)
# else:
#     print('Rerun and enter the correct input')


# def bi(x):
#     if x>=2:
#         q=x//2
#         r=x%2
#         # print(q,r)
#         li.append(r)
#         qu.append(q)
#         # print(qu)
#         # print(li)
#         return bi(q)
#
#     # else:
#     #     q=x
#     #     return bi(x)
#
#
# x = int(input('enter num'))
# li=[]
# qu=[]
# c=bi(x)
# s=qu[-1]
# li.append(s)
# li.reverse()
# for i in li:
#     print(i,end='')


# def bi(x):
#     if x >= 2:
#         q = x // 2
#         r = x % 2
#         # print(q,r)
#         li.append(str(r))
#         print(q,r)
#         print(li)
#         if x == 2:
#             print(q,r)
#             li.append(str(q))
#             # li.append(q)
#             return li
#         bi(q)
#
#
# x = int(input('enter num'))
# li = []
# bi(x)
# print(li)
# li.reverse()
# print(li)
# s = ''.join(li)
# print(int(s))
# sample = ''
# for i in li:
#     print(i, end='')


# vow='aAeEiIoOuU'
# st=input('enter a word')
# count=0
# for i in st :
#     if i in vow:
#         count+=1
# print(count)


# cc=(input('enter Credit Card num'))
# ccc=list(cc)
# # print(ccc)
# s=[]
# if (len(ccc))==16:
#     for i in range(len(ccc)):
#         if i <12:
#             s.append('x')
#             # print(s)
#
#         else:
#             s.append(ccc[i])
#             # print(s)
# s = ''.join(s)
# print(s)


# st=input('entr X nd O')
# print(type(st))
# cO=0
# cX=0
# for i in st:
#     if (i== 'x' or  i =='X'):
#         print(i)
#         cX+=1
#     if (i == 'o'or i=='O'):
#         cO+=1
# if cO==cX:
#     print(True)
# else:
#     print(False)


# i1=int(input('1st int'))
# i2=int(input('2nd int'))
# op=input('enter operator')
# if op=='+':
#     c=i1+i2
#     print('sum',c)
# elif op == '-':
#     c=i1-i2
#     print('diff',c)
# elif op == '*':
#     c=i1*i2
#     print('prod',c)
# elif op == '/':
#     c=i1/i2
#     print('division',c)


# org=int(input('enter original price'))
# dis=int(input('enter discount %'))
# d=dis/100
# c=org*d
# discprice=org-c
# print(discprice)


# x=input('enter elements')
# li=[]
# ans=[]
# for i in x:
#     li.append(i)
# print(li)
# for j in li:
#     if j.isdigit():
#         ans.append(j)
# print(ans)


# x=input('')
# s=''
# for i in x:
#     s=s+i
#     s=s+i
# print(s)


# x=int(input('int'))
# d={}
# for i in range(1,x+1):
#     d[(i)]=(i)*(i)
# print(d)


# class stringupper:
#     def __init__(self,x):
#         self.string=x
#     def printstr(self):
#         c=self.string.upper()
#
#
#         return c
#
#
# i=input('')
# inp=stringupper(i)
#
# print(inp.printstr())


# x=int(input('int'))
# s=''
# for i in range(1,x+1):
#     s=s.__add__(str(i*x))
# print(s,end='')


# X = [[1,2,3],
# [4 ,5,6],
# [7 ,8,9]]
#
#
# Y = [[9,8,7],
# [6,5,4],
# [3,2,1]]
#
# add=[[0,0,0],
#      [0,0,0],
#      [0,0,0]]
# # ele=[]
# for i in range(len(X)):
#     # print(i)
#     for j in range(len(Y)):
#
#             add[i][j]=X[i][j]+Y[i][j]
# for r in add:
#     print(r)


# Y = [[9,8,7],
# [6,5,4],
# [3,2,1]]
#
# add=[[0,0,0],
#      [0,0,0],
#      [0,0,0]]
# for i in range(len(Y)):
#     for j in range(len(Y)):
#         add[i][j]=Y[j][i]
# for r in add:
#     print(r)


# A = [[12, 7, 3],
# [4, 5, 6],
# [7, 8, 9]]
# B = [[5, 8, 1, 2],
# [6, 7, 3, 0],
# [4, 5, 9, 1]]
# result = [[0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0]]
# for i in range(len(A)):
#     for j in range(len(B[0])):
#         for k in range(len(B)):
#             result[i][j] += A[i][k] * B[k][j]
# for r in result:
#     print(r)


# from collections import Counter
# i=input('')
# d=Counter(i)
# print(''+str (d))
# coun=0
# for x in range(len(i)):
#     if x < len(i):
#         if  i[x]==i[x+1]:
#             coun+=1
#

# x=int(input('how many students'))
# d=[]
# for i in range(x):
#     name=input('n')
#     age=(input('a'))
#     score=(input('s'))
#     d.append((name,age,score))
# print(d)
#
# d.sort()
# # ag=d.sort(age)
# # sc=d.sort(score)
# print(d)


# s=''
# for i in ar:
#     c=i[0]
#     if
#     s=s+c
#     pass
# print(s)


#     for k in range(len(i)):
#         for j in i:
#             if j in ar[0]:
#                 if j not in s:
#                     s=s+j
#
# print(s)


# li=['abcd','abcde','abcd','abcdfrrs']
# st=''
# c=min(li,key=len)
# print(c)
# for i in range(len(c)):
#     li1=[]
#     for j in li:
#         s=j[i]
#         print('@@@@@@@',s)
#         li1.append(s)
#         print(li1)
#     # for w in li1:
#     #     if li1[0]==w:
#     #         if w not in st:
#     #             st=st+w
#     #             print(st)
#     #     else:
#     #         break
#     an=all(ele==li1[0] for ele in li1)
#     if an :
#         st=st+li1[0]
#     else:
#         pass
# print(li1)
# print(st)
# def func(current, prev, n):
#     k = 3
#     while k <= n:
#         current = []
#         current.insert(0, 1)
#         current.insert(-1, 1)
#         for x in range(1, k-1):
#             val = prev[x-1] + prev[x]
#             current.insert(x, val)
#         final_lst.append(current)
#         prev = current
#         k = k + 1
#         # print(prev, k)
#
# n = 5
# a = [1]
# b = [1, 1]
# final_lst = []
# current = []
# # prev = []
# if n == 1:
#     final_lst.append(a)
# elif n == 2:
#     final_lst.append(a)
#     final_lst.append(b)
# else:
#     prev = b
#     final_lst.append(a)
#     final_lst.append(b)
#     func(current, prev, n)
#
#
# for entry in final_lst:
#     print(entry, end="\n")

#
# n =3
# a = [1]
# b = [1, 2]
# final = []
# if n == 1:
#     final.append(a)
# elif n == 2:
#     final.append(a)
#     final.append(b)
# else:
#     k = 3
#     pre=[1,2]
#     while k <= n:
#         curr = []
#         for m in range(n):
#             curr.insert(m,pre[m])
#         for i in range(2, k):
#             curr.insert(i, pre[i - 1] + 1)
#         final.append(curr)
#         pre = curr
#         k += 1
#
# for e in final:
#     print(e, end='\n')
#






# n = 6
#
# for x in range(1,n+1):
#     lst = []
#     for y in range(1, x+1):
#         print(x,y)
#         lst.append(y)
#     print(lst)






#
# s = [1,0,-1,0,-2,2]
# s.sort()
# print(s)
# for i in s:
#



# x=int('enter num for factorial')
# for x in range(len(x)):

#
# target=0
# a=[-1,0,1,-2,2]
# a.sort()
# print(a)
# for i in range(len(a)-1) :
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==target:
#             print('ans is (',a[i],',',a[j],')')


# A = [1, 2, 3, 4]
# for i in range(len(A)):
#     if A[i]



# def sub_lists (l):
#     lists = [[]]
#     return lists
#     for i in range(len(l) + 1):
#         for j in range(i):
#             lists.append(l[j: i])
# l=[1,2,3,4]
# lists=sub_lists(l)
# print(lists)
#


# a=(1,2,3,4,5)
#
# for i in range(len(a)):
#     p = 1
#     for k in range(i+1,len(a)):
#
#         for j in a:
#             if j == a[i]:
#                 p=p*a[k]
#             else:
# print(p)




# def productArray(arr, n):
#     if(n == 1):
#         print(0)
#         return
#     left = [0]*n
#     right = [0]*n
#     prod = [0]*n
#     left[0] = 1
#     right[n - 1] = 1
#     for i in range(1, n):
#         left[i] = arr[i - 1] * left[i - 1]
#     for j in range(n-2, -1, -1):
#         right[j] = arr[j + 1] * right[j + 1]
#     for i in range(n):
#         prod[i] = left[i] * right[i]
#     for i in range(n):
#         print(prod[i], end =' ')
# arr = [10, 3, 5, 6, 2]
# n = len(arr)
# print("The product array is:")
# productArray(arr, n)




# x=20
# y=bin(x)
# print (y)
#
# def binary(x):
#     y=bin(x)
#     return y
#
#
# x=int(input('enter num'))
# y=binary(x)
# print(y)







# from tkinter import *
# import requests
# def self_bar():
#     res=requests.get(url='https://api.kanye.rest/')
#     res.raise_for_status()
#     data=res.json()
#     quotes=data["quote"]
#     canvas.itemconfig(nm,text=quotes)
# window=Tk()
# window.title('Vaa da Kanna')
# window.config(padx=50,pady=50)
#
# canvas=Canvas(width=300,height=414)
# bg=PhotoImage(file='bg.png')
# canvas.create_image(150,200,image=bg)
# nm=canvas.create_text(150,200,text='Suprise MotherFathers')
# canvas.grid(row=1,column=1)
#
# button=Button(text='Press da Chellam',command=self_bar)
# button.grid(row=0,column=1)

# window.mainloop()










# l = [1,2,3,4,5,6,1]
# print(l)
# s=set(l)
# print(s)
# if len(l)==len(s):
#     print('No dup')
# else:
#     print('dup')





# st='hello'
# print(len(st))
# st=st[::-1]
# print(st)
# # for i in range(len(st)):





# dic={'1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI',''






# roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
# class Solution:
#     def romanToInt(self, S: str) -> int:
#         summ= 0
#         for i in range(len(S)-1,-1,-1):
#             num = roman[S[i]]
#             if 3*num < summ:
#                 summ = summ-num
#             else:
#                 summ = summ+num
#         return summ

# print(Solution().romanToInt('XLIX'))




# roman= {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
# class Solution:
#     def ans(self,s):
#         sum=0
#         for i in range(0,len(s)):
#             num=roman[s[i]]
#             if 3*num > sum:
#                 sum = -(sum-num)
#             else :
#                 sum=sum+num
#         return sum
# x=Solution().ans('XI')
# print(x)


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         count = 0
#         new = ''
#         for i in s:
#             if i not in new:
#                 count += 1
#                 new += i
#         if s[0]==new[0]:
#             new=new.replace(new[0],'')
#             print(new)
#         return len(new)
#
#
# print(Solution().lengthOfLongestSubstring('pwwkew'))




# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         num=x
#         rev=0
#         while (num>0):
#             rem=num%10
#             rev=(rev*10)+rem
#             num=num//10
#         if rev==x:
#             return True
#         else:
#             return False
# print(Solution().isPalindrome(121))


# class Solution:
#    def longestCommonPrefix(self, strs):
#       if len(strs) == 0:
#          return ''
#       current = strs[0]
#
#       for i in range(1, len(strs)):
#          temp = ''
#          if len(current) == 0:
#             break
#          for j in range(len(strs[i])):
#             if j < len(current) and current[j] == strs[i][j]:
#                temp += current[j]
#             else:
#                break
#          current = temp
#       return current
#
#
# print(Solution().longestCommonPrefix(['flower', 'flow', 'flight']))


# class Solution:
#    def maxProfit(self, prices):
#       for i in prices:
#          if i == min(prices):
#             buy = i
#          elif i == max(prices):
#             sell = i
#       ans = sell - buy
#       return ans
#
#
# print('Profit', Solution().maxProfit([7, 1, 5, 3, 6, 4]))

#
# class Solution:
#    def maxProfit(self, prices):
#       mn, mx = float('inf'), 0
#       for i in range(len(prices)):
#          mn = min(prices[i], mn)
#          mx = max(mx, prices[i] - mn)
#       return mx
#
# print(Solution().maxProfit([7,1,5,3,6,4]))
#
#
#
#
#
#
#






# from collections import *
#
#
# class Solution:
#    def firstUniqChar(self, s: str) -> int:
#       d = Counter(s)
#       print(d)
#       for keys, value in d.items():
#          if d[keys] == 1:
#             a=keys
#             for j in range(len(s)):
#                if a==s[j]:
#                   return j
#       else:
#          return -1
#
#
# print(Solution().firstUniqChar('loveleetcode'))



################         OR           #####################


# class Solution:
#    def firstUniqChar(self, s: str) -> int:
#       d = Counter(s)
#       print(d)
#       for keys, value in d.items():
#          for j in range(len(s)):
#                if d[keys] == 1:
#                   a=keys
#
#                   if a==s[j]:
#                      return j
#       else:
#          return -1
#
#
# print(Solution().firstUniqChar('aabb'))





# import numpy as np
#
#
# from array import *
# arr=array('i',[-2,1,-3,4,-1,2,1,-5,4])
# new=array(arr.typecode,(a for a in arr))
# print(new)
# r=1
# c=4
# d=np.reshape(arr(r,c)).tolist()
# print(d)


# class Solution:
#     def maxSubArray(self, nums:int) -> int:
#         sum = 0
#         mxm = -99999
#
#         for n in nums:
#             sum += n
#
#             mxm = max(mxm, sum)
#
#             sum = 0 if sum < 0 else sum
#
#         return mxm
#
# print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


# l=[1,2,3,0,0,0]
# print(l[:3])

# class Solution:
#     def merge(self, nums1, m: int, nums2, n: int) -> None:
#         # print(nums1[:m], nums2[:n])
#         nums1[:] = sorted(nums1[:m] + nums2[:n])
        # print(nums1[:m],nums2[:n])


# Solution().merge([1,2,3,0,0,0],3,[2,5,6],3)
# print(nums1)

# nums1=[0]
# m=0
# nums2=[1]
# n=1
# nums1[:] = sorted(nums1[:m] + nums2[:n])
# print(nums1)






# class Solution:
#     def intersect(self, nums1, nums2) :
#         li=[]
#         for n in range(len(nums1)):
#             if nums1[n] in nums2:
#                 li.append(nums1[n])
#                 nums2.remove(nums1[n])
#         return li
# print(Solution().intersect([1,2,2,1],[2]))





####### DONT KNOW HOW IT RUNS......  BUT WORKS.......
# class Solution:
#    def maxProfit(self, prices):
#       mn, mx = float('inf'), 0
#       for i in range(len(prices)):
#          mn = min(prices[i], mn)
#          print(mn)
#          mx = max(mx, prices[i] - mn)
#          print(mx)
#       return mx
#
# print(Solution().maxProfit([7,1,5,3,6,4]))






# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         o=-1
#         for i in haystack:
#             o += 1
#             if i in needle:
#
#                 haystack=haystack.replace(i,"")
#                 print(haystack)
#                 return o
#             else:
#                 return o
#
# print(Solution().strStr('aaaaa','bba'))






# n=int(input('e'))
# for i in range(1,n+1):
#     count =0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#     if count==0 :
#         print (i)


# import math
# x=math.sqrt(5)
# print(int(x))


# class Solution:
#     def plusOne(self, List) :
#         i=[str(j) for j in List]
#         a_str=''.join(i)
#         a_int=int(a_str)
#         ans=a_int+1
#         ans_str=str(ans)
#
#         lis=[]
#         for k in ans_str:
#             lis.append(k)
#         return lis
# print(Solution().plusOne([1,2,3]))


# s='Appp'
# s=s.lo


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         s = ''.join(c for c in s if c.isalnum())
#         if s == s[::-1]:
#             return True
#         else:
#             return False
#
#
# print(Solution().isPalindrome("A man, a plan, a canal: Panama"))






# from collections import Counter
# l=[1,2,2]
# d=Counter(l)
# print(d)


# from collections import Counter
# class Solution:
#     def singleNumber(self, nums) -> int:
#         d=Counter(nums)
#         print(d)
#         for keys,value in d.items():
#             if d[keys]==1:
#                 return keys
# print(Solution().singleNumber([2,2,1]))



# x='B'
# print(ord(x))


# class Solution:
#     def titleToNumber(self, columnTitle: str) -> int:
#         ans, pos = 0, 0
#         for letter in reversed(columnTitle):
#             digit = ord(letter) - 64
#             ans += digit * 26 ** pos
#             pos += 1
#
#         return ans
# print(Solution().titleToNumber('AB'))




# s=["h","e","l","l","o"]
# print(s[::-1])



# class Solution:
#     def reverseString(self, s) -> None:
#         s=s[::-1]                   #s.reverse()
#         return s
# print(Solution().reverseString(["h","e","l","l","o"]))





# def isPower_of_Three(n):
#     if (n <= 0):
#         return False
#     if (n % 3 == 0):
#         return isPower_of_Three(n // 3)
#     if (n == 1):
#         return True
#     return False
#
#
# # Driver code
# num1 = 27
# if (isPower_of_Three(num1)):
#     print("Yes")
# else:
#     print("No")
#
# num2 = 6
# if (isPower_of_Three(num2)):
#     print("Yes")
# else:
#     print("No")
#
# # This code is contributed by shivanisinghss2110


# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         if n % 3 == 0:
#             return Solution().isPowerOfThree(n // 3)
#         if n == 1:
#             return True
#
#         return False
#
#
# num = 27
# if (Solution().isPowerOfThree(num)):
#     print('Yes')
# else:
#     print('No')






#
# class Solution:
#     def moveZeroes(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in nums:
#             if i==0:
#                 nums.remove(i)
#                 nums.append(i)
#         return nums
# print(Solution().moveZeroes([0,1,0,3,12]))




# h=[1,2,2]
# h.reverse()
# print(h)







# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
#             itr = itr.next
#         print(llstr)
#
#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next
#
#         return count
#
#     def insert_at_begining(self, data):
#         node = Node(data, self.head)
#         self.head = node
#
#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#
#         itr = self.head
#
#         while itr.next:
#             itr = itr.next
#
#         itr.next = Node(data, None)
#
#     def insert_at(self, index, data):
#         if index<0 or index>self.get_length():
#             raise Exception("Invalid Index")
#
#         if index==0:
#             self.insert_at_begining(data)
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 break
#
#             itr = itr.next
#             count += 1
#
#     def remove_at(self, index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")
#
#         if index==0:
#             self.head = self.head.next
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break
#
#             itr = itr.next
#             count+=1
#
#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)
#
#
# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.insert_at(1,"blueberry")
#     ll.remove_at(2)
#     ll.print()
#
#     ll.insert_values([45,7,12,567,99])
#     ll.insert_at_end(67)
#     ll.print()





# import math
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         num = n
#         num2s = 0
#         ways = 0
#         while num >= num2s:
#             ways += math.comb(num, num2s)
#             num -= 1
#             num2s += 1
#
#         return ways
# print(Solution().climbStairs(2))



# c=math.comb(2,0)
# print(c)









# SYMMETRIC TREE
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if root is None:
#             return True
#         else:
#             return self.is_mirror(root.right, root.left)
#
#     def is_mirror(self, right, left):
#         if left is None and right is None:
#             return True
#         elif left is None or right is None:
#             return False
#         else:
#             if left.val != right.val:
#                 return False
#             else:
#                 return self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left)