target = open("pattern.txt", 'w')
def rows(a):
	for k in a:
		for i in range(1,k):
			for j in range(i):
				target.write("*")
			target.write("\n")



#python -m timeit -s "import pattern; import numpy as np; a = [v for v in range(150)]" "pattern.rows(a)"

