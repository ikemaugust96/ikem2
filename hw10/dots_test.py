from dots import Dots


def test_constructor():
    ds = Dots(600, 600, 150, 450, 150, 450)
    assert ds.WIDTH == 600
    assert ds.HEIGHT == 600
    assert ds.TH == 150
    assert ds.BH == 450
    assert ds.LV == 150
    assert ds.RV == 450
    assert len(ds.bottom_row) == len(ds.top_row) == ds.WIDTH // ds.SPACING + 1
    assert len(ds.left_col) == len(ds.right_col) == ds.HEIGHT // ds.SPACING + 1
    for i in range(len(ds.left_col)):
        assert ds.left_col[i].x == ds.LV
        assert ds.left_col[i].y == ds.SPACING * i
    for i in range(len(ds.right_col)):
        assert ds.right_col[i].x == ds.RV
        assert ds.right_col[i].y == ds.SPACING * i
    for i in range(len(ds.top_row)):
        assert ds.top_row[i].x == ds.SPACING * i
        assert ds.top_row[i].y == ds.TH
    for i in range(len(ds.bottom_row)):
        assert ds.bottom_row[i].x == ds.SPACING * i
        assert ds.bottom_row[i].y == ds.BH


def test_eat():
    ds = Dots(600, 600, 150, 450, 150, 450)
    initial_dots_left = ds.dots_left()

    # Pac-Man's position
    pacman_x, pacman_y = 150, 150

    # Call the eat method
    ds.eat(pacman_x, pacman_y)

    # Verify dots close to Pac-Man are removed
    for dot in ds.left_col:
        assert dot.distance_to(pacman_x, pacman_y) > ds.EAT_DIST
    for dot in ds.right_col:
        assert dot.distance_to(pacman_x, pacman_y) > ds.EAT_DIST
    for dot in ds.top_row:
        assert dot.distance_to(pacman_x, pacman_y) > ds.EAT_DIST
    for dot in ds.bottom_row:
        assert dot.distance_to(pacman_x, pacman_y) > ds.EAT_DIST

    # Verify that the total number of dots has decreased
    assert ds.dots_left() < initial_dots_left


def test_dots_left():
    ds = Dots(600, 600, 150, 450, 150, 450)
    dl = ds.dots_left()
    assert dl == ((ds.WIDTH // ds.SPACING + 1) * 2 + (ds.HEIGHT // ds.SPACING + 1) * 2)
