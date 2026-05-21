# viết c. trình nhập vào 1 dãy số thực X1, X2,... Xn (O<n< 100), sau đó tìm trung bình cộng các P. tử âm trong dãy mà g.trị nằm trong khoảng (-1000,-10)

n =  int(input("Nhập số phần tử n:"))

a=[]

for i in range (n):

 x = float (input(f" Nhập phần tử thứ {i+1}:"))

 a.append (x)

tong = 0

dem=0
for x in a:

 if  -1000 < x < - 10:

  tong += x

  dem += 1

if dem > 0:

 tbc=tong/dem

 print("Trung bình cộng các phần tử thỏa mãn là:", tbc)

else:

 print (" không có phần tử âm trong khoảng (-1000,-10)")