from MP3FileReader import MP3FileReader
from ID3Handler import ID3v1Handler, ID3v2Handler
from Song import Song

class mp3py(object):
	ID3v1_handler = ID3v1Handler
	ID3v2_handler = ID3v2Handler

	def load_from_file(filename):
		reader = MP3FileReader(filename)
		v1 = reader.get_v1_data()
		v1_handler = mp3py.ID3v1_handler()
		v1_handler.set_data(v1)
		s = Song()
		s.set_metadata(v1_handler.read_all())
		return s