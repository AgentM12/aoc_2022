import os

def part1(inp):
	pass

def part2(inp):
	pass

def get_coords(inp):
	c = set()
	for line in inp:
		pts = line.split(" -> ")
		px, py = None, None
		for pt in pts:
			xy = pt.split(',')
			x, y = int(xy[0]), int(xy[1])
			
			if px is None:
				px = x
				py = y
				continue
			c.add(x, y)
			while px != x and py != y:
				if x > px:
					px += 1
				elif x < px:
					px -= 1
				elif y > py:
					py += 1
				elif y < py:
					py -= 1
				c.add(x, y)
	return c

def get_input(fname):
	inp_file_name = f"{fname}_input.txt"
	with open(inp_file_name, 'r') as f:
		return [line.strip() for line in f]

def main():
	fname = os.path.splitext(os.path.basename(__file__))[0]
	day = int(fname[3:]) # dayXX
	inp = get_input(fname)
	print(f"\n === Day {day} ===")
	print(f" - Part 1: {part1(inp)}")
	print(f" - Part 2: {part2(inp)}")

if __name__ == '__main__':
	main()