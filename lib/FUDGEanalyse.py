import FUDGEheader
import os,sys,time,struct,binascii

def dbgprint():
    print "nothing"

class ANALYSE(object):
	
	def __init__(self):
		
		""" 	file	- the file to analyse	
			stat 	- os.stat results of self.file 
			type 	- the current type of pattern test
			plugin	- choosen pluginclass to test for
			lonelyplugin - choosen lonely plugin for test
			fd 	- the filedescriptor of open and close
			search 	- the search string/bytes
			string 	- for convert2hex
			data	- the binary data field, where the bytes are filled in
			offset	- the offset delivered back for writing to self.cut
			extract	- number of the found files in file
			cut	- dict for offsets for the extractfile method
			dir	- output directory for putting files
			outname	- name of the output files part
			reportfile - name of the status report
			files - list with paths of extracte files
			"""
	
 
		self.file=None
		self.stat=None
		self.type=None
		self.plugin=None
		self.lonelyplugin=None
		self.reportfile=None
		self.files=[]
		self.fd=None
		self.search=None
		self.string=""
		self.data=[]
		self.offset=0
		self.extract=0
		self.cut={}
		self.set_offset=0
		self.set_string=0
		self.debug=0
		self.dir=""
		self.outname="Extract"
		self.length=0
		self.version="0.3"

	def privileges(self):
		if self.stat.st_uid != os.getuid():
			print "[!] Attention file owner is %d" % self.stat.st_uid

	def printargs(self):

		size=self.stat.st_size
		Kilo=1024.0
		Mega=1048576.0

		print "[+] Fudger Version %s - Fileinformation" % self.version
		print "[+] Filename %s" % self.file

		if size<=Mega:
			sizeK=size/Kilo
			print "[+] Size %.2fK - %dB" % (sizeK,size)

		elif size>=Mega:
			sizeM=size/Mega
			sizeK=size/Kilo
			print "[+] Size %.2fM - %.2fK - %dB" % (sizeM,sizeK,size)
		else:
			print "[+] Size %d" % size

		print "[+] User %d" % self.stat.st_uid
		print "[+] Group %d" % self.stat.st_gid
		#print "[+] Search for %s" % self.search

	
	def openfile(self):
		
		self.stat=os.stat(self.file)
		print "[+] Open %s" % (self.file)
		self.fd=open(self.file,"r")

	def closefile(self):

		print "[+] Close %s" % self.file
		self.fd.close()

	def create_dir(self):

	        try:
			print "[+] Creating directory %s" % (self.dir)
			os.mkdir(self.dir)
			return(0)
		except OSError, e:
			print "[-] Error %d %s" % (e.args[0], e.args[1])
			return(1)
	
	def convert2array(self):
		
		for byte in range(len(self.string)):
			print "\'%c\'," % self.string[byte],

	def checkheader(self):
		self.data=[]	
		offset=0
#		print "[+] Checking for FS Type Headers"
		try:
			for byte in self.fd.read(self.stat.st_size):
#			print "[+] Bytes in %s" % self.stat.st_size
				self.data.append(byte)
				#print "[+] data %s" % self.data
				#print "in for loop"
				if len(self.data) == len(self.search):
					#print "set o =0"
					o=0
					#print "[+] Datalen is %d" % len(self.data)
					for i in range(len(self.data)):	
						if self.data[i]==self.search[i]:
#						print self.data[i]
#						print self.search[i]
							o+=1
					#	i+=1
					if o==len(self.search):
						offlen=offset-len(self.data)+1
						print "[+] FOUND at Offset %d to %d" % (offlen,offset)
				#		print "FIELD " + str(self.data)
						self.cut[self.extract]=offlen
#					print "%s" % str(self.cut)
#					print "%d" % self.cut[self.extract]
						o=0
						self.data.pop(0)
						self.extract+=1
					else:
					#	print "Nope"
#					print self.data
						self.data.pop(0)
						o=0
					#print "set i=0"	
					i=0	
					
				offset+=1	

		except KeyboardInterrupt:
		    print "\n[!] KeyboardInterrupt at check %s" % self.type
		    sys.exit(1)

	def extractcount(self):
	
		print "[+] Found %d possible types" % (self.extract)


	def seekinto(self):
		allbytes=""
		self.fd=open(self.file,"r")
		self.fd.seek(0,0)
		self.fd.seek(self.set_offset,0)
		for byte in self.fd.read(self.length):
			byte=binascii.hexlify(byte)
			allbytes=allbytes + "\\x"+byte
		print "%s" % allbytes,


	def manglefile(self):
		mangle_file=open(self.file,"r")
		for part in range(self.extract):
			mangle_file.seek(0,0)
			mangle_file.seek(self.cut[part],0)
			readbytes=mangle_file.read(8)
			print "readed %s " % readbytes
			mangle_file.close()	
			mangle_file=open(self.file,"r+")
			mangle_file.seek(0,0)
			mangle_file.seek(self.cut[part],0)
			mangle_file.write(self.set_string)
		mangle_file.close()	


	def extractfile(self):
		""" its working just need some cleanups, and small fixes """	

		exo_file=open(self.file,"r")

		for part in range(self.extract):
		#	dbgprint "part %d" % part
			exo_file.seek(0,0)
			exo_file.seek(self.cut[part],0)

			suffix=self.type
			suffix=suffix.split(" ")
			suffix=suffix[0]
			FILENAME=self.dir+"/"+self.outname+"-"+str(self.extract)+"-"+str(self.cut[part])+"." + suffix
			print "[+] FILENAME: %s" % FILENAME
			exw_file=open(FILENAME,"w")
		
			TOWRITE=(self.stat.st_size)-self.cut[part]
			for byte in exo_file.read(TOWRITE):
			#for byte in exo_file.read(self.stat.st_size):
				exw_file.write(byte)
			
			exw_file.close()
#complicated
	#		print "written %d" % self.cut[self.extract]
		exo_file.close()

#lets add it to files if reportfile shall be written
	#	if self.reportfile!=None:
		self.files.append(FILENAME)

	def generateReport(self):
	    print "[+] Found %d extracted files" % len(self.files)
	    print 
	    print "file Report"
	    print "="*11
	    for extracted in self.files:
		    #print "[+] %s " % extracted
		    os.spawnl(os.P_WAIT,"/usr/bin/file","file",extracted)

	def showplugins(self):
		""" 	ok this method is not part of the CLASS ANALYSE 
			maybe i change this later"""
		i=0
		print "[+] Plugins:"
		for type in range(len(FUDGEheader.TYPES)):
			if type==0:
				stringtype="FS"
			elif type==1:
				stringtype="EXEC"
			elif type==2:
				stringtype="PACKERS"
			elif type==3:
				stringtype="DOCS"
			elif type==4:
				stringtype="BOOT"
			elif type==5:
				stringtype="ASM"
			elif type==6:
				stringtype="PICTURES"
			elif type==7:
				stringtype="DEVICES"
			elif type==8:
				stringtype="ROUTER"
			print "%s:" % stringtype
			for plugin in range(len(FUDGEheader.TYPES[type])):
				print "\t\t- %s" % FUDGEheader.TYPES[type][plugin][3]
				i+=1

		print "\n[+] Found %d plugins." % i
		print "[+] Done"

