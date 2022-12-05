import os

prio = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part1(inp):
	ps = 0
	for items in inp:
		l = len(items)
		h1, h2 = items[:l//2], items[l//2:]
		h1c = []
		for c in h1:
			h1c.append(c)
		for c in h2:
			if c in h1c:
				ps += prio.find(c)
				break
	return ps


def part2(inp):
	ps = 0
	for i in range(0, len(inp), 3):
		h1, h2, h3 = inp[i], inp[i+1], inp[i+2]
		h1c, h2c = [], []
		for c in h1:
			h1c.append(c)
		for c in h2:
			if c in h1c:
				h2c.append(c)
		for c in h3:
			if c in h2c:
				ps += prio.find(c)
				break
	return ps

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