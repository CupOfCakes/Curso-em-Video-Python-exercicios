n = int(input("qual o numero que deseja saber a tabuada? "))

for c in range(1, 11):
    print("{} * {} = {}".format(n, c, n*c))
