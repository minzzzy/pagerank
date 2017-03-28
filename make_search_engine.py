#!/usr/bin/python

from Search_engine import Search_engine
import pprint

mingle = Search_engine()
index, graph = mingle.crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = mingle.compute_ranks(graph, 0)

# search 'for'
print mingle.ordered_search(index, ranks, 'for')
