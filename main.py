import tkinter as tk
from tkinter import messagebox as msgb

def hello_world():
    try:
        nombre = str(input1.get())
        edad = int(input2.get())
        nivel_Hormonas = float(input3.get())
        resultado = ""
        if ((edad >= 12) and (edad <= 14)) and ((nivel_Hormonas < 14) or (nivel_Hormonas < 27)):
            resultado = "Resultado de embarazo: Positivo"
        elif ((edad >= 15) and (edad <= 16)) and ((nivel_Hormonas < 11) or (nivel_Hormonas < 19)):
            resultado = "Resultado de embarazo: Positivo"
        elif ((edad >= 17) and (edad <= 20)) and ((nivel_Hormonas < 11) or (nivel_Hormonas < 15)):
            resultado = "Resultado de embarazo: Positivo"
        elif ((edad >= 21) and (edad <= 24)) and ((nivel_Hormonas < 11.5) or (nivel_Hormonas < 15)):
            resultado = "Resultado de embarazo: Positivo"
        elif((edad >= 25) and (edad <= 33)) and ((nivel_Hormonas < 13.6) or (nivel_Hormonas < 16.5)):
            resultado = "Resultado de embarazo: positivo"
        else:
            resultado = "Resultado de embarazo: Negativo"
            #Mandamos el resultado al input de la app
            text_result1.config(text=f"Nombre paciente:{nombre} edad:{edad}")
            text_result2.config(text=f"Nivel Hormonas:{nivel_Hormonas}")
            text_result3.config(text=resultado)
    except ValueError:
        msgb.showerror("Error","Campos vacios")





view = tk.Tk()
view.geometry("650x450")
view.config(background="black")
view.title("Hormonas")

img = tk.PhotoImage(file="src/background.png",width=650,height=450)

fondo = tk.Label(view,image=img)
fondo.pack()

frame = tk.Label(view,bg="#39C1EB")

#formulary frame
frame.place(relheight=0.6,relwidth=0.4,relx=0.3,rely=0.2)

#title
title = tk.Label(frame,text="viva1 IPS",font="Helvetica",background="#74bc04")
title.place(x=0,y=15,relwidth=1)

#FirstTextLabel
text1 = tk.Label(frame,text="Digite su nombre",font="Helvetica",background="#39C1EB")
text1.place(x=0,y=60,relwidth=0.5)

#FirstInput
input1 = tk.Entry(frame,width=30)
input1.place(x=130,y=65,relwidth=0.5)

#SecondTextLabel
text2 = tk.Label(frame,text="Digite su edad",font="Helvetica",background="#39C1EB")
text2.place(x=0,y=100,relwidth=0.5)

#secondInput
input2 = tk.Entry(frame,width=30)
input2.place(x=130,y=100,relwidth=0.5)

#ThirdTextLabel
text3 = tk.Label(frame,text="Nivel Hormonas:",font="Helvetica",background="#39C1EB")
text3.place(x=0,y=140,relwidth=0.5)

#ThirdInput
input3 = tk.Entry(frame,width=30)
input3.place(x=130,y=140,relwidth=0.5)

#Btn
btn_sent = tk.Button(frame,text="calcular",activebackground="#74bc04",command=hello_world)
btn_sent.place(x=90,y=240,relheight=0.1,relwidth=0.3)


#input_Result
result = tk.Label(frame,text=" ")
result.place(x=0,y=170,relheight=0.25,relwidth=1)

#textResultado = Aca va el texto, el input_result es el frame
text_result1 = tk.Label(result,text=" ",foreground="black")
text_result1.place(x=0,y=0,relwidth=1,relheight=0.3)

text_result2 = tk.Label(result,text=" ",foreground="black")
text_result2.place(x=0,y=20,relwidth=1,relheight=0.3)
#
text_result3 = tk.Label(result,text=" ",foreground="black")
text_result3.place(x=0,y=40,relwidth=1,relheight=0.3)

view.resizable("false","false")
view.mainloop()