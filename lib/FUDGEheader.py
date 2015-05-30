#complete list
TYPES		= 0x00

#categories
FS		= 0x00
EXEC		= 0x01
PACKERS		= 0x02
DOCS		= 0x03
BOOT		= 0x04
ASM		= 0x05
PICTURES	= 0x06
DEVICES		= 0x07
ROUTERS		= 0x08
CRYPTO		= 0x09

#Filesystem Type Definitions
MSDOS		= 0x00
CRAMFS1		= 0x01
CRAMFS2		= 0x02		#difference is another searchstring
ROM1FS		= 0x03
SQUASHFS1	= 0x04		#difference is another searchstring
SQUASHFS2	= 0x05
FAT32		= 0x06
CDUNIX		= 0x07
ADF		= 0x08
SGI		= 0x09
SGIXFS		= 0x0a
ST40		= 0x0b
CBM		= 0x0c
WINIMAGE	= 0x0d
COB		= 0x0e
UFS1		= 0x0f
QEMU1		= 0x10
JFFSL		= 0x11
JFFSB		= 0x12
JFFS2L		= 0x13
JFFS2B		= 0x14

#Executeable File Definitions
ELF		= 0x00
BFLT		= 0x01
PE		= 0x02
MSDOSCOM	= 0x03
DOSCOM		= 0x04
SPSSPORTABLE	= 0x05
SPSSSYSTEM	= 0x06
PPCPEF		= 0x07

#Packing Specific definitions
ZIP1		= 0x00
ZIP2		= 0x01
BZIP		= 0x02
GZIP		= 0x03
ACE		= 0x04
TAR		= 0x05
TRX1		= 0x06
TRX2		= 0x07
LZMA		= 0x08
UPX		= 0x09
GNUTAR		= 0x0A
CRUSH		= 0x0B
HLSQZ		= 0x0B
SQWEZ		= 0x0C
HPAK		= 0x0D
LZOP		= 0x0E
MDCD		= 0x0F
MSCOMPRESS	= 0x10
INSTALLSHIELD	= 0x11
PAQ		= 0x12
JARARJ		= 0x13
STUFFIT		= 0x14
VAX3		= 0x15
VAX5		= 0x16
ARCHIVE		= 0x17
ARCHIVEFILE	= 0x18
HRB		= 0x19
RISCOS		= 0x1a
HAP		= 0x1b
LIM		= 0x1c
FREEZE		= 0x1d
ZOO		= 0x1e
RAR		= 0x1f
EET		= 0x20
RZIP		= 0x21
SQSH		= 0x22
ISC		= 0x23
NWFILE		= 0x24
DSIGDCC		= 0x25
ARJ		= 0x26

#Document Fileformats
PDF		= 0x00
DOC		= 0x01
RTF		= 0x02

#Bootloader Definitions
UBOOT		= 0x00

#Assembler object codes
AVR		= 0x00

#Image Files(pictures etc.)
GIMPXCF		= 0x00

#Devices Specific Firmware characteristics
LTRX1		= 0x00
LTRX2		= 0x01
WGR614BOOT	= 0x02
WGR614		= 0x03

#Router Specific Firmware characteristics specifications

#Crypto stuff, certificates, keys, typical indications of crypto
SSHDSA		= 0x00 #-----BEGIN DSA PRIVATE KEY-----	    -----END DSA PRIVATE KEY-----
SSHRSA		= 0x02 #-----BEGIN RSA PRIVATE KEY-----	    -----END RSA PRIVATE KEY-----
SSHPUB		= 0x03 # ssh-dss
CACERT		= 0x04 #-----BEGIN CERTIFICATE-----	    -----END CERTIFICATE-----
CERTREQ		= 0x05 #-----BEGIN CERTIFICATE REQUEST----- -----END CERTIFICATE REQUEST-----
PGPMSG		= 0x10 #-----BEGIN PGP MESSAGE-----	    -----END PGP MESSAGE-----

#Header definitions
HEADER1		= 0x01		#start header
HEADER2		= 0x02		#stop trailer/header
DESC		= 0x03		#teh description
TOOLS		= 0x04		#tools of trade to work with that kind of files
SUFFIX		= 0x05		#the ending of the file, some tools want to have a proper ending, gzip for instance
CHANCE		= 0x06		#chance calculator, if at least "chance" bytes are correct print out possibility...


