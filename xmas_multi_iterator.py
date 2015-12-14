#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time

def elim28(i): return (i % 28 == 0) 
def elim30(i): return (i % 30 == 0)  
def elim31(i): return (i % 31 == 0)  
def dedupe(i): return len(set(str(i))) == 3
def strip(p, i, l):
	rl = []
	for li in l:
		if str(li)[p] == i:
			rl.append(li)
	return rl
def run():
	jm = filter(dedupe, filter(elim31, range(124,962,31)))
	for a in filter(dedupe, filter(elim30, range(120,980,30))):
		l = []
		l.extend(str(a))
		for m in strip(1,l[0], jm):
			sm = str(m)
			if not (l[0] != sm[1] or sm[0] in l or sm[2] in l):
				l.extend([sm[0], sm[2]])
				for j in strip(1,l[0], jm):
					sj = str(j)
					if not (l[0] != sj[1] or sj[0] in l or sj[2] in l):
						l.extend([sj[0], sj[2]])
						for f in filter(elim28, range(140,980,28)):
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