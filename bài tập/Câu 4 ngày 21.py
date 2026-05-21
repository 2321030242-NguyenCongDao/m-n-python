#Câu 4Viết chương trình nhập vào 2 số nguyên dương a và b, sau đó tính tổng (a+b) và tìm ra chữ số lớn nhất trong tổng đó.
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

tong = a + b
tam = tong
max_cs = 0

while tam > 0:
    chu_so = tam % 10
    
    if chu_so > max_cs:
        max_cs = chu_so
        
    tam //= 10

print("Tổng a + b =", tong)
print("Chữ số lớn nhất trong tổng là:", max_cs)
