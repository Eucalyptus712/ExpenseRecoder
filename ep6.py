#HW

from tkinter import *
from tkinter import ttk, messagebox  # ttk is theme of Tk
import csv
from datetime import datetime


days = {'Mon':'จันทร์',
		'Tue':'อังคาร',
		'Wed':'พุธ',
		'Thu':'พฤหัส',
		'Fri':'ศุกร์', 
		'sat':'เสาร์',
		'Sun':'อาทิตย์'}

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย Ver 0.1')
GUI.geometry('600x700+400+50')  #ขนาดจอ  ,+ คือตำแหน่งx,y

#-------------------Menu Bar----------------------------------
menubar = Menu(GUI)
GUI.config(menu=menubar)

#file menu
filemenu = Menu(menubar,tearoff=0)      #tearoff=0 ลบเส้นปปะ
menubar.add_cascade(label='Flie',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export CSV')
#Help
def About():
	messagebox.showinfo('About','สวัสดีครับ งงอะดิ ผมก็งง')
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)
#Donate
donate = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donate)


#-------------------------------------------------------------

#เพิ่มTAB
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1) #figขนาด  

icon_t1 = PhotoImage(file='t1_expense.png')  #เรียกรูปภาพที่ใช้ใน tab  #.subsample(2)=ย่อรูป
icon_t2 = PhotoImage(file='t2_list.png') 

Tab.add(T1, text=f'{"ค่าใช้จ่าย":^{30}}',image=icon_t1,compound='top')  #ตำแหน่ง top bottom ritgh
Tab.add(T2, text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=icon_t2,compound='top')

F1 = Frame(T1)    #ย้ายF1 เข้า T1
#F1.place(x=100,y=40) #location
F1.pack()   #ขนาดหน้าจอ

def Save(event=None):
	expense = v_expense.get() 
	price = v_price.get()
	number = v_number.get()

	if expense == '':     #เงื่อนไขการพิมไม่ครบ
		print('NO data')
		messagebox.showwarning('Error','กรุณากรอกข้อมูลรายการค่าใช้จ่าย')
		return   #return คือการไม่ให้ทำต่อแล้ว จบแค่ตรงนี้ถ้าตรงเงื่อนไข if
	elif price == '':
		messagebox.showwarning('Error','กรุณากรอกข้อมูลราคาค่าใช้จ่าย')
		return
	elif number == '':
		#number = 1 # กำหนดค่าเองที่ 1 ชิ้น
		messagebox.showwarning('Error','กรุณากรอกข้อมูลจำนวนชิ้น')
		return

	total = int(price)*int(number)
	try:
		total = int(price)*int(number)
		print('ชื่อรายการ: {} ราคา: {} บาท จำนวน: {} ราคารวม: {}'.format(expense,price,number,total))

		#setค่าผลลัพธ์ ที่แสดง
		text = 'ชื่อรายการ: {} ราคา: {} บาท\n'.format(expense,price)
		text = text + 'จำนวน: {} ราคารวม: {} บาท'.format(number,total)
		v_result.set(text)

		#clear ข้อมูลเก่า
		v_expense.set('') 
		v_price.set('')
		v_number.set('')
	   
		today = datetime.now().strftime('%a') #days['Mon'] = จันทร์
		dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		dt = days[today] + '-'+ dt
		#บันทึกข้อมูลลง csv
		with open('savedata.csv','a',encoding='utf-8',newline='') as f:

			fw = csv.writer(f) #สร้างฟังชั่นสำหรับการเขียนข้อมูล
			data = [dt,expense,price,number,total]
			fw.writerow(data)

		#ทำให้ เคอเซอร์ กลับไปตำแหน่งช่องกรอก E1
		E1.focus()
		update_table()  #อัพเดพtable

	except Exception as e:
		print('ERROR',e)
		#messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่')    #popup
		messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่')
		#messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่')
		v_expense.set('')   #resetข้อมูล กรอกใหม่
		v_price.set('')
		v_number.set('')

