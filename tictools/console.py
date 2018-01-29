import cart,argparse

def codesize():
	parser = argparse.ArgumentParser(prog="codesize",description="Determines the size of your code.")
	parser.add_argument("cart",help="The filename of the cart.")
	args = parser.parse_args()
	ncart = cart.Cart(args.cart)
	for i in range(8):
		if ncart.code.get(i,None):
			if i==0:
				print("Bank %d: %d/65536" % (i,len(ncart.code[i])+len(ncart.format_metadata())))
			else:
				print("Bank %d: %d/65536" % (i,len(ncart.code[i])))
