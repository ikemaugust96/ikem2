# flake8: noqa


cols = 2
rows = 2
cell_size = 100  #
grid = [["" for _ in range(cols)] for _ in range(rows)]
current_color = "RED"
game_over = False
falling_disks = []


class FallingDisk:
    def __init__(self, color, col, row):
        self.color = color
        self.col = col
        self.row = row
        self.y = cell_size / 2


def setup():
    size(cols * cell_size, (rows + 1) * cell_size)
    textSize(34)


def draw():
    global game_over

    background(150)

    for r in range(rows):
        for c in range(cols):
            x, y = c * cell_size, (r + 1) * cell_size
            if grid[r][c] == "RED":
                draw_disk(x, y, "RED")
            elif grid[r][c] == "YELLOW":
                draw_disk(x, y, "YELLOW")

    if falling_disks:
        current_disk = falling_disks[0]
        x = current_disk.col * cell_size + cell_size / 2
        fill(240, 0, 0) if current_disk.color == "RED" else fill(255, 255, 0)
        noStroke()
        ellipse(x, current_disk.y, cell_size * 0.8, cell_size * 0.8)
        current_disk.y += cell_size / 20
        if (
            current_disk.y
            >= (current_disk.row + 1) * cell_size + cell_size / 2
        ):
            grid[current_disk.row][current_disk.col] = current_disk.color
            falling_disks.pop(0)
            check_game_over()

    draw_grid()

    if not game_over and mouseY < cell_size and not falling_disks:
        col = mouseX // cell_size
        x = col * cell_size + cell_size / 2
        fill(240, 0, 0) if current_color == "RED" else fill(255, 255, 0)
        noStroke()
        ellipse(x, cell_size / 2, cell_size * 0.8, cell_size * 0.8)


def draw_grid():
    stroke(0, 0, 400)
    strokeWeight(cell_size / 8)
    for c in range(cols + 1):
        x = c * cell_size
        line(x, cell_size, x, height)
    for r in range(rows + 1):
        y = cell_size + r * cell_size
        line(0, y, width, y)


def draw_disk(x, y, color):
    fill(240, 0, 0) if color == "RED" else fill(255, 255, 0)
    noStroke()
    ellipse(
        x + cell_size / 2, y + cell_size / 2, cell_size * 0.8, cell_size * 0.8
    )


def mouseReleased():
    global current_color

    if game_over or mouseY >= cell_size or falling_disks:
        return

    col = mouseX // cell_size

    for r in range(rows - 1, -1, -1):
        if grid[r][col] == "":
            falling_disks.append(FallingDisk(current_color, col, r))
            current_color = "YELLOW" if current_color == "RED" else "RED"
            break


def check_game_over():
    global game_over

    if not any("" in row for row in grid):
        game_over = True
        print("Game Over!")
