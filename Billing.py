from tkinter import*
import math,random,os
from tkinter import messagebox as msg
import mysql.connector

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700")
        bg_color="#074463"
        self.root.title("Billing Software")
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
  
        #=========================VARIABLE========================
        #===========COSMETIC.......
        self.bath_soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_spray=IntVar()
        self.body_lotion=IntVar()

        #===========GROCERY.......
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.Wheat=IntVar()
        self.sugar=IntVar()
            
        #===========    OTHER .......
        self.maza=IntVar()
        self.coke=IntVar()
        self.fruit=IntVar()
        self.nimkos=IntVar()
        self.biscuits=IntVar()

        # ============ total price & tax ==========

        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.other_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.other_tax=StringVar()

        self.customer_name=StringVar()
        self.phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search=StringVar()

        
        # ########customer detail ======================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="customer Details",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0, y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer name",bg=bg_color,fg="white",font=("time new roman",18,"bold"))
        cname_lbl.grid(row=0,column=0,padx=20,pady=5)

        cname_txt = Entry(F1,width=16,textvariable=self.customer_name,font="arial 15",bd=7,relief=SUNKEN)
        cname_txt.grid(row=0,column=1,pady=5,padx=10)

        cphone_lbl=Label(F1,text="Phone no.",bg=bg_color,fg="white",font=("time new roman",18,"bold"))
        cphone_lbl.grid(row=0,column=2,padx=20,pady=5)

        cphone_txt = Entry(F1,width=16,textvariable=self.phone,font="arial 15",bd=7,relief=SUNKEN)
        cphone_txt.grid(row=0,column=3,pady=5,padx=10)

        bill_lbl=Label(F1,text="Bill no.",bg=bg_color,fg="white",font=("time new roman",18,"bold"))
        bill_lbl.grid(row=0,column=4,padx=5,pady=5)
        
        bill_txt = Entry(F1,width=14,textvariable=self.bill_no,font="arial 15",bd=7,relief=SUNKEN)
        bill_txt.grid(row=0,column=5,pady=5,padx=50)

        btn = Button(F1,text="ENTER",command=self.find_bill,width=10,bd=7,font="arial 12 bold",bg=bg_color,fg="white")
        btn.grid(row=0,column=6)


