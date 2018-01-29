import tictools

cart = tictools.Cart("test.lua")

print len(cart.sprites)
print len(cart.code[0])
cart.code[1]="local function poo()\n\tpoo()\nend\n"
print cart.output()
