#!/usr/bin/python

"""
Creates a large number of random files in a specific directory and calculates 
how long it takes to write and read the files. This is designed for testing 
local read/write times versus filer read/write times.
"""
import os
import random
import string
import time

loc = raw_input("Where do you want to perform the read/write?: ")
toss = raw_input("Do you want to delete the files?[y/n]: ")

start_time = time.time()

for i in range(1, 101):
        digits = "".join( [random.choice(string.digits) for y in xrange(8)] )
        chars = "".join( [random.choice(string.letters) for y in xrange(15)] )
        theFile = "%s/%i" % (loc, i)
        myFile = file("%s/%i" % (loc, i), 'w')
        print >> myFile, (digits + chars)

for i in range(1, 101):
        f = open('%s/%i' % (loc, i), 'r')
        data = f.read()
        print data

print time.time() - start_time, "seconds"

if toss == "y":
	for i in range(1, 101):
		os.remove('%s/%i' % (loc, i))
	print("cleaned %s of all files" % (loc))
exit()
