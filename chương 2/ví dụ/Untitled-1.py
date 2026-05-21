# ví dụ:nhập vào 3 điểm Toán, Lý, Hóa và tính điểm TB. K.tra xem điểm TB <5 yếu, TB<7 TB,TB <9 khá, còn lại giỏi.

Toan = float(input ("Nhập điểm toán: "))

Ly = float(input("Nhập điểm lý: "))

Hoa = float (input ("Nhập điểm Hóa: "))

TB= (Toan+Ly+Hoa)/3

print ("điểm trung bình:", round (TB,2))
if TB <5:

    print ("xếp loại: yếu")

elif TB <7:

    print("xếp loại:Trung Bình")

elif TB < 9:

     print ("xếp loại: khá")

else:

    print("xếp loại: giỏi")