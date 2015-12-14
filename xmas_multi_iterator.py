#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time,xmas

if __name__ == '__main__':
	it = 1000
	e = 0
	for i in range(0,it):
		t = time.time()
		a = xmas.run()
		e += time.time() - t

	sys.stdout.write(str('%s\n%iµs\n' % (a, (e/it) * 1000000)))