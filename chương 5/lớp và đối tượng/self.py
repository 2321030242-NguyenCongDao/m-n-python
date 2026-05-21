class Circle:

 def Dien_tich (self):

  return self.bk*self. bk * 3, 141592

 def Nhap(self):

  self.bk = float(input (" Nhập bán kính :"))
                         
C = Circle()

C.Nhap()

print(" diện tích của hình tròn là:", C.Dien_tich ())
