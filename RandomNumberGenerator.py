import random
import string

class RandomNumberGenerator:
	def __init__(self):
		binary = 'bin'
		octal = 'oct'
		decimal = 'dec'
		hexadec = 'hex'
		MIN = 0
		MAX = 15
		
		self.min = MIN
		self.max = MAX
		self.rand_nums = rand_nums = []
		self.bin = binary
		self.oct = octal
		self.dec = decimal
		self.hex = hexadec
	
	
	def generate(self, num_base = 'dec', length = 1, ):
		max_dec = 9
		max_oct = 7
		
		if num_base == self.bin or num_base == self.hex:
			for count in range(self.min, length):
				self.rand_nums.append(str(random.randint(self.min, self.max)))
		
		elif num_base == self.oct:
			for count in range(self.min, length):
				self.rand_nums.append(str(random.randint(self.min, max_oct)))
		
		elif num_base == self.dec:
			for count in range(self.min, length):
				self.rand_nums.append(str(random.randint(self.min, max_dec)))
		
		if num_base == self.hex or num_base == self.bin or num_base == self.oct:
			if num_base == self.bin:
				ret_val = str(bin(int(''.join(self.rand_nums))))
				self.rand_nums.clear()
			
			elif num_base == self.hex:
				ret_val = str(hex(int(''.join(self.rand_nums))))
				self.rand_nums.clear()
			
			elif num_base == self.oct:
				ret_val = str(oct(int(''.join(self.rand_nums))))
				self.rand_nums.clear()
			
			return ret_val[2:]
		
		elif num_base == self.dec:
			ret_val = ''.join(self.rand_nums)
			self.rand_nums.clear()
			
			return ret_val
	


RNG = RandomNumberGenerator()
