
import struct
import math


def plainSum():
	with open('./mountain-spring.bmp', 'rb') as fp:
	    total = nancount = 0
	    b = fp.read(8)
	    while len(b) == 8:
	    	v = struct.unpack('d', b)[0]
	    	if math.isnan(v):
	    		nancount += 1
	    	else:
	    		v = v - 10e4 * math.floor(v / 10e4)
	    		total += v # % 10e4
	    	b = fp.read(8)

	return total, nancount


def numpySum():
	
	import numpy  # please don't do local-scope imports like this.

	a = numpy.fromfile('./mountain-spring.bmp', dtype='float64')
	nanidx = numpy.isnan(a)
	nancount = len(a[nanidx])
	nonans = a[~nanidx]
	return numpy.sum(nonans - 10e4 * numpy.floor(nonans / 10e4)), nancount


if __name__ == '__main__':
	#print plainSum()
	print numpySum()
