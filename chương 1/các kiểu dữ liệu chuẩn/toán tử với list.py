lst = [1,2]
lst += ['one','two']
print(lst)
lst = [1,2]*3
print(lst)
lst1 = [123,'abc', 'xyz']
print ("độ dài của lst1 là:", len(lst1))
lst2 = [123,321, 456]
print ( "phần tử lớn nhất là:", max(lst2))
lst2 = [123,321, 456]
print ( "phần tử bé nhất là:", min(lst2))
atuple = ('123','abc', 'xez')
alist = list(atuple)
print ( "các phần tử của tuple là:", atuple)
print ( "các phần tử của list là:", alist)
list = ['java','python','c++']
list.append('php')
print (list)
list1 = ['java','python','c++', 'python']
print("số lần python xuất hiện là =",list1.count('python'))
# phương thức extend
list1 = ['Java', 'python','c++']

list2 = ['C++', 'sql']

list1.extend (list2);

print("List sau khi duoc mo rong them là:",list1)
# phương thức index
list3 = ['java', 'Python', 'C++', 'php', 'Sql']

print(list3.index('C++'))
# phương thức insert
list4=['java','python','c++','sql']

list4. insert (3, 'android')
print(list4)
#phương thức pop
list1 = ['java', 'Python', 'C++', 'php', 'Sql']

print(list1.pop(2))
print(list1)
#phương thức remove
list1=['Java', 'Python', 'C++', 'php', 'sql']

list1. remove ('C++')

print ("list:", list1)
#xoá phần tử khỏi list
fruits = ["apple", "banana", "guave"];

del fruits [0]

print (fruits)
#phương thức reverse
list1 = ['Java', 'Python', 'C++', 'php', 'sql']

list1. reverse();

print("list bi dao nguoc:", list1)
#phương thức clear
fruits = ["apple","banana", "guava"]

fruits.clear()

print (fruits)