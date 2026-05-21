import datetime

X= datetime.datetime (2026, 5, 21)

print (X)
#
import datetime

now = datetime.datetime. now ()

print (now)

s = now.strftime("%d/%m/%Y/%H:%M:%S")

# định dạng dd/mm/YY

print ("s:",s)
#
from datetime import datetime
dt_string="21/06/2026"
ngay_thang= datetime.strptime(dt_string, "%d/%m/%Y")
