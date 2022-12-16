import os

def part1(inp):	
	tx, ty = 0, 0
	hx, hy = 0, 0

	vc = set()
	vc.add((0, 0))

	for dirc, dist in inp:
		for i in range(dist):
			
			# update head
			if dirc == 'U':
				hy -= 1
			elif dirc == 'D':
				hy += 1
			elif dirc == 'L':
				hx -= 1
			elif dirc == 'R':
				hx += 1

			# update tail
			tx, ty = retail(hx, hy, tx, ty)

			vc.add((tx, ty))

	return len(vc)

# 4745>SOL>2184
def part2(inp):
	hx, hy = 0, 0
	rope = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
	
	vc = set()
	vc.add((0, 0))

	for dirc, dist in inp:
		#printpos(vc, rope, (hx, hy))
		#print(hx, hy)
		#print(rope)
		#input(vc)
		for i in range(dist):
			# update head
			if dirc == 'U':	  hy -= 1
			elif dirc == 'D': hy += 1
			elif dirc == 'L': hx -= 1
			elif dirc == 'R': hx += 1

			lx, ly = hx, hy # store the head postpos

			for knoti in range(len(rope)):
				rx, ry = rope[knoti] # get the current knot pos

				# update tail
				tx, ty = retail(lx, ly, rx, ry) # update the current knot pos

				# pos did not update
				if rx == tx and ry == ty: 
					break

				rope[knoti] = (tx, ty) # store the knot pos that may be updated.

				lx, ly = tx, ty # store new output pos of current knot

			vc.add(rope[-1])
	#printpos(vc)
	return len(vc)

def printpos(vc, rope=None, hpos=None):
	lx, ly = -50, -10
	hx, hy = 10, 50
	for x, y in vc:
		lx, ly = min(lx, x), min(ly, y)
		hx, hy = max(hx, x), max(hy, y)

	for y in range(ly, hy+1):
		for x in range(lx, hx+1):
			if (hpos is not None and (x, y) == hpos): print('H', end='')
			elif (rope is not None and (x, y) in rope): print('x', end='')
			elif ((x, y) in vc): print('#', end='')
			else: print('.', end='')
		print()

def retail(hx, hy, tx, ty):
	case = 0
	if (tx > hx + 1 or tx < hx - 1):
		case = 1
	if (ty > hy + 1 or ty < hy - 1 ):
		case += 2
	
	if case == 0:
		return tx, ty
	elif case == 1:
		return int((tx + hx) / 2), hy
	elif case == 2:
		return hx, int((ty + hy) / 2)
	elif case == 3:
		return int((tx + hx) / 2), int((ty + hy) / 2)


def parse_input(inp):
	commands = []
	for command in inp:
		dirc, dist = command.split()
		dist = int(dist)
		commands.append((dirc, dist))
	return commands

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