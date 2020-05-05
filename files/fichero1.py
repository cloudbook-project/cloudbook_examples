import fichero2
from subdir import fichero3 as file3

def f1():
	print("f1")

#__CLOUDBOOK:MAIN__
def main():
	f1()
	fichero2.f2("pepe")
	file3.f3()

if __name__ == "__main__":
    main()