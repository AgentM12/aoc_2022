import os
from functools import cmp_to_key

def part1(inp):
	index = 0
	correct = []
	for left, right in inp:
		index += 1
		if (check(left, right) <= 0): # Should be 0 or negative for correctly ordered packets.
			correct.append(index)
	
	return sum(correct)

def check(left, right):
	'''
	Comparator (left: int or list, right: int or list): int
	 - 0 if equal
	 - Negative if Left < Right (right order)
	 - Positive if Left > Right (wrong order)
	'''
	if isinstance(left, int) and isinstance(right, int):
		return left - right
	if isinstance(left, list) and isinstance(right, list):
		ml = max(len(left), len(right))
		for i in range(ml):
			if i >= len(left):
				return -1
			if i >= len(right):
				return 1
			v = check(left[i], right[i])
			if v != 0:
				return v # difference found.
		return 0 # same length and elems
	if isinstance(left, int):
		return check([left], right)
	if isinstance(right, int):
		return check(left, [right])

def part2(inp):
	dv0, dv1 = [[2]], [[6]]

	# flat map
	sorted_list = []
	for left, right in inp:
		sorted_list.append(left)
		sorted_list.append(right)
	
	# add dividers
	sorted_list.append(dv0)
	sorted_list.append(dv1)

	# sort
	sorted_list.sort(key=cmp_to_key(check))

	return (sorted_list.index(dv0) + 1) * (sorted_list.index(dv1) + 1)

def get_input(fname):
	inp_file_name = f"{fname}_input.txt"
	with open(inp_file_name, 'r') as f:
		return [line.strip() for line in f]

def parse_input(inp):
	pairs = []
	state = 0
	p1, p2 = None, None
	for line in inp:
		if line.strip() == "":
			p1, p2 = None, None
			state = 0
		elif state == 0:
			p1 = parse_line(line, 0)
			state = 1
		elif state == 1:
			p2 = parse_line(line, 0)
			pairs.append((p1, p2))
			state = 0

	return pairs

def parse_line(line, i):
	li = []
	while i < len(line):
		c = line[i]
		i += 1
		if c == '[':
			i, lixt = parse_line(line, i)
			li.append(lixt)
		elif c == ']':
			return i, li
		elif c == ',':
			pass
		else:
			if (c == '1' and line[i] == '0'):
				li.append(10) # special case only for 10
				i += 1 # increment i by 1 more
			else:
				li.append(int(c))
	return li[0]


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