# EPOCH4 Packet - ID 16 #

## Description ##
60 Second Epoch Data

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
        <td>2</td>
        <td>X Counts</td>
        <td>Total counts over epoch for x-axis.</td>
    </tr>
    <tr>
        <td>2</td>
        <td>2</td>
        <td>Y Counts</td>
        <td>Total counts over epoch for y-axis.</td>
    </tr>
    <tr>
        <td>4</td>
        <td>2</td>
        <td>Z Counts</td>
        <td>Total counts over epoch for z-axis.</td>
    </tr>
    <tr>
        <td>6</td>
        <td>1</td>
        <td>Steps</td>
        <td>Total steps over epoch</td>
    </tr>
    <tr>
        <td>7</td>
        <td>1</td>
        <td>Heart Rate</td>
        <td>Average BPM over epoch.</td>
    </tr>
    <tr>
        <td>8</td>
        <td>1</td>
        <td>Wear Detection</td>
        <td>0=not worn, 1=worn, 2=calibrating, 3=plugged into USB (0, 2 &3 are non-wear values)</td>
    </tr>
</table>