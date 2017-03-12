#!/usr/bin/python

from crawl import Crawling
import pprint

mingrome = Crawling()
index, graph = mingrome.crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = mingrome.compute_ranks(graph, 0)

# search 'for'
print mingrome.ordered_search(index, ranks, 'for')
