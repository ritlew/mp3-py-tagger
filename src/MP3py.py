from MP3File import MP3File
from ID3Handler import ID3v1Handler, ID3v2Handler

class mp3py(object):
	ID3v1_handler = ID3v1Handler
	ID3v2_handler = ID3v2Handler

	def __init__(self, filename=None):
		self.v1_handler = mp3py.ID3v1_handler()
		self.v2_handler = mp3py.ID3v2_handler()
		self.file = None
		self.v1_metadata = dict()
		self.v2_metadata = dict()
		if filename is not None:
			self.load_from_file(filename)

	def dump_metadata(self):
		return [[pair[0], pair[1]] for pair in self.v1_metadata.items()]

	def load_from_file(self, filename):
		self.filename = filename
		self.file = MP3File(filename)
		v1 = self.file.get_v1_data()
		self.v1_handler.set_data(v1)
		self.v1_metadata = self.v1_handler.read_all()

	def write_to_file(self, filename=None):
		if filename is None:
			filename = self.filename

		v1_bytes = self.v1_handler.format_all()
		self.file.write_v1_data(v1_bytes)
