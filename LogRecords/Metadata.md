# METADATA Packet - ID 6 #

## Description ##
Arbitrary metadata content. ActiGraph's software system stores anything we might need at a later date. Such as: biometric information, what version of software initialized the device, if the device was initialized with a group of devices, and/or specific devices to look for when using proximity tagging.

## Format of Data ##
Most metadata content is stored in [JSON](http://en.wikipedia.org/wiki/JSON "JSON wiki") string format. It is [UTF-8 encoded](http://en.wikipedia.org/wiki/UTF-8 "UTF-8 wiki") strings.

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
* Seperator - 0x1E at offset 00
* Type - 0x06 at offset 01
* Timestamps - 0x71E8B454 at offset 02 (1421142129 or 1/13/2015 09:42:09)
* Size - 0x7C00 at offset 06 (124)

### Payload ###

```
0x7B 0x22 0x4D 0x65 0x74 0x61 0x64 0x61 0x74 0x61 0x54 0x79 0x70 0x65 0x22 0x3A
0x22 0x42 0x69 0x6F 0x22 0x2C 0x22 0x53 0x75 0x62 0x6A 0x65 0x63 0x74 0x4E 0x61
0x6D 0x65 0x22 0x3A 0x22 0x43 0x4C 0x45 0x32 0x41 0x31 0x34 0x31 0x35 0x31 0x36
0x31 0x37 0x22 0x2C 0x22 0x52 0x61 0x63 0x65 0x22 0x3A 0x22 0x22 0x2C 0x22 0x4C
0x69 0x6D 0x62 0x22 0x3A 0x22 0x22 0x2C 0x22 0x53 0x69 0x64 0x65 0x22 0x3A 0x22
0x22 0x2C 0x22 0x44 0x6F 0x6D 0x69 0x6E 0x61 0x6E 0x63 0x65 0x22 0x3A 0x22 0x22
0x2C 0x22 0x50 0x61 0x72 0x73 0x65 0x64 0x22 0x3A 0x66 0x61 0x6C 0x73 0x65 0x2C
0x22 0x4A 0x53 0x4F 0x4E 0x22 0x3A 0x6E 0x75 0x6C 0x6C 0x7D
```

#### Raw string data ####
```
{"MetadataType":"Bio","SubjectName":"CLE2A14151617","Race":"","Limb":"","Side":"","Dominance":"","Parsed":false,"JSON":null}
```

#### Formatted json string ####
```json
{
	"MetadataType":"Bio",
	"SubjectName":"CLE2A14151617",
	"Race":"",
	"Limb":"",
	"Side":"",
	"Dominance":"",
	"Parsed":false,
	"JSON":null
}
```

### Checksum ###
Offset = 8 + size (124) = 132
```` 0xF8 ````

## Files Initialized in UTC ##
Certain .gt3x files are initialized in [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time "UTC wiki page"). These files were most likely initialized inside of [ActiGraph's web portal, Study Admin](http://www.actigraphcorp.com/product-category/study-admin/). A file's timestamps are in UTC if it contains the following:
1. A metadata packet with *MetadataType* "LocalTimeLog"
2. *UsedUtc* is set to true in the LocalTimeLog packet

### Example LocalTimeLog JSON ###
```json
{
   "MetadataType":"LocalTimeLog",
	...
   "UsedUtc":true
}
```

To determine how much to adjust the timestamps to match the local time zone, use the *UtcOffset* property in the *SubjectTimeLog* packet. It is in the format HOURS:MINUTES:SECONDS. In the example below, the file was initialized in Central Time with an offset of -6 hours.

### Example SubjectTimeLog JSON ###
```
{
   "MetadataType":"SubjectTimeLog",
   "UtcOffset":"-06:00:00",
   "Name":"(UTC-06:00) Central Time (US & Canada)"
}
```
