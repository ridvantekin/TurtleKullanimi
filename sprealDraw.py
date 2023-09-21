import turtle


arayuz = turtle.Screen()
arayuz.bgcolor("light green")
arayuz.title("Renkli Spreal Arayüz Ekranı")

spreal = turtle.Turtle()


colors_list = ["red" , "orange" , "black" , "white", "yellow","grey"]

genislik = 10
eksiGenislik = -10
turtle.speed(0)

for i in range(15):
    genislik += 10
    eksiGenislik -= 10

    spreal.circle(genislik)
    spreal.circle(eksiGenislik)
    spreal.color(colors_list[i % 6])



turtle.mainloop() # sürekli çalışacak. işi bittiğinde sorun çıkarmayacak.

turtle.done()