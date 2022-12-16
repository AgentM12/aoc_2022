import os

sol2 = "ZRARLFZU" # HARDCODED TEXT RESULT EXTRACTED FROM SCREEN GRAPHIC

cmd_registry = {
	"noop": (1, 0),
	"addx": (2, 1)
}

def part1(inp):
	poi = [20, 60, 100, 140, 180, 220]
	res = computer_run(inp, poi)

	s = 0
	for i in range(len(poi)):
		s += poi[i] * res[i]
	return s

def part2(inp):
	screen = computer_draw(inp, 40, 6)
	return f"{sol2}\n" + "\n".join(["".join(line) for line in screen])

def computer_draw(program, w, h):
	cycles = 0
	rx = 1
	screen = []
	for dh in range(h):
		screen.append([])

	for command in program:
		cmdparts = command.split()
		cmdinfo = cmd_registry[cmdparts[0]]

		for c in range(cmdinfo[0]):
			tx = cycles % w
			ty = int(cycles / w)
			if (ty >= h): return screen

			if tx >= rx - 1 and tx <= rx + 1:
				screen[ty].append('#')
			else:
				screen[ty].append('.')
			cycles += 1

		if cmdinfo[1] > 0:
			args = cmdparts[1:]
			if cmdparts[0] == 'addx' and cmdinfo[1] == 1:
				rx += int(args[0])
			else: raise Exception("Currently unsupported")
	return screen

def computer_run(program, probepoi):
	store = []
	nextpoi = 0
	cycles = 0
	rx = 1

	for command in program:
		cmdparts = command.split()
		cmdinfo = cmd_registry[cmdparts[0]]

		cycles += cmdinfo[0]

		if (cycles >= probepoi[nextpoi]):
			store.append(rx)
			nextpoi += 1
			if nextpoi >= len(probepoi): return store

		if cmdinfo[1] > 0:
			args = cmdparts[1:]
			if cmdparts[0] == 'addx' and cmdinfo[1] == 1:
				rx += int(args[0])
			else: raise Exception("Currently unsupported")


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