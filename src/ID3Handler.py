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
		self.read_handlers = {
			"str": lambda data: data.decode().split('\x00')[0],
			"int": lambda data: int.from_bytes(data, byteorder="big")
		}

		self.write_handlers = {
			"str": lambda data, length: data[0:length].encode().ljust(length, b'\0'),
			"int": lambda data, length: data.to_bytes(length, 'big')
		}

	def read_all(self):
		if self.raw_data != None:
			self.metadata = {
				info[0]: self.read_handlers[info[3]](self.raw_data[info[1]: info[1] + info[2]]) for info in self.data_info
			 }
		return self.metadata

	def format_all(self):
		byte_string = b"ID3" + b"".join([
			self.write_handlers[self.data_info[i][3]](list(self.metadata.values())[i], self.data_info[i][2]) for i in range(len(self.data_info))
		])
		return byte_string


class ID3v2Handler(ID3Handler):
	def __init__(self):
		super(ID3v2Handler, self).__init__()

	def read_all(self):
		pass