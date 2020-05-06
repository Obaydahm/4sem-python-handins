# os.path.isfile: return true if file path exists
# os.path.join: returns a concatenation of the
# path containing any members of *paths
# urllib.parse: breaks down the url
from os import path
import urllib.request as req
from urllib.parse import urlparse


def download(url, to=None):
    """
    Download a remote file specified by a URL to a 
    local directory.

    :param url: str
        URL pointing to a remote file.

    :param to: str
        Local path, absolute or relative, with a filename 
        to the file storing the contents of the remote file.
    """
    destination = ""
    if to != None:
        destination = to

    if not path.isfile(destination + path.basename(url)):
        req.urlretrieve(url, destination + path.basename(url))
        print(path.basename(url), "has been downloaded!")
    else:
        print("File already exists!")


download("https://omoussa.dk/ffplan2/user/online/ob.jpg", "test/")

