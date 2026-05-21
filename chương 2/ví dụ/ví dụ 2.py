#C.trình cho phập vào 1 ma trận gồm m hàng và n cột số thực, in ra ma trận vừa nhập


m=int(input("nhập m = "))

n=int(input("nhập n = "))

a=[]

for i in range (0, m):

    a. append ([])

    for j in range (0, n):

        x= float (input("nhap phan tu thu a[%d] [%d]: "% (i+1, j +1)))

        a[i].append(x)

print ("Mang vua nhap la :")

for i in range (0, m):

    for j in range (0, n):

        print ( "%8.2f"% a[i][j], end = '')

    print ()