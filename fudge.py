#!/usr/bin/env python2
#
# by dash@hack4.org in 2008
############################

from lib.FUDGEanalyse import *
from lib.FUDGEheader import *
import getopt,sys,os

#maybe put that later somewhere else
extractit=0
fileReport=0

def fudge_banner():
	inst2=ANALYSE()
	print "[+] FirmareFudger %s by dash@hack4.org" % inst2.version
	print "[+] tool for firmware analyses written in August 2008"
	print "[+] "
	inst2=[]

def fudge_usage():
	inst2=ANALYSE()
	print "[+] FirmareFudger %s by dash@hack4.org" % inst2.version
	print "[+] tool for firmware analyses written in August 2008"
	print "[+] "
	print "[+]\t-f <inputfile>"
	print "[+]\t-o <outdir>"
	print "[+]\t-n <outputfilename>"
	print "[+]\t-x extract found files"
	print "[+]\t-P <FS/EXEC/PACKERS/DOCS/BOOT/ASM/PICTURES/DEVICES/ROUTERS>"
	print "[+]\t-p <name the plugin format, example: CRAMFS>"
	print "[+]\t-r do an investigation on extracted files with file"
	print "[+]\t-l list all available plugins"
	print "[+]\t-v verbose mode on"
	print "[+]\t-V Version"
	print "[+]"
	print "[+] Example:"
	print "[+] python %s -f input.img -o outdir -n outname -x" % sys.argv[0]
	print ""
	inst2=[]

def generateFilereport(instance):
	
	if fileReport==1:
		print "[+] Generating file Report"
		instance.generateReport()
	else:
		print "[-] Don't enabled file Report mode"

def extractdata(instance, extractit):
	instance.extractcount()

	if extractit==1:		
		print "[+] Extracting found files"
		instance.extractfile()		
	else:
		print "[-] Don't enabled extraction mode"

	instance.closefile()

try:
	opts, args = getopt.getopt(sys.argv[1:], "n:o:P:p:lvf:xVr")

#let's check if we got some arguments, dont we?!
	if len(opts)==0:
		fudge_usage()
		sys.exit(1)

except getopt.GetoptError, err:
	fudge_usage()
	print "[!] %s" % str(err)	
	sys.exit(1)

for option, arg in opts:
	if option == "-f":
		file=arg
		inst2=ANALYSE()
		inst2.file=file
	elif option == "-o":
		inst2.dir=arg
		inst2.create_dir()
	elif option == "-n":
		inst2.outname=arg
	elif option == "-r":
		fileReport=1
	elif option == "-p":
		lonelyplugin=arg
		inst2.lonelyplugin=lonelyplugin
	elif option == "-P":
		plugin=arg
		inst2.plugin=plugin
	elif option == "-l":
		fudge_banner()
		inst2=ANALYSE()
		inst2.showplugins()
		inst2=[]
		sys.exit(1)
	elif option == "-v":
		print "verbose"
	elif option == "-V":
		fudge_banner()
		sys.exit(0)
	elif option == "-x":
		extractit=1
	else:
		print "unknown option"
		fudge_usage()
		sys.exit(1)

#print the banner :D
fudge_banner()
inst2.openfile()
inst2.printargs()

#check for named plugin(VAX is currently 2)
true=0
if inst2.lonelyplugin!=None:
	lonely=inst2.lonelyplugin
	for type in range(len(TYPES)):
		for plugin in range(len(TYPES[type])):
			inst2.type=TYPES[type][plugin][3]
			compare=inst2.type.split(" ")
			compare=compare[0]
			compare.strip(" ")
#			print "-%s-" % lonely
#			print "-%s-" % compare
			if lonely==compare:
				true=1
				print "[+] Checking for %s" % inst2.type
				inst2.fd.seek(0,0)
				inst2.search=TYPES[type][plugin][1]
				inst2.checkheader()
	
	extractdata(inst2,extractit)
	generateFilereport(inst2)
	
	if true!=1:
		print "[-] Sorry couldn't find %s " % inst2.lonelyplugin

	sys.exit(0)

if inst2.plugin!=None:
	KIND=inst2.plugin
	if KIND=="FS":
		type=0
	elif KIND=="EXEC":
		type=1
	elif KIND=="PACKERS":
		type=2
	elif KIND=="DOCS":
		type=3
	elif KIND=="BOOT":
		type=4
	elif KIND=="ASM":
		type=5
	elif KIND=="PICTURES":
		type=6
	elif KIND=="DEVICES":
		type=7
	elif KIND=="ROUTERS":
		type=8
	else:
		print "[-] Unkown plugin class %s !" % inst2.plugin
		sys.exit(1)

#only check for the asked TYPE
	print "[+] Testing only for %s plugins" % (KIND)
	for plugin in range(len(TYPES[type])):
		inst2.type=TYPES[type][plugin][3]
		print "[+] Checking for %s" % inst2.type
		inst2.fd.seek(0,0)
		inst2.search=TYPES[type][plugin][1]
		inst2.checkheader()
else:	

#check for all TYPES
	for type in range(len(TYPES)):
		for plugin in range(len(TYPES[type])):
			inst2.type=TYPES[type][plugin][3]
			print "[+] Checking for %s" % inst2.type
			inst2.fd.seek(0,0)
			inst2.search=TYPES[type][plugin][1]
			inst2.checkheader()

	

extractdata(inst2,extractit)
generateFilereport(inst2)
