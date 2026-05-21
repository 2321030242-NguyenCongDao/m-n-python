#Câu 5Viết chương trình nhập vào 2 số nguyên dương m và n, sau đó kiểm tra xem m có chia hết cho tổng các chữ số của n hay không. Ví dụ: m = 45, n = 123, tổng các chữ số của n là 1 + 2 + 3 = 6, và 45 không chia hết cho 6.
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

tong = 0
tam = n

print("Tổng các chữ số của n =", tong)

if tong != 0 and m % tong == 0:
    print("m chia hết cho tổng các chữ số của n")
else:
    print("m không chia hết cho tổng các chữ số của n")