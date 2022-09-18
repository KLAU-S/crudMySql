from tkinter import CURRENT
from connect import *
curobj = connection.cursor()
# cursor = curobj.cursor(buffered=True)
# curobj.execute("select * from customers")
# res = curobj.fetchall()
# for val in res:
#     print(val)
curobj.reset()
curobj.execute("select customerName from customers where customerName IS NOT NULL")
res = curobj.fetchall()
for val in res:
    print(val)
