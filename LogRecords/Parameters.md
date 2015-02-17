# PARAMETERS Packet - ID 21 #

## Description ##
The PARAMETERS record is written during initialization of the device, and it should appear just after the METADATA record. It contains a list of key/value pairs that describe the initialization parameters of the device and various other device conditions of interest at the time of initialization.

The content of this record may vary in number and types of variables. It is safe to ignore any variables that have an unknown key. Some variables are included for diagnostic purposes that are unnecessary for interpreting other log data.

## Format of Data ##
The record payload is of variable length consisting of 8-byte key/value pairs. The key is made up of a 16-bit unsigned address space and 16-bit unsigned identifier. All values are encoded in a 32-bit unsigned integer. The address space, identifier and value are in little-endian byte order.

Floating point values are encoded using a three-byte fraction and one-byte exponent. The fraction is a two’s-complement integer; its absolute value is 2<sup>23</sup> times the floating-point value’s mantissa (which is always between 0.5 inclusive and 1.0 not inclusive, i.e. the floating-point value is normalized), and its sign is that of the floating-point value. The exponent is a two’s-complement 8-bit number, signifying a power of 2 from -128 to +127. A zero value is represented by fraction and exponent both zero.

The following C# code performs the described floating-point encoding and decoding:
<pre>
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace DeviceUtilities
{
    public class SspCodec
    {
        const double FLOAT_MINIMUM = 0.00000011920928955078125;  /* 2^-23 */
        const double FLOAT_MAXIMUM = 8388608.0;                  /* 2^23  */
        const UInt32 ENCODED_MINIMUM = 0x00800000;
        const UInt32 ENCODED_MAXIMUM = 0x007FFFFF;
        const UInt32 SIGNIFICAND_MASK = 0x00FFFFFFu;
        const int EXPONENT_MINIMUM = -128;
        const int EXPONENT_MAXIMUM = 127;
        const UInt32 EXPONENT_MASK = 0xFF000000u;
        const int EXPONENT_OFFSET = 24;

        public static double Decode(UInt32 value)
        {
            double significand;
            double exponent;
            Int32 i32;

            /* handle numbers that are too big */
            if (ENCODED_MAXIMUM == value)
                return double.MaxValue;
            else if (ENCODED_MINIMUM == value)
                return -double.MaxValue;

            /* extract the exponent */
            i32 = (Int32) ((value & EXPONENT_MASK) >> EXPONENT_OFFSET);
            if (0 != (i32 & 0x80))
                i32 = (Int32)((UInt32)i32 | 0xFFFFFF00u);
            exponent = (double)i32;

            /* extract the significand */
            i32 = (Int32)(value & SIGNIFICAND_MASK);
            if (0 != (i32 & ENCODED_MINIMUM))
                i32 = (Int32)((UInt32)i32 | 0xFF000000u);
            significand = (double)i32 / FLOAT_MAXIMUM;

            /* calculate the floating point value */
            return significand * Math.Pow(2.0, exponent);
        }

        public static UInt32 Encode(double f)
        {
            double significand;
            UInt32 code;
            int exponent;

            /* check for zero values */
            significand = Math.Abs(f);
            if (FLOAT_MINIMUM > significand)
                return 0;

            /* normalize the number */
            exponent = 0;
            while (1.0 <= significand)
            {
                significand /= 2.0;
                exponent += 1;
            }
            while (0.5 > significand)
            {
                significand *= 2.0;
                exponent -= 1;
            }

            /* handle numbers that are too big */
            if (EXPONENT_MAXIMUM < exponent)
                return ENCODED_MAXIMUM;
            else if (EXPONENT_MINIMUM > exponent)
                return ENCODED_MINIMUM;

            /* pack the exponent and significand */
            code = (UInt32)(significand * FLOAT_MAXIMUM);
            if (0.0 > f)
                code = (UInt32)(-(Int32)code);
            code &= SIGNIFICAND_MASK;
            code |= ((UInt32)exponent &lt;&lt; EXPONENT_OFFSET) & EXPONENT_MASK;

            return code;
        }
    }
}
</pre>

## Example ##

