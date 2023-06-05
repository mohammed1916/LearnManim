from manim import *
from manim.utils.color import *
import itertools


# class Permutations(Scene):
#     def construct(self):
#         # Create five buckets
#         self.buckets = []
#         for i in range(5):
#             self.buckets.append(
#                 Circle(radius=0.5, color=colors.get_random_color()))

#         # Create 10 balls
#         self.balls = []
#         for i in range(10):
#             self.balls.append(
#                 Circle(radius=0.2, color=colors.get_random_color()))

#         # Insert the balls into the buckets in a random order
#         for ball in self.balls:
#             bucket = self.buckets[random.randint(0, 4)]
#             bucket.add_to_back(ball)

#         # Display the buckets and balls
#         self.wait(2)
#         for bucket in self.buckets:
#             self.play(ShowCreation(bucket))
#         for ball in self.balls:
#             self.play(ShowCreation(ball))

#         # Wait for the user to press enter
#         self.wait(2)
#         self.input("Press enter to continue")


# class Permutations(Scene):
#     def construct(self):
#         buckets = VGroup(
#             *[Square(side_length=1, fill_opacity=0.5, fill_color=BLUE_D) for _ in range(5)])
#         buckets.arrange(RIGHT, buff=1)

#         balls = VGroup(*[Dot() for _ in range(10)])

#         self.play(Create(buckets))
#         self.play(Write(balls))

#         self.wait()

#         # Generate all permutations of the balls
#         permutations = self.get_permutations(balls)

#         for permutation in permutations:
#             self.insert_balls_into_buckets(permutation, buckets)
#             self.wait(1)
#             self.clear_balls_from_buckets(buckets)

#         self.wait()

#     def get_permutations(self, balls):
#         return list(itertools.permutations(balls))

#     def insert_balls_into_buckets(self, balls, buckets):
#         for ball, bucket in zip(balls, buckets):
#             self.play(ball.animate.move_to(bucket))

#     def clear_balls_from_buckets(self, buckets):
#         self.play(*[ball.animate.move_to(ORIGIN) for ball in buckets])


# from manim import *
# from manim.utils.color import *


# class Permutations(Scene):
#     def construct(self):
#         buckets = VGroup(
#             *[Square(side_length=1, fill_opacity=0.5, fill_color=BLUE_D) for _ in range(3)])
#         buckets.arrange(RIGHT, buff=1)

#         balls = VGroup(*[Dot() for _ in range(3)])

#         self.play(Create(buckets))
#         self.play(Write(balls))

#         self.wait()

#         # Generate all permutations of the balls
#         permutations = self.get_permutations(balls)

#         for permutation in permutations:
#             self.insert_balls_into_buckets(permutation, buckets)
#             self.wait(1)
#             self.clear_balls_from_buckets(buckets)

#         self.wait()

#     def get_permutations(self, balls):
#         return list(itertools.permutations(balls))

#     def insert_balls_into_buckets(self, balls, buckets):
#         for ball, bucket in zip(balls, buckets):
#             self.play(ball.animate.move_to(bucket))

#     def clear_balls_from_buckets(self, buckets):
#         self.play(*[ball.animate.move_to(ORIGIN) for ball in buckets])

from manim import *
from manim.utils.color import *


class Permutations(Scene):
    def construct(self):
        buckets = VGroup(
            *[Square(side_length=1, fill_opacity=0.5, fill_color=BLUE_D) for _ in range(3)])
        buckets.arrange(RIGHT, buff=1)

        balls = VGroup(*[Dot() for _ in range(3)])

        self.play(Create(buckets))
        self.play(Write(balls))

        self.wait()

        # Generate all permutations of the balls
        permutations = self.get_permutations(balls)

        for permutation in permutations:
            self.insert_balls_into_buckets(permutation, buckets)
            self.wait(1)
            self.clear_balls_from_buckets(buckets)

        self.wait()

    def get_permutations(self, balls):
        return list(itertools.permutations(balls))

    def insert_balls_into_buckets(self, balls, buckets):
        for ball, bucket in zip(balls, buckets):
            self.play(ball.animate.move_to(bucket.get_center() + DOWN * 1.5))
            self.play(ball.animate.move_to(bucket))

    def clear_balls_from_buckets(self, buckets):
        self.play(*[ball.animate.move_to(ORIGIN) for ball in buckets])
