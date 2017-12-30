import os

class MP3File(object):
	def __init__(self, filename):
		self.endianness = "big"
		self.filename = filename
		self.v1_data = None
		self.v2_data = None
		# every mp3 has v1 metadata
		self.has_v1 = True 
		self.has_v2 = False

	def read_v1_data(self):
		with open(self.filename, "rb") as file:
			# v1 header is always last 128 bytes
			file.seek(-128, os.SEEK_END)
			self.v1_data = file.read(128)

	def read_v2_data(self):
		with open(self.filename, "rb") as file:
			# Check for v2 header
			if file.read(3) == b"ID3":
				self.has_v2 = True
				# read size of v2 metadata
				file.seek(6, os.SEEK_SET)
				size = int.from_bytes(file.read(4), self.endianness)
				# read the rest of the header
				self.v2_data = file.read(size)

	def get_v1_data(self):
		self.read_v1_data()
		return self.v1_data

	def write_v1_data(self, v1_bytes):
		if len(v1_bytes) == 128:
			with open(self.filename, "rb+") as file:
				file.seek(-128, os.SEEK_END)
				file.write(v1_bytes)
		else:
			print("ID3v1 write data is not exactly 128 bytes. It is " + str(len(v1_bytes)) + ". Aborting write.")

	def get_v2_data(self):
		self.read_v2_data()
		return self.v2