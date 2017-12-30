class Song(object):
	def __init__(self):
		self.metadata = dict()

	def set_metadata(self, meta):
		self.metadata = meta

	def dump_metadata(self):
		return [[pair[0], pair[1]] for pair in self.metadata.items()]