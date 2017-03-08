#!/usr/bin/python

class Crawling(object):

    def __init__(self):
        self.index = {}
        self.graph = {}

    #def record_user_click(self,index,keyword,url):
    #    return

    def get_page(self,url):
        try:
            if url == "http://www.udacity.com/cs101x/index.html":
                return '''<html> <body> This is a test page for learning to crawl!
    <p> It is a good idea to
    <a href="http://www.udacity.com/cs101x/crawling.html">
    learn to crawl</a> before you try to
    <a href="http://www.udacity.com/cs101x/walking.html">walk</a> or
    <a href="http://www.udacity.com/cs101x/flying.html">fly</a>.</p></body></html>'''

            elif url == "http://www.udacity.com/cs101x/crawling.html":
                return '''<html> <body> I have not learned to crawl yet, but I am
    quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.
    </body> </html>'''

            elif url == "http://www.udacity.com/cs101x/walking.html":
                return '''<html> <body> I cant get enough
    <a href="http://www.udacity.com/cs101x/index.html">crawling</a>!</body></html>'''

            elif url == "http://www.udacity.com/cs101x/flying.html":
                return '<html><body>The magic words are Squeamish Ossifrage!</body></html>'
        except:
            return ""
        return ""

    def remove_tags(self, string):
        start, end = 0, 0
        while True:
            start = string.find('<')
            if start == -1:
                return string.split()
            end = string.find('>', start)
            string = string[:start] + ' ' + string[end+1:]

    def crawl_web(self, seed):
        tocrawl = [seed]
        crawled = []
        while tocrawl:
            page = tocrawl.pop()
            if page not in crawled:
                content = self.get_page(page)
                self.add_page_to_index(self.index, page, content)
                outlinks = self.get_all_links(content)
                self.union(tocrawl, outlinks)
                self.graph[page] = outlinks
                crawled.append(page)
        return self.index, self.graph

    def add_to_index(self,index, keyword, url):
        if keyword in index:
            index[keyword].append(url)
        else:
            index[keyword] = [url]

    def add_page_to_index(self, index, url, content):
        words = content.split()
        for word in words:
            self.add_to_index(index, word, url)

    def get_next_target(self, page):
        start_link = page.find('<a href=')
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote+1)
        url = page[start_quote+1:end_quote]
        return url, end_quote

    def get_all_links(self, page):
        links = []
        while True:
            url, endpos = self.get_next_target(page)
            if url:
                links.append(url)
                page = page[endpos:]
            else:
                break
        return links

    def union(self, a, b):
        for e in b:
            if e not in a:
                a.append(e)

    def lookup(self, index, keyword):
        if keyword not in index:
            return index[keyword]
        return None

    def compute_ranks(self, graph, k):
        d = 0.8
        numloops = 2
        ranks = {}
        npages = len(graph)
        for page in graph:
            ranks[page] = 1.0 / npages
        
        for i in range(0, numloops):
            newranks = {}
            for page in graph:
                newrank = (1 - d) / npages
                for node in graph:
                    if page in graph[node]:
                        if not self.is_reciprocal_link(graph, node, page, k):
                            newrank = newrank + d*ranks[node]/len(graph[node])
                newranks[page] = newrank
            ranks = newranks
        return ranks

    def is_reciprocal_link(self, graph, source, destination, k):
        if k == 0:
            if source == destination:
                return True
            return False
        if source in graph[destination]:
            return True
        for node in graph[destination]:
            if self.is_reciprocal_link(graph, source, node, k-1):
                return True
        return False

    def quicksort(self, l):
        if len(l) <= 1:
            return l
        pivot = l[len(l)/2]
        smaller = []
        bigger = []
        equal = []
        for e in l:
            if e < pivot:
                smaller.append(e)
            elif e == pivot:
                equal.append(e)
            else:
                bigger.append(e)
        return self.quicksort(bigger) + equal + self.quicksort(smaller)

    ## Ascending
    def ordered_search(self, index, ranks, keyword):
        dic = {}
        res = []
        for e in index[keyword]:
            if e in ranks:
                dic[ranks[e]] = e
        key = self.quicksort(dic.keys())
        for i in key:
            res.append(dic[i])
        return res
