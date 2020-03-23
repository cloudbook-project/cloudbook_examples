class NumComplejo:
	def __init__(self,r = 0,i = 0):
		self.real = r
		self.imag = i

	def create(self,r,i):
		self.real = r
		self.imag = i

	def getOperators():
		op_a = NumComplejo()
		op_b = NumComplejo()
		op_a.real,op_a.imag = input("Operador a (separado por comas):").split(",")
		op_b.real,op_b.imag = input("Operador b (separado por comas):").split(",")
		op_a.real,op_a.imag = int(op_a.real),int(op_a.imag)
		op_b.real,op_b.imag = int(op_b.real),int(op_b.imag)
		return op_a,op_b
 
	def suma():
		numa,numb = NumComplejo.getOperators()
		result = NumComplejo()
		result.real = numa.real + numb.real
		result.imag = numa.imag + numb.imag
		NumComplejo.printResult("+",numa,numb,result)

	def resta():
		numa,numb = NumComplejo.getOperators()
		result = NumComplejo()
		result.real = numa.real - numb.real
		result.imag = numa.imag - numb.imag
		NumComplejo.printResult("-",numa,numb,result)

	def mult():
		numa,numb = NumComplejo.getOperators()
		result = NumComplejo()
		result.real = (numa.real*numb.real) - (numa.imag*numb.imag)
		result.imag = (numa.real*numb.imag) + (numa.imag*numb.real)
		NumComplejo.printResult("*",numa,numb,result)

	def div():
		numa,numb = NumComplejo.getOperators()
		result = NumComplejo()
		#(ac+bd)/(c^2+d^2) 
		result.real = ((numa.real*numb.real)+(numa.imag*numb.imag))/((numb.real*numb.real) + (numb.imag*numb.imag))
		#(bc-ad)/(c^2+d^2)
		result.imag = ((numa.imag*numb.real)-(numa.real*numb.imag))/((numb.real*numb.real) + (numb.imag*numb.imag))
		NumComplejo.printResult("/",numa,numb,result)

	def printResult(op,opa,opb,res):
		print(" "*4,end="")
		opa.getData()
		print("  ",op)
		print(" "*4,end="")
		opb.getData()
		print(" "*4,end="")
		print("======")
		print(" "*4,end="")
		res.getData()
		input("press enter to continue")

	def getData(self):
		print("{0}+{1}i".format(self.real,self.imag))

def creayprinta():
	print("Soy la invocación local")
	c1 = NumComplejo(2,3)
	c2 = NumComplejo(1,2)
	c1.getData()
	c2.getData()
	creayprinta2()
	input("press enter to continue")

#__CLOUDBOOK:PARALLEL__
def creayprinta2():
	print("Soy la parallel")
	c1 = NumComplejo(20,30)
	c2 = NumComplejo(10,20)
	c1.getData()
	c2.getData()

#__CLOUDBOOK:MAIN__
def main():
	while (True):		
		#os.system('cls')  # on windows
		print("")
		print("Int complex calculator")
		print("======================")
		print(" t: test")
		print(" s: suma")
		print(" r: resta")
		print(" m: mult")
		print(" d: div")
		print(" q: quit")
		
		command=input ("command?:")
		if (command=="t"):
			creayprinta()
		elif (command=="s"):
			NumComplejo.suma()
		elif (command=="r"):
			pass
			NumComplejo.resta()
		elif (command=="m"):
			pass
			NumComplejo.mult()
		elif (command=="d"):
			pass
			NumComplejo.div()
		elif (command=="q"):
			return("done")

main()
