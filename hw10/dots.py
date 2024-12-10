# flake8: noqa
# -*- coding: utf-8 -*-


from dot import Dot


class Dots:
    """A collection of dots."""

    def __init__(
        self, WIDTH, HEIGHT, LEFT_VERT, RIGHT_VERT, TOP_HORIZ, BOTTOM_HORIZ
    ):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TH = TOP_HORIZ
        self.BH = BOTTOM_HORIZ
        self.LV = LEFT_VERT
        self.RV = RIGHT_VERT
        self.SPACING = 75
        self.EAT_DIST = 55
        # Initialize four rows of dots, based on spacing and width of the maze
        self.top_row = [
            Dot(self.SPACING * i, self.TH)
            for i in range(self.WIDTH // self.SPACING + 1)
        ]
        self.bottom_row = [
            Dot(self.SPACING * i, self.BH)
            for i in range(self.WIDTH // self.SPACING + 1)
        ]
        self.left_col = [
            Dot(self.LV, self.SPACING * i)
            for i in range(self.HEIGHT // self.SPACING + 1)
        ]
        self.right_col = [
            Dot(self.RV, self.SPACING * i)
            for i in range(self.HEIGHT // self.SPACING + 1)
        ]

    def display(self):
        """Calls each dot's display method"""
        for dot in (
            self.top_row + self.bottom_row + self.left_col + self.right_col
        ):
            dot.display()

    def eat(self, wall, pacman_position):
        """Removes dots within EAT_DIST based on Pac-Man's position and specified wall."""
        if wall == "TOP":
            self.top_row = [
                dot
                for dot in self.top_row
                if abs(pacman_position - dot.x) >= self.EAT_DIST
            ]
        elif wall == "BOTTOM":
            self.bottom_row = [
                dot
                for dot in self.bottom_row
                if abs(pacman_position - dot.x) >= self.EAT_DIST
            ]
        elif wall == "LEFT":
            self.left_col = [
                dot
                for dot in self.left_col
                if abs(pacman_position - dot.y) >= self.EAT_DIST
            ]
        elif wall == "RIGHT":
            self.right_col = [
                dot
                for dot in self.right_col
                if abs(pacman_position - dot.y) >= self.EAT_DIST
            ]

    def dots_left(self):
        """Returns the number of remaining dots in the collection."""
        return (
            len(self.top_row)
            + len(self.bottom_row)
            + len(self.left_col)
            + len(self.right_col)
        )
