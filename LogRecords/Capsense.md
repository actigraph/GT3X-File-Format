# CAPSENSE Packet - ID 13 #

## Description ##
Capacitive sensor data that is logged once a minute.

## Format of Data ##
6 bytes that log if device detected contact with skin.

<table>
    <tr>
        <th>Offset (bytes)</th>
        <th>Size (bytes)</th>
        <th>Name</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>0</td>
        <td>2</td>
        <td>Signal</td>
        <td>UInt16 that is the signal of the sensor.</td>
    </tr>
    <tr>
        <td>2</td>
        <td>2</td>
        <td>Reference</td>
        <td>UInt16</td>
    </tr>
    <tr>
        <td><b>4</b></td>
        <td><b>1</b></td>
        <td><b>State</b></td>
        <td><b>UInt8 that determines if the device is being worn or not.<br><br>0 = not worn<br>1 = worn</b></td>
    </tr>
    <tr>
        <td>5</td>
        <td>1</td>
        <td>Bursts</td>
        <td>UInt8</td>
    </tr>
</table>

## Example ##

## Sample C# Parsing Code ##

```c#
int offsetCapsense = 0;
ushort signal = BitConverter.ToUInt16(Payload, offsetCapsense);
offsetCapsense += 2;

ushort reference = BitConverter.ToUInt16(Payload, offsetCapsense);
offsetCapsense += 2;

byte state = Payload[offsetCapsense];	//0 == NOT worn, 1 == worn
offsetCapsense++;

byte bursts = Payload[offsetCapsense];
```

## Notes ##
**Earlier versions of .gt3x files logged only if there was a change in the state. Newer versions log every minute regardless of change. If there are missing minutes, assume the previous value continues.**