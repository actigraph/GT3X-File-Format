from struct import pack

sn = 'TAS0C32140026'
tx = 0
rssi = -42

buf = pack('13sBb', sn, tx, rssi)

s = None
for b in buf:
    if s:
        s += ' %02X' % ord(b)
    else:
        s = '%02X' % ord(b)

print s
