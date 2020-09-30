import argparse


def find_next_unmarked(sector_grid):
    for y, row in enumerate(sector_grid):
        for x, col in enumerate(row):
            if col == 0:
                return x, y


def valid_coordinates(x, y, grid):
    if x < 0 or y < 0:
        return False
    try:
        looc = grid[y][x]
        return True
    except IndexError:
        return False


def count_areas(grid):
    sectored = [[0 for i in row] for row in grid]
    # start sector counter at 1
    stats = {}
    sector = 1

    while find_next_unmarked(sectored):
        stack = []
        x_start, y_start = find_next_unmarked(sectored)

        color = grid[y_start][x_start]

        # update stats
        if stats.get(color):
            stats[color] += 1
        else:
            stats[color] = 1

        stack.append([x_start, y_start])

        while len(stack) > 0:
            x, y = stack.pop()

            if not valid_coordinates(x, y, grid):
                continue
            if grid[y][x] != color:
                continue
            if sectored[y][x] != 0:
                continue
            sectored[y][x] = sector

            stack.append([x + 1, y])
            stack.append([x - 1, y])
            stack.append([x, y + 1])
            stack.append([x, y - 1])

        sector += 1

    return stats


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('rb'))

    def list_str_int(values):
        return list(map(int, values.split(',')))

    parser.add_argument('--size', type=list_str_int)
    args = parser.parse_args()

    # get args
    byte_string = args.file.read()
    size = args.size
    width = size[0]
    list_1d = list(byte_string)
    list_2d = list(zip(*[iter(list_1d)] * width))

    print(count_areas(list_2d))
