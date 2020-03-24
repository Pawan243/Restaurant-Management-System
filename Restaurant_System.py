from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800")
root.title("Restaurant Management Systems")
global text_input
text_input = StringVar()
operator =""

Tops = Frame(root, width = 1600, height = 50,bg="light blue", relief=SUNKEN)
Tops.pack(side=TOP)


f1 = Frame(root, width = 800,height = 700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300,height = 700, bg="light blue", relief=SUNKEN)
f2.pack(side=RIGHT)
#=====================TIME===========================
localtime = time.asctime(time.localtime(time.time()))


#=======================INFO==========================
#Restaurant Management System
lblInfo = Label(Tops, font=('arial',50, 'bold'), text = "Restaurant Management System", fg = "steel blue", bd = 10,anchor ='w')
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial',20, 'bold'), text = localtime, fg = "steel blue", bd = 10,anchor ='w')
lblInfo.grid(row=1, column=0)



#=======================CALCULATION===========================================================================================================
def btnClick(numbers):
        global operator
        operator=operator + str(numbers)
        text_input.set(operator)
        
def btnClearDisplay():
        global operator
        operator=""
        text_input.set("")
        
def btnEqualsInput():
        global operator
        sumup = str(eval(operator))
        text_input.set(sumup)
        operator=""
def Ref():
        x = random.randint(12000, 50098)
        randomRef = str(x)
        rand.set(randomRef)
        '''Malai_Cofta = StringVar()
Rajma = StringVar()
Mutter_Paneer = StringVar()
kalli_Daal = StringVar()
Chapati = StringVar()
Chhole = StringVar()'''

        CoMalai_Cofta = float(Malai_Cofta.get())
        CoRajma = float(Rajma.get())
        CoMutter_Paneer = float(Mutter_Paneer.get())
        Cokalli_Daal= float(kalli_Daal.get())
        CoChapati = float (Chapati.get())
        CoChhole =  float(Chhole.get())
        
        CostofMalai_Cofta = CoMalai_Cofta * 0.99
        CostofRajma = CoRajma  * 1.00
        CostofMutter_Paneer = CoMutter_Paneer * 2.99 
        Costofkalli_Daal = Cokalli_Daal * 2.87
        CostofChapati = CoChapati * 2.89
        CostofChhole = CoChhole * 2.69

        CostofMeal = "$", str('%.2f' %( CostofMalai_Cofta + CostofRajma + CostofMutter_Paneer + Costofkalli_Daal + CostofChapati + CostofChhole ))
        
        PayTax = ((CostofMalai_Cofta + CostofRajma + CostofMutter_Paneer + Costofkalli_Daal + 
                                                                CostofChapati + CostofChhole )* 0.2)
                                                                
        TotalCost = (CostofMalai_Cofta + CostofRajma + CostofMutter_Paneer + Costofkalli_Daal + 
                                                                CostofChapati + CostofChhole )
                                                                
        Ser_Charge =(( CostofMalai_Cofta + CostofRajma + CostofMutter_Paneer + Costofkalli_Daal + 
                                                                CostofChapati + CostofChhole )/99)

        Service = "$", str('%.2f' % Ser_Charge)
        
        OverAllCost = "$", str('%.2f' % (PayTax + TotalCost + Ser_Charge))

        PaidTax = "$",str('%.2f' %PayTax)

        service_Charge.set(Service)
        Cost.set(CostofMeal)
        Tax.set(PaidTax)
        SubTotal.set(CostofMeal)
        Total.set(OverAllCost)
        
def qExit():
        root.destroy()

def Reset():
        rand.set("")
        Malai_Cofta.set("")
        Rajma.set("")
        Mutter_Paneer.set("")
        kalli_Daal.set("")
        Chapati.set("")
        Chhole.set("")
        service_Charge.set("")
        Tax.set("")
        Cost.set("")
        SubTotal.set("")
        Total.set("")


        
txtDisplay = Entry(f2, font=('arial',20, 'bold'), textvariable=text_input, bd = 30, insertwidth=4, bg = "powder blue", justify = 'right')
txtDisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="7", bg="powder blue", command=lambda:btnClick(7))
btn7.grid(row=2, column = 0)

btn8 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="8", bg="powder blue", command=lambda:btnClick(8))
btn8.grid(row=2, column = 1)

btn9 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="9", bg="powder blue", command=lambda:btnClick(9))
btn9.grid(row=2, column = 2)

Addition = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="+", bg="powder blue", command=lambda:btnClick("+"))
Addition.grid(row=2, column = 3)

#=============================================================================================================================================
btn4 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="4", bg="powder blue", command=lambda:btnClick(4))
btn4.grid(row=3, column = 0)

btn5 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="5", bg="powder blue", command=lambda:btnClick(5))
btn5.grid(row=3, column = 1)

btn6 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="6", bg="powder blue", command=lambda:btnClick(6))
btn6.grid(row=3, column = 2)

Subtraction = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="-", bg="powder blue", command=lambda:btnClick("-"))
Subtraction.grid(row=3, column = 3)
#=============================================================================================================================================
btn1 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="1", bg="powder blue", command=lambda:btnClick(1))
btn1.grid(row=4, column = 0)

btn2 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="2", bg="powder blue", command=lambda:btnClick(2))
btn2.grid(row=4, column = 1)

btn3 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="3", bg="powder blue", command=lambda:btnClick(3))
btn3.grid(row=4, column = 2)

Multiplication = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="*", bg="powder blue", command=lambda:btnClick("*"))
Multiplication.grid(row=4, column = 3)

