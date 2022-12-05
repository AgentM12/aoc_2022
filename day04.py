import os




def a_subset_b(a, b):
	return a[0] >= b[0] and a[1] <= b[1]

def overlap(a, b):
	return a[1] >= b[0] and a[0] <= b[1]

def part1(inp):
	c = 0
	for pair in inp:
		if a_subset_b(*pair) or a_subset_b(pair[1], pair[0]): c += 1
	return c

def part2(inp):
	c = 0
	for pair in inp:
		if overlap(*pair) or overlap(pair[1], pair[0]): c += 1
	return c

def get_input(fname):
	inp_file_name = f"{fname}_input.txt"
	with open(inp_file_name, 'r') as f:
		return [line.strip() for line in f]

def parse(inp):
	parsed = []
	for line in inp:
		r1, r2 = line.split(',') # guaranteed to be split in 2
		r11, r12, r21, r22 = *r1.split('-'), *r2.split('-')
		parsed.append(((int(r11), int(r12)), (int(r21), int(r22))))
	return parsed

def main():
	fname = os.path.splitext(os.path.basename(__file__))[0]
	day = int(fname[3:]) # dayXX
	inp = get_input(fname)

	inp = parse(inp)

	print(f"\n === Day {day} ===")
	print(f" - Part 1: {part1(inp)}")
	print(f" - Part 2: {part2(inp)}")

if __name__ == '__main__':
	main()