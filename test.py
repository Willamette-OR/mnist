import os
import unittest


from config import DATA_ROOT
from utils.download import maybe_download


class UtilsCase(unittest.TestCase):
    """Unit tests for utilities"""

    def test_download(self):
        """Test the download function"""

        filename = 'notMNIST_small.tar.gz'
        test_filename = maybe_download('notMNIST_small.tar.gz', 8458043,
                                       force=True)
        self.assertEqual(test_filename, os.path.join(DATA_ROOT, filename))


if __name__ == '__main__':
    unittest.main(verbosity=2)
