import sprites,re
from collections import OrderedDict
class Cart:
	"""A TIC-80 cartridge. Has metadata, code, tiles, waveforms, SFX and a palette."""
	def __init__(self,filename=None):
		self.initialize_metadata()
		self.initialize_waves()
		self.initialize_sfx()
		self.initialize_code()
		self.initialize_gfx()
		if filename:
			self.initialize_waves(True)
			self.initialize_sfx(True)
			with open(filename,"r") as f:
				lines = [l.rstrip() for l in f]
				stage=0
				tag = ""
				for line in lines:
					if not line:
						continue # skip empty lines
					if stage==0:
						if line.startswith("-- "):
							parts=line[3:].split(": ",2)
							self.metadata[parts[0]]=parts[1]
						else:
							stage=1
					if stage==1:
						if not line.startswith("-- <"):
							self.code[0]+="{}\n".format(line)
						else:
							stage=2
					if stage==2:
						match = re.search(r"-- <(.+)>",line)
						if not match:
							raise Exception("Invalid line for stage 2")
						if match.group(1) not in ["TILES","WAVES","SFX","PALETTE"]+["CODE"+str(i) for i in range(8)]:
							raise Exception("Invalid tag!")
						tag = match.group(1)
						if tag.startswith("CODE"):
							self.code[int(tag[-1])]=""
						stage = 3
					elif stage==3:
						if line=="-- </{}>".format(tag):
							stage = 2
						else:
							if tag.startswith("CODE"):
								self.code[int(tag[-1])]+="{}\n".format(line)
								continue
							if tag=="TILES":
								# Sprite class is implemented!
								self.sprites.append(sprites.Sprite(line[3:]))
							elif tag=="PALETTE":
								self.palette = sprites.Palette(line[3:])
							elif tag=="WAVES":
								self.waves.append(line[3:])
							elif tag=="SFX":
								self.sfx.append(line[3:])

	def export_tagged_group(self,name,a=" ",ls=[],prefix="-- "):
		if not ls:
			if not hasattr(self,a):
				if not hasattr(self,name):
					return False
				a = name
			ls = getattr(self,a)
		if type(ls)!=list:
			ls = [ls]
		ret = ["-- <{}>".format(name)]
		for i in ls:
			if hasattr(i,"output"):
				ret.append(prefix+i.output())
			else:
				ret.append(prefix+i)
		ret.append("-- </{}>".format(name))
		return "\n".join(ret)

	def format_metadata(self):
		ret = []
		for k in self.metadata.keys():
			ret.append("-- {}: {}".format(k,self.metadata[k]))
		return "\n".join(ret)

	def initialize_metadata(self):
		self.metadata = OrderedDict()
		self.metadata["title"]="game title"
		self.metadata["author"]="game developer"
		self.metadata["desc"]="short description"
		self.metadata["script"]="lua"

	def initialize_code(self):
		self.code = {0:""}

	def initialize_waves(self,empty=False):
		if empty:
			self.waves = []
		else:
			self.waves = ["000:00000000ffffffff00000000ffffffff","001:0123456789abcdeffedcba9876543210","002:0123456789abcdef0123456789abcdef"]

	def initialize_sfx(self,empty=False):
		if empty:
			self.sfx = []
		else:
			self.sfx = ["000:000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000304000000000"]

	def initialize_gfx(self):
		self.sprites=[]
		self.palette=sprites.Palette("000:140c1c44243430346d4e4a4e854c30346524d04648757161597dced27d2c8595a16daa2cd2aa996dc2cadad45edeeed6")

	def output(self):
		ret = []
		ret.append(self.format_metadata())
		ret.append(self.code[0].rstrip())
		for i in range(1,8):
			if self.code.get(i,None):
				ret.append(self.export_tagged_group("CODE"+str(i),ls=self.code[i].rstrip().split("\n"),prefix="")) # code banks don't do comments
		for i in "TILES WAVES SFX PALETTE".split():
			if i=="TILES":
				ret.append(self.export_tagged_group("TILES","sprites"))
			else:
				ret.append(self.export_tagged_group(i,i.lower()))
		return "\n".join(ret)