#ทำให้กด ENTER ได้        
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(event=None) ด้วย
#gui.bind ตัวเช็คปุ่ม
	
FONT1 = (None,20)   #ขนาดฟอนต์  'Angsana New'

#=========image mian icon ==================
main_icon = PhotoImage(file='iconmoney.png')

Mainicon = Label(F1,image=main_icon)
Mainicon.pack()




#----------------->ชื่อรายการ<--------------------------
L = ttk.Label(F1,text='ชื่อรายการ',font=FONT1).pack()
v_expense = StringVar() 
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#----------------------------------------------------

#------------------>ราคา<---------------------------
L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar() 
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1) 
E2.pack()
#-------------------------------------------------

#------------------>จำนวน<---------------------------
L = ttk.Label(F1,text='จำนวน',font=FONT1).pack()
v_number = StringVar() 
E3 = ttk.Entry(F1,textvariable=v_number,font=FONT1) 
E3.pack()
#-------------------------------------------------

icon_b1 = PhotoImage(file='save.png')

B2 = ttk.Button(F1,text=f'{"บันทึก": >{10}}',image=icon_b1,compound='left',command=Save)  #สร้างชื่อปุ่ม command=hello callfuction
B2.pack(ipadx=20,ipady=10,pady=20) #ติดปุ่ม iขนาดปุ่ม    #pady ระยะปุ่ม

#สร้างตำแน่งแสดงผลลัพธ์
v_result = StringVar()
v_result.set('-------ผลลัพธ์-------')
result = ttk.Label(F1, textvariable=v_result,font=FONT1,foreground='green')
result.pack(pady=20)




##########################################TAB2########EP6#####################

def read_csv():
	with open('savedata.csv',newline='',encoding='utf-8') as f:   #ให้เปิดไฟล์ชื่อว่า savedata.csv แล้วตั้งชื่อว่า f   ป้องกันลืมclose
		fr = csv.reader(f)    #file reader=fr
		data = list(fr)
		# print(data)
		# print('--------')
		# print(data[0])
		# for a,b,c,d,e in data:
		# 	print(b) 
	return data   #ส่งค่าไปยัง reslut ที่ต้องการ

# rs = read_csv() #####readcsv
# print(rs) 

####table*****

L=ttk.Label(T2,text='ตารางแสดงผลลัพธ์',font=FONT1).pack(pady=20)    #ใส่หัวข้อ

header = ['วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=20)   #ความสูงของช่องผลลัพธ์
resulttable.pack()

#ใส่ข้อความที่ header
# resulttable.heading(header[0],text=header[0])  #ใส่ข้อความ เน้นการ ref  แบบที่ 1
# resulttable.heading(header[1],text=header[1])
# resulttable.heading(header[2],text=header[2])
# resulttable.heading(header[3],text=header[3])
# resulttable.heading(header[4],text=header[4])
 
# for i in range(len(header)):                            #แบบที่2
# 	resulttable.heading(header[i],text=header[i])

for h in header:                                         #แบบที่3
	resulttable.heading(h,text=h)

headerwidth = [150,170,80,80,80]       # กำหนดความกว้างแต่ละช่อง
for h,w in zip(header,headerwidth):
	resulttable.column(h,width=w)  # กำหนดความกว้างคอลัมน์


# resulttable.insert('','end',value=['จันทร์','น้ำ','30','5','150'])
# resulttable.insert('','end',value=['อังคาร','น้ำ','30','5','150'])

def update_table():    #อัพเดตข้อมูล
	resulttable.delete(*resulttable.get_children())  #ลบข้อมูลเก่าก่อน อัพเดตข้อมูลใหม่ print(*...) ปริ้นแบบไม่เอา , ''
	# for c in resulttable.get_children():           # แบบที่ 2
	# 	resulttable.delete(c)

	data = read_csv()
	for d in data:
		resulttable.insert('',0,value=d)

update_table()


GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()

