#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time
  
def dedupe(i): return len(set(str(i))) == 3
def strip(p, i, l):
	rl = []
	for li in l:
		if i == str(li)[p]:
			rl.append(li)
	return rl
def run():
	jm = map(str, filter(dedupe, range(124,962,31)))
	for a in filter(dedupe, range(120,980,30)):
		l = list(str(a))
		for m in strip(1,l[0], jm):
			if not (l[0] != m[1] or m[0] in l or m[2] in l):
				l.extend([m[0], m[2]])
				for j in strip(1,l[0], jm):
					if not (l[0] != j[1] or j[0] in l or j[2] in l):
						l.extend([j[0], j[2]])
						for f in range(140,980,28):
							sf = str(f)
							if not (sf[0] in l or sf[1] in l or sf[2] in l):
								return [sf[0], sf[1], sf[2]]

if __name__ == '__main__':
	it = 1000
	e = 0
	for i in range(0,it):
		t = time.time()
		a = ''.join(run())
		e += time.time() - t

	sys.stdout.write(str('%s\n%iµs\n' % (a, round((e/it) * 1000000))))