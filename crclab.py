# Patrick Behrens
# Homework #1 - COMP 346 - Telecommunications 

# 

import crcmod
import io


# Needed files for lab
# Two altered text, audio and image files

initialTextFileName = "initial_text_file.txt"
alteredTextFileName = "altered_text_file.txt"
initialImageFileName = "initial_image_file.jpg"
alteredImageFileName = "altered_image_file.jpg"
intialAudioFileName = "initial_audio_file.mp3"
alterdAudioFileName = "altered_audio_file.mp3"


def genHash(fileName, crcHasher):
	fd = open(fileName,"rb")
	bufferedFile = io.open(fileName, buffering=4096)

	with open(fileName, 'rb') as f:
		data = f.read()	
	fileHash = crcHasher(data)
	print fileName + " : " + str(fileHash)
	return fileHash


def main():
	crc8 = crcmod.predefined.mkCrcFun('crc-8')
	crc32 = crcmod.predefined.mkCrcFun('crc-32')
	
	# crc8 hashes

	print "CRC 8 Hashes"
	print "\n"

	initialTextHash8 = genHash(initialTextFileName, crc8)
	alteredTextHash8 = genHash(alteredTextFileName, crc8)
	initialImageHash8 = genHash(initialImageFileName, crc8)
	alteredImageHash8 = genHash(alteredImageFileName, crc8)
	intialAudioHash8 = genHash(intialAudioFileName, crc8)
	alteredAudioHash8  = genHash(alterdAudioFileName, crc8)


	print "============================================================"
	print "\n"
	print "CRC 32 Hashes"
	print "\n"

	# crc32 hashes
	initialTextHash32 = genHash(initialTextFileName, crc32)
	alteredTextHash32 = genHash(alteredTextFileName, crc32)
	initialImageHash32 = genHash(initialImageFileName, crc32)
	alteredImageHash32 = genHash(alteredImageFileName, crc32)
	intialAudioHash32 = genHash(intialAudioFileName, crc32)
	alteredAudioHash32  = genHash(alterdAudioFileName, crc32)



	# print hex(initialTextHash)
	# print "\n hash 2 \n"
	# print alteredTextHash

if __name__ == "__main__":
    main()