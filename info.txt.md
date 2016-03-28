# info.txt Format

info.txt is a plain text file that contains key items to help parse activity data

The data in the info.txt file is stored in a modified key/value format with each item stored on a new line. 

The items are stored as "{key}: {value}" without the quotes.

##Items in the File

<table>
  <tr>
    <th>Key</th>
    <th>Value</th>
	<th>Type</th>
  </tr>
  <tr>
    <td>Serial Number</td>
    <td>The serial number of the device that was used.</td>
	<td>string</td>
  </tr>
  <tr>
    <td>Firmware</td>
    <td>The firmware version of the device that was used.</td>
    <td>string</td>
  </tr>
  <tr>
    <td>Battery Voltage</td>
    <td>The battery voltage of the device that was used at the time of download.</td>
    <td>double</td>
  </tr>
  <tr>
    <td>Sample Rate</td>
    <td>The sample rate (in hz) that the device was initialized in. ActiGraph devices record at 30, 40, 50, 60, 70, 80, 90, and 100 Hz.</td>
    <td>double</td>
  </tr>
  <tr>
    <td>Start Date</td>
    <td>The start date and time that the device was initialized in. It's stored in <a href=http://msdn.microsoft.com/en-us/library/system.datetime.ticks.aspx>.NET Ticks</a></td>
    <td>long (64-bit signed integer)</td>
  </tr>
  <tr>
    <td>Stop Date</td>
    <td>The stop date and time that the device was initialized with. It's stored in <a href=http://msdn.microsoft.com/en-us/library/system.datetime.ticks.aspx>.NET Ticks</a></td>
    <td>long (64-bit signed integer)</td>
  </tr>
  <tr>
    <td>Download Date</td>
    <td>The date and time that the device was downloaded. It's stored in <a href=http://msdn.microsoft.com/en-us/library/system.datetime.ticks.aspx>.NET Ticks</a></td>
    <td>long (64-bit signed integer)</td>
  </tr>
  <tr>
    <td>Board Revision</td>
    <td>The board revision of the device.</td>
    <td>int</td>
  </tr>
  <tr>
    <td>Subject Name</td>
    <td>The subject name given to the device on initialization.</td>
    <td>string</td>
  </tr>
</table>

## Sample File

```CSS
Serial Number: NEO1C16110020
Firmware: 2.2.0
Battery Voltage: 4.25
Sample Rate: 30
Start Date: 634556532600000000
Stop Date: 0
Download Date: 634570285571111563
Board Revision: 2
Subject Name: josfew2342
```