# lệnh if tìm max của 3 số thực a, b và c

a= float (input("Nhap so thu nhat = "))

b = float (input ("Nhập so thu Hai = "))

c= float ( input ("Nhap so Thu Ba = "))

max = a

if (b > max):

    max = b

if (c > max):

    max = c

print("Số lớn nhất trong a, b, c là:", max)
# lệnh if-else
n = int(input ("Nhap vao mot so Nguyen: "))

if (n % 2 == 0 ):

    print ("số",n," là số chẵn.")
else:
    print ("số",n," là số lẻ. ")
#giải PT ax + b = 0 (a, b nhập từ bàn phím (a, b là số nguyên))

a= float (input ("Nhập hệ số a ="))

b = float (input("Nhập hệ số b="))

if ( a == 0):
    if (b == 0):

        print (" Phương trình vô số nguyệm")

    else:

        print ("Phương trình vô nghiệm")

else: 
    x = (- b)/a

print ("x= ",x)
#lệnh if-elif-else
#mã   dân tộc
#1      kinh
#2      tày
#3      nùng
#4      thái
#5      khơme
ma = int(input("nhập mã dân tộc (1-5): "))

if ma == 1:

    print (" Dân tộc: Kinh")

elif ma == 2:

    print ("Dân tộc: Tày")

elif ma == 3:

    print ("Dân tộc: Nùng")

elif ma == 4:

    Print(" Dân tộc: Thái")

else:

    Print (" Dân tộc: Khơme")