<pre>
1E 15 F2 24 D2 54 A8 01 00 00 06 00 02 00 00 00
00 00 07 00 81 95 41 03 00 00 08 00 03 00 00 00
00 00 09 00 27 AA 0D 54 00 00 0D 00 25 00 01 01
00 00 10 00 00 00 80 E4 00 00 14 00 00 00 00 00
00 00 15 00 00 00 00 00 00 00 16 00 00 00 00 00
00 00 17 00 00 00 00 00 00 00 1A 00 02 00 00 00
00 00 1C 00 7D 01 00 00 00 00 1D 00 07 00 00 00
00 00 20 00 01 00 01 01 00 00 25 00 00 04 00 00
00 00 26 00 00 00 00 00 00 00 31 00 00 00 40 0C
00 00 32 00 37 89 41 05 00 00 33 00 07 3A 6D 03
00 00 37 00 00 00 40 09 00 00 39 00 AE 77 53 09
00 00 3A 00 00 00 54 05 01 00 00 00 00 00 00 00
01 00 01 00 44 D4 12 AF 01 00 02 00 14 01 00 00
01 00 03 00 07 00 00 00 01 00 04 00 49 FF FF FF
01 00 05 00 1A FF FF FF 01 00 06 00 52 FF FF FF
01 00 07 00 31 01 00 00 01 00 08 00 20 01 00 00
01 00 09 00 24 01 00 00 01 00 0A 00 1E 00 00 00
01 00 0C 00 E0 25 D2 54 01 00 0D 00 70 85 D3 54
01 00 0E 00 F2 24 D2 54 01 00 0F 00 44 00 00 00
01 00 10 00 1F 00 00 00 01 00 11 00 3F 00 00 00
01 00 14 00 00 00 00 00 01 00 15 00 00 00 00 00
01 00 21 00 60 EA 00 00 01 00 22 00 1E F8 FF FF
01 00 23 00 A7 F7 FF FF 01 00 24 00 DC F7 FF FF
01 00 25 00 1D 08 00 00 01 00 26 00 A4 07 00 00
01 00 27 00 00 08 00 00 01 00 28 00 00 00 00 00
01 00 29 00 00 00 00 00 01 00 2A 00 FE FF FF FF
01 00 2B 00 37 00 00 00 01 00 2C 00 00 00 00 00
9B
</pre>

<table>
    <tr>
        <th>Data</th>
        <th>Interpretation</th>
    <tr>
        <td>1E</td>
        <td>start of frame</td>
    </tr>
    <tr>
        <td>15</td>
        <td>record type (PARAMETERS)</td>
    </tr>
    <tr>
        <td>F2 24 D2 54</td>
        <td>Wed, 04 Feb 2015 13:56:02 GMT</td>
    </tr>
    <tr>
        <td>A8 01</td>
        <td>payload size (424 bytes)</td>
    </tr>
    <tr>
        <td>00 00 06 00 02 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 07 00 81 95 41 03</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 08 00 03 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 09 00 27 AA 0D 54</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 0D 00 25 00 01 01</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 10 00 00 00 80 E4</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 14 00 00 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 15 00 00 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 16 00 00 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 17 00 00 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 1A 00 02 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 1C 00 7D 01 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 1D 00 07 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 20 00 01 00 01 01</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 25 00 00 04 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 26 00 00 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 31 00 00 00 40 0C</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 32 00 37 89 41 05</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 33 00 07 3A 6D 03</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 37 00 00 00 40 09</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 39 00 AE 77 53 09</td>
        <td></td>
    </tr>
    <tr>
        <td>00 00 3A 00 00 00 54 05</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 00 00 00 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 01 00 44 D4 12 AF</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 02 00 14 01 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 03 00 07 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 04 00 49 FF FF FF</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 05 00 1A FF FF FF</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 06 00 52 FF FF FF</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 07 00 31 01 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 08 00 20 01 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 09 00 24 01 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 0A 00 1E 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 0C 00 E0 25 D2 54</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 0D 00 70 85 D3 54</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 0E 00 F2 24 D2 54</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 0F 00 44 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 10 00 1F 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 11 00 3F 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 14 00 00 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 15 00 00 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 21 00 60 EA 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 22 00 1E F8 FF FF</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 23 00 A7 F7 FF FF</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 24 00 DC F7 FF FF</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 25 00 1D 08 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 26 00 A4 07 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 27 00 00 08 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 28 00 00 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 29 00 00 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 2A 00 FE FF FF FF</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 2B 00 37 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>01 00 2C 00 00 00 00 00</td>
        <td></td>
    </tr>
    <tr>
        <td>9B</td>
        <td>checksum</td>
    </tr>
