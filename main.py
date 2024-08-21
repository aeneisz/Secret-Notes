import tkinter as tk
from tkinter import font
from tkinter import messagebox
import base64


window = tk.Tk()
window.title("Secret Notes")
window.minsize(600, 800)
window.resizable(False, False)
window.configure(bg="cornflowerblue",padx=30,pady=30)


#image

resim=tk.PhotoImage(file="topSecret.png")
resimLb=tk.Label(image=resim,background="cornflowerblue")
resimLb.pack(pady=20)


#encode
def encode(key,clear):
    enc=[]
    for i in range(len(clear)):
        key_c=key[i % len(key)]
        enc_c=chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#decode
def decode(key,enc):
    dec=[]
    enc=base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c=key[i % len(key)]
        dec_c=chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)



def mesajGir():
        sifre=entrySifre.get()
        baslik = entryBaslik.get();
        mesaj = txtNot.get("1.0", tk.END).strip()
        if(len(mesaj)==0 or len(baslik)==0 ):
            messagebox.showinfo(title="Hata",message="Boş alan bırakamazsınız!")
        else:
            if(sifre==SIFRE):
                mesajEnc=encode(sifre,mesaj)
                try:
                    with open("Secrets.txt", "a") as dosya:
                        dosya.write("Title: " + baslik + "\n")
                        dosya.write("Secret: " + mesajEnc + "\n")
                    messagebox.showinfo(title="Bilgi", message="Secret başarıyla kaydedildi")
                except FileNotFoundError:
                    with open("Secrets.txt","w") as dosya:
                        dosya.write("Title: " + baslik + "\n")
                        dosya.write("Secret: " + mesajEnc + "\n")
                    messagebox.showinfo(title="Bilgi", message="Dosya oluşturuldu.\nSecret başarıyla kaydedildi")

                finally:
                    entrySifre.delete(0, tk.END)
                    txtNot.delete("1.0", tk.END)
                    entryBaslik.delete(0, tk.END)

            else:
                messagebox.showinfo(title="Hata", message="Hatalı şifre girdiniz!")

def mesajCoz():
    sifre = entrySifre.get()
    mesaj = txtNot.get("1.0", tk.END).strip()
    if (len(mesaj) == 0):
        messagebox.showinfo(title="Hata", message="Boş alan bırakamazsınız!")
    else:
        if (sifre == SIFRE):
            try:
                mesajDec = decode(sifre, mesaj)
                txtNot.delete("1.0",tk.END)
                txtNot.insert("1.0",mesajDec)
            except:
                messagebox.showinfo(title="Hata",message="Doğru kodu gir")

        else:
            messagebox.showinfo(title="Hata", message="Hatalı şifre girdiniz!")


#Font
FONT = font.Font(family='Comic Sans MS', size=20, weight='normal')
FONT2 = font.Font(family='Comic Sans MS', size=16, weight='normal')

SIFRE="archon"


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
txtNot=tk.Text(height=18,width=45)
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
btnCoz=tk.Button(text="Çözümle",width=20,command=mesajCoz)
btnCoz.pack()



window.mainloop()


