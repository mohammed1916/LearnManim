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
#             self.play(ball.animate.move_to(bucket.get_center() + DOWN * 1.5))
#             self.play(ball.animate.move_to(bucket))

#     def clear_balls_from_buckets(self, buckets):
#         self.play(*[ball.animate.move_to(ORIGIN) for ball in buckets])

# from manim import *
# from manim.utils.color import *


# class Permutations(Scene):
#     def construct(self):
#         start_basket = Square(
#             side_length=1, fill_opacity=0.5, fill_color=YELLOW)
#         target_buckets = VGroup(
#             *[Square(side_length=1, fill_opacity=0.5, fill_color=BLUE_D) for _ in range(3)])
#         target_buckets.arrange(RIGHT, buff=1)

#         balls = VGroup(*[Dot() for _ in range(3)])

#         self.play(Create(start_basket))
#         self.play(start_basket.animate.shift(UP * 2))

#         self.play(Write(balls))

#         self.wait()

#         # Generate all permutations of the balls
#         permutations = self.get_permutations(balls)

#         for permutation in permutations:
#             self.insert_balls_into_buckets(
#                 permutation, start_basket, target_buckets)
#             self.wait(1)
#             self.clear_balls_from_buckets(target_buckets)

#         self.wait()

#     def get_permutations(self, balls):
#         return list(itertools.permutations(balls))

#     def insert_balls_into_buckets(self, balls, start_basket, target_buckets):
#         for ball, bucket in zip(balls, target_buckets):
#             self.play(ball.animate.move_to(start_basket.get_center()))
#             self.play(ball.animate.move_to(bucket.get_center() + DOWN * 1.5))
#             self.play(ball.animate.move_to(bucket))

#     def clear_balls_from_buckets(self, buckets):
#         self.play(*[ball.animate.move_to(ORIGIN) for ball in buckets])


# from manim import *
# from manim.utils.color import *


# class Permutations(Scene):
#     def construct(self):
#         start_basket = Square(
#             side_length=1, fill_opacity=0.5, fill_color=YELLOW)
#         target_buckets = VGroup(
#             *[Square(side_length=1, fill_opacity=0.5, fill_color=BLUE_D) for _ in range(3)])
#         target_buckets.arrange(RIGHT, buff=1)

#         colors = [RED, GREEN, BLUE]  # Add more colors if needed

#         balls = VGroup(*[Dot(color=color) for color in colors])

#         self.play(Create(start_basket))
#         self.play(start_basket.animate.shift(UP * 2))

#         self.play(Write(balls))

#         self.wait()

#         # Generate all permutations of the balls
#         permutations = self.get_permutations(balls)

#         for permutation in permutations:
#             self.insert_balls_into_buckets(
#                 permutation, start_basket, target_buckets)
#             self.wait(1)
#             self.clear_balls_from_buckets(target_buckets)

#         self.wait()

#     def get_permutations(self, balls):
#         return list(itertools.permutations(balls))

#     def insert_balls_into_buckets(self, balls, start_basket, target_buckets):
#         for ball, bucket in zip(balls, target_buckets):
#             self.play(ball.animate.move_to(start_basket.get_center()))
#             self.play(ball.animate.move_to(bucket.get_center() + DOWN * 1.5))
#             self.play(ball.animate.move_to(bucket))

#     def clear_balls_from_buckets(self, buckets):
#         self.play(*[ball.animate.move_to(ORIGIN) for ball in buckets])


# from manim import *
# from manim.utils.color import *


# class Permutations(Scene):
#     def construct(self):
#         start_basket = Square(
#             side_length=1, fill_opacity=0.5, fill_color=YELLOW)
#         target_buckets = VGroup(
#             *[Square(side_length=1, fill_opacity=0, stroke_color=WHITE) for _ in range(3)])
#         target_buckets.arrange(RIGHT, buff=1)

#         colors = [RED, GREEN, BLUE]  # Add more colors if needed

#         balls = VGroup(*[Dot(color=color) for color in colors])

#         self.play(Create(start_basket))
#         self.play(start_basket.animate.shift(UP * 2))

#         self.wait()

#         self.play(Create(target_buckets))

#         self.play(Write(balls))

#         self.wait()

#         # Generate all permutations of the balls
#         permutations = self.get_permutations(balls)

#         for permutation in permutations:
#             self.insert_balls_into_buckets(
#                 permutation, start_basket, target_buckets)
#             self.wait(1)
#             self.clear_balls_from_buckets(target_buckets)

#         self.wait()

#     def get_permutations(self, balls):
#         return list(itertools.permutations(balls))

#     def insert_balls_into_buckets(self, balls, start_basket, target_buckets):
#         for ball, bucket in zip(balls, target_buckets):
#             self.play(ball.animate.move_to(start_basket.get_center()))
#             self.play(ball.animate.move_to(bucket.get_center() + DOWN * 1.5))
#             self.play(ball.animate.move_to(bucket))

#     def clear_balls_from_buckets(self, buckets):
#         self.play(*[ball.animate.move_to(ORIGIN) for ball in buckets])


# from manim import *
# from manim.utils.color import *


# class Permutations(Scene):
#     def construct(self):
#         start_basket = Square(
#             side_length=1, fill_opacity=0.5, fill_color=YELLOW)

#         colors = [RED, GREEN, BLUE]  # Add more colors if needed

#         balls = VGroup(*[Dot(color=color) for color in colors])

#         self.play(Create(start_basket))
#         self.play(start_basket.animate.shift(UP * 2))

#         self.wait()

#         self.play(Write(balls))

#         self.wait()

#         # Generate all permutations of the balls
#         permutations = self.get_permutations(balls)

#         target_buckets = None

#         for i, permutation in enumerate(permutations):
#             if i == 0:
#                 target_buckets = self.create_target_buckets(permutation)
#             else:
#                 self.clear_balls_from_buckets(target_buckets)
#                 target_buckets = self.create_target_buckets(permutation)

#             self.insert_balls_into_buckets(
#                 permutation, start_basket, target_buckets)
#             self.wait(1)

#         self.wait()

#     def get_permutations(self, balls):
#         return list(itertools.permutations(balls))

#     def create_target_buckets(self, balls):
#         target_buckets = VGroup(
#             *[Square(side_length=1, fill_opacity=0.5, fill_color=BLUE_D) for _ in range(len(balls))])
#         target_buckets.arrange(RIGHT, buff=1)
#         self.play(Create(target_buckets))
#         return target_buckets

#     def insert_balls_into_buckets(self, balls, start_basket, target_buckets):
#         for ball, bucket in zip(balls, target_buckets):
#             self.play(ball.animate.move_to(start_basket.get_center()))
#             self.play(ball.animate.move_to(bucket.get_center() + DOWN * 1.5))
#             self.play(ball.animate.move_to(bucket))

#     def clear_balls_from_buckets(self, buckets):
#         self.play(*[ball.animate.move_to(ORIGIN) for ball in buckets])


# from manim import *
# from manim.utils.color import *


# class Permutations(Scene):
#     def construct(self):
#         start_basket = Square(
#             side_length=1, fill_opacity=0.5, fill_color=YELLOW)
#         target_bucket_groups = []

#         colors = [RED, GREEN, BLUE]  # Add more colors if needed

#         balls = VGroup(*[Dot(color=color) for color in colors])

#         self.play(Create(start_basket))
#         self.play(start_basket.animate.shift(UP * 2))

#         self.wait()

#         self.play(Write(balls))

#         self.wait()

#         # Generate all permutations of the balls
#         permutations = self.get_permutations(balls)

#         for i, permutation in enumerate(permutations):
#             target_buckets = self.create_target_buckets(permutation)
#             target_bucket_groups.append(target_buckets)

#             self.insert_balls_into_buckets(
#                 permutation, start_basket, target_buckets)
#             self.wait(1)

#         self.wait()

#     def get_permutations(self, balls):
#         return list(itertools.permutations(balls))

#     def create_target_buckets(self, balls):
#         target_buckets = VGroup(
#             *[Square(side_length=1, fill_opacity=0.5, fill_color=BLUE_D) for _ in range(len(balls))])
#         target_buckets.arrange(RIGHT, buff=1)
#         self.play(Create(target_buckets))
#         return target_buckets

#     def insert_balls_into_buckets(self, balls, start_basket, target_buckets):
#         for ball, bucket in zip(balls, target_buckets):
#             self.play(ball.animate.move_to(start_basket.get_center()))
#             self.play(ball.animate.move_to(bucket.get_center() + DOWN * 1.5))
#             self.play(ball.animate.move_to(bucket))

#     def clear_balls_from_buckets(self, buckets):
#         self.play(*[ball.animate.move_to(ORIGIN) for ball in buckets])


# from manim import *
# from manim.utils.color import *


# class Permutations(Scene):
#     def construct(self):
#         start_basket = Square(
#             side_length=1, fill_opacity=0.5, fill_color=YELLOW)
#         target_bucket_groups = []

#         colors = [RED, GREEN, BLUE]  # Add more colors if needed

#         balls = VGroup(*[Dot(color=color) for color in colors])

#         self.play(Create(start_basket))
#         self.play(start_basket.animate.shift(UP * 2))

#         self.wait()

#         self.play(Write(balls))

#         self.wait()

#         # Generate all permutations of the balls
#         permutations = self.get_permutations(balls)

#         for i, permutation in enumerate(permutations):
#             target_buckets = self.create_target_buckets(permutation)
#             target_bucket_groups.append(target_buckets)

#             self.insert_balls_into_buckets(
#                 permutation, start_basket, target_buckets)
#             self.wait(1)

#         self.wait()

#     def get_permutations(self, balls):
#         return list(itertools.permutations(balls))

#     def create_target_buckets(self, balls):
#         target_buckets = VGroup(
#             *[Square(side_length=1, fill_opacity=0.5, fill_color=BLUE_D) for _ in range(len(balls))])
#         target_buckets.arrange(RIGHT, buff=1)
#         self.play(Create(target_buckets))
#         return target_buckets

#     def insert_balls_into_buckets(self, balls, start_basket, target_buckets):
#         for ball, bucket in zip(balls, target_buckets):
#             self.play(ball.animate.move_to(
#                 start_basket.get_center()), run_time=0.5)
#             self.play(ball.animate.move_to(
#                 bucket.get_center() + DOWN * 1.5), run_time=0.5)
#             self.play(ball.animate.move_to(bucket), run_time=0.5)

#     def clear_balls_from_buckets(self, buckets):
#         self.play(*[ball.animate.move_to(ORIGIN) for ball in buckets])


# from manim import *
# from manim.utils.color import *


# class Permutations(Scene):
#     def construct(self):
#         start_basket = Square(
#             side_length=1, fill_opacity=0.5, fill_color=YELLOW)
#         target_bucket_groups = []

#         colors = [RED, GREEN, BLUE]  # Add more colors if needed

#         balls = VGroup(*[Dot(color=color) for color in colors])

#         self.play(Create(start_basket))
#         self.play(start_basket.animate.shift(UP * 2))

#         self.wait()

#         self.play(Write(balls))

#         self.wait()

#         # Generate all permutations of the balls
#         permutations = self.get_permutations(balls)

#         for i, permutation in enumerate(permutations):
#             target_buckets = self.create_target_buckets(permutation)
#             target_bucket_groups.append(target_buckets)

#             self.insert_balls_into_buckets(permutation, target_buckets)
#             self.wait(1)

#         self.wait()

#     def get_permutations(self, balls):
#         return list(itertools.permutations(balls))

#     def create_target_buckets(self, balls):
#         target_buckets = VGroup(
#             *[Square(side_length=1, fill_opacity=0.5, fill_color=BLUE_D) for _ in range(len(balls))])
#         target_buckets.arrange(RIGHT, buff=1)
#         self.play(Create(target_buckets))
#         return target_buckets

#     def insert_balls_into_buckets(self, balls, target_buckets):
#         for ball, bucket in zip(balls, target_buckets):
#             self.play(ball.animate.move_to(bucket), run_time=0.5)

#     def clear_balls_from_buckets(self, buckets):
#         self.play(*[ball.animate.move_to(ORIGIN) for ball in buckets])


from manim import *
from manim.utils.color import *


class Permutations(Scene):
    def construct(self):
        start_basket = Square(
            side_length=1, fill_opacity=0.5, fill_color=YELLOW)
        target_bucket_groups = []

        colors = [RED, GREEN, BLUE]  # Add more colors if needed

        self.play(Create(start_basket))
        self.play(start_basket.animate.shift(UP * 2))

        self.wait()

        # Generate all permutations of the balls
        permutations = self.get_permutations(colors)

        for i, permutation in enumerate(permutations):
            target_buckets = self.create_target_buckets(permutation)
            target_bucket_groups.append(target_buckets)

            balls = VGroup(*[Dot(color=color) for color in permutation])

            self.play(Write(balls))

            self.wait()

            self.insert_balls_into_buckets(balls, start_basket, target_buckets)
            self.wait(1)

            self.play(FadeOut(balls))

        self.wait()

    def get_permutations(self, colors):
        return list(itertools.permutations(colors))

    def create_target_buckets(self, balls):
        target_buckets = VGroup(
            *[Square(side_length=1, fill_opacity=0.5, fill_color=BLUE_D) for _ in range(len(balls))])
        target_buckets.arrange(RIGHT, buff=1)
        self.play(Create(target_buckets))
        return target_buckets

    def insert_balls_into_buckets(self, balls, start_basket, target_buckets):
        for ball, bucket in zip(balls, target_buckets):
            self.play(ball.animate.move_to(
                start_basket.get_center()), run_time=0.5)
            self.play(ball.animate.move_to(
                bucket.get_center() + DOWN * 1.5), run_time=0.5)
            self.play(ball.animate.move_to(bucket), run_time=0.5)

    def clear_balls_from_buckets(self, buckets):
        self.play(*[ball.animate.move_to(ORIGIN) for ball in buckets])
