# PassPattern
reverse hash matcher to determine how weak passwords were generated

# What it does

This is just a simple script that accepts a key and a hash (or part of one) and then attempts to determine what hash funciton produced the hash.

The motivation for this is from the university apartment I'm staying in, which gave residents a wifi username and password.  The password was clearly a Base64 hash of some kind.  I figured perhaps they were just being lazy and hashing the username.  This script is the result -- I just give it the username and password and it hashes the username a whole bunch of different ways and checks to see if any of the results match the actual password.
