# pagerank-mingle  


## Create a search engine
There are 3 steps in crawl.py

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


### ordered_search
- input : index, ranks, keyword
- output : ordered_list

## How to use
Use web.py
