import tictools,tictools.sprites
import os.path as fs

cart = tictools.Cart()
cart.initialize_metadata()

with open("testcode.lua") as f:
	cart.code[0]=f.read()

with open("sprites/order") as f:
	for l in f:
		with open(fs.join("sprites",l.rstrip())) as f2:
			spr = tictools.sprites.Sprite()
			spr.id = int(l.split(".")[0])
			spr.pixels = [int(x,16) for x in f2.read().replace("\n","")]
			cart.sprites.append(spr)

print cart.output()