</table>

## Notes ##
<table>
    <tr>
        <th>Address Space</th>
        <th>Identifier</th>
        <th>Label</th>
        <th>Type</th>
        <th>Range</th>
        <th>Units</th>
        <th>Description</th>
    </tr>
<tr>
    <td>0</td>
    <td>6</td>
    <td>BATTERY_STATE</td>
    <td>int</td>
    <td>0 = BATTERY_CHARGINGÂ  Â  
1 = BATTERY_CHARGED
2 = BATTERY_NORMAL
3 = BATTERY_WARN
4 = BATTERY_SHUTDOWN
5 = BATTERY_FAULT</td>
    <td></td>
    <td>Returns the current state of the battery</td>
</tr>
<tr>
    <td>0</td>
    <td>7</td>
    <td>BATTERY_VOLTAGE</td>
    <td>float</td>
    <td>[0, 6]</td>
    <td>volts</td>
    <td>Returns the indicated ADC value in volts.</td>
</tr>
<tr>
    <td>0</td>
    <td>8</td>
    <td>BOARD_REVISION</td>
    <td>int</td>
    <td>[0,15]</td>
    <td></td>
    <td>Digital input reading from the hardware revision resistors.</td>
</tr>
<tr>
    <td>0</td>
    <td>9</td>
    <td>CALIBRATION_TIME</td>
    <td>int</td>
    <td></td>
    <td>seconds</td>
    <td></td>
</tr>
<tr>
    <td>0</td>
    <td>13</td>
    <td>FIRMWARE_VERSION</td>
    <td>int</td>
    <td></td>
    <td></td>
    <td>Firmware version number encoded as (major << 24) | (minor << 16) | build.</td>
</tr>
<tr>
    <td>0</td>
    <td>16</td>
    <td>MEMORY_SIZE</td>
    <td>int</td>
    <td></td>
    <td>bytes</td>
    <td>Maximum capacity of the NAND flash hardware not excluding possible bad blocks.</td>
</tr>
<tr>
    <td>0</td>
    <td>28</td>
    <td>FEATURE_CAPABILITIES</td>
    <td>int</td>
    <td>Bit 0 = Heart Rate Monitor,
Bit 1 = Data Summary,
Bit 2 = Sleep Mode,
Bit 3 = Proximity Tagging,
Bit 4 = Epoch Data,
Bit 5 = No Raw Data,
Bit 6 = IMU,
Bit 7 = Spare,
Bit 8 = Configurable Proximity Interval</td>
    <td></td>
    <td>Reports the supported features of this hardware/firmware configuration.</td>
</tr>
<tr>
    <td>0</td>
    <td>29</td>
    <td>DISPLAY_CAPABILITIES</td>
    <td>int</td>
    <td>Bit 0 = Display On/Off
Bit 1 = 12/24-hour Time
Bit 2 = Feedback On/Off
Bit 3 = kcals On/Off</td>
    <td></td>
    <td>Reports the supported LCD configurations.</td>
</tr>
<tr>
    <td>0</td>
    <td>32</td>
    <td>WIRELESS_FIRMWARE_VERSION</td>
    <td>int</td>
    <td></td>
    <td></td>
    <td>Firmware version number encoded as (major << 24) | (minor << 16) | build.</td>
</tr>
<tr>
    <td>0</td>
    <td>37</td>
    <td>WIRELESS_STATE</td>
    <td>int</td>
    <td>Bits 0 -> 7 (CC2541)
0 = Idle
1 = Central
2 = Peripheral
3 = Test
Bits 8 -> 15 (Atmel)
0 = Init
1 = Firmware Request
2 = Active
3 = Test
4 = Deep Sleep
5 = Peripheral Sleep
6 = Request Bootloader
7 = Bootloader</td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>0</td>
    <td>49</td>
    <td>IMU_ACCEL_SCALE</td>
    <td>float</td>
    <td></td>
    <td></td>
    <td>Scale factor for conversion to acceleration normalized to g.</td>
</tr>
<tr>
    <td>0</td>
    <td>50</td>
    <td>IMU_GYRO_SCALE</td>
    <td>float</td>
    <td></td>
    <td></td>
    <td>Scale factor for conversion to degrees/second.</td>
