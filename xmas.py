#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time
def dedupe(i): 
	i = str(i)
	return not (i[0] == i[1] or i[0] == i[2] or i[1] == i[2])
def strip(p, i, l):
	rl = []
	for li in l:
		if i == li[p]:
			rl.append(li)
	return rl
def run():
	jm = map(str, filter(dedupe, range(124,962,31)))
	for a in map(str, filter(dedupe, range(120,980,30))):
		l = list(a)
		for m in strip(1,l[0], jm):
			if not (l[0] != m[1] or m[0] in l or m[2] in l):
				l.extend([m[0], m[2]])
				for j in strip(1,l[0], jm):
					if not (l[0] != j[1] or j[0] in l or j[2] in l):
						l.extend([j[0], j[2]])
						for f in map(str,range(140,980,28)):
							if not (f[0] in l or f[1] in l or f[2] in l):
								return ''.join([f[0], f[1], f[2]])

if __name__ == '__main__':
	t = time.time()
	a = run()
	e = time.time() - t

	sys.stdout.write(str('%s\n%iµs\n' % (a, e * 1000000)))