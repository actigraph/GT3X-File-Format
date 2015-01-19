# TAG Packet - ID 7 #

## Description ##

The TAG record is used to record proximity with a beacon device as detected over wireless. Each record contains of a list of beacons detected during the timestamped scan interval. The scan defaults to once per minute, bit it is configurable with the latest Bluetooth Low Energy (BLE) activity monitors.
## Format of Data ##

The TAG payload consist of multiple records per detected beacon. Each record is 15 bytes with the beacon serial number as 13 byte ASCII string, 1 byte transmit (TX) power in decibels (dB), 1 signed byte received signal strength indicator (RSSI) in dB.

## Example ##

### Binary Payload (hexadecimal) ###

54 41 53 30 43 33 32 31 34 30 30 32 36 00 D6
4D 4F 53 32 50 32 30 31 33 30 30 31 39 00 C1

### Interpretation ###

<table>
<tr>
<th>Device</th>
<th>Serial Number</th>
<th>TX Power (dB)</th>
<th>RSSI (dB)</th>
</tr>
<tr>
<td>1</td>
<td>TAS0C32140026</td>
<td>0</td>
<td>-42</td>
<tr>
<tr>
<td>2</td>
<td>MOS2P20130019</td>
<td>0</td>
<td>-63</td>
<tr>
</table>

## Notes ##

The TX power and RSSI information is not a reliable source for distance calculations. Atmospheric conditions and obstacles will contribute to varying RSSI readings at the same distance from a monitor to a beacon.