</tr>
<tr>
    <td>0</td>
    <td>51</td>
    <td>IMU_MAG_SCALE</td>
    <td>float</td>
    <td></td>
    <td></td>
    <td>Scale factor for conversion to microTesla.</td>
</tr>
<tr>
    <td>0</td>
    <td>55</td>
    <td>ACCEL_SCALE</td>
    <td>float</td>
    <td></td>
    <td></td>
    <td>Scale factor for conversion to primary acceleration normalized to g.</td>
</tr>
<tr>
    <td>0</td>
    <td>57</td>
    <td>IMU_TEMP_SCALE</td>
    <td>float</td>
    <td></td>
    <td></td>
    <td>Scale factor for conversion to temperature in Celsius.</td>
</tr>
<tr>
    <td>0</td>
    <td>58</td>
    <td>IMU_TEMP_OFFSET</td>
    <td>float</td>
    <td></td>
    <td></td>
    <td>Offset for temperature in Celsius.</td>
</tr>
<tr>
    <td>1</td>
    <td>0</td>
    <td>WIRELESS_MODE</td>
    <td>int</td>
    <td>0 = Disabled,
1 = Central,
2 = Peripheral</td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>1</td>
    <td>1</td>
    <td>WIRELESS_SERIAL_NUMBER</td>
    <td>int</td>
    <td>[1, 4294967295]</td>
    <td></td>
    <td>Serial number for wireless identification.</td>
</tr>
<tr>
    <td>1</td>
    <td>2</td>
    <td>FEATURE_ENABLE</td>
    <td>int</td>
    <td>Bit 0 = Heart Rate Monitor,
Bit 1 = Data Summary,
Bit 2 = Sleep Mode,
Bit 3 = Proximity Tagging,
Bit 4 = Epoch Data,
Bit 5 = No Raw Data</td>
    <td></td>
    <td>Enables or disables various features.</td>
</tr>
<tr>
    <td>1</td>
    <td>3</td>
    <td>DISPLAY_CONFIGURATION</td>
    <td>int</td>
    <td>Bit 0 = Display On/Off (0=Off, 1=On)
Bit 1 = 12/24-hour Time (0=12, 1=24)
Bit 2 = Feedback On/Off (0=Off, 1=On)
Bit 3 = kcals On/Off (0=Off, 1=On)</td>
    <td></td>
    <td>Bit-flags for configuring LCD behavior in various modes.</td>
</tr>
<tr>
    <td>1</td>
    <td>4</td>
    <td>NEGATIVE_G_OFFSET_X</td>
    <td>int</td>
    <td>[-2048, 2047]</td>
    <td></td>
    <td>X-axis -1 G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>5</td>
    <td>NEGATIVE_G_OFFSET_Y</td>
    <td>int</td>
    <td>[-2048, 2047]</td>
    <td></td>
    <td>Y-axis -1 G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>6</td>
    <td>NEGATIVE_G_OFFSET_Z</td>
    <td>int</td>
    <td>[-2048, 2047]</td>
    <td></td>
    <td>Z-axis -1 G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>7</td>
    <td>POSITIVE_G_OFFSET_X</td>
    <td>int</td>
    <td>[-2048, 2047]</td>
    <td></td>
    <td>X-axis +1 G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>8</td>
    <td>POSITIVE_G_OFFSET_Y</td>
    <td>int</td>
    <td>[-2048, 2047]</td>
    <td></td>
    <td>Y-axis +1 G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>9</td>
    <td>POSITIVE_G_OFFSET_Z</td>
    <td>int</td>
    <td>[-2048, 2047]</td>
    <td></td>
    <td>Z-axis +1 G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>10</td>
    <td>SAMPLE_RATE</td>
    <td>int</td>
    <td></td>
    <td>Hz</td>
    <td>30, 40, 50, 60, 70, 80, 90 or 100 Hz</td>
</tr>
<tr>
    <td>1</td>
    <td>12</td>
    <td>TARGET_START_TIME</td>
    <td>int</td>
    <td></td>
    <td>seconds</td>
    <td>Desired start of data in POSIX time format</td>
</tr>
<tr>
    <td>1</td>
    <td>13</td>
    <td>TARGET_STOP_TIME</td>
    <td>int</td>
    <td></td>
    <td>seconds</td>
    <td>Desired end of data in POSIX time format or zero if no stop time is desired.</td>
