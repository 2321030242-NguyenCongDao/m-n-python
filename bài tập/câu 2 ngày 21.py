#Câu 2Viết chương trình nhập vào một số nguyên dương n, kiểm tra xem tổng các chữ số của n có phải là số chia hết cho 3 hay không
n = int(input("Nhập số nguyên dương n: "))


tong = 0
tam = n

while tam > 0:
    tong += tam % 10
    tam //= 10

print("Tổng các chữ số =", tong)

if tong % 3 == 0:
    print("Tổng các chữ số chia hết cho 3")
else:
    print("Tổng các chữ số không chia hết cho 3")