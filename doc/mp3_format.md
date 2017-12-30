# MP3 Format Information

This document details the tagging information relevant to the project. It does not discuss anything about the data.

Data was gathered from the following websites:
- http://www.multiweb.cz/twoinches/mp3inside.htm
- https://en.wikipedia.org/wiki/ID3
- http://id3.org/id3v2.3.0 (ID3v2)

## General

There are two versions of the metadata tag. Both of them are optional. The first version is simpler and goes at the end of the file. The second one is more complicated, stores more data, and is at the end of a file.

### Tag version 1

Simpler version of the metadata.

- At the end of the file
- 128 bytes long

Structure:

Bytes	  	Length	    Content
0-2		    3		    Tag identifier. Must contain "TAG" string if Tag is valid.
3-32		30		    Song Name
33-62		30		    Artist
63-92		30		    Album
93-96		4		    Year
97-126		30		    Comment
127		    1		    Genre

126th byte can also be used as the number of song. 
Items should be padded with NULL (ASCII 0) or with a space (ASCII 32).

### Tag version 2

Header (10 bytes): 

ID3v2/file identifier (3 bytes)   "ID3"
ID3v2 version (2 bytes)           $03 00
ID3v2 flags ( 1 byte)             %abc00000
- a - Unsycnronization
- b - Extended header 
- c - Experimental
ID3v2 size (4 bytes)              4 * %0xxxxxxx

Extended header seems to be rarely used.

A ID3v2 Frame (10 bytes):
	
Frame ID (4 bytes)       $xx xx xx xx (four characters)
Size (4 bytes)           $xx xx xx xx
Flags (2 bytes)          $xx xx

Frame ID is a 4 character predefined code. IDs starting with X, Y, or Z are experimental and free to use. Size is a 4 byte integer.

For the flags: "The first byte is for 'status messages' and the second byte is for encoding purposes." They follow the format %abc00000 %ijk00000.

Specific types of frames can be found at http://id3.org/id3v2.3.0#Declared_ID3v2_frames. They are also included in the source directory codes.txt.
