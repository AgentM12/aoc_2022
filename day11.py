import os
import math

class Monkey:

	def __init__(self, items, op, cond, ta, fa):
		self.items = items # items starting with
		self.op = op # operation to perform
		self.cond = cond # condition to test item divisible by 'cond'
		self.ta = ta # reference monkey if True
		self.fa = fa # reference monkey if False
		self.inspections = 0
		self.lcm = None

	def inspect_all(self):
		while (len(self.items) > 0):
			self.inspect()

	def inspect(self):
		self.inspections += 1
		# next item
		item = self.items[0]
		del self.items[0]

		# inspect item
		item = self.op(item)

		# bored
		if self.lcm is None:
			item = int(item / 3)
		else:
			item %= self.lcm

		# test
		if (item % self.cond == 0):
			throw(item, self.ta)
		else:
			throw(item, self.fa)

	def give(self, item):
		self.items.append(item)

	def __repr__(self):
		return str(self)

	def __str__(self):
		return f"\n - Items: {self.items}.\n - Result of op(x) for 1 to 3: {self.op(1)}, {self.op(2)}, {self.op(3)}\n - if (i % {self.cond})\n   - then {self.ta}\n   - else {self.fa}\n"

monkeys = None

def throw(item, monkey_id):
	global monkeys
	monkeys[monkey_id].give(item)

def part1(inp):
	global monkeys
	init_monkeys(inp)
	
	return play(20)

def part2(inp):
	global monkeys
	init_monkeys(inp, True)
	
	return play(10000)

def play(rounds):
	for r in range(rounds):
		for m in monkeys:
			m.inspect_all()

	best2 = [0, 0]
	for m in monkeys:
		it = m.inspections
		for bi in range(len(best2)):
			if it > best2[bi]:
				it, best2[bi] = best2[bi], it
	return best2[0] * best2[1]

def init_monkeys(inp, disable_div=False):
	global monkeys
	monkeys = []
	
	items, op, cond, ta, fa = None, None, None, None, None

	i = 0
	for line in inp:
		i += 1
		if i % 7 == 1:
			pass
		elif i % 7 == 2:
			its = line.strip().split(":")[1].split(',')
			items = [int(it.strip()) for it in its]
		elif i % 7 == 3:
			sop = line.strip().split(":")[1].strip()
			_, _, _, o, b = sop.split()

			if b == "old" and o == '*':
				op = lambda x: x * x
			elif o == '+':
				op = lambda x, b=b: x + int(b)
			elif o == '*':
				op = lambda x, b=b: x * int(b)
			else:
				raise Exception(f"Unrecognized operation: {line}")
		elif i % 7 == 4:
			cond = int(line.strip().split()[3])
		elif i % 7 == 5:
			ta = int(line.strip().split()[5])
		elif i % 7 == 6:
			fa = int(line.strip().split()[5])
		elif i % 7 == 0:
			monkeys.append(Monkey(items, op, cond, ta, fa))
	monkeys.append(Monkey(items, op, cond, ta, fa))

	if disable_div:
		f = 1
		for m in monkeys:
			f *= m.cond
		lcm = f // math.gcd(*[m.cond for m in monkeys])
		for m in monkeys:
			m.lcm = lcm

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