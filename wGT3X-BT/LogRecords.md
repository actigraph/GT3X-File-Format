# wGT3X-BT Log Records #

### List of Devices that Use these Records ###

* wGT3X-BT with serial numbers {BLAH}
* wActiSleep-BT with serial numbers {BLAH}

<table>
   <tr>
      <th>ID</th>
      <th>Type</th>
      <th>Description</th>
   </tr>
   <tr>
      <td>0</td>
      <td><a href=LogRecords/Activity.md>ACTIVITY</a></td>
      <td>One second of raw activity samples packed into 12-bit values in YXZ order</td>
   </tr>
   <tr>
      <td>1</td>
      <td><a href=LogRecords/AntPlus.md>ANT_PLUS</a></td>
      <td></td>
   </tr>
   <tr>
      <td>2</td>
      <td><a href=LogRecords/Battery.md>BATTERY</a></td>
      <td>Battery voltage</td>
   </tr>
   <tr>
      <td>3</td>
      <td><a href=LogRecords/Event.md>EVENT</a></td>
      <td>0 = RTT Overflow, 1 = Unexpected Reset, 2 = Unhandled Event</td>
   </tr>
   <tr>
      <td>4</td>
      <td><a href=LogRecords/HeartRateBPM.md>HEART_RATE_BPM</a></td>
      <td></td>
   </tr>
   <tr>
      <td>5</td>
      <td><a href=LogRecords/Lux.md>LUX</a></td>
      <td>Lux</td>
   </tr>
   <tr>
      <td>6</td>
      <td><a href=LogRecords/Metadata.md>METADATA</a></td>
      <td>Arbitrary metadata content</td>
   </tr>
   <tr>
      <td>7</td>
      <td><a href=LogRecords/Tag.md>TAG</a></td>
      <td>13 Byte Serial, 1 Byte Tx Power, 1 Byte (signed) RSSI</td>
   </tr>
   <tr>
      <td>8</td>
      <td><a href=LogRecords/Temperature.md>TEMPERATURE</a></td>
      <td></td>
   </tr>
   <tr>
      <td>9</td>
      <td><a href=LogRecords/Epoch.md>EPOCH</a></td>
      <td></td>
   </tr>
   <tr>
      <td>10</td>
      <td><a href=LogRecords/DailySummary.md>DAILY_SUMMARY</a></td>
      <td></td>
   </tr>
   <tr>
      <td>11</td>
      <td><a href=LogRecords/HeartRateAnt.md>HEART_RATE_ANT</a></td>
      <td></td>
   </tr>
   <tr>
      <td>12</td>
      <td><a href=LogRecords/Epoch2.md>EPOCH2</a></td>
      <td>Cletus & Moses epoch data</td>
   </tr>
   <tr>
      <td>13</td>
      <td><a href=LogRecords/Capsense.md>CAPSENSE</a></td>
      <td>Capacitive sense data</td>
   </tr>
   <tr>
      <td>14</td>
      <td><a href=LogRecords/HeartRateBLE.md>HEART_RATE_BLE</a></td>
      <td>Bluetooth heart rate information (BPM and RR)</td>
   </tr>
   <tr>
      <td>15</td>
      <td><a href=LogRecords/Epoch3.md>EPOCH3</a></td>
      <td>Moses epoch data</td>
   </tr>
   <tr>
      <td>16</td>
      <td><a href=LogRecords/Epoch4.md>EPOCH4</a></td>
      <td>Taso epoch data</td>
   </tr>
   <tr>
      <td>17</td>
      <td><a href=LogRecords/IMU.md>IMU</a></td>
      <td>One second of raw IMU data (acceleration and gyroscope in that order) in XYZ order as 16-bit signed integers</td>
   </tr>
   <tr>
      <td>18</td>
      <td><a href=LogRecords/Magnetometer.md>MAGNETOMETER</a></td>
      <td>One second of raw magnetometer data as 16-bit signed integers</td>
   </tr>
   <tr>
      <td>19</td>
      <td><a href=LogRecords/FifoError.md>FIFO_ERROR</a></td>
      <td>Records timestamp of Fifo Errors</td>
   </tr>
   <tr>
      <td>20</td>
      <td><a href=LogRecords/FifoDump.md>FIFO_DUMP</a></td>
      <td>FIFO diagnostic record recorded if enabled and an error is detected</td>
   </tr>
   <tr>
      <td>21</td>
      <td><a href=LogRecords/Parameters.md>PARAMETERS</a></td>
      <td>Records various configuration parameters and device attributes on initialization.</td>
   </tr>
</table>