#================consmetic ============


        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5, y=173,width=325,height=380)

        Bath_saop=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        Bath_saop.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Bath_saop=Entry(F2,width=10,textvariable=self.bath_soap,font="arial 15",bd=7,relief=SUNKEN)
        Bath_saop.grid(row=0,column=1,pady=14,padx=10)

        face_cream=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        face_cream.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream=Entry(F2,width=10,textvariable=self.face_cream,font="arial 15",bd=7,relief=SUNKEN)
        face_cream.grid(row=1,column=1,pady=14,padx=10)

        face_wash=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        face_wash.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_wash=Entry(F2,width=10,textvariable=self.face_wash,font="arial 15",bd=7,relief=SUNKEN)
        face_wash.grid(row=2,column=1,pady=14,padx=10)

        Hair_spray=Label(F2,text="Hair spray",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        Hair_spray.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_spray=Entry(F2,width=10,textvariable=self.hair_spray,font="arial 15",bd=7,relief=SUNKEN)
        Hair_spray.grid(row=3,column=1,pady=14,padx=10)

        Body_Lotion=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        Body_Lotion.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Body_Lotion=Entry(F2,width=10,textvariable=self.body_lotion,font="arial 15",bd=7,relief=SUNKEN)
        Body_Lotion.grid(row=4,column=1,pady=14,padx=10)

#============grocery=========
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=330, y=173,width=325,height=380)

        Rice=Label(F3,text="  Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        Rice.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Rice=Entry(F3,width=10,textvariable=self.rice,font="arial 15",bd=7,relief=SUNKEN)
        Rice.grid(row=0,column=1,pady=14,padx=10)

        Food_oil=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        Food_oil.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Food_oil=Entry(F3,width=10,textvariable=self.food_oil,font="arial 15",bd=7,relief=SUNKEN)
        Food_oil.grid(row=1,column=1,pady=14,padx=10)
        
        Daal=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        Daal.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Daal=Entry(F3,width=10,textvariable=self.daal,font="arial 15",bd=7,relief=SUNKEN)
        Daal.grid(row=2,column=1,pady=14,padx=10)

        Wheat=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        Wheat.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Wheat=Entry(F3,width=10,textvariable=self.Wheat,font="arial 15",bd=7,relief=SUNKEN)
        Wheat.grid(row=3,column=1,pady=14,padx=10)

        Sugar=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        Sugar.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Sugar=Entry(F3,width=10,textvariable=self.sugar,font="arial 15",bd=7,relief=SUNKEN)
        Sugar.grid(row=4,column=1,pady=14,padx=10)



#            +++++++++++++++++++++      +++++++++   other       +++++++++         ++++++++++++++++++

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=655, y=173,width=325,height=380)

        mazza=Label(F4,text=" Mazza",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        mazza.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        mazza=Entry(F4,width=10,textvariable=self.maza,font="arial 15",bd=7,relief=SUNKEN)
        mazza.grid(row=0,column=1,pady=14,padx=10)

        coke=Label(F4,text=" Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        coke.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coke=Entry(F4,width=10,textvariable=self.coke,font="arial 15",bd=7,relief=SUNKEN)
        coke.grid(row=1,column=1,pady=14,padx=10)

        frooti=Label(F4,text=" Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        frooti.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        frooti=Entry(F4,width=10,textvariable=self.fruit,font="arial 15",bd=7,relief=SUNKEN)
        frooti.grid(row=2,column=1,pady=14,padx=10)

        Nimkos=Label(F4,text=" Nimkos",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        Nimkos.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Nimkos=Entry(F4,width=10,textvariable=self.nimkos,font="arial 15",bd=7,relief=SUNKEN)
        Nimkos.grid(row=3,column=1,pady=14,padx=10)

        Biscuits=Label(F4,text=" Biscuits",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        Biscuits.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Biscuits=Entry(F4,width=10,textvariable=self.biscuits,font="arial 15",bd=7,relief=SUNKEN)
        Biscuits.grid(row=4,column=1,pady=14,padx=10)


# +++++++++++++++++++   +++++++++++                  Bill area              +++++++++++++             ++++++++++++++++++++++

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=980, y=173,width=382,height=380)

        bill_title=Label(F5,text="BILL AREA",font="arial 15",bd=10,relief=GROOVE)
        bill_title.pack(fill=X)

        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(fill=Y, side=RIGHT)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

# +++++++++++++++++++   +++++++++++                  button frame              +++++++++++++             ++++++++++++++++++++++

        
        
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="BILL MENU",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0, y=550,relwidth=1,height=180)

        t_cosmatic =Label(F6,text="Total Cosmatic",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        t_cosmatic.grid(row=0,column=0,padx=20,pady=1,sticky="W")
        t_cosmatic=Entry(F6,width=10,textvariable=self.cosmetic_price,font="arial 15",bd=7,relief=SUNKEN)
        t_cosmatic.grid(row=0,column=1,padx=10,pady=2)

        t_grocery=Label(F6,text="Total Grocery",font=("times new roman",16,"bold"),fg="white",bg=bg_color)
        t_grocery.grid(row=1 , column=0,padx=20,pady=1,sticky="W")
        t_grocery=Entry(F6,width=10,textvariable=self.grocery_price,font="ariel 15",bd=7,relief=SUNKEN)
        t_grocery.grid(row=1,column=1,padx=10,pady=2)

        t_other=Label(F6,text="Total Other",font=("times new roman",16,"bold"),fg="white",bg=bg_color)
        t_other.grid(row=2 , column=0,padx=20,pady=1,sticky="W")
        t_other=Entry(F6,width=10,textvariable=self.other_price,font="ariel 15",bd=7,relief=SUNKEN)
        t_other.grid(row=2,column=1,padx=10,pady=2)

        tax_cosmatic =Label(F6,text="Cosmatic Tax",font=("times new roman",16,"bold"),bg=bg_color,fg="white")
        tax_cosmatic.grid(row=0,column=3,padx=20,pady=1,sticky="W")
        tax_cosmatic=Entry(F6,width=10,textvariable=self.cosmetic_tax,font="arial 15",bd=7,relief=SUNKEN)
        tax_cosmatic.grid(row=0,column=4,padx=10,pady=2)

        tax_grocery=Label(F6,text="Grocery Tax",font=("times new roman",16,"bold"),fg="white",bg=bg_color)
        tax_grocery.grid(row=1 , column=3,padx=20,pady=1,sticky="W")
        tax_grocery=Entry(F6,width=10,textvariable=self.grocery_tax,font="ariel 15",bd=7,relief=SUNKEN)
        tax_grocery.grid(row=1,column=4,padx=10,pady=2)

        tax_other=Label(F6,text="Other Tax",font=("times new roman",16,"bold"),fg="white",bg=bg_color)
        tax_other.grid(row=2 , column=3,padx=20,pady=1,sticky="W")
        tax_other=Entry(F6,width=10,textvariable=self.other_tax,font="ariel 15",bd=7,relief=SUNKEN)
        tax_other.grid(row=2,column=4,padx=10,pady=2)

        F7_btn = Frame(F6,bg=bg_color,bd=7,relief=GROOVE).place(x=650,width=700,height=100)

        total_btn=Button(F7_btn,text="TOTAL",bd=7,font="ariel 16 bold",fg="white",bg=bg_color,command=self.total)
        total_btn.place(x=700, y=600)

        generate_btn=Button(F7_btn,text="Generate Bill",command=self.bill_area,bd=7,font="ariel 16 bold",fg="white",bg=bg_color,)
        generate_btn.place(x=870, y=600)

        clear_btn=Button(F7_btn,text="Clear",command=self.clear,bd=7,font="ariel 16 bold",fg="white",bg=bg_color)
        clear_btn.place(x=1100, y=600)

        Exit_btn=Button(F7_btn,text="Exit",command=self.Exit,bd=7,font="ariel 16 bold",fg="white",bg=bg_color)
        Exit_btn.place(x=1250, y=600)


        # welcome_bill()  # call funvtion

    def  total(self):
         
         # make variables of all item present in cosmetic for addition price o prodeuct
        self.price_bath_soap=self.bath_soap.get()*40
        self.price_face_cream=self.face_cream.get()*100
        self.price_face_wash=self.face_wash.get()*20
        self.price_hair_spray=self.hair_spray.get()*150
        self.price_body_lotion=self.body_lotion.get()*120

        self.total_cosmetic_price=float(
                                        self.price_bath_soap +
                                        self.price_face_cream +
                                        self.price_face_wash  +
                                        self.price_hair_spray +
                                        self.price_body_lotion
                                )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.var_cosmetic_price=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.var_cosmetic_price))

        #  make variables of all item present in groccery for addition price o prodeuct

        self.price_rice=self.rice.get()*40
        self.price_food_oil=self.food_oil.get()*100
        self.price_daal=self.daal.get()*20
        self.price_Wheat=self.Wheat.get()*150
        self.price_sugar=self.sugar.get()*120

        self.total_grocery_price=float(
                                        self.price_rice +
                                        self.price_food_oil +
                                        self.price_daal +
                                        self.price_Wheat +
                                        self.price_sugar
                                )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.var_grocery_price=round((self.total_grocery_price*0.05),2)
        self.grocery_tax.set("Rs. "+str(self.var_grocery_price))

        #  make variables of all item present in groccery for addition price o prodeuct
        self.price_maza=self.maza.get()*40
        self.price_coke=self.coke.get()*100
        self.price_fruit=self.fruit.get()*20
        self.price_nimkos=self.nimkos.get()*150
        self.price_biscuits=self.biscuits.get()*120

        self.total_other_price=float(
                                        self.price_maza+
                                        self.price_coke+
                                        self.price_fruit+
                                        self.price_nimkos+
                                        self.price_biscuits                                        
                                )        
        self.other_price.set("Rs. "+str(self.total_other_price))
        self.var_otherprice=round((self.total_other_price*0.05),2)
        self.other_tax.set("Rs. "+str(self.var_otherprice))

        self.total_bill=float(
                                    self.total_cosmetic_price+
                                    self.total_grocery_price+
                                    self.total_other_price +
                                    self.var_cosmetic_price +
                                    self.var_grocery_price + 
                                    self.var_otherprice 
        )

    def welcome_bill(self):
        self.textarea.delete("1.0",END)   #delete function delete old data on bill area and generate only current data
        self.textarea.insert(END,"\tWelcome To Hanan's Retail\n")
        self.textarea.insert(END,f"\n  Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END,f"\n  Customer Name : {self.customer_name.get()}")
        self.textarea.insert(END,f"\n  Phone No : {self.phone.get()}\n")
        self.textarea.insert(END,"="*42)
        self.textarea.insert(END,"Product           QTY           Price\n")
        self.textarea.insert(END,"="*42)


    def bill_area(self):
        if self.customer_name.get()=="" or self.phone.get()=="":
            msg.showerror("error","Customer Details Are Mandatory.")

        #elif self.cosmetic_price.get()=="Rs. 0.0"and self.grocery_price.get()=="Rs. 0.0" and self.other_price=="Rs. 0.0":
        #    msg.showerror("error","Product Not Purchased")
        
        else:
            self.welcome_bill()
            # price is 0 so not print but price is not 0 so print name qty and price in bill area .

            # ======  cosmetic =====

            if self.bath_soap.get() !=0:
                self.textarea.insert(END, f"\n Bath Soap           {self.bath_soap.get()}             {self.price_bath_soap}\n")
            if self.face_cream.get() !=0:
                self.textarea.insert(END, f"\n Face Cream          {self.face_cream.get()}            {self.price_face_cream}\n")
            if self.face_wash.get() !=0:
                self.textarea.insert(END, f"\n Face Wash           {self.face_wash.get()}             {self.price_face_wash}\n")
            if self.hair_spray.get() !=0:
                self.textarea.insert(END, f"\n Hair Spray          {self.hair_spray.get()}            {self.price_hair_spray}\n")
            if self.body_lotion.get() !=0:
                self.textarea.insert(END, f"\n Body Lotion         {self.body_lotion.get()}           {self.price_body_lotion}\n")
            
            # ======  grocery =====

            if self.rice.get() !=0:
                self.textarea.insert(END, f"\n Rice                {self.rice.get()}            {self.price_rice}\n")
            if self.food_oil.get() !=0:
                self.textarea.insert(END, f"\n Food Oil            {self.food_oil.get()}          {self.price_food_oil}\n")
            if self.daal.get() !=0:
                self.textarea.insert(END, f"\n Daal                {self.daal.get()}            {self.price_daal}\n")
            if self.Wheat.get() !=0:
                self.textarea.insert(END, f"\n Wheat               {self.Wheat.get()}           {self.price_Wheat}\n")
            if self.sugar.get() !=0:
                self.textarea.insert(END, f"\n Sugar               {self.sugar.get()}           {self.price_sugar}\n")
            
            # ======  other =====

            if self.maza.get() !=0:
                self.textarea.insert(END, f"\n Mazza               {self.maza.get()}             {self.price_maza}\n")
            if self.coke.get() !=0:
                self.textarea.insert(END, f"\n Coke                {self.coke.get()}             {self.price_coke}\n")
            if self.fruit.get() !=0:    
                self.textarea.insert(END, f"\n Frooti              {self.fruit.get()}            {self.price_fruit}\n")
            if self.nimkos.get() !=0:    
                self.textarea.insert(END, f"\n Nimkas              {self.nimkos.get()}           {self.price_Wheat}\n")
            if self.biscuits.get() !=0:    
                self.textarea.insert(END, f"\n Biscuits            {self.biscuits.get()}          {self.price_biscuits}\n")

            self.textarea.insert(END,"-"*42)
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Cosmetic Tax        {self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Grocery Tax         {self.cosmetic_tax.get()}")
            if self.other_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Other Tax           {self.cosmetic_tax.get()}\n")

            self.textarea.insert(END,"="*42)
            self.textarea.insert(END,f" Total Price :        {self.total_bill}\n")
            self.textarea.insert(END,"="*42)
            self.save_bill()

    def save_bill(self):
        op=msg.askyesno("save bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea().get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            msg.showinfo("saved",f"Billno. {self.bill_no.get()} Saved Successfully")
        else:
            return

    def find_bill(self):
        for i in os.listdir("bills/"):
            print(i)

        
# =========== CLEAR BUTTON=============

    def clear(self):
        self.bath_soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.hair_spray.set(0)
        self.body_lotion.set(0)
        #===========GROCERY.......
        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.Wheat.set(0)
        self.sugar.set(0)
            
        #===========    OTHER .......
        self.maza.set(0)
        self.coke.set(0)
        self.fruit.set(0)
        self.nimkos.set(0)
        self.biscuits.set(0)

        # ============ total price & tax ==========

        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.other_price.set("")

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.other_tax.set("")

        self.customer_name.set("")
        self.phone.set("")
        self.bill_no.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search.set("")
        self.welcome_bill()


# ============ exit button use for  exit window=======

    def Exit(self):
        op=msg.askyesno("Exit","Do you want to EXIT")
        if op>0:
            self.root.destroy()


def mysql(Bill_App):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_tops"
)
mycursor=mydb.cursor()

sql = "INSERT INTO bill software (Customer name, Phone no. , Bill no.) VALUES (%s, %s, %s)"
val = (self.customer_name, self.phone, self.bill_no)

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")



root=Tk()
obj=Bill_App(root)
root.mainloop()


