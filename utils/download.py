import os
from urllib.request import urlretrieve


from config import DATA_ROOT, MNIST_URL


def maybe_download(filename, expected_bytes,
                   url=MNIST_URL,
                   data_root=DATA_ROOT,
                   force=False):
    """Download files and verify"""

    dest_filename = os.path.join(data_root, filename)

    if not os.path.exists(dest_filename) or force:
        print("\nAttempting to download:", filename)
        filename, _ = urlretrieve(url + filename, dest_filename,
                                  reporthook=None)
        print("\nDownload completed!")

    statinfo = os.stat(dest_filename)
    if statinfo.st_size == expected_bytes:
        print("Found and verified", dest_filename)
    else:
        raise Exception("Failed to verify " + dest_filename +
                        ". Can you get to it with a browser?")

    return dest_filename
