#dùng hàm filter() để lọc ra các số chẵn trong list.

list_goc= [10,9,8,7,6, 1,2,3,4,5]

list_moi = list (filter (lambda a: (a%2==0), list_goc))

print (list_moi)