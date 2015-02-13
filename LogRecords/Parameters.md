# PARAMETERS Packet - ID 21 #

## Description ##
The PARAMETERS record is written during initialization of the device, and it should appear just after the METADATA record. It contains a list of key/value pairs that describe the initialization parameters of the device and various other device conditions of interest at the time of initialization.

The content of this record may vary in number and types of variables. It is safe to ignore any variables that have an unknown key. Some variables are included for diagnostic purposes that are unnecessary for interpreting other log data.

## Format of Data ##
The record payload is of variable length consisting of 8-byte key/value pairs. The key is made up of a 16-bit unsigned address space and 16-bit unsigned identifier. All values are encoded in a 32-bit unsigned integer. The address space, identifier and value are in little-endian byte order.


## Example ##

## Notes ##
