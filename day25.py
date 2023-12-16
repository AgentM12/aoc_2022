import os

def part1(inp):
	s = 0
	for line in inp:
		s += snafu_to_dec(line)
	return dec_to_snafu(s)

def snafu_to_dec(sn):
	n = 0
	p = 1
	for c in reversed(sn):
		if c == '=':
			sd = -2
		elif c == '-':
			sd = -1
		else:
			sd = int(c)
		n += sd * p
		p *= 5
	return n

def dec_to_snafu(n):
	sn = ""
	while n > 0:
		d = n % 5
		if d == 3:
			sd = '='
			n += 5
		elif d == 4:
			sd = '-'
			n += 5
		else:
			sd = str(d)
		sn = sd + sn
		n = int(n / 5)
	return sn


def part2(inp):
	sf = """1
2
1=
1-
10
11
12
2=
2-
20
1=0
1-0
1=11-2
1-0---0
1121-1110-1=0""".split('\n')
	for line in sf:
		print(dec_to_snafu(snafu_to_dec(line)))


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
	#print(f" - Part 2: {part2(inp)}") # No part 2 on day 25, it's a freebie.

if __name__ == '__main__':
	main()