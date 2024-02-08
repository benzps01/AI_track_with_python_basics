"""read(6) consists of an integer, then the file first reads upto that character 
and then the rest if another read() is provided below."""

# with open("camelot.txt") as song:
#     print(song.read(2))
#     print(song.read(8))
#     print(song.read())

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())
        """strip() is used b'coz just appending 
        also adds newline character \n"""
print(camelot_lines)
