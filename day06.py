import os

def part1(inp):
	start_mk_buff = []
	start_mk_index = -1
	for i in range(len(inp)):
		start_mk_buff.append(inp[i])

		# keep 4 in buff
		if (len(start_mk_buff) >= 4):
			if (len(start_mk_buff) > 4):
				del start_mk_buff[0]

			# Make sure all 4 are distinct from each other
			if (start_mk_buff[0] != start_mk_buff [1]
			and start_mk_buff[0] != start_mk_buff [2]
			and start_mk_buff[0] != start_mk_buff [3]
			and start_mk_buff[1] != start_mk_buff [2]
			and start_mk_buff[1] != start_mk_buff [3]
			and start_mk_buff[2] != start_mk_buff [3]):
				start_mk_index = i + 1 # 1 indexed garbage
				break
	return start_mk_index


def part2(inp):
	start_mk_buff = []
	start_mk_index = -1
	for i in range(len(inp)):
		start_mk_buff.append(inp[i])

		# keep 4 in buff
		if (len(start_mk_buff) >= 14):
			if (len(start_mk_buff) > 14):
				del start_mk_buff[0]

			# Make sure all 14 are distinct from each other
			for j in range(13):
				for k in range(j + 1, 14):
					if (start_mk_buff[j] == start_mk_buff[k]):
						break # Failed, end loop early.
				else: continue
				break # Failed end loop early.
			else:
				start_mk_index = i + 1 # 1 indexed garbage
				break
	return start_mk_index

def get_input(fname):
	inp_file_name = f"{fname}_input.txt"
	with open(inp_file_name, 'r') as f:
		return [line.strip() for line in f]

def main():
	fname = os.path.splitext(os.path.basename(__file__))[0]
	day = int(fname[3:]) # dayXX
	inp = get_input(fname)[0]
	print(f"\n === Day {day} ===")
	print(f" - Part 1: {part1(inp)}")
	print(f" - Part 2: {part2(inp)}")

if __name__ == '__main__':
	main()