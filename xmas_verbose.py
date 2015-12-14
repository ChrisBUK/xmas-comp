#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time

def elim28(i): 
	''' a custom method for filter() to remove any numbers from a list that aren't divisible by 28 '''
	''' it's faster to have a separate method for the three divisors than roll it into one single one '''
	return (i % 28 == 0) 

def elim30(i): 
	''' a custom method for filter() to remove any numbers from a list that aren't divisible by 30 '''
	return (i % 30 == 0)  

def elim31(i): 
	''' a custom method for filter() to remove any numbers from a list that aren't divisible by 31 '''
	return (i % 31 == 0)  

def dedupe(i): 
	''' a custom method for filter() to eliminate any three digit numbers where two of the digits are identical '''
	''' it's faster to generate a set and check length than it is just to compare 0 with 1, 0 with 2, and 1 with 2. '''
	return len(set(str(i))) == 3

def strip(pos, value, listobj):
	''' a method to filter down a list to only contain items where [item] appears in [pos] of each member of [listobj] '''
	''' There may be further gains to be made here, but nothing else I tried generated good results ''' 
	return_list = []
	for item in listobj:
		if str(item)[pos] == value:
			return_list.append(item)
	return return_list

def run():
	''' the job runner, this does all of the calculation '''

	''' 
	we want all the possible numbers than can represent january/may. We calculate this list here because we use it 
	twice and its cheaper to only calculate it once.

	The dedupe and elim methods used in the filter make sure we're not including numbers in the list that would break the rules
	of the task (ie, not divisible, non unique)
	'''

	jm = filter(dedupe, filter(elim31, range(124,962,31)))
	

	'''
	because we know that in APR, r=0 and its important to know what values A can be for when we come to JAN/MAY, we start to 
	iterate through it, again using the filters to remove any numbers that we can be sure are not valid.

	The range used represents the lowest possible divisible number and the highest possible divisible number that are still 3 digits.
	'''
	for a in filter(dedupe, filter(elim30, range(120,980,30))):

		''' we build a list whose first three members represent A, P and R. It's faster than using a dictionary object to key the values '''
		l = []
		l.extend(str(a))

		'''
		Now we iterate the values for MAY for each iteration of APR - but we only try numbers where 'A' represents the only number it can be from APR
		as looping is expensive.
		'''
		for m in strip(1,l[0], jm):
			sm = str(m)

			''' 
			We want to add to the list when we have a number that satisfies the rules of the contest.
			It's more efficient to check that things are NOT something OR something else, than it is to check that things are something AND something else
			because with OR, if the first check fails, we don't even need to compute the ones after.
			'''
			
			if not (l[0] != sm[1] or sm[0] in l or sm[2] in l):
				l.extend([sm[0], sm[2]])

				''' We've added more numbers to our list, so that means we're on the right track, and should try to calculate JAN. '''
				for j in strip(1,l[0], jm):
					sj = str(j)
					if not (l[0] != sj[1] or sj[0] in l or sj[2] in l):
						l.extend([sj[0], sj[2]])

						''' 
						To be here, our list must now contain valid numbers representing APR, MAY and JAN 
						We should filter down the candidates for FEB as much as we can, and then iterate them.
						'''
						for f in filter(elim28, range(140,980,28)):
							sf = str(f)

							''' If we find a match here that passes all the rules, this must be the answer. Stop immediately! '''
							if not (sf[0] in l or sf[1] in l or sf[2] in l):
								return [sf[0], sf[1], sf[2]]

if __name__ == '__main__':

	''' Let's only measure execution time for execution, not parsing. The gains are practically zero but we're dealing with microseconds here :-) '''
	t = time.time()
	a = ''.join(run())
	e = time.time() - t

	''' In earlier versions, the write out was part of the measured execution time, so it was tested and sys.stdout.write was marginally faster than print '''
	sys.stdout.write(str('%s\n%iµs\n' % (a, e * 1000000)))
	