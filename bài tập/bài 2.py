#Viết C.trình nhập vào 1 dãy số nguyên X1, x2 , Xn (0<n<200), tính tổng các P.tử chẫn trong dãy và k.tra xem tổng này có chia hết cho 7 và nhỏ hơn 200 không?

n = int(input(" Nhập số phần tử n: "))

a =[]

for i in range (n):

 X = int (input (f" Nhập phần tử thứ {i+1}:"))

 a. append(X)

tong = 0

for x in a:

 if x%2==0:

  tong += x

print ("Tổng các phần tử chẵn là:", tong)

if tong %7 ==0 and tong < 200:

 print(" Tổng chia hết cho 7 và nhỏ hơn 200")

else:

 print ("Tổng không thỏa mãn điều kiện")