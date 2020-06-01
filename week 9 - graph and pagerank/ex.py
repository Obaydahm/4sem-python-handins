
import networkx as nx
import gzip
import numpy as np
import pygraphviz
from webget import download
import os

# ex 1
file = "facebook_combined.txt.gz"
def download_file():
    download_link = "https://snap.stanford.edu/data/facebook_combined.txt.gz"
    if os.path.isfile(file):
        print("file exists")
    else:
        download(download_link, file)


download_file()
with gzip.open(file, "r") as f:
    graph = nx.read_edgelist(f)


# ex 2
print(nx.info(graph))
