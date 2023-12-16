import os

alpha = "abcdefghijklmnopqrstuvwxyz"

def part1(grid, w, h, start, end):
	return find_dist_from_s_to_e(grid, w, h, start, end)

def part2(grid, w, h, end):
	# Find lowest
	m_distance = -1
	for y in range(h):
		for x in range(w):
			if (grid[y * w + x] != 0): continue

			d = find_dist_from_s_to_e(grid, w, h, (x, y), end)
			if (d == -1): continue
			if m_distance == -1: m_distance = d
			else: m_distance = min(m_distance, d)

	return m_distance

def find_dist_from_s_to_e(grid, w, h, start, end):
	# Keep track of visited cells and distance to start.
	dist = [-1] * (w * h)

	# Start location is 0 away
	dist[start[1] * w + start[0]] = 0

	queue = []
	queue.append(start)
	while len(queue) > 0:
		# pop first
		x, y = queue[0]
		del queue[0]

		# current score
		cur = grid[w * y + x]

		# try the neighbors (Left)
		if x > 0 and grid[w * y + x - 1] <= cur + 1:
			# allow checking if we can do better
			if dist[w * y + x - 1] == -1 or dist[w * y + x - 1] > dist[w * y + x] + 1:
				dist[w * y + x - 1] = dist[w * y + x] + 1
				queue.append((x - 1, y))
		# Right
		if x < w - 1 and grid[w * y + x + 1] <= cur + 1:
			# allow checking if we can do better
			if dist[w * y + x + 1] == -1 or dist[w * y + x + 1] > dist[w * y + x] + 1:
				dist[w * y + x + 1] = dist[w * y + x] + 1
				queue.append((x + 1, y))
		# Down
		if y > 0 and grid[w * (y - 1) + x] <= cur + 1:
			# allow checking if we can do better
			if dist[w * (y - 1) + x] == -1 or dist[w * (y - 1) + x] > dist[w * y + x] + 1:
				dist[w * (y - 1) + x] = dist[w * y + x] + 1
				queue.append((x, y - 1))
		# Up
		if y < h - 1 and grid[w * (y + 1) + x] <= cur + 1:
			# allow checking if we can do better
			if dist[w * (y + 1) + x] == -1 or dist[w * (y + 1) + x] > dist[w * y + x] + 1:
				dist[w * (y + 1) + x] = dist[w * y + x] + 1
				queue.append((x, y + 1))

	return dist[end[1] * w + end[0]]

def get_input(fname):
	inp_file_name = f"{fname}_input.txt"
	with open(inp_file_name, 'r') as f:
		return [line.strip() for line in f]

def parse_map(inp):
	w, h = len(inp[0]), len(inp)
	
	grid = [0] * (w * h)
	s, e = ((0,0), (0,0))
	for y in range(h):
		for x in range(w):
			if inp[y][x] in alpha:
				grid[y * w + x] = alpha.index(inp[y][x])
			else:
				if inp[y][x] == 'S':
					grid[y * w + x] = 0
					s = (x, y)
				elif inp[y][x] == 'E':
					grid[y * w + x] = len(alpha) - 1
					e = (x, y)
				else: raise Exception(f"Bad symbol {inp[y][x]} at ({x},{y})")
	return (grid, w, h, s, e)

def main():
	fname = os.path.splitext(os.path.basename(__file__))[0]
	day = int(fname[3:]) # dayXX
	inp = get_input(fname)
	grid, w, h, s, e = parse_map(inp)
	print(f"\n === Day {day} ===")
	print(f" - Part 1: {part1(grid, w, h, s, e)}")
	print(f" - Part 2: {part2(grid, w, h, e)}")

if __name__ == '__main__':
	main()