</tr>
<tr>
    <td>1</td>
    <td>14</td>
    <td>TIME_OF_DAY</td>
    <td>int</td>
    <td></td>
    <td>seconds</td>
    <td>Current date/time in POSIX time format</td>
</tr>
<tr>
    <td>1</td>
    <td>15</td>
    <td>ZERO_G_OFFSET_X</td>
    <td>int</td>
    <td>[-2048, 2047]</td>
    <td></td>
    <td>X-axis zero-G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>16</td>
    <td>ZERO_G_OFFSET_Y</td>
    <td>int</td>
    <td>[-2048, 2047]</td>
    <td></td>
    <td>Y-axis zero-G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>17</td>
    <td>ZERO_G_OFFSET_Z</td>
    <td>int</td>
    <td>[-2048, 2047]</td>
    <td></td>
    <td>Z-axis zero-G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>20</td>
    <td>HRM_SERIAL_NUMBER_H</td>
    <td>int</td>
    <td>Ex. Serial = "25894813" H = "2589"</td>
    <td></td>
    <td>Contains the high 4 bytes of the HRM serial number stored in little endian.</td>
</tr>
<tr>
    <td>1</td>
    <td>21</td>
    <td>HRM_SERIAL_NUMBER_L</td>
    <td>int</td>
    <td>Ex. Serial = "25894813" L = "4813"</td>
    <td></td>
    <td>Contains the low 4 bytes of the HRM serial number stored in little endian.</td>
</tr>
<tr>
    <td>1</td>
    <td>33</td>
    <td>PROXIMITY_INTERVAL</td>
    <td>int</td>
    <td></td>
    <td>milliseconds</td>
    <td>Interval in seconds for wireless proximity detection.</td>
</tr>
<tr>
    <td>1</td>
    <td>34</td>
    <td>IMU_NEGATIVE_G_OFFSET_X</td>
    <td>int</td>
    <td>[-16384, 16383]</td>
    <td></td>
    <td>IMU X-axis -1 G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>35</td>
    <td>IMU_NEGATIVE_G_OFFSET_Y</td>
    <td>int</td>
    <td>[-16384, 16383]</td>
    <td></td>
    <td>IMU Y-axis -1 G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>36</td>
    <td>IMU_NEGATIVE_G_OFFSET_Z</td>
    <td>int</td>
    <td>[-16384, 16383]</td>
    <td></td>
    <td>IMU Z-axis -1 G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>37</td>
    <td>IMU_POSITIVE_G_OFFSET_X</td>
    <td>int</td>
    <td>[-16384, 16383]</td>
    <td></td>
    <td>IMU X-axis +1 G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>38</td>
    <td>IMU_POSITIVE_G_OFFSET_Y</td>
    <td>int</td>
    <td>[-16384, 16383]</td>
    <td></td>
    <td>IMU Y-axis +1 G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>39</td>
    <td>IMU_POSITIVE_G_OFFSET_Z</td>
    <td>int</td>
    <td>[-16384, 16383]</td>
    <td></td>
    <td>IMU Z-axis +1 G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>40</td>
    <td>UTC_OFFSET</td>
    <td>int</td>
    <td>[-43200, 50400]</td>
    <td>seconds</td>
    <td>Local time offset from UTC in seconds</td>
</tr>
<tr>
    <td>1</td>
    <td>41</td>
    <td>IMU_ZERO_G_OFFSET_X</td>
    <td>int</td>
    <td>[-16384, 16383]</td>
    <td></td>
    <td>IMU X-axis zero-G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>42</td>
    <td>IMU_ZERO_G_OFFSET_Y</td>
    <td>int</td>
    <td>[-16384, 16383]</td>
    <td></td>
    <td>IMU Y-axis zero-G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>43</td>
    <td>IMU_ZERO_G_OFFSET_Z</td>
    <td>int</td>
    <td>[-16384, 16383]</td>
    <td></td>
    <td>IMU Z-axis zero-G offset calibration constant</td>
</tr>
<tr>
    <td>1</td>
    <td>44</td>
    <td>SENSOR_CONFIGURATION</td>
    <td>int</td>
    <td>Bit 0 = IMU Accelerometer,
Bit 1 = IMU Gyroscope,
Bit 2 = IMU Magnetometer,
Bit 3 = IMU Temperature</td>
    <td></td>
    <td>Enables or disables auxiliary sensors.</td>
</tr>
</table>