#Filesystem Specifications
#
#still much too add
###########################################
TYPES = { FS: { \
		MSDOS:{ \
			HEADER1: ('M','Z','H','H'),\
			HEADER2: None,\
			DESC: "MSDOS - Filesystem",\
			CHANCE: 2},
		CRAMFS1:{ \
			HEADER1: ('\x45','\x3d','\xcd','\x28'),\
			HEADER2: None,\
			DESC: "CRAMFS - Compressed ROMFS",\
			CHANCE: 2},

		CRAMFS2:{ \
			HEADER1: ('C','o','m','p','r','e','s','s','e','d','\x20','R','O','M','F','S'),\
			HEADER2: None,\
			DESC: "CRAMFS2 - Compressed ROMFS",\
			CHANCE: 8},

		ROM1FS:{ \
			HEADER1: ('-','r','o','m','1','f','s'),\
			HEADER2: None,\
			DESC: "ROM1FS - ROM FILE SYSTEM",\
			CHANCE: 3},

		SQUASHFS1:{ \
			HEADER1: ('h','s','q','s'),\
			HEADER2: None,\
			DESC: "SQUASHFS - Big Endian",\
			CHANCE: 2},

		SQUASHFS2:{ \
			HEADER1: ('s','q','s','h'),\
			HEADER2: None,\
			DESC: "SQUASHFS - Little Endian",\
			CHANCE: 2},

		FAT32:{ \
			HEADER1: ('\x46','\x41','\x54','\x33','\x32'),\
			HEADER2: None,\
			DESC: "FAT32 - Filessystem",\
			CHANCE: 2},

		CDUNIX:{ \
			HEADER1: ('\x01','\x43','\x44','\x30','\x30','\x31','\x01'),\
			HEADER2: None,\
			DESC: "CDUNIX - Filessystem",\
			CHANCE: 2},

		ADF:{ \
			HEADER1: ('D','O','S','\x00'),\
			HEADER2: None,\
			DESC: "ADF - Amiga Filessystem",\
			CHANCE: 2},

		SGI:{ \
			HEADER1: ('\x0B','\xE5','\xA9','\x41'),\
			HEADER2: None,\
			DESC: "SGI - SGI disk label (volume header)",\
			CHANCE: 2},

		SGIXFS:{ \
			HEADER1: ('\x58','\x46','\x53','\x42'),\
			HEADER2: None,\
			DESC: "SGI XFS - filesystem data",\
			CHANCE: 2},

		ST40:{ \
			HEADER1: ('\x13','\xa9','\xf1','\x7e'),\
			HEADER2: None,\
			DESC: "ST40 - component image format",\
			CHANCE: 2},
		CBM:{ \
			HEADER1: ('C','B','M'),\
			HEADER2: None,\
			DESC: "Power 64 - C64 Emulator Snapshot",\
			CHANCE: 2},

		WINIMAGE:{ \
			HEADER1: ('W','I','N','I','M','A','G','E'),\
			HEADER2: None,\
			DESC: "WinImage - WinImage Archive data",\
			CHANCE: 2},
		COB:{ \
			HEADER1: ('C','o','B','1'),\
			HEADER2: None,\
			DESC: "CoB1 - lantronix html/webserver filesystem",\
			CHANCE: 2},
		UFS1:{ \
			HEADER1: ('\x00','\x01','\x19','\x54'),\
			HEADER2: None,\
			DESC: "UFS1 - Unix Fast File system [v1] (little-endian)",\
			CHANCE: 2},
		QEMU1:{ \
			HEADER1: ('\x51','\x46','\x49','\xfb'),\
			HEADER2: None,\
			DESC: "QEMU1 - Qemu Image, Format: Qcow",\
			CHANCE: 2},
		JFFSL:{ \
			HEADER1: ('\x31','\x39','\x38','\x34'),\
			HEADER2: None,\
			DESC: "JFFS - version 1, little endian",\
			TOOLS: "mtd-tools, mkfs.jffs etc.",\
			CHANCE: 2},

		JFFSB:{ \
			HEADER1: ('\x34','\x38','\x39','\x31'),\
			HEADER2: None,\
			DESC: "JFFS - version 1, big endian",\
			TOOLS: "mtd-tools, mkfs.jffs etc.",\
			CHANCE: 2},

		JFFS2L:{ \
			HEADER1: ('\x85','\x19','\x03','\x20'),\
			HEADER2: None,\
			DESC: "JFFS - version 2, little endian",\
			TOOLS: "mtd-tools, mkfs.jffs etc.",\
			CHANCE: 2},

		JFFS2B:{ \
			HEADER1: ('\x19','\x85','\x20','\x03'),\
			HEADER2: None,\
			DESC: "JFFS - version 2, big endian",\
			TOOLS: "mtd-tools, mkfs.jffs etc.",\
			CHANCE: 2}
		},

	EXEC: {
		ELF:{ \
			HEADER1: ('\x7f','E','L','F'),\
			HEADER2: None,\
			DESC: "ELF - File Format",\
			CHANCE: 2},
		BFLT:{ \
			HEADER1: ('b','F','L','T'),\
			HEADER2: None,\
			DESC: "bFLT - File Format",\
			CHANCE: 2},
		PE:{ \
			HEADER1: ('P','E','\x00','\x00'),\
			HEADER2: None,\
			DESC: "PE - File Format",\
			CHANCE: 2},
		MSDOSCOM:{ \
			HEADER1: ('\xfc','\x57','\xf3','\xa5','\xc3'),\
			HEADER2: None,\
			DESC: "COM executable for MS-DOS",\
			CHANCE: 2},
		DOSCOM:{ \
			HEADER1: ('\xfc','\x57','\xf3','\xa4','\xc3'),\
			HEADER2: None,\
			DESC: "COM executable for DOS",\
			CHANCE: 2},
		SPSSPORTABLE:{ \
			HEADER1: ('\xc1','\xe2','\xc3','\xc9'),\
			HEADER2: None,\
			DESC: "SPSS Portable File",\
			CHANCE: 2},
		SPSSSYSTEM:{ \
			HEADER1: ('$','F','L','2'),\
			HEADER2: None,\
			DESC: "SPSS System File",\
			CHANCE: 2},
		PPCPEF:{ \
			HEADER1: ('J','o','y','!','p','e','f','f','p','w','p','c'),\
			HEADER2: None,\
			DESC: "header for PowerPC PEF executable",\
			CHANCE: 2}
	},

	PACKERS:  {
		ZIP1:{ \
			HEADER1: ('\x50','\x4b','\x03','\x04'),\
			HEADER2: None,\
			DESC: "ZIP1 - Phil Katz ",\
			CHANCE: 2},
		ZIP2:{ \
			HEADER1: ('\x50','\x4b','\x01','\x02'),\
			HEADER2: None,\
			DESC: "ZIP2 - Phil Katz ",\
			CHANCE: 2},
		BZIP:{ \
			HEADER1: ('\x42','\x5a','\x68'),\
			HEADER2: None,\
			DESC: "BZIP - a block-sorting file compressor",\
			CHANCE: 2},
		GZIP:{ \
			HEADER1: ('\x1f','\x8b'),\
			HEADER2: None,\
			DESC: "GZIP - Lempel-Ziv coding (LZ77)",\
			CHANCE: 2},
		ACE:{ \
			HEADER1: ('*','*','A','C','E','*','*'),\
			HEADER2: None,\
			DESC: "ACE - e-merge GmbH - winace.com",\
			CHANCE: 2},
		TAR:{ \
			HEADER1: ('\x00','u','s','t','a','r','\x00'),\
			HEADER2: None,\
			DESC: "TAR - tape archiver",\
			CHANCE: 2},
		TRX1:{ \
			HEADER1: ('\x30','\x52','\x44','\x48'),\
			HEADER2: None,\
			DESC: "TRX1 - ",\
			CHANCE: 2},
		TRX2:{ \
			HEADER1: ('H','D','R','0'),\
			HEADER2: ('0','R','D','H'),\
			DESC: "TRX2 - ",\
			CHANCE: 2},
		LZMA:{ \
			HEADER1: ('\x5d','\x00','\x00','\x80'),\
			HEADER2: None,\
			DESC: "LZMA - Lempel-Ziv-Markov chain-Algorithm",\
			CHANCE: 2},
		UPX:{ \
			HEADER1: ('U','P','X','!'),\
			HEADER2: None,\
			DESC: "UPX - Ultimate Packer for eXecuteables",\
			CHANCE: 2},
		GNUTAR:{ \
			HEADER1: ('u','s','t','a','r','\x20','\x20','\x00'),\
			HEADER2: None,\
			DESC: "GNUTAR - tar == teer + tape archiver",\
			CHANCE: 2},
		CRUSH:{ \
			HEADER1: ('C', 'R', 'U', 'S', 'H'),\
			HEADER2: None,\
			DESC: "CRUSH - Crush archive data",\
			CHANCE: 2},

		HLSQZ:{ \
			HEADER1: ('H', 'L', 'S', 'Q', 'Z'),\
			HEADER2: None,\
			DESC: "HLSQZ - Squeeze It archive data",\
			CHANCE: 2},

		SQWEZ:{ \
			HEADER1: ('S', 'Q', 'W', 'E', 'Z'),\
			HEADER2: None,\
			DESC: "SQWEZ - archive data",\
			CHANCE: 2},
		HPAK:{ \
			HEADER1: ('H', 'P', 'A', 'K'),\
			HEADER2: None,\
			DESC: "HPAK - archive data",\
			CHANCE: 2},
		LZOP:{ \
			HEADER1: ('\x89','\x4c','\x5a','\x4f','\x00','\x0d','\x0a','\x1a','\x0a'),\
			HEADER2: None,\
			DESC: "LZOP - lzop comrpressed data",\
			CHANCE: 2},
		MDCD:{ \
			HEADER1: ('M', 'D', 'm', 'd'),\
			HEADER2: None,\
			DESC: "MDCD - archive data",\
			CHANCE: 2},
		MSCOMPRESS:{ \
			HEADER1: ('\x88','\xf0','\x27'),\
			HEADER2: None,\
			DESC: "MS Compress archive data",\
			CHANCE: 2},
		INSTALLSHIELD:{ \
			HEADER1: ('\x13','\x5d','\x65','\x8c'),\
			HEADER2: None,\
			DESC: "InstallShield - Z archive Data",\
			CHANCE: 2},
		PAQ:{ \
			HEADER1: ('\xaa','\x40','\x5f','\x77','\x1f','\xe5','\x82','\x0d'),\
			HEADER2: None,\
			DESC: "PAQ - archive data",\
			CHANCE: 2},
		JARARJ:{ \
			HEADER1: ('\x1a','J','a','r','\x1b'),\
			HEADER2: None,\
			DESC: "JAR (ARJ Software, Inc.) archive data",\
			CHANCE: 2},
		STUFFIT:{ \
			HEADER1: ('S','t','u','f','f','I','t'),\
			HEADER2: None,\
			DESC: "StuffIt Archive",\
			CHANCE: 2},
		VAX3:{ \
			HEADER1: ('\x65','\xff','\x00','\x00'),\
			HEADER2: None,\
			DESC: "VAX 3.0 archive",\
			CHANCE: 2},
		VAX5:{ \
			HEADER1: ('\x3c','\x61','\x72','\x3e'),\
			HEADER2: None,\
			DESC: "VAX 5.0 archive",\
			CHANCE: 2},
		ARCHIVE:{ \
			HEADER1: ('=','<','a','r','>'),\
			HEADER2: None,\
			DESC: "archive",\
			CHANCE: 2},
		ARCHIVEFILE:{ \
			HEADER1: ('21','3c','61','72'),\
			HEADER2: None,\
			DESC: "archive file",\
			CHANCE: 2},
		HRB:{ \
			HEADER1: ('\xc0','H','R','B'),\
			HEADER2: None,\
			DESC: "Harbour HRB file",\
			CHANCE: 2},
		RISCOS:{ \
			HEADER1: ('A','r','c','h','i','v','e'),\
			HEADER2: None,\
			DESC: "RISC OS archive (ArcFS format)",\
			CHANCE: 2},
		HAP:{ \
			HEADER1: ('\x91','\x33','H','F'),\
			HEADER2: None,\
			DESC: "HAP archive data",\
			CHANCE: 2},
		LIM:{ \
			HEADER1: ('L','I','M','\x1a'),\
			HEADER2: None,\
			DESC: "LIM archive data",\
			CHANCE: 2},
		FREEZE:{ \
			HEADER1: ('\x1f','\x9f','\x4a','\x10','\x0a'),\
			HEADER2: None,\
			DESC: "Freeze archive data",\
			CHANCE: 2},
		ZOO:{ \
			HEADER1: ('\xfd','\xc4','\xa7','\xdc'),\
			HEADER2: None,\
			DESC: "Zoo archive data",\
			CHANCE: 2},
		RAR:{ \
			HEADER1: ('R','a','r','!'),\
			HEADER2: None,\
			DESC: "RAR archive data",\
			CHANCE: 2},
		EET:{ \
			HEADER1: ('\x1e','\xe7','\xff','\x00'),\
			HEADER2: None,\
			DESC: "EET archive",\
			CHANCE: 2},
		RZIP:{ \
			HEADER1: ('R','Z','I','P'),\
			HEADER2: None,\
			DESC: "rzip compressed data",\
			CHANCE: 2},
		SQSH:{ \
			HEADER1: ('S','Q','S','H'),\
			HEADER2: None,\
			DESC: "squished archive data (Acorn RISCOS)",\
			CHANCE: 2},
		ISC:{ \
			HEADER1: ('I','S','c','('),\
			HEADER2: None,\
			DESC: "InstallShield CAB",\
			CHANCE: 2},
		NWFILE:{ \
			HEADER1: ('P','a','c','k','e','d','\\',' ','F','i','l','e','\\'),\
			HEADER2: None,\
			DESC: "Personal NetWare Packed File",\
			CHANCE: 2},
		DSIGDCC:{ \
			HEADER1: ('D','S','I','G','D','C','C'),\
			HEADER2: None,\
			DESC: "CrossePAC archive data",\
			CHANCE: 2},
		ARJ:{ \
			HEADER1: ('\x60','\xea'),\
			HEADER2: None,\
			DESC: "ARJ",\
			CHANCE: 2}
	},

	DOCS: { \
		PDF:{ \
			HEADER1: ('\x25','\x50','\x44','\x46','\x2e'),\
			HEADER2: None,\
			DESC: "PDF - Portable Document Format",\
			CHANCE: 2},
		DOC:{ \
			HEADER1: ('\xd0','\xcf','\x11','\xe0','\xa1','\xb1','\x1a','\xe1'),\
			HEADER2: None,\
			DESC: "DOC - Microsoft Document Format",\
			CHANCE: 2},
		RTF:{ \
			HEADER1: ('{','\\','\\','r','t','f'),\
			HEADER2: None,\
			DESC: "RTF - Rich Text Format data",\
			CHANCE: 2}
	},

	BOOT: { \
		UBOOT:{ \
			HEADER1: ('\x27','\x05','\x19','\x56'),\
			HEADER2: None,\
			DESC: "UBOOT - PPCBoot Image - maybe bootloader",\
			CHANCE: 2}

},
	ASM: { \
		AVR:{ \
			HEADER1: ('a','v','a','o','b','j'),\
			HEADER2: None,\
			DESC: "AVR assembler object code",\
			CHANCE: 2}
},
	PICTURES: { \
		GIMPXCF:{ \
			HEADER1: ('g','i','m','p','\\',' ','x','c','f'),\
			HEADER2: None,\
			DESC: "GIMP XCF image data",\
			CHANCE: 2}
},

	DEVICES: { \
		LTRX1:{ \
			HEADER1: ('D','S','T','-','L','T','R','X'),\
			HEADER2: None,\
			DESC: "LTRX1 - Lantronics Firmware Part detected",\
			CHANCE: 2},

		LTRX2:{ \
			HEADER1: ('L','T','R','X'),\
			HEADER2: None,\
			DESC: "LTRX2 - Lantronics Firmware Part detected",\
			CHANCE: 2},

		WGR614BOOT:{ \
			HEADER1: ('*','#','$','^'),\
			HEADER2: None,\
			DESC: "NETGEAR WGR614v9 Bootware - unknown bootloader maybe",\
			CHANCE: 2},

		WGR614:{ \
			HEADER1: ('@','U','1','2','H','0','9','4','T'),\
			HEADER2: None,\
			DESC: "NETGEAR WGR614v9 Firmware",\
			CHANCE: 2}

}
}
