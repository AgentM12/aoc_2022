import os

def part1(inp):
	return walksum(inp, 100_000)

def part2(inp):
	total = 70_000_000
	target = 30_000_000
	used = sumup(inp)
	rem = total - used
	req = target - rem
	return walkmin(inp, req, total)

def getat(pth, dic):
	at = dic["/"]
	pth = pth[1:]
	paths = pth.split("\\")
	if (paths == [""]): return at
	
	for x in paths:
		at = at[x]
	return at

def walkmin(dic, req, best):
	for x in dic:
		if (isinstance(dic[x], dict)):
			ts = sumup(dic[x]) # this dir
			if (ts < best and ts >= req):
				best = ts
			
			# only try child dirs if parent is big enough.
			if ts >= req:
				ts = walkmin(dic[x], req, best) # child dir
				if (ts < best and ts >= req):
					best = ts
	return best

def walksum(dic, maximum):
	sm = 0
	for x in dic:
		if (isinstance(dic[x], dict)):
			ts = sumup(dic[x], maximum)
			if (ts <= maximum):
				sm += ts
			sm += walksum(dic[x], maximum)
	return sm

def sumup(dic, maximum=None):
	sm = 0
	for x in dic:
		if (isinstance(dic[x], dict)):
			ts = sumup(dic[x], maximum)
			sm += ts
			if (maximum is not None and sm > maximum): return maximum + 1
		elif (isinstance(dic[x], int)):
			sm += dic[x]
	return sm

def parse_input(inp):
	cwd = None
	filedict = {
		"/": {}
	}

	for line in inp:
		# player input
		if (line.startswith("$")):
			cmdsplits = line.lstrip('$').lstrip().split()
			cmd = cmdsplits[0]

			if (cmd == "cd"):
				loc = cmdsplits[1]
				if (loc == "/"):
					cwd = "/"
				elif loc == "..":
					cwd = os.path.dirname(cwd)
				else:
					cwd = os.path.join(cwd, loc)

			elif (cmd == "ls"):
				pass
		
		# output (always after ls)
		else:
			szdir, name = line.split()
			if (szdir == "dir"):
				getat(cwd, filedict)[name] = {}
			else:
				sz = int(szdir)
				getat(cwd, filedict)[name] = sz
	return filedict

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