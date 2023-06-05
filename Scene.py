from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        # circle.set_fill(PINK, opacity=0.5)  # set color and transparency
        circle.set_stroke(TEAL_E, width=8)  # set color and transparency

        self.play(Create(circle))  # animate the creation of the square
