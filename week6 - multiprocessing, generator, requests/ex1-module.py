from urllib.parse import urlparse
import os
import requests
import concurrent.futures

# init(self, url_list)
# download(url,filename) raises NotFoundException when url returns 404
# multi_download() uses threads to download multiple urls as text and stores filenames as a property
# iter() returns an iterator
# next() returns the next filename (and stops when there are no more)
# urllist_generator() returns a generator to loop through the urls
# avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text
# hardest_read() returns the filename of the text with the highest vowel score (use all the cpu cores on the computer for this work.


class NotFoundException(Exception):
    def __init(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class MyModule:
    def __init__(self, url_list: list):
        self._url_list = url_list
        self._count = -1
        self._filenames = []

    def __iter__(self):
        return self

    def __next__(self):
        self._count += 1
        if self._count < len(self._filenames):
            return self._filenames[self._count]
        raise StopIteration

    def download(self, url, filename=None):
        if filename == None:
            filename = os.path.basename(urlparse(url).path)

        res = requests.get(url)
        if res.status_code == 404:
            raise NotFoundException("404 - Not found")
        
        #open/create a new file and write(binary) the response content in that file
        with open(f"./downloads/{filename}", "wb") as file:
            file.write(res.content)

        self._url_list.append(url)
        return filename

    def multi_download(self, url_list: list):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            self._filenames = list(executor.map(self.download, url_list))

    #Generator expressions provide an additional shortcut to build generators out of expressions similar to that of list comprehensions.
    #In fact, we can turn a list comprehension into a generator expression by replacing the square brackets ("[ ]") with parentheses. 
    #Alternately, we can think of list comprehensions as generator expressions wrapped in a list constructor.
    #https://wiki.python.org/moin/Generators
    def urllist_generator(self):
        #traditional
        #for url in self._url_list:
        #    yield url

        #generator expression
        return (url for url in self._url_list)

def test():
    url_list = [
        "https://www.gutenberg.org/files/376/376-0.txt",
        "https://www.gutenberg.org/cache/epub/25525/pg25525.txt",
        "https://www.gutenberg.org/files/11/11-0.txt",
        "https://www.gutenberg.org/files/84/84-0.txt",
        "http://www.gutenberg.org/cache/epub/25525/pg25525.txt",
        "https://www.gutenberg.org/files/43/43-0.txt"
    ]
    md = MyModule([])
    md.multi_download(url_list)

    iterator = iter(md)
    e1 = next(iterator)
    e2 = next(iterator)
    print(e1, e2)

    #urllist generator
    gen = md.urllist_generator()
    print(gen)
    print(next(gen))

    #md.download("https://api.github.com/search/repositories?q=language:python&sort=stars", "git.json")
#test()

