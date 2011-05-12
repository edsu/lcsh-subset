#!/usr/bin/env python

import sys
import rdflib
import feedparser

q = sys.argv[1]
page = 0
graph = rdflib.Graph()

while True:

    page += 1

    url = "http://id.loc.gov/search/?q=%s&page=1&format=atom&cs=cs%%3Alcsh&page=%i" % (q, page)

    print url
    feed = feedparser.parse(url)

    if len(feed.entries) == 0:
        break

    for entry in feed.entries:
        for link in entry.links:
            if link.type == "application/rdf+xml":
                print entry.title, link.href
                graph.load(link.href)

graph.serialize(file("subset.rdf", "w"))
