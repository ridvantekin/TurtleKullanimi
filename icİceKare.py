import turtle


arayüz = turtle.Screen()
arayüz.bgcolor("Light blue")
arayüz.title("İç İçe Kare Ekranı")

kare = turtle.Turtle()
kare.color("red")

def kare_ciz(uzunluk):
    for i in range(4):
        kare.forward(uzunluk)
        kare.left(90)
        uzunluk = uzunluk -5


for x in range(7):
    uzunLuk = 200
    kare_ciz(uzunLuk)
    uzunLuk = uzunLuk -20
turtle.done()