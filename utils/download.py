import os
import sys
from urllib.request import urlretrieve


from config import DATA_ROOT, MNIST_URL


last_reported_percentage = 0


def report_progress(count_blocks, block_size, total_size):
    """A call back to report the progress of downloads"""

    global last_reported_percentage
    percentage = int(100 * count_blocks * block_size / total_size)

    if percentage != last_reported_percentage:
        if percentage % 5 == 0:
            sys.stdout.write('{}%'.format(percentage))
            sys.stdout.flush()
        else:
            sys.stdout.write('.')
            sys.stdout.flush()

    last_reported_percentage = percentage


def maybe_download(filename, expected_bytes,
                   url=MNIST_URL,
                   data_root=DATA_ROOT,
                   force=False):
    """Download files and verify"""

    dest_filename = os.path.join(data_root, filename)

    if not os.path.exists(dest_filename) or force:
        print("\nAttempting to download:", filename)
        filename, _ = urlretrieve(url + filename, dest_filename,
                                  reporthook=report_progress)
        print("\nDownload completed!")

    statinfo = os.stat(dest_filename)
    if statinfo.st_size == expected_bytes:
        print("Found and verified", dest_filename)
    else:
        raise Exception("Failed to verify " + dest_filename +
                        ". Can you get to it with a browser?")

    return dest_filename
