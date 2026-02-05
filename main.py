MusicList = []

print("m3u8 playlist to wpl converter (to use in media player classic).")
print("="*20)
print("Please be sure that input file is in same folder as this script")

filename = input("Enter file name (playlist name) without extension: ")

#Open files start
with open("{}.m3u8".format(filename), "r", encoding="utf-8") as InFile:
    MusicListRaw = InFile.read().splitlines()

for i in range(len(MusicListRaw)):
    if not MusicListRaw[i].startswith("#"):
        MusicList.append(MusicListRaw[i])

with open("{}.wpl".format(filename), "w", encoding="utf-8") as OutFile:
    OutFile.write('<?wpl version="1.0"?>\n')
    OutFile.write('<smil>\n')
    OutFile.write('    <head>\n')
    OutFile.write('        <meta name="Generator" content="Microsoft Windows Media Player -- 12.0.26100.7309"/>\n')
    OutFile.write('        <meta name="ItemCount" content="{}"/>\n'.format(len(MusicList)))
    OutFile.write('        <title>{}</title>\n'.format(filename))
    OutFile.write('    </head>\n')
    OutFile.write('    <body>\n')
    OutFile.write('        <seq>\n')
    for Music in MusicList:
        OutFile.write('            <media src="{}"/>\n'.format(Music))
    OutFile.write('        </seq>\n')
    OutFile.write('    </body>\n')
    OutFile.write('</smil>')

print("Done :)")