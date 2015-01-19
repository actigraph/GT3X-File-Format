# METADATA Packet - ID 6 #

## Description ##
Arbitrary metadata content

## Format of Data ##

## Example ##

```
Offset(d) 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15

00000000  1E 06 71 E8 B4 54 7C 00 7B 22 4D 65 74 61 64 61
00000016  74 61 54 79 70 65 22 3A 22 42 69 6F 22 2C 22 53
00000032  75 62 6A 65 63 74 4E 61 6D 65 22 3A 22 43 4C 45
00000048  32 41 31 34 31 35 31 36 31 37 22 2C 22 52 61 63
00000064  65 22 3A 22 22 2C 22 4C 69 6D 62 22 3A 22 22 2C
00000080  22 53 69 64 65 22 3A 22 22 2C 22 44 6F 6D 69 6E
00000096  61 6E 63 65 22 3A 22 22 2C 22 50 61 72 73 65 64
00000112  22 3A 66 61 6C 73 65 2C 22 4A 53 4F 4E 22 3A 6E
00000128  75 6C 6C 7D F8 1E 06 71 E8 B4 54 9F 00 7B 22 4D
```

### Header ###
Seperator - 0x1E at offset 00
Type - 0x06 at offset 01
Timestamps - 0x71E8B454 at offset 02 (1421142129 or 1/13/2015 09:42:09)
Size - 0x7C00 at offset 06 (124)

### Payload ###

### Checksum ###
Offset = 8 + size (124) = 132
```` 0xF8 ````

## Notes ##