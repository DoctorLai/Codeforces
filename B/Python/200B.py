#!/usr/bin/env python

n = int(raw_input())

print "%.8f" % (sum([x for x in map(int, raw_input().split(' '))]) / float(n))





