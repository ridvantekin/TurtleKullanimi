import turtle


arayuz = turtle.Screen()
arayuz.bgcolor("light green")
arayuz.title("Renkli Spreal Arayüz Ekranı")

spreal = turtle.Turtle()
spreal.color("orange")

colors_list = ["red" , "orange" , "black" , "white" , "yellow"]

for i in range(15):
    genislik = 10
    eksiGenislik = -10

    spreal.circle(genislik)
    spreal.circle(eksiGenislik)

    eksiGenislik -= 10
    genislik += 10






turtle.done()