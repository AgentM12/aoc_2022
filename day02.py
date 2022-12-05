import os

m1 = {'A': 'R', 'B': 'P', 'C': 'S'}
s = {'R': 1, 'P': 2, 'S': 3}


def win(a, b):
	if a == b: return 0
	if a == 'R':
		if b == 'P': return 1
		else: return -1
	if a == 'P':
		if b == 'S': return 1
		else: return -1
	if a == 'S':
		if b == 'R': return 1
		else: return -1
	raise Exception("Invalid inputs, must be either 'R' 'P' 'S' (case sensitive)")

def part1(inp):
	m2 = {'X': 'R', 'Y': 'P', 'Z': 'S'}
	ts = 0
	for line in inp:
		a, b = m1[line[0]], m2[line[2]]
		# output_score = l:0,d:3,w:6 + score_picked
		os = (win(a, b) + 1) * 3 + s[b]
		ts += os
	return ts

def part2(inp):
	cycle_w = {'R': 'P', 'P': 'S', 'S': 'R'}
	cycle_l = {'R': 'S', 'P': 'R', 'S': 'P'}

	def m2(a, xyz):
		if xyz == 'X':
			return cycle_l[a]
		if xyz == 'Y':
			return a
		if xyz == 'Z':
			return cycle_w[a]

	ts = 0
	for line in inp:
		a = m1[line[0]]
		b = m2(a, line[2])
		# output_score = l:0,d:3,w:6 + score_picked
		os = (win(a, b) + 1) * 3 + s[b]
		ts += os
	return ts

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