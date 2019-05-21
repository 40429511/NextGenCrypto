# implementation is a translation of the pseudocode
# specified in RFC7748: https://tools.ietf.org/html/rfc7748
# 
# libraries required for implementation
from os import urandom
from eccsnacks.curve25519 import scalarmult, scalarmult_base
import binascii

# (l) is a random selected point for Reader RFID
l = urandom(32)
a = scalarmult_base(l)

# (e) is a random seclected point for RFID tag
e = urandom(32)
b = scalarmult_base(e)

# reference points defined by the scalar multiplication from the elliptic curve
c = scalarmult(e, a)
d = scalarmult(l, b)

# Reader RFID and RFID tag private key values
print "RFID private key: ",binascii.hexlify(e)
print "Reader private key: ",binascii.hexlify(l)

# printing value of A and B in function of (a) and (b) with the Binary ASCII 
print "A value: ",binascii.hexlify(a)
print "B value: ",binascii.hexlify(b)

# printing value of A and B in function of (c) and (d) with the Binary ASCII
print "C value: ",binascii.hexlify(c)
print "D value: ",binascii.hexlify(d)

# Check that C is equal to D,
or compare the shared keys value at A and B 
