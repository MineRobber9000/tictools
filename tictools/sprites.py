import re

class Palette:
	"""A palette."""
	def __init__(self,line):
		line = line[4:]
		parts = re.findall('..?',line)
		self.colors = []
		for i in range(0,len(parts),3):
			self.colors.append([int(x,16) for x in (parts[i],parts[i+1],parts[i+2])])

	def output(self):
		ret = "000:" # not sure why, but all palette lines I've encountered start with "000:" (possibly banks?)
		for p in self.colors:
			for c in p:
				ret += hex(c)[2:].zfill(2)
		return ret

class Sprite:
	"""A TIC-80 Sprite."""
	def __init__(self,line="000:000000000000000000000000000000000000000000000000000000000000000"):
		parts = line.split(":")
		self.id = int(parts[0])
		self.pixels = [int(x,16) for x in parts[1]]

	def output(self):
		return "%s:%s" % (str(self.id).zfill(3),"".join(map(lambda x: hex(x)[2:],self.pixels)))

if __name__=="__main__":
	print "Palette test:"
	p = Palette("000:140c1c44243430346d4e4a4e854c30346524d04648757161597dced27d2c8595a16daa2cd2aa996dc2cadad45edeeed6")
	print len(p.colors)
	print [hex(x)[2:].zfill(2) for x in p.colors[0]]
	p.colors[0]=[156,156,156]
	print p.output()
	print "Sprite test:"
	line = "001:efffffffff222222f8888888f8222222f8fffffff8ff0ffff8ff0ffff8ff0fff"
	s = Sprite("001:efffffffff222222f8888888f8222222f8fffffff8ff0ffff8ff0ffff8ff0fff")
	print s.id
	print s.pixels[0]
	print s.output()==line
	ns = Sprite()
	ns.id=16
	ns.pixels[0:15]=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	print ns.output()
