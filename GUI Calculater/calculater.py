from tkinter import *
from PIL import Image,ImageTk
import winsound
class Calculater:
    def __init__(self,root):
        self.root=root
        self.root.title("Calculater Software")
        self.root.geometry("285x435+500+100")
        self.root.configure(background="white")
        self.root.resizable(False,False)
        # frame
        self.frame=Image.open("image/frame.png")
        self.frame=self.frame.resize((291,435))
        self.pho1=ImageTk.PhotoImage(self.frame)
        self.frame_label=Label(self.root,image=self.pho1,bd=0)
        self.frame_label.place(x=0,y=0)
        
        try:
            with open("folder_sound/s.txt","r") as rd:
                var=rd.read()
                if var=="0" or var=="1":
                    self.sound=int(var) 
                else:
                    self.sound=1
        except FileNotFoundError:
            self.sound=1

        
        # Display
        self.scvariable=StringVar()
        self.display=Entry(self.root,justify=RIGHT,textvariable=self.scvariable,width=15,font="Helvetica 24",bd=1,background="#D9D9D9",cursor="arrow",relief=SOLID)
        self.display.place(x=5,y=50)
        # ========== row 0 =========
        # pi button
        self.btn_pi_image=Image.open("image/pi.png")
        self.btn_pi_image_resize=self.btn_pi_image.resize((50,50))
        self.btn_image_pi=ImageTk.PhotoImage(self.btn_pi_image_resize)
        self.btn1=Button(root,image=self.btn_image_pi,bd=0,width=55,height=45,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button("pi"))
        self.btn1.place(x=10,y=135)
        
        # power button
        self.btn_power_image=Image.open("image/power.png")
        self.btn_power_image_resize=self.btn_power_image.resize((50,50))
        self.btn_image_power=ImageTk.PhotoImage(self.btn_power_image_resize)
        self.btn2=Button(root,image=self.btn_image_power,bd=0,width=55,height=45,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button("^"))
        self.btn2.place(x=80,y=135)
        
        # delete button
        self.btn_del_image=Image.open("image/del.png")
        self.btn_del_image_resize=self.btn_del_image.resize((50,50))
        self.btn_image_del=ImageTk.PhotoImage(self.btn_del_image_resize)
        self.btn3=Button(root,image=self.btn_image_del,bd=0,width=55,height=45,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button("del"))
        self.btn3.place(x=150,y=135)
        
        # arrow button
        self.btn_arrow_image=Image.open("image/arrow.png")
        self.btn_arrow_image_resize=self.btn_arrow_image.resize((50,50))
        self.btn_image_arrow=ImageTk.PhotoImage(self.btn_arrow_image_resize)
        self.btn4=Button(root,image=self.btn_image_arrow,bd=0,width=55,height=45,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button("arrow"))
        self.btn4.place(x=220,y=135)
        
        # ========== row 1 =========
        # seven button
        self.btn_seven_image=Image.open("image/seven.png")
        self.btn_seven_image_resize=self.btn_seven_image.resize((50,50))
        self.btn_image_seven=ImageTk.PhotoImage(self.btn_seven_image_resize)
        self.btn5=Button(root,image=self.btn_image_seven,bd=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button(7))
        
        self.btn5.place(x=10,y=195)
        
        # eight button
        self.btn_eight_image=Image.open("image/eight.png")
        self.btn_eight_image_resize=self.btn_eight_image.resize((50,50))
        self.btn_image_eight=ImageTk.PhotoImage(self.btn_eight_image_resize)
        self.btn6=Button(root,image=self.btn_image_eight,bd=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button(8))
        self.btn6.place(x=80,y=195)
        
        # nine button
        self.btn_nine_image=Image.open("image/nine.png")
        self.btn_nine_image_resize=self.btn_nine_image.resize((50,50))
        self.btn_image_nine=ImageTk.PhotoImage(self.btn_nine_image_resize)
        self.btn7=Button(root,image=self.btn_image_nine,bd=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button(9))
        self.btn7.place(x=150,y=195)
        
        # divide button
        self.btn_divide_image=Image.open("image/divide.png")
        self.btn_divide_image_resize=self.btn_divide_image.resize((50,50))
        self.btn_image_divide=ImageTk.PhotoImage(self.btn_divide_image_resize)
        self.btn8=Button(root,image=self.btn_image_divide,bd=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button("/"))
        self.btn8.place(x=220,y=195)
        
        # ========== row 2 =========
        # four button
        self.btn_four_image=Image.open("image/four.png")
        self.btn_four_image_resize=self.btn_four_image.resize((50,50))
        self.btn_image_four=ImageTk.PhotoImage(self.btn_four_image_resize)
        self.btn9=Button(root,image=self.btn_image_four,bd=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button(4))
        self.btn9.place(x=10,y=255)
        
        # five button
        self.btn_five_image=Image.open("image/five.png")
        self.btn_five_image_resize=self.btn_five_image.resize((50,50))
        self.btn_image_five=ImageTk.PhotoImage(self.btn_five_image_resize)
        self.btn10=Button(root,image=self.btn_image_five,bd=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button(5))
        self.btn10.place(x=80,y=255)
        
        # six button
        self.btn_six_image=Image.open("image/six.png")
        self.btn_six_image_resize=self.btn_six_image.resize((50,50))
        self.btn_image_six=ImageTk.PhotoImage(self.btn_six_image_resize)
        self.btn11=Button(root,image=self.btn_image_six,bd=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button(6))
        self.btn11.place(x=150,y=255)
        
        # multiply button
        self.btn_multiply_image=Image.open("image/multiply.png")
        self.btn_multiply_image_resize=self.btn_multiply_image.resize((50,50))
        self.btn_image_multiply=ImageTk.PhotoImage(self.btn_multiply_image_resize)
        self.btn12=Button(root,image=self.btn_image_multiply,bd=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button("X"))
        self.btn12.place(x=220,y=255)
        
        
        # ========== row 3 =========
        # one button
        self.btn_one_image=Image.open("image/one.png")
        self.btn_one_image_resize=self.btn_one_image.resize((50,50))
        self.btn_image_one=ImageTk.PhotoImage(self.btn_one_image_resize)
        self.btn13=Button(root,image=self.btn_image_one,bd=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button(1))
        self.btn13.place(x=10,y=315)
        
        # two button
        self.btn_two_image=Image.open("image/two.png")
        self.btn_two_image_resize=self.btn_two_image.resize((50,50))
        self.btn_image_two=ImageTk.PhotoImage(self.btn_two_image_resize)
        self.btn14=Button(root,image=self.btn_image_two,bd=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button(2))
        self.btn14.place(x=80,y=315)
        
        # three button
        self.btn_three_image=Image.open("image/three.png")
        self.btn_three_image_resize=self.btn_three_image.resize((50,50))
        self.btn_image_three=ImageTk.PhotoImage(self.btn_three_image_resize)
        self.btn15=Button(root,image=self.btn_image_three,bd=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button(3))
        self.btn15.place(x=150,y=315)
        
        # minus button
        self.btn_minus_image=Image.open("image/minus.png")
        self.btn_minus_image_resize=self.btn_minus_image.resize((50,50))
        self.btn_image_minus=ImageTk.PhotoImage(self.btn_minus_image_resize)
        self.btn16=Button(root,image=self.btn_image_minus,bd=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button("-"))
        self.btn16.place(x=220,y=315)
        
        # ========== row 4 =========
        # zero button
        self.btn_zero_image=Image.open("image/zero.png")
        self.btn_zero_image_resize=self.btn_zero_image.resize((50,50))
        self.btn_image_zero=ImageTk.PhotoImage(self.btn_zero_image_resize)
        self.btn16=Button(root,image=self.btn_image_zero,bd=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button(0))
        self.btn16.place(x=10,y=375)
        
        # dot button
        self.btn_dot_image=Image.open("image/dot.png")
        self.btn_dot_image_resize=self.btn_dot_image.resize((50,50))
        self.btn_image_dot=ImageTk.PhotoImage(self.btn_dot_image_resize)
        self.btn17=Button(root,image=self.btn_image_dot,borderwidth=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button("."))
        self.btn17.place(x=80,y=375)
        
        # isequla button
        lis=['*','/','*','+','^','minus','Left','Right']
        
        self.btn_isequal_image=Image.open("image/isequal.png")
        self.btn_isequal_image_resize=self.btn_isequal_image.resize((60,30))
        self.btn_image_isequal=ImageTk.PhotoImage(self.btn_isequal_image_resize)
        self.btn18=Button(root,image=self.btn_image_isequal,bd=0,width=65,height=40,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button("="))
        self.display.bind("<Key>","break")
        for i in range(0,9+1): 
            self.display.bind(f"<KeyPress-{i}>","continue")
            
        for i in lis:
            self.display.bind(f"<KeyPress-{i}>","continue")
        
        self.display.bind("<BackSpace>","continue")
        self.display.bind("<KeyPress-=>",lambda e:self.click_button("="))
        self.display.bind("<Return>",lambda e:self.click_button("="))
        self.btn4.bind("<Double-Button-1>",lambda e:self.display.delete(0,END))
        
    
        self.display.focus_set()
        self.btn18.place(x=150,y=380)
        
        # # add button
        self.btn_add_image=Image.open("image/add.png")
        self.btn_add_image_resize=self.btn_add_image.resize((50,50))
        self.btn_image_add=ImageTk.PhotoImage(self.btn_add_image_resize)
        self.btn19=Button(root,image=self.btn_image_add,bd=0,width=55,height=50,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=lambda:self.click_button("+"))
        self.btn19.place(x=220,y=380)
        
        if self.sound==1:
            self.sound_on()
        else:
            self.sound_off()
        
    def sound_on(self):
        # on button
        self.btn_on_image=Image.open("image/on.png")
        self.btn_on_image_resize=self.btn_on_image.resize((40,15))
        self.btn_image_on=ImageTk.PhotoImage(self.btn_on_image_resize)
        self.btn20=Button(root,image=self.btn_image_on,bd=0,width=40,height=25,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=self.sound_off)
        self.btn20.place(x=210,y=5)
        self.sound=1
        with open("folder_sound/s.txt","w") as wr:
            wr.write(str(self.sound))
    def sound_off(self):
        # off button
        self.btn_off_image=Image.open("image/off.png")
        self.btn_off_image_resize=self.btn_off_image.resize((40,15))
        self.btn_image_off=ImageTk.PhotoImage(self.btn_off_image_resize)
        self.btn21=Button(root,image=self.btn_image_off,bd=0,width=40,height=25,background="#D9D9D9",activebackground="#D9D9D9",relief=GROOVE,command=self.sound_on)
        self.btn21.place(x=210,y=5)
        self.sound=0
        with open("folder_sound/s.txt","w") as wr:
            wr.write(str(self.sound))
    
        
    
    def click_button(self,event):
        if self.sound==1:
            winsound.PlaySound('msic/m2.mp3',1)
           
            
        if event=="arrow":
            position=self.display.index(INSERT)
            dig=self.display.get()
            sto=dig[0:position]
            sto=sto[0:-1]
            t=sto+dig[position:]
            self.display.delete(0,END)
            self.display.insert(0,t)
            self.display.icursor(position-1)
            
            return
        
        if event=="pi":
            self.display.insert(END,"3.1415926535897")
            return
        if event=="del":
            self.display.delete(0,'end')
            try:
                self.show_pre.destroy()
                
            except AttributeError:
                pass
            
            return
        if event=="X":
            self.display.insert(END,"*")
            return
        if event=="=":
            
            try:
                ex=self.display.get()
                
                if ex.find("^")!=-1:
                    ex=ex.split("^")
                    ex=ex[0]+"**"+ex[1]
                
                answer=eval(ex)
                
                self.display.delete(0,'end')
                
                self.display.insert(0,answer)
                # ----
                try:
                    self.show_pre.destroy()
                except AttributeError:
                    pass
                
                self.show_pre=Label(self.root,text=ex,font="Helvetica 15",background="#D9D9D9")
                self.show_pre.place(x=10,y=15)
                # ---
            except ZeroDivisionError:
                self.display.delete(0,'end')
                self.display.insert(0,"Cannot be divided by 0")
            except SyntaxError:
                self.display.delete(0,'end')
                self.display.insert(0,"SyntaxError")
            
        else:
            position=self.display.index(INSERT)
            dig=self.display.get()
            read_num=dig[0:position]
            read_num=read_num+str(event)
            t=read_num+dig[position:]
            self.display.delete(0,END)
            self.display.insert(0,t)
            self.display.icursor(position+1)
    
    
            
if __name__=="__main__":
    
    root=Tk()
    calculater=Calculater(root)
    root.mainloop()