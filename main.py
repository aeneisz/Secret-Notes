import tkinter as tk
from tkinter import font
from tkinter import messagebox

window = tk.Tk()
window.title("Secret Notes")
window.minsize(600, 800)
window.resizable(False, False)
window.configure(bg="cornflowerblue")



def mesajGir():
        sifre=entrySifre.get()
        baslik = entryBaslik.get();
        mesaj = txtNot.get("1.0", tk.END).strip()
        if(len(mesaj)==0 or len(baslik)==0 ):
            messagebox.showinfo(title="Hata",message="Boş alan bırakamazsınız!")
        else:
            if(sifre==SIFRE):
                with open("Secrets.txt", "a") as dosya:
                    dosya.write("Title:"+baslik + "\n")
                    dosya.write("Secret:"+mesaj + "\n")
                entrySifre.delete(0, tk.END)
                txtNot.delete("1.0", tk.END)
                entryBaslik.delete(0, tk.END)
                messagebox.showinfo(title="Bilgi", message="Secret başarıyla kaydedildi")

            else:
                messagebox.showinfo(title="Hata", message="Hatalı şifre girdiniz!")


#Font
FONT = font.Font(family='Comic Sans MS', size=20, weight='normal')
FONT2 = font.Font(family='Comic Sans MS', size=16, weight='normal')

SIFRE="archon"

#Label
label = tk.Label(text="Secret Quiz", background="cornflowerblue", font=FONT,foreground='white')
label.pack(pady=40)


#Label
label2 = tk.Label(text="Başlığı giriniz", background="cornflowerblue", font=FONT2,foreground='white')
label2.pack()

#Baslık Entryy
entryBaslik=tk.Entry(width=30)
entryBaslik.pack(pady=5)


#Label
label3 = tk.Label(text="Notunuzu giriniz", background="cornflowerblue", font=FONT2,foreground='white')
label3.pack()

#Not Text
txtNot=tk.Text(height=20,width=40)
txtNot.pack(pady=5)

#Label
label4 = tk.Label(text="Şifrenizi giriniz", background="cornflowerblue", font=FONT2,foreground='white')
label4.pack()

#Şifre Entryy
entrySifre=tk.Entry(width=30)
entrySifre.pack(pady=5)

#Buton Kaydet
btnKaydet=tk.Button(text="Kaydet",width=20,command=mesajGir)
btnKaydet.pack(pady=20)

#Buton Cözümle
btnCoz=tk.Button(text="Çözümle",width=20)
btnCoz.pack()



window.mainloop()


