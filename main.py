from PIL import Image, ImageDraw
def solve_maze(filename):
    with open(filename, 'r') as f:
        maze = [list(map(int, line.strip())) for line in f]
    maze_rows = len(maze)
    maze_cols = len(maze[0])
    queue = []
    queue.append((0, 0))
    visited = set()
    previous = {}
    while queue:
        row, col = queue.pop(0)
        if col == maze_cols - 1:
            cell_size = 50
            maze_image = Image.new('RGB', (maze_cols * cell_size, maze_rows * cell_size), color='white')
            draw = ImageDraw.Draw(maze_image)
            for r in range(maze_rows):
                for c in range(maze_cols):
                    if maze[r][c] == 1:
                        draw.rectangle([c * cell_size, r * cell_size, (c + 1) * cell_size, (r + 1) * cell_size],
                                       fill='black')
            path = []
            while (row, col) != (0, 0):
                path.append((row, col))
                row, col = previous[(row, col)]
            path.append((0, 0))
            for r, c in path[::-1]:
                draw.rectangle([c * cell_size, r * cell_size, (c + 1) * cell_size, (r + 1) * cell_size], fill='red')
            maze_image.save('maze_solution.png')
            return "Maze solved!"
        for neighbor_row, neighbor_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= neighbor_row < maze_rows:
                if 0 <= neighbor_col < maze_cols:
                    if (maze[neighbor_row][neighbor_col] == 0):
                        if (neighbor_row, neighbor_col) not in visited:
                            queue.append((neighbor_row, neighbor_col))
                            visited.add((neighbor_row, neighbor_col))
                            previous[(neighbor_row, neighbor_col)] = (row, col)
    return "Maze could not be solved"
filename = 'maze.txt'
print(solve_maze(filename))

