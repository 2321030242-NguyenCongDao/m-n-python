#lệnh while nhập số Ptử trong tổng. sd while để tính tổng 1 -> n
i = 1
while i <= 6:

    s = int (input ("Nhập n: "))

    tong = 0

    j = 1

    while j <= s:
        tong = tong + j
        j = j + 1

    print("Tổng là", tong)

    i = i + 1
#lệnh break

var = 10

while var > 0:
    print("Giá trị biến hiện tại là:", var)

    var = var - 1

    if var == 5:
        break
#lệnh continue
var = 5

while var >0:

    var = var-1

    if var == 3:

        continue

    print ('Gia try bien hien tai la: ', var)
#lệnh pass
i =1

while i<=10:

    if(i%2==0):

        pass

    else:

        print (i)

    i=i+1




