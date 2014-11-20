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
      <td>ACTIVITY</td>
      <td>One second of raw activity samples packed into 12-bit values in YXZ order</td>
   </tr>
   <tr>
      <td>1</td>
      <td>ANT_PLUS</td>
      <td></td>
   </tr>
   <tr>
      <td>2</td>
      <td>BATTERY</td>
      <td>Battery voltage</td>
   </tr>
   <tr>
      <td>3</td>
      <td>EVENT</td>
      <td>0 = RTT Overflow, 1 = Unexpected Reset, 2 = Unhandled Event</td>
   </tr>
   <tr>
      <td>4</td>
      <td>HEART_RATE_BPM</td>
      <td></td>
   </tr>
   <tr>
      <td>5</td>
      <td>LUX</td>
      <td>Lux</td>
   </tr>
   <tr>
      <td>6</td>
      <td>METADATA</td>
      <td>Arbitrary metadata content</td>
   </tr>
   <tr>
      <td>7</td>
      <td>TAG</td>
      <td>13 Byte Serial, 1 Byte Tx Power, 1 Byte (signed) RSSI</td>
   </tr>
   <tr>
      <td>8</td>
      <td>TEMPERATURE</td>
      <td></td>
   </tr>
   <tr>
      <td>9</td>
      <td>EPOCH</td>
      <td></td>
   </tr>
   <tr>
      <td>10</td>
      <td>DAILY_SUMMARY</td>
      <td></td>
   </tr>
   <tr>
      <td>11</td>
      <td>HEART_RATE_ANT</td>
      <td></td>
   </tr>
   <tr>
      <td>12</td>
      <td>EPOCH2</td>
      <td>Cletus & Moses epoch data</td>
   </tr>
   <tr>
      <td>13</td>
      <td>CAPSENSE</td>
      <td>Capacitive sense data</td>
   </tr>
   <tr>
      <td>14</td>
      <td>HEART_RATE_BLE</td>
      <td>Bluetooth heart rate information (BPM and RR)</td>
   </tr>
   <tr>
      <td>15</td>
      <td>EPOCH3</td>
      <td>Moses epoch data</td>
   </tr>
   <tr>
      <td>16</td>
      <td>EPOCH4</td>
      <td>Taso epoch data</td>
   </tr>
   <tr>
      <td>17</td>
      <td>IMU</td>
      <td>One second of raw IMU data (acceleration and gyroscope in that order) in XYZ order as 16-bit signed integers</td>
   </tr>
   <tr>
      <td>18</td>
      <td>MAGNETOMETER</td>
      <td>One second of raw magnetometer data as 16-bit signed integers</td>
   </tr>
   <tr>
      <td>19</td>
      <td>FIFO_ERROR</td>
      <td>Records timestamp of Fifo Errors</td>
   </tr>
   <tr>
      <td>20</td>
      <td>FIFO_DUMP</td>
      <td>FIFO diagnostic record recorded if enabled and an error is detected</td>
   </tr>
   <tr>
      <td>21</td>
      <td>PARAMETERS</td>
      <td>Records various configuration parameters and device attributes on initialization.</td>
   </tr>
</table>