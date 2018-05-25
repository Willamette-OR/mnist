import os
import unittest


from config import DATA_ROOT, NUM_CLASSES
from utils.download import maybe_download
from utils.extract import maybe_extract


class UtilsCase(unittest.TestCase):
    """Unit tests for utilities"""

    def setUp(self):
        """Set up space for testing"""

        self.filename = 'notMNIST_small.tar.gz'
        self.num_classes = NUM_CLASSES

    def test_download(self):
        """Test the download function"""

        test_filename = maybe_download(self.filename, 8458043, force=True)
        self.assertEqual(test_filename, os.path.join(DATA_ROOT, self.filename))

    def test_extract(self):
        """Test downloaded file extraction"""

        test_filename = os.path.join(DATA_ROOT, self.filename)
        test_data_folders = maybe_extract(test_filename, force=True)
        self.assertTrue(isinstance(test_data_folders, list))
        self.assertEqual(len(test_data_folders), self.num_classes)


if __name__ == '__main__':
    unittest.main(verbosity=2)
