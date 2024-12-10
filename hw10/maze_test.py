from maze import Maze
from game_controller import GameController


def test_constructor():
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450, 100, 300, g)
    assert m.LEFT_VERT == 150
    assert m.RIGHT_VERT == 450
    assert m.TOP_HORIZ == 100
    assert m.BOTTOM_HORIZ == 300
    assert m.WIDTH == 600
    assert m.HEIGHT == 400
    assert m.gc is g
    assert m.dots.dots_left() == (
        (m.dots.WIDTH // m.dots.SPACING + 1) * 2
        + (m.dots.HEIGHT // m.dots.SPACING + 1) * 2
    )


def test_eat_dots():
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450, 100, 300, g)

    # Initial number of dots
    initial_dots_left = m.dots.dots_left()

    # Pac-Man's position
    pacman_x, pacman_y = 150, 100

    # Call the eat_dots method
    m.eat_dots(pacman_x, pacman_y)

    # Verify dots close to Pac-Man are removed
    for dot in m.dots.left_col:
        assert dot.distance_to(pacman_x, pacman_y) > m.dots.EAT_DIST
    for dot in m.dots.top_row:
        assert dot.distance_to(pacman_x, pacman_y) > m.dots.EAT_DIST

    # Verify total number of dots decreased
    assert m.dots.dots_left() < initial_dots_left
