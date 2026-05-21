#nhập 1 số n viết hàm tính ra giai thừa của số đó

def giai_thua(m):

    gt = 1

    for i in range(1, m + 1):
        gt = gt * i

    return gt


n = int(input("Nhập vào 1 số nguyên dương: "))

print("%d! = %d" % (n, giai_thua(n)))
