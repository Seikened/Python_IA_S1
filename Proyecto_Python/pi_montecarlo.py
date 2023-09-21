# Mindshop Fisica
# Ciclo Mecanica Newtoniana y Relativista
# @Author: Pedro Velez

from manim import *
import numpy as np
import random as ran


class MonteCarlo(Scene):
	def construct(self):

		# Para que el cículo y cuadrado se dibujen a la izquierda
		offset = (-4, 0, 0)

		circle = Circle(radius=2, color=RED)
		circle.move_to(offset)

		square = Rectangle(width=4, height=4)
		square.move_to(offset)

		# Agregando las figuras geometricas
		self.add(circle)
		self.add(square)
		self.wait(1)

		# El texto que muestra el numero total de puntos
		point_text, point_number = point_label = VGroup(
			Text("Total de puntos : "),
			DecimalNumber(
				0,
				show_ellipsis=False,
				num_decimal_places=0
			)
		)

		# El texto que muestra el numero de puntos dentro del circulo
		in_text, in_number = in_label = VGroup(
			Text("Puntos en el circulo : "),
			DecimalNumber(
				0,
				show_ellipsis=False,
				num_decimal_places=0
			)
		)

		# El texto que muestra el valor aproximado de PI
		pi_text, pi_number = pi_label = VGroup(
			Text("Valor aproximado de pi : "),
			DecimalNumber(
				0,
				show_ellipsis=True,
				num_decimal_places=4
			)
		)
		point_label.arrange(RIGHT)
		in_label.arrange(RIGHT)
		pi_label.arrange(RIGHT)

		point_label.move_to((2, -1, 0))
		in_label.move_to((2, 0, 0))
		pi_label.move_to((2, 1, 0))

		self.add(point_label, in_label, pi_label)

		count_all = 0
		c = 0
		apx_pi = 0

		# Las funciones que actualizan los valores de cada etiqueta
		point_number.add_updater(lambda m: m.set_value(count_all))
		in_number.add_updater(lambda m: m.set_value(c))
		pi_number.add_updater(lambda m: m.set_value(apx_pi))

		ran.seed(1)

		# Se realiza la corrida para 10 mil valores
		for i in range(1, 10001):
			# Se genera un punto aleatorio
			pos = (-6 + ran.random() * 4, -2 + ran.random() * 4, 0)
			# Si el punto esta dentro del ciculo se pinta en rojo y se incrementa el contador correspondiente
			if ((pos[0] + 4) ** 2 + pos[1] ** 2 < 4):
				d = Dot(color=RED, radius=0.01)
				c += 1
			# De lo contrario se pinta en verde
			else:
				d = Dot(color=GREEN, radius=0.01)
			d.move_to(pos)

			# Se agrega un punto nuevo cada .01 segundos
			self.play(Create(d, run_time=0.01))
			count_all = i
			# Se calcula el valor aproximado de PI usando la formula pi/4 = (puntosDentroDelCirculo/totalDePuntos)
			apx_pi = c / (i) * 4

		# Al final espera 2 segundos antes de finalizar el video
		self.wait(2)
