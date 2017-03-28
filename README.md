# pagerank-mingle  
It is in class, [Intro to computer science](https://www.udacity.com/course/intro-to-computer-science--cs101) of Udacity.  
I made a simple web search engine based on the contents of the lecture.  


## Create a search engine
There are 3 steps in search_engine.py

### crawl_web
- input : url
- output : index, graph

```python  
def crawl_web(self, seed):
        tocrawl = [seed]
        crawled = []
        while tocrawl:
            page = tocrawl.pop()
            if page not in crawled:
                content = self._get_page(page)
                self._add_page_to_index(self.index, page, content)
                outlinks = self._get_all_links(content)
                self._union(tocrawl, outlinks)
                self.graph[page] = outlinks
                crawled.append(page)
        return self.index, self.graph
```


### compute_ranks
- input : graph
- output : ranks

```python
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
                        if not self._is_reciprocal_link(graph, node, page, k):
                            newrank = newrank + d*ranks[node]/len(graph[node])
                newranks[page] = newrank
            ranks = newranks
        return ranks
```


### ordered_search
- input : index, ranks, keyword
- output : ordered_list

```python
def ordered_search(self, index, ranks, keyword):
        dic = {}
        res = []
        for e in index[keyword]:
            if e in ranks:
                dic[ranks[e]] = e
        key = self._quicksort(list(dic.keys()))
        for i in key:
            res.append(dic[i])
        return res
 ```

## How to use
Use make_search_engine.py
```python
mingle = Search_engine()
index, graph = mingle.crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = mingle.compute_ranks(graph, 0)

# search 'for'
print mingrome.ordered_search(index, ranks, 'for')
```

