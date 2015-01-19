# HEART_RATE_ANT Packet - ID 1 #

## Description ##
Heart Rate RR information from ANT+ sensor. Each packet can contain multiple heart rate RR values. 

## Format of Data ##
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
        <td>Heart Beat Count</td>
        <td>Incremental count of beat count (0 - 255). Rolls over at 255</td>
    </tr>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>Previous Time</td>
        <td>UInt16<br>
			Relative time of the previous valid heart beat event<br>
			1/1024 s/LSB [zero (0) is invalid]
		</td>
    </tr>
    <tr>
        <td>3</td>
        <td>2</td>
        <td>Current Time</td>
        <td>UInt16<br>
			relative time of the last valid heart beat event<br>
			(1/1024 s/LSB)
		</td>
    </tr>
</table>

## Sample C# Parsing Code ##

```c#

public class HeartRRRecord
{
    public byte HeartBeatCount { get; set; }
    public DateTime Timestamp { get; set; }
    public int PreviousTime { get; set; }
    public int CurrentTime { get; set; }
    public double MillisecondsSinceLastBeat { get; set; }
}

List<HeartRRRecord> heartRateRRRecords = new List<HeartRRRecord>();

for (int i = 0; i < Payload.Length; i += 5)
{
    //generate rr record for current information
    HeartRRRecord rrRecord = new HeartRRRecord();
    rrRecord.HeartBeatCount = Payload[i];
    rrRecord.PreviousTime = BitConverter.ToUInt16(Payload, i + 1);
    rrRecord.CurrentTime = BitConverter.ToUInt16(Payload, i + 3);

    if (heartRateRRRecords.Count > 0)
    {
        HeartRRRecord lastRecord = heartRateRRRecords[heartRateRRRecords.Count - 1];

        if (lastRecord.HeartBeatCount == rrRecord.HeartBeatCount &&
            (lastRecord.PreviousTime == rrRecord.PreviousTime ||
            lastRecord.CurrentTime == rrRecord.CurrentTime))
        {
            //make sure we skip any RR records that are duplicates
            continue;
        }
    }

    //see if we are missing records from current information and last known/generated beat
    if (heartRateRRRecords.Count > 0 && (byte)(heartRateRRRecords[heartRateRRRecords.Count - 1].HeartBeatCount + 1) != rrRecord.HeartBeatCount)
    {
        //we can only generate a record if we are missing ONE beat
        if ((byte)(heartRateRRRecords[heartRateRRRecords.Count - 1].HeartBeatCount + 2) == rrRecord.HeartBeatCount && rrRecord.PreviousTime != 0)
        {
            //only missing one beat, we can fudge it then
            HeartRRRecord recordInsert = new HeartRRRecord();
            recordInsert.HeartBeatCount = (byte)(heartRateRRRecords[heartRateRRRecords.Count - 1].HeartBeatCount + 1);
            recordInsert.CurrentTime = rrRecord.PreviousTime;
            recordInsert.PreviousTime = heartRateRRRecords[heartRateRRRecords.Count - 1].CurrentTime;

            //figure out how many seconds to insert based on previous and current time
            int secondsInsert;
            if (recordInsert.CurrentTime >= recordInsert.PreviousTime)  //we haven't wrapped around
                secondsInsert = recordInsert.CurrentTime - recordInsert.PreviousTime;
            else   //we have wrapped around and need to account for it
                secondsInsert = (recordInsert.CurrentTime + UInt16.MaxValue + 1) - recordInsert.PreviousTime;

            recordInsert.MillisecondsSinceLastBeat = 1000.0 * secondsInsert / 1024.0;
            DateTime timestampInsert = heartRateRRRecords[heartRateRRRecords.Count - 1].Timestamp + TimeSpan.FromSeconds(secondsInsert / 1024.0);

            recordInsert.Timestamp = timestampInsert;
            heartRateRRRecords.Add(recordInsert);
        }
        else
        {
            //unable to insert HR RR epoch because we are missing more than ONE beat
        }
    }

    int previousTime = 0;

    //figure out previous time value
    if (heartRateRRRecords.Count == 0)
        previousTime = rrRecord.PreviousTime;
    else if (rrRecord.PreviousTime == 0 && (byte)(heartRateRRRecords[heartRateRRRecords.Count - 1].HeartBeatCount + 1) == rrRecord.HeartBeatCount)
        previousTime = heartRateRRRecords[heartRateRRRecords.Count - 1].CurrentTime;
    else if (rrRecord.PreviousTime != 0)
        previousTime = rrRecord.PreviousTime;

    int sinceLast;
    if (previousTime == 0)
        sinceLast = 0;
    else if (rrRecord.CurrentTime >= previousTime)
        sinceLast = rrRecord.CurrentTime - previousTime;
    else
        sinceLast = (rrRecord.CurrentTime + UInt16.MaxValue + 1) - previousTime;

    rrRecord.MillisecondsSinceLastBeat = 1000.0 * sinceLast / 1024.0;

    //for the very first RR record, we have to make up a timestamp
    //also, for a record after a missing chunk of records, we have to make up a timestamp
    //for both of these cases, we base if off the Record's timestamp
    bool useRecordTimestampToCalculateRRTimestamp = heartRateRRRecords.Count == 0 ||
                                                (byte)(heartRateRRRecords[heartRateRRRecords.Count - 1].HeartBeatCount + 1) != rrRecord.HeartBeatCount;

    DateTime timestamp;
    if (useRecordTimestampToCalculateRRTimestamp)
        timestamp = Header.TimeStamp + TimeSpan.FromSeconds(sinceLast / 1024.0);   //have to guess at the first timestamp
    else
        timestamp = heartRateRRRecords[heartRateRRRecords.Count - 1].Timestamp + TimeSpan.FromSeconds(sinceLast / 1024.0);

    rrRecord.Timestamp = timestamp;

    heartRateRRRecords.Add(rrRecord);
}
```