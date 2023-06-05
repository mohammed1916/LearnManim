import itertools
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
            # Set origin to start_basket
            balls.move_to(start_basket.get_center())

            self.play(Write(balls))

            self.wait()

            self.insert_balls_into_buckets(balls, target_buckets)
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

    def insert_balls_into_buckets(self, balls, target_buckets):
        for ball, bucket in zip(balls, target_buckets):
            self.play(ball.animate.move_to(bucket), run_time=0.5)

    def clear_balls_from_buckets(self, buckets):
        self.play(*[ball.animate.move_to(ORIGIN) for ball in buckets])
