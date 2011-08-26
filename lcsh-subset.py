#!/usr/bin/env python

import sys
import urllib

import rdflib
import feedparser

# get the query 
q = urllib.quote(sys.argv[1])

# the graph to persist the concepts to
graph = rdflib.Graph()

# use OpenSearch Atom to aggregate the RDF for the search results
start = 0
while True:

    # TODO: the awkward 2nd q param for scoping to lcsh will hopefully 
    # be changed to be a bit simpler...till then this looks ugly
    url = "http://id.loc.gov/search/?q=%s&format=atom&start=%i&q=cs%%3Ahttp%%3A%%2F%%2Fid.loc.gov%%2Fauthorities%%2Fsubjects" % (q, start)

    # fetch the atom feed
    feed = feedparser.parse(url)

    # no need to continue if there aren't any hits
    if len(feed.entries) == 0:
        break

    # load the rdf for each hit
    for entry in feed.entries:
        start += 1
        for link in entry.links:
            if link.type == "application/rdf+xml":
                print "loading %s <%s>" % (entry.title, link.href)
                graph.load(link.href)

# output the resulting graph as RDF/XML
filename = "%s.rdf" % sys.argv[1].replace(" ", "_")

graph.serialize(file(filename, "w"))
