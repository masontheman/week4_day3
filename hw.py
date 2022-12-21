words = ['this' , 'is', 'a', 'sentence', '.','poophead','final','finalfinal']
def reverse_list(listA):
   print(id(listA))
   for x in range(0,len(listA) //2):
    listA[x],listA[len(listA)-(x+1)] = listA[len(listA)-(x+1)][::-1],listA[x][::-1]
   print(id(listA))
   return listA
reverse_list(words)

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
def dict_count(listy):
    my_dict = {element: listy.lower().split().count(element) for element in listy.lower().split()}
    return my_dict
dict_count(a_text)


nums_list = [10,23,45,70,11,15]
target = 70
def linear_search_array(listA,target):
  a = [nums_list.index(x) for x in listA if x == target]
  return a if a else -1
linear_search_array(nums_list,70)