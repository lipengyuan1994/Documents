#!/usr/bin/python

import turtle
import datetime


def love():
	def func(x, y):
		main()
	turtle.title("19Happy Valentine's Day!!")
	lv=turtle.Turtle()
	lv.hideturtle()
	lv.getscreen().bgcolor('white')
	lv.color('black','red')
	lv.pensize(1)
	lv.speed(2)
	lv.up()
	lv.goto(0,-150)
  
	lv.down()
	lv.begin_fill()
	lv.goto(0, -150)
	lv.goto(-175.12, -8.59)
	lv.left(140)
	pos = []
	for i in range(19):
		lv.right(10)
		lv.forward(20)
		pos.append((-lv.pos()[0], lv.pos()[1]))
	for item in pos[::-1]:
		lv.goto(item)
	lv.goto(175.12, -8.59)
	lv.goto(0, -150)
	lv.left(50)
	lv.end_fill()
	
	lv.up()
	lv.goto(0, 80)
	lv.down()
	lv.write('To all my connentions on LinkedIn',font=(50),align="center")
	lv.up()
	lv.goto(0, 0)
	lv.down()
	lv.write("Happy",font=(30),align="center")
	lv.up()
	lv.goto(0, -40)
	lv.down()
	lv.write("Valentine's Day!",font=(30),align="center")
	

	lv.showturtle()


def main():
	pass

if __name__ == '__main__':
	if datetime.date.today() == datetime.date(2019, 2, 13):
		love()
	else:
		main()
