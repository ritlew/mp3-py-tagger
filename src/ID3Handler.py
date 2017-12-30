import struct

# super class for ID3 handlers
class ID3Handler(object):
	def __init__(self):
		self.raw_data = None
		self.metadata = dict()

	def set_data(self, data):
		self.raw_data = data

	def get_tags(self):
		return self.metadata

	# should be implemented by subclasses
	def read_all(self):
		pass

class ID3v1Handler(ID3Handler):
	def __init__(self):
		super(ID3v1Handler, self).__init__()
		# list of header information
		# (Field name, offset, length, type)
		self.data_info = [
			("Song Name", 3, 30, "str"),
			("Artist", 33, 30, "str"),
			("Album", 63, 30, "str"),
			("Year", 93, 4, "str"),
			("Comment", 97, 30, "str"),
			("Genre", 127, 1, "int")
		]

		# handlers for converting data from bytes
		self.data_handlers = {
			"str": lambda data: data.decode().split('\x00')[0],
			"int": lambda data: int.from_bytes(data, byteorder="big")
		}

	def read_all(self):
		if self.raw_data != None:
			for info in self.data_info:
				self.metadata[info[0]] = self.data_handlers[info[3]](self.raw_data[info[1] : info[1] + info[2]])
		return self.metadata
class ID3v2Handler(ID3Handler):
	def __init__(self):
		super(ID3v1Handler, self).__init__()

	def read_all(self):
		pass