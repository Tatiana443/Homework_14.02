# Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума 
# и не больше заданного максимума)
import random
base_list=[random.randint(-10, 10) for i in range(random.randint(10,20))]
print(base_list)
max_num=int(input("Max: "))
min_num=int(input("Min: "))
new_list=[]
if max_num>=min_num:
   for i in range(len(base_list)):
      if max_num>=base_list[i] and min_num<=base_list[i]:
         new_list.append(i)
print(new_list)
