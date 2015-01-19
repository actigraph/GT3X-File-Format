# SENSOR_SCHEMA Packet - ID 24 #

## Description ##
This record allows dynamic definition of a SENSOR_DATA record format.

## Format of Data ##

## Example ##

## Sample C# Parsing Code ##

```c#
public class SensorSchema
{
	public int ID { get; protected set; }
	public int ColumnsPerRow { get; protected set; }
	public int SamplesInEachRecord { get; protected set; }
	public List<SensorColumn> SensorColumns { get; protected set; }

	public SensorSchema(int id, int columnsPerRow, int samplesInEachRecord)
	{
		ID = id;
		ColumnsPerRow = columnsPerRow;
		SamplesInEachRecord = samplesInEachRecord;
		SensorColumns = new List<SensorColumn>(columnsPerRow);
	}
}

public class SensorColumn
{
	public bool IsBigEndian { get; set; }
	public bool IsSigned { get; set; }

	/// <summary>
	/// Bit offset for the start of this column within the sample.
	/// </summary>
	public byte Offset { get; set; }

	/// <summary>
	/// Bit size of this column within the samples.
	/// </summary>
	public byte Size { get; set; }

	/// <summary>
	/// An SSP encoded floating-point scale factor for the column value. Devide the encoded value by this number to get the output in the proper units.
	/// </summary>
	public double ScaleFactor { get; set; }

	/// <summary>
	/// A fixed-length whitespace-padded ASCII string containing a human-readable name for the column suitable for use in a CSV output.
	/// </summary>
	public string Label { get; set; }
}

int id = BitConverter.ToInt16(Payload, 0);
int columns = BitConverter.ToInt16(Payload, 2);
int samples = BitConverter.ToInt16(Payload, 4);

var sensorSchema = new SensorSchema(id, columns, samples);

const int BYTES_PER_COLUMN = 23;
for (int i = 0; i < columns; i++)
{    
    int startingOffset = 6 + (BYTES_PER_COLUMN * i);
    byte columnFlags = Payload[startingOffset];

	bool bigEndian = ((byte)(columnFlags & (1 << 0)) != 0);
	bool signed = ((byte)(columnFlags & (1 << 1)) != 0);

    byte columnOffset = Payload[startingOffset + 1];
	byte columnSize = Payload[startingOffset + 2];
    uint value = BitConverter.ToUInt32(Payload, startingOffset + 3);

	double columnScaleFactor = Math.Round(DeviceUtilities.SspCodec.Decode(value), 6,
		MidpointRounding.AwayFromZero);

	var columnLabel = Encoding.ASCII.GetString(Payload, startingOffset + 7, 16).Trim();
	SensorColumn column = new SensorColumn
	{
		IsBigEndian = bigEndian,
		IsSigned = signed,
		Offset = columnOffset,
		Size = columnSize,
		ScaleFactor = columnScaleFactor,
		Label = columnLabel
	};

    sensorSchema.SensorColumns.Add(column);
}
```

## Notes ##