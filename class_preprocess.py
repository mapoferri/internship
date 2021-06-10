import sys
import os, inspect

#class Foo():
#    def __init__(self):
#        self.path = os.path.relpath(inspect.getfile(self.__class__))


#foo = Foo()
#print(foo.path)

class PreProcessing(object):
	_filename = None

	#defining the constructor
	def __init__(self, path):
		self.path = path
		#self.path = os.path.relpath(inspect.getfile(self.__class__))
		#print (f"{self.path}")
		#would be set once the class is called

#not working unless the file is in the same directory as the Class
#there is another way to do that? don't know.
	@property
	def filename(self):
		if self._filename is None:
			for file in os.listdir(self.path):
				#print (file)
				if file.endswith(".fasta"):
					#print (file)
					self._filename = file
		return self._filename


#Creation of single fasta file from multi-fasta file input	
#Removing also the multi-fasta file
	def separator(self):
		#print (self.filename)	
		#print (self.path)
		infile = open(self.filename)
		outfile = []
		for line in infile:
			if line.startswith(">"):
				if (outfile != []): 
					outfile.close()
				genename = line.strip().split('|')[1].split('.')[0]
				filename = genename+".fasta"
				outfile = open(filename,'w')
				outfile.write(line)
			else:
				outfile.write(line)
		outfile.close()
		#os.remove(self.filename)
	
	def oneliner(self):
		for file in os.listdir(self.path):
			if file.endswith(".fasta"):
				fasta = open(file)
				fasta_one = []
				headers, sequences = [],[]
				for line in fasta:
					if line.startswith('>'):
						genename = line.strip().split('|')[1].split('.')[0]
						output = genename+"_one.fasta"
						fasta_one = open(output, 'w')
						#print (line.strip())
						fasta_one.write(line)
					else :
						seq = line.strip()
						#print (seq)
						if len(seq) > 0: 
							fasta_one.write(seq)
				fasta_one.close()
				#os.remove(file)

	def checklenght(self):
		for file in os.listdir(self.path):
			if file.endswith("_one.fasta"):
				with open(file) as oneliner:
					for line in oneliner:
						seq = oneliner.readline()
						print (seq)
						#seq = oneliner.readline()
						#print (seq)
						if len(seq) <= 40:
							print ('Error')
						else :
							print (file)



prova = PreProcessing("/home/mariapaola/Desktop/Pymol/class")
prova.separator()
prova.oneliner()
prova.checklenght()