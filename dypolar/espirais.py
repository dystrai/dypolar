import math
from typing import Callable
import turtle

def grafico_coord_polar(f: Callable):
    turtle.penup()
    x = f(0)*math.cos(0)
    y = f(0)*math.sin(0)
    turtle.goto(x, y)
    turtle.down()

    for ang_graus in range(0, 10*360+1, 5):
        ang_rad = math.pi*(ang_graus/180)
        x = f(ang_rad)*math.cos(ang_rad)
        y = f(ang_rad)*math.sin(ang_rad)
        turtle.goto(x, y)

def graficos_coord_polar(f1: Callable, f2: Callable):
    t1 = turtle.clone()
    t2 = turtle.clone()

    t1.penup()
    x1 = f1(0)*math.cos(0)
    y1 = f1(0)*math.sin(0)
    t1.goto(x1, y1)
    t1.down()

    t2.penup()
    x2 = f2(0)*math.cos(0)
    y2 = f2(0)*math.sin(0)
    t2.goto(x2, y2)
    t2.down()

    for ang_graus in range(0, 10*360+1, 5):
        ang_rad = math.pi*(ang_graus/180)

        x1 = f1(ang_rad)*math.cos(ang_rad)
        y1 = f1(ang_rad)*math.sin(ang_rad)
        t1.goto(x1, y1)

        x2 = f2(ang_rad)*math.cos(ang_rad)
        y2 = f2(ang_rad)*math.sin(ang_rad)
        t2.goto(x2, y2)



def espiral_arquimedes(ang_rad: float) -> float:
    return 5*ang_rad

def espiral_mermat_neg(ang_rad: float) -> float:
    return 40*(-math.sqrt(ang_rad))

def espiral_mermat_pos(ang_rad: float) -> float:
    return 40*(+math.sqrt(ang_rad))

def main():
    turtle.speed('fastest')
    turtle.hideturtle()

    grafico_coord_polar(espiral_arquimedes)
    turtle.clear()

    graficos_coord_polar(espiral_mermat_neg, espiral_mermat_pos)
    turtle.done()

if __name__ == '__main__':
    main()