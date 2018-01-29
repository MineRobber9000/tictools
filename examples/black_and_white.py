import tictools
c = tictools.Cart("test.lua")
def blank(n):
	return 0 if n >= 8 else 15

for i in range(9):
	if i==4:
		continue
	c.sprites[i].pixels = [blank(x) for x in c.sprites[i].pixels]

with open("umm.lua","w") as f:
	f.write(c.output())
