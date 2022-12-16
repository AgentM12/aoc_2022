import os
from functools import reduce

def part1(inp):
	w, h = len(inp[0]), len(inp)

	dirm = ((w, h, True, False),
		    (h, w, False, False),
		    (w, h, True, True),
		    (h, w, False, True))

	# from all 4 directions approach the trees.
	vis_coords = set()
	for m in dirm:
		vis_coords.update(walktrees(inp, *m))


	return len(vis_coords)

def part2(inp):
	w, h = len(inp[0]), len(inp)

	tsmax = 0
	for y in range(1, h-1):
		for x in range(1, w-1):
			tsmax = max(tsmax, get_ts(inp, x, y, w, h))
	return tsmax

# Gets scenic score of tree at x,y (5762400>)
def get_ts(inp, x, y, w, h):
	ct = inp[y][x]
	if (ct == 0): return 1 # 0 tree never can have a high score.

	dirs = ((range(x + 1, w), False), (range(y + 1, h), True), (range(x - 1, -1, -1), False), (range(y - 1, -1, -1), True))

	# east score
	scs = []
	for d in dirs:
		scs.append(0)
		for a in d[0]:
			mx, my = (x, a) if d[1] else (a, y)
			ot = inp[my][mx]
			scs[-1] += 1
			if (ot >= ct): break
			
	s = reduce(lambda u, v: u * v, scs, 1)
	return s


def walktrees(inp, end_a, end_b, type_a_is_x, rev_b):
	vs = set()

	def reversed_conditional(range_to_rev, should_rev):
		if should_rev:
			return reversed(range_to_rev)
		else:
			return range_to_rev

	for a in range(end_a):
		lh = -1
		for b in reversed_conditional(range(end_b), rev_b):
			x, y = (a, b) if type_a_is_x else (b, a)
			ct = inp[y][x]
			
			# Tree is visible
			if (ct > lh):
				lh = ct
				vs.add((x, y))
			
	return vs

def parse_input(inp):
	line = []
	for y in inp:
		line.append([int(x) for x in y])
	return line

def get_input(fname):
	inp_file_name = f"{fname}_input.txt"
	with open(inp_file_name, 'r') as f:
		return [line.strip() for line in f]

def main():
	fname = os.path.splitext(os.path.basename(__file__))[0]
	day = int(fname[3:]) # dayXX
	inp = get_input(fname)
	inp = parse_input(inp)
	print(f"\n === Day {day} ===")
	print(f" - Part 1: {part1(inp)}")
	print(f" - Part 2: {part2(inp)}")

if __name__ == '__main__':
	main()