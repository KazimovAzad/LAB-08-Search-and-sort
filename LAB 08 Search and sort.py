#1
##import random
##List = [random.randint(0,6) for x in range(int(input()))]
##x = int(input('ne axtaririq: '))
##s = 0
##for i in range(len(List)):
##    if List[i] == x:
##        print(i, 'ci indeks')
##    else:
##        s += 1
##if s == 0:
##    print('tapilmadi')
#2
##List = [int(x) for x in input().split()]
##List2 =[]
##def selection_sort(A,B):
##   N = len(A)
##   for i in range(N):
##       i_min = i
##       for j in range(i + 1, N):
##           if A[j] > A[i_min]:
##               i_min = j
##       A[i], A[i_min] = A[i_min], A[i]
##       B[i], B[i_min] = B[i_min], B[i]
##   return B
##for i in List:
##    s = 0
##    while i > 0:
##        k = i % 10
##        i = i // 10
##        s += k
##    List2 += [s]
##print(selection_sort(List2,List))
#3
##List = []
##new = []
##def selection_sort(a):
##    for i in range(len(a)):
##        i_min = i
##        for j in range(i + 1, len(a)):
##            if a[j] < a[i_min]:
##                i_min = j
##        a[i], a[i_min] = a[i_min], a[i]
##    return a 
##for i in range(5):
##    a = input()
##    List += [a]
##for t in List:
##    new += [t[2:]]
##print(selection_sort(new))
#4
##List = []
##new = []
##def selection_sort(A,B):
##   N = len(A)
##   for i in range(N):
##       i_min = i
##       for j in range(i + 1, N):
##           if A[j] < A[i_min]:
##               i_min = j
##       A[i], A[i_min] = A[i_min], A[i]
##       B[i], B[i_min] = B[i_min], B[i]
##   return B
##for i in range(3):
##    a = input()
##    List += [a]
##for t in List:
##    new += [t[4:]]
##print(selection_sort(new,List))
#5
##import random
##List = [random.randint(-100,101) for x in range(10)]
##def selection_sort(a):
##    for i in range(len(a)):
##        i_min = i
##        for j in range(i + 1, len(a)):
##            if a[j] > a[i_min]:
##                i_min = j
##        a[i], a[i_min] = a[i_min], a[i]
##    return a
##def selection_sort2(a):
##    for i in range(len(a)):
##        i_min = i
##        for j in range(i + 1, len(a)):
##            if a[j] < a[i_min]:
##                i_min = j
##        a[i], a[i_min] = a[i_min], a[i]
##    return a
##print('unsorted:', List)
##print('sorted_1:', selection_sort(List))
##print('sorted_2:', selection_sort2(List[:len(List)//2]) + selection_sort2(List[len(List)//2:]))
#6
##import random
##a = [random.randint(-100, 101) for i in range(int(input()))]
##list1 =[]
##list2 =[]
##list_um = []
##def selection_sort1(a):
##    n = len(a)
##    for i in range(n):
##        i_min = i
##        for j in range(i + 1, n):
##            if a[j] > a[i_min]:
##                i_min = j
##        a[i], a[i_min] = a[i_min], a[i]
##    return a
##def selection_sort2(a):
##    n = len(a)
##    for i in range(n):
##        i_min = i
##        for j in range(i + 1, n):
##            if a[j] < a[i_min]:
##                i_min = j
##        a[i], a[i_min] = a[i_min], a[i]
##    return a
##s = 0
##for i in a:
##    if i > 0:
##        list1 = [i] + list1
##        s += 1
##    elif i < 0:
##        list2 = list2 + [i]
##list_um = selection_sort1(list1) + selection_sort2(list2)
##print(list_um, s, sep = ' musbetlerin sayi:')





