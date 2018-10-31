
# Funcao principal em Python
def main ():
    with open("pontos.txt") as infile:
        lines = infile.read().splitlines()
        for i in range(len(lines)):
            line = lines[i]
            temp = line.split()
            x,y,z = temp[0], temp[1], temp[2]
            print(x,y,z)

if __name__ == "__main__":
	main()	
