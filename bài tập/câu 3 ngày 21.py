#Câu 3Viết chương trình nhập vào một số nguyên dương n, kiểm tra xem tích các chữ số của n có phải là số chẵn và lớn hơn 20 hay không.
n = int(input("Nhập số nguyên dương n: "))

tich = 1
tam = n

while tam > 0:
    chu_so = tam % 10
    tich *= chu_so
    tam //= 10

print("Tích các chữ số =", tich)

if tich % 2 == 0 and tich > 20:
    print("Tích các chữ số là số chẵn và lớn hơn 20")
else:
    print("Tích các chữ số không thỏa mãn điều kiện")