#================================================================================================================================================
btn0 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="0", bg="powder blue", command=lambda:btnClick(0))
btn0.grid(row=5,column = 0)

Del = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="Del", bg="powder blue", command=btnClearDisplay)
Del.grid(row=5, column = 3)

Equal = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="=", bg="powder blue", command=btnEqualsInput)
Equal.grid(row=5, column = 2)

Division = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="/", bg="powder blue", command=lambda:btnClick("/"))
Division.grid(row=5, column = 1)
#===============================================================================================================================================
rand =StringVar()
Malai_Cofta = StringVar()
Rajma = StringVar()
Mutter_Paneer = StringVar()
kalli_Daal = StringVar()
Chapati = StringVar()
Chhole = StringVar()
service_Charge = StringVar()
Tax = StringVar()
Cost = StringVar()
SubTotal = StringVar()
Total = StringVar()



lblReference = Label(f1,font=('arial',12, 'bold'),text = "Reference",bd = 16,anchor='w')
lblReference.grid(row=0,column=0)

txtReference = Entry(f1,font=('arial',12, 'bold'),textvariable = rand,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtReference.grid(row=0,column=1)

lblMalai_Cofta = Label(f1,font=('arial',12, 'bold'),text = "Malai Cofta",bd = 16,anchor='w')
lblMalai_Cofta.grid(row=1,column=0)

txtMalai_Cofta = Entry(f1,font=('arial',12, 'bold'),textvariable = Malai_Cofta,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtMalai_Cofta.grid(row=1,column=1)

#===============================================================================================================================

lblRajma = Label(f1,font=('arial',12, 'bold'),text = "Rajma",bd = 16,anchor='w')
lblRajma.grid(row=2,column=0)

txtRajma = Entry(f1,font=('arial',12, 'bold'),textvariable = Rajma,insertwidth = 3, bg = 'powder blue',bd =4,justify ='right')
txtRajma.grid(row=2,column=1)

lblMutter_Paneer = Label(f1,font=('arial',12, 'bold'),text = "Mutter Paneer",bd = 16,anchor='w')
lblMutter_Paneer.grid(row=3,column=0)

txtFilet = Entry(f1,font=('arial',12, 'bold'),textvariable = Mutter_Paneer,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtFilet.grid(row=3,column=1)

lblSubTotal = Label(f1,font=('arial',12, 'bold'),text = "SubTotal",bd = 16,anchor='w')
lblSubTotal.grid(row=4,column=2)

txtSubTotal = Entry(f1,font=('arial',12, 'bold'),textvariable = SubTotal,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtSubTotal.grid(row=4,column=3)

lblTotal = Label(f1,font=('arial',12, 'bold'),text = "Total",bd = 16,anchor='w')
lblTotal.grid(row=5,column=2)

txtTotal = Entry(f1,font=('arial',12, 'bold'),textvariable = Total,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtTotal.grid(row=5,column=3)

lblservice_Charge = Label(f1,font=('arial',12, 'bold'),text = "service_Charge",bd = 16,anchor='w')
lblservice_Charge.grid(row=3,column=2)

txtservice_Charge = Entry(f1,font=('arial',12, 'bold'),textvariable = service_Charge,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtservice_Charge.grid(row=3,column=3)

lblTax = Label(f1,font=('arial',12, 'bold'),text = "Tax",bd = 16,anchor='w')
lblTax.grid(row=1,column=2)

txtTax = Entry(f1,font=('arial',12, 'bold'),textvariable = Tax,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtTax.grid(row=1,column=3)

lblCost = Label(f1,font=('arial',12, 'bold'),text = "Cost",bd = 16,anchor='w')
lblCost.grid(row=2,column=2)

txtCost = Entry(f1,font=('arial',12, 'bold'),textvariable = Cost,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtCost.grid(row=2,column=3)

lblkalli_Daal = Label(f1,font=('arial',12, 'bold'),text = "Kalli Daal",bd = 16,anchor='w')
lblkalli_Daal.grid(row=0,column=2)

txtkalli_Daal = Entry(f1,font=('arial',12, 'bold'),textvariable = kalli_Daal,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtkalli_Daal.grid(row=0,column=3)

lblChapati = Label(f1,font=('arial',12, 'bold'),text = "Chapati",bd = 16,anchor='w')
lblChapati.grid(row=4,column=0)

txtChapati = Entry(f1,font=('arial',12, 'bold'),textvariable = Chapati,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtChapati.grid(row=4,column=1)

lblChhole = Label(f1,font=('arial',12, 'bold'),text = "Chhole",bd = 16,anchor='w')
lblChhole.grid(row=5,column=0)

txtChhole = Entry(f1,font=('arial',12, 'bold'),textvariable = Chhole,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtChhole.grid(row=5,column=1)
#=================================================================================================================================================================
btnTotal= Button(f1,padx=16,pady = 16,bd= 16,fg= "black",font = ('arial',16,'bold'),width = 10,text= "Total", bg = "powder blue",  command = Ref ).grid(row= 7,column = 1)

btnReset= Button(f1,padx=16,pady = 16,bd= 16,fg= "black",font = ('arial',16,'bold'),width = 10,text= "Reset", bg = "powder blue",  command = Reset ).grid(row= 7,column = 2)

btnExit= Button(f1,padx=16,pady = 16,bd= 16,fg= "black",font = ('arial',16,'bold'),width = 10,text= "Exit", bg = "powder blue",  command = qExit ).grid(row= 7,column = 3)


	
root.mainloop()
