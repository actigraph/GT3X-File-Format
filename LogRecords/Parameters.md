# PARAMETERS Packet - ID 21 #

## Description ##
The PARAMETERS record is written during initialization of the device, and it should appear just after the METADATA record. It contains a list of key/value pairs that describe the initialization parameters of the device and various other device conditions of interest at the time of initialization.

The content of this record may vary in number and types of variables. It is safe to ignore any variables that have an unknown key. Some variables are included for diagnostic purposes that are unnecessary for interpreting other log data.

## Format of Data ##
The record payload is of variable length consisting of 8-byte key/value pairs. The key is made up of a 16-bit unsigned address space and 16-bit unsigned identifier. All values are encoded in a 32-bit unsigned integer. The address space, identifier and value are in little-endian byte order.


## Example ##

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


<td>0</td>
<td>6</td>
<td>BATTERY_STATE</td>
<td>int</td>
<td>0 = BATTERY_CHARGING    
1 = BATTERY_CHARGED
2 = BATTERY_NORMAL
3 = BATTERY_WARN
4 = BATTERY_SHUTDOWN
5 = BATTERY_FAULT</td>
<td></td>
<td>Returns the current state of the battery</td>


<td>0</td>
<td>7</td>
<td>BATTERY_VOLTAGE</td>
<td>float</td>
<td>[0, 6]</td>
<td>volts</td>
<td>Returns the indicated ADC value in volts.</td>


<td>0</td>
<td>8</td>
<td>BOARD_REVISION</td>
<td>int</td>
<td>[0,15]</td>
<td></td>
<td>Digital input reading from the hardware revision resistors.</td>


<td>0</td>
<td>9</td>
<td>CALIBRATION_TIME</td>
<td>int</td>
<td></td>
<td>seconds</td>
<td></td>


<td>0</td>
<td>13</td>
<td>FIRMWARE_VERSION</td>
<td>int</td>
<td></td>
<td></td>
<td>Firmware version number encoded as (major << 24) | (minor << 16) | build.</td>


<td>0</td>
<td>16</td>
<td>MEMORY_SIZE</td>
<td>int</td>
<td></td>
<td>bytes</td>
<td>Maximum capacity of the NAND flash hardware not excluding possible bad blocks.</td>


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


<td>0</td>
<td>32</td>
<td>WIRELESS_FIRMWARE_VERSION</td>
<td>int</td>
<td></td>
<td></td>
<td>Firmware version number encoded as (major << 24) | (minor << 16) | build.</td>


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


<td>0</td>
<td>49</td>
<td>IMU_ACCEL_SCALE</td>
<td>float</td>
<td></td>
<td></td>
<td>Scale factor for conversion to acceleration normalized to g.</td>


<td>0</td>
<td>50</td>
<td>IMU_GYRO_SCALE</td>
<td>float</td>
<td></td>
<td></td>
<td>Scale factor for conversion to degrees/second.</td>


<td>0</td>
<td>51</td>
<td>IMU_MAG_SCALE</td>
<td>float</td>
<td></td>
<td></td>
<td>Scale factor for conversion to microTesla.</td>


<td>0</td>
<td>55</td>
<td>ACCEL_SCALE</td>
<td>float</td>
<td></td>
<td></td>
<td>Scale factor for conversion to primary acceleration normalized to g.</td>


<td>0</td>
<td>57</td>
<td>IMU_TEMP_SCALE</td>
<td>float</td>
<td></td>
<td></td>
<td>Scale factor for conversion to temperature in Celsius.</td>


<td>0</td>
<td>58</td>
<td>IMU_TEMP_OFFSET</td>
<td>float</td>
<td></td>
<td></td>
<td>Offset for temperature in Celsius.</td>


<td>1</td>
<td>0</td>
<td>WIRELESS_MODE</td>
<td>int</td>
<td>0 = Disabled,
1 = Central,
2 = Peripheral</td>
<td></td>
<td></td>


<td>1</td>
<td>1</td>
<td>WIRELESS_SERIAL_NUMBER</td>
<td>int</td>
<td>[1, 4294967295]</td>
<td></td>
<td>Serial number for wireless identification.</td>


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


<td>1</td>
<td>4</td>
<td>NEGATIVE_G_OFFSET_X</td>
<td>int</td>
<td>[-2048, 2047]</td>
<td></td>
<td>X-axis -1 G offset calibration constant</td>


<td>1</td>
<td>5</td>
<td>NEGATIVE_G_OFFSET_Y</td>
<td>int</td>
<td>[-2048, 2047]</td>
<td></td>
<td>Y-axis -1 G offset calibration constant</td>


<td>1</td>
<td>6</td>
<td>NEGATIVE_G_OFFSET_Z</td>
<td>int</td>
<td>[-2048, 2047]</td>
<td></td>
<td>Z-axis -1 G offset calibration constant</td>


<td>1</td>
<td>7</td>
<td>POSITIVE_G_OFFSET_X</td>
<td>int</td>
<td>[-2048, 2047]</td>
<td></td>
<td>X-axis +1 G offset calibration constant</td>


