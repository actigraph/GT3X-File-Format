# SENSOR_DATA Packet - ID 25 #

## Description ##
This record stores sensor data according to a SENSOR_SCHEMA definition.

## Format of Data ##

## Example ##

## Sample C# Parsing Code ##

```c#
int schemaId = BitConverter.ToInt16(Payload, 0);
if (!_sensorSchemata.ContainsKey(schemaId))
	throw new ArgumentException("Sensor schemata doesn't have entry for ID #" + schemaId);

List<SensorPacket> = new List<SensorPacket>(100);

SensorSchema schema = _sensorSchemata[schemaId];

const int BITS_PER_BYTE = 8;
int offset = 2;

Ticker tick = new Ticker(schema.SamplesInEachRecord); //this helps calculate timestamps
long rawSecondCounter = 0;

DateTime firstSample = Header.TimeStamp.Date +
                       new TimeSpan(TimeStamp.Hour,
                           TimeStamp.Minute, TimeStamp.Second);

for (int i = 0; i < schema.SamplesInEachRecord; i++)
{
    SensorPacket sensorPacket =
		new SensorPacket(firstSample.AddMilliseconds(rawSecondCounter),
            schema.SensorColumns.Select(x => x.Label));
    
    foreach (SensorColumn column in schema.SensorColumns)
    {
		//get bytes
		short sensorValue = 0;

        int bytesInValue = column.Size/BITS_PER_BYTE;

        if (column.IsSigned)
        {
            if (bytesInValue == 1)
                sensorValue = Payload[offset];
			else if (bytesInValue == 2)
				sensorValue = BitConverter.ToInt16(Payload, offset);
			else
			{
				//unable to parse
			}
        }
        else
        {
			if (bytesInValue == 1)
			{
				sensorValue = Payload[offset];
			}
			else if (bytesInValue == 2)
			{
				var uintvalue = BitConverter.ToUInt16(Payload, offset);
				sensorValue = (short)uintvalue;
			}
			else
			{
				//unable to parse
			}
        }

        if (column.IsBigEndian)
			sensorValue = sensorValue.SwapEndianness();

		double result = column.ScaleFactor != 0 ? sensorValue / column.ScaleFactor : sensorValue;

        if (column.Label.Equals("temperature", StringComparison.CurrentCultureIgnoreCase))
            result += 21;

		//only add values for non-empty column names
		if (!string.IsNullOrEmpty(column.Label))
			sensorPacket.Values[column.Label] = result;

		offset += (column.Size / BITS_PER_BYTE);
    }
	rawSecondCounter += tick.GetNextMillisecondsToAddToTimestamp();
	SensorPackets.Add(sensorPacket);
}
```

## Notes ##