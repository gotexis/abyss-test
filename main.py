from dataclasses import dataclass


@dataclass
class Pixel:
    x: int
    y: int
    color: int
    sector: int = None


def find_next_unmarked(grid):
    for row in grid:
        for j in row:
            if j.sector is None:
                return j


# the main function
def count_areas(pic):
    # get boundary of pic
    max_y = len(pic) - 1
    max_x = len(pic[0]) - 1

    # convert to Pixel grid
    # & make a flat list of Pixels
    pic_flat = []
    pic_grid = [
        [
            Pixel(y=y, x=x, color=color) for x, color in enumerate(line)
        ] for y, line in enumerate(pic)
    ]
    for a in pic_grid:
        for b in a:
            pic_flat.append(b)

    # define the mark function locally
    # arguably can refactor this into a class method
    def mark(pixel: Pixel, color: int, sector: int):
        # don't do anything if already marked
        if pixel.sector is not None:
            return

        if color != pixel.color:
            return
        # mark sector if same color
        if color == pixel.color:
            pixel.sector = sector
        x = pixel.x
        y = pixel.y

        surroundings = []
        # mark surroundings
        if x < max_x:
            surroundings.append(pic_grid[y][x + 1])
        if x > 0:
            surroundings.append(pic_grid[y][x - 1])
        if y > 0:
            surroundings.append(pic_grid[y - 1][x])
        if y < max_y:
            surroundings.append(pic_grid[y + 1][x])

        for p in surroundings:
            try:
                mark(p, color, sector)
            except IndexError:
                # out of range
                ...

    # statistics init
    sector = 0
    colors = {}

    # loop until all is marked
    while True:
        next_pixel = find_next_unmarked(pic_grid)
        if not next_pixel:
            break
        next_unmarked = find_next_unmarked(pic_grid)
        mark(next_unmarked, next_unmarked.color, sector)

        # next sector
        sector += 1
        # record count
        if colors.get(next_unmarked.color):
            colors[next_unmarked.color] += 1
        else:
            colors[next_unmarked.color] = 1

    return {
        "total_sectors": sector,
        "colors": colors
    }
