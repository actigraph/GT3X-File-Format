# HEART_RATE_BLE Packet - ID 14 #

## Description ##
Bluetooth heart rate information (BPM and RR)

## Format of Data ##
The format of this information is straight from the <a href="https://developer.bluetooth.org/gatt/characteristics/Pages/CharacteristicViewer.aspx?u=org.bluetooth.characteristic.heart_rate_measurement.xml">Bluetooth standard heart rate measurement</a>

## Example ##
* Payload of: ``` 0x16 0x42 0x18 0x04 0x70 0x01 ```
* HR = 66
* EE = false
* RR = true (2 values)
* RR value #1 - 1048 (1.0234 milliseconds)
* RR value #2 - 368 (0.359 milliseconds)

## Sample C# Parsing Code ##

```c#
//first byte denotes Flags
byte flags = Payload[0];

ushort hrOffset = 1; //skip over flags

short hr = 0;
bool HRC2 = (flags & 1) == 1;
if (HRC2) //this means the BPM is un uint16
{
	//since the actigraph device isn't able to handle 2 byte BPM, we can't use this one!
    break;
}
else //BPM is uint8
{
	hr = Payload[hrOffset];
	hrOffset += 1;

	var sample = new Data<byte>(Header.TimeStamp, (byte)hr);
	heartRate.Add(sample);
}

//see if EE is available
//if so, pull 2 bytes
bool ee = (flags & (1 << 3)) != 0;
if (ee)
    hrOffset += 2;

//see if RR is present
//if so, the number of RR values is total bytes left / 2 (size of uint16)
bool rr = (flags & (1 << 4)) != 0;
if (rr)
{
    int count = (Payload.Length - hrOffset)/2;
    for (int i = 0; i < count; i++)
    {
		//each existence of these values means an R-Wave was detected previously
		//the ushort means the time (1/1024 seconds) since last r-wave
		ushort value = BitConverter.ToUInt16(Payload, hrOffset);

		double milliSeconds = value / 1024.0;
		HeartRRBluetoothRecord rrBluetoothRecord = new HeartRRBluetoothRecord
		{
			Timestamp = Header.TimeStamp,
			SecondsSinceLastBeat = milliSeconds,
			HR = hr
		};

		_heartRateRRBluetoothRecords.Add(rrBluetoothRecord);

		hrOffset += 2;
    }
}
```
