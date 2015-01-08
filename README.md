# ActiGraph .gt3x File Format

## Introduction

This documentation provides information on getting activity data out of [ActiGraph](http://www.actigraphcorp.com/ "ActiGraph site") .gt3x files. 

## Valid .gt3x Files ##

This documentation is valid for .gt3x files downloaded from the following devices:
* GT3X+ (serial numbers starting with NEO and firmware 3.0 and higher)
* wGT3X+ (serial numbers starting with CLE)
* wGT3X-BT (serial numbers starting with MOS0 and MOS2)
* ActiSleep+ (serial numbers starting with MRA and firmware 3.0 and higher)
* wActiSleep+ (serial numbers starting with MOS3
* wActiSleep-BT (serial numbers starting with MOS4)
* GT9X Link (serial numbers starting with TAS) 

## Invalid .gt3x Files ##
**NOTE:** Devices with serial numbers that start with "NEO" or "MRA" and have firmware version of 2.5.0 or earlier use an older format of the .gt3x file. Please see this GitHub repo for more information: https://github.com/actigraph/NHANES-GT3X-File-Format

## Log Records ##
Binary .gt3x file data is grouped into timestamped records of varying types that are written sequentially as the data becomes available on the activity monitor. The format is similar to common protocols used for serial communication. Each log record includes a header with a record separator, record type, timestamp and payload size. After the variable length payload is a checksum for ensuring data integrity.

### Log Record Format ###
<table>
    <tr>
        <th>Offset (bytes)</th>
        <th>Size (bytes)</th>
        <th>Name</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>0</td>
        <td>1</td>
        <td>Seperator</td>
        <td>An ASCII record separator byte (1Eh) marks the beginning of each log record.</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>Type</td>
        <td>A type identifier is used to interpret the payload of the record.</td>
    </tr>
    <tr>
        <td>2</td>
        <td>4</td>
        <td>Timestamp</td>
        <td>The date and time of the data contained in the record are marked to the nearest second in [Unix time](http://en.wikipedia.org/wiki/Unix_time) format.</td>
    </tr>
    <tr>
        <td>6</td>
        <td>2</td>
        <td>Size</td>
        <td>The size of the payload is given in bytes as an little-endian unsigned integer.</td>
    </tr>
    <tr>
        <td>8</td>
        <td>n</td>
        <td>Payload</td>
        <td>This is the actual data that varies based on the record *Type* field. It's size is provided in the *Size* field. Please refer to the appropriate section for the record type for the indiviual payload formats.</td>
    </tr>
    <tr>
        <td>8 + n</td>
        <td>1</td>
        <td>Checksum</td>
        <td>A 1-byte checksum immediately follows the record payload. It is a 1's complement, exclusive-or (XOR) of the log header and payload with an initial value of zero.</td>
    </tr>
</table>

<table>
   <tr>
      <th>Device Type</th>
      <th>Log Record Link</th>
   </tr>
   <tr>
      <td>wGT3X+</td>
      <td><a href=wGT3X+LogRecords.md>Log Records</a></td>
   </tr>
   <tr>
      <td>wGT3X-BT</td>
      <td><a href=wGT3X-BTLogRecords.md>Log Records</a></td>
   </tr>
   <tr>
      <td>ActiGraph Link</td>
      <td><a href=LinkLogRecords.md>Log Records</a></td>
   </tr>
</table>

**Prepared By:**

* [Daniel Judge](https://github.com/dwjref "Daniel's GitHub Profile") - Software Architect
* [Judge Maygarden](https://github.com/jmaygarden "Judge's GitHub Profile") - Hardware/Firmware Engineer
