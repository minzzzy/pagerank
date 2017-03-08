#!/usr/bin/python

from crawl import Crawling

mingrome = Crawling()
index, graph = mingrome.crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = mingrome.compute_ranks(graph, 0)
#print index
print ranks
#print mingrome.ordered_search(index, ranks, 'for')