<td>1</td>
<td>8</td>
<td>POSITIVE_G_OFFSET_Y</td>
<td>int</td>
<td>[-2048, 2047]</td>
<td></td>
<td>Y-axis +1 G offset calibration constant</td>


<td>1</td>
<td>9</td>
<td>POSITIVE_G_OFFSET_Z</td>
<td>int</td>
<td>[-2048, 2047]</td>
<td></td>
<td>Z-axis +1 G offset calibration constant</td>


<td>1</td>
<td>10</td>
<td>SAMPLE_RATE</td>
<td>int</td>
<td></td>
<td>Hz</td>
<td>30, 40, 50, 60, 70, 80, 90 or 100 Hz</td>


<td>1</td>
<td>12</td>
<td>TARGET_START_TIME</td>
<td>int</td>
<td></td>
<td>seconds</td>
<td>Desired start of data in POSIX time format</td>


<td>1</td>
<td>13</td>
<td>TARGET_STOP_TIME</td>
<td>int</td>
<td></td>
<td>seconds</td>
<td>Desired end of data in POSIX time format or zero if no stop time is desired.</td>


<td>1</td>
<td>14</td>
<td>TIME_OF_DAY</td>
<td>int</td>
<td></td>
<td>seconds</td>
<td>Current date/time in POSIX time format</td>


<td>1</td>
<td>15</td>
<td>ZERO_G_OFFSET_X</td>
<td>int</td>
<td>[-2048, 2047]</td>
<td></td>
<td>X-axis zero-G offset calibration constant</td>


<td>1</td>
<td>16</td>
<td>ZERO_G_OFFSET_Y</td>
<td>int</td>
<td>[-2048, 2047]</td>
<td></td>
<td>Y-axis zero-G offset calibration constant</td>


<td>1</td>
<td>17</td>
<td>ZERO_G_OFFSET_Z</td>
<td>int</td>
<td>[-2048, 2047]</td>
<td></td>
<td>Z-axis zero-G offset calibration constant</td>


<td>1</td>
<td>20</td>
<td>HRM_SERIAL_NUMBER_H</td>
<td>int</td>
<td>Ex. Serial = "25894813" H = "2589"</td>
<td></td>
<td>Contains the high 4 bytes of the HRM serial number stored in little endian.</td>


<td>1</td>
<td>21</td>
<td>HRM_SERIAL_NUMBER_L</td>
<td>int</td>
<td>Ex. Serial = "25894813" L = "4813"</td>
<td></td>
<td>Contains the low 4 bytes of the HRM serial number stored in little endian.</td>


<td>1</td>
<td>33</td>
<td>PROXIMITY_INTERVAL</td>
<td>int</td>
<td></td>
<td>milliseconds</td>
<td>Interval in seconds for wireless proximity detection.</td>


<td>1</td>
<td>34</td>
<td>IMU_NEGATIVE_G_OFFSET_X</td>
<td>int</td>
<td>[-16384, 16383]</td>
<td></td>
<td>IMU X-axis -1 G offset calibration constant</td>


<td>1</td>
<td>35</td>
<td>IMU_NEGATIVE_G_OFFSET_Y</td>
<td>int</td>
<td>[-16384, 16383]</td>
<td></td>
<td>IMU Y-axis -1 G offset calibration constant</td>


<td>1</td>
<td>36</td>
<td>IMU_NEGATIVE_G_OFFSET_Z</td>
<td>int</td>
<td>[-16384, 16383]</td>
<td></td>
<td>IMU Z-axis -1 G offset calibration constant</td>


<td>1</td>
<td>37</td>
<td>IMU_POSITIVE_G_OFFSET_X</td>
<td>int</td>
<td>[-16384, 16383]</td>
<td></td>
<td>IMU X-axis +1 G offset calibration constant</td>


<td>1</td>
<td>38</td>
<td>IMU_POSITIVE_G_OFFSET_Y</td>
<td>int</td>
<td>[-16384, 16383]</td>
<td></td>
<td>IMU Y-axis +1 G offset calibration constant</td>


<td>1</td>
<td>39</td>
<td>IMU_POSITIVE_G_OFFSET_Z</td>
<td>int</td>
<td>[-16384, 16383]</td>
<td></td>
<td>IMU Z-axis +1 G offset calibration constant</td>


<td>1</td>
<td>40</td>
<td>UTC_OFFSET</td>
<td>int</td>
<td>[-43200, 50400]</td>
<td>seconds</td>
<td>Local time offset from UTC in seconds</td>


<td>1</td>
<td>41</td>
<td>IMU_ZERO_G_OFFSET_X</td>
<td>int</td>
<td>[-16384, 16383]</td>
<td></td>
<td>IMU X-axis zero-G offset calibration constant</td>


<td>1</td>
<td>42</td>
<td>IMU_ZERO_G_OFFSET_Y</td>
<td>int</td>
<td>[-16384, 16383]</td>
<td></td>
<td>IMU Y-axis zero-G offset calibration constant</td>


<td>1</td>
<td>43</td>
<td>IMU_ZERO_G_OFFSET_Z</td>
<td>int</td>
<td>[-16384, 16383]</td>
<td></td>
<td>IMU Z-axis zero-G offset calibration constant</td>


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

</table>
