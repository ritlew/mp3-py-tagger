from MP3py import mp3py
import pprint


if __name__ == "__main__":
	printer = pprint.PrettyPrinter(indent=4)
	song = mp3py("Plastic Love.mp3")

	printer.pprint(song.dump_metadata())

	song.v1_metadata["Song Name"] = "Plastic Love"

	song.write_to_file()