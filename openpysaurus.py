#!/usr/bin/env python

import simplejson
import urllib2
import sys

for term in sys.argv[1:]:
    url="http://www.openthesaurus.de/synonyme/search?format=application/json&q=%s" % term
    f = urllib2.urlopen(url)
    ret=simplejson.loads(f.read())
    print "%s" % term
    for cat in ret.get('synsets'):
    	print "%s %s: %s" % (cat.get('id'),", ".join(cat.get('categories')) or "",", ".join([synonym.get('term') for synonym in cat.get('terms')]))
