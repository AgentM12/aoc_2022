import os
import copy

def part1(inp):
	stacks, moves = inp
	for move in moves:
		amount, src, dest = move
		for _ in range(amount):
			stacks[dest].append(stacks[src].pop())

	return ''.join([s[-1] for s in stacks])

def part2(inp):
	stacks, moves = inp
	for move in moves:
		amount, src, dest = move
		
		stacks[dest].extend(stacks[src][-amount:])
		stacks[src] = stacks[src][:-amount]
			
	return ''.join([s[-1] for s in stacks])

def parse_input(inp):
	stack_img_str = []
	moves = []
	
	state = 0
	for line in inp:
		if line.strip() == '':
			state = 1
		elif state == 0:
			stack_img_str.append(line)
		elif state == 1:
			_, amount, _, src, _, dest = line.split(' ')
			moves.append((int(amount), int(src)-1, int(dest)-1)) # 0 indexing
	# parse stacks
	stacks = []
	stacks_amount = None
	for s in reversed(stack_img_str):
		if state == 2:
			# stack
			for i in range(stacks_amount):
				char = s[4 * i + 1]
				if char != ' ':
					stacks[i].append(char)
		elif state == 1:
			# init stacks
			stacks_amount = int(s.strip()[-1])
			for i in range(stacks_amount): # 0 indexing
				stacks.append([]) # new list
			state = 2
	return (stacks, moves)

def get_input(fname):
	inp_file_name = f"{fname}_input.txt"
	with open(inp_file_name, 'r') as f:
		return [line.strip('\n') for line in f]

def main():
	fname = os.path.splitext(os.path.basename(__file__))[0]
	day = int(fname[3:]) # dayXX
	inp = get_input(fname)
	inp = parse_input(inp)
	print(f"\n === Day {day} ===")
	print(f" - Part 1: {part1(copy.deepcopy(inp))}") # pass a deep copy so the stacks remain pristine for p2
	print(f" - Part 2: {part2(inp)}")

if __name__ == '__main__':
	main()