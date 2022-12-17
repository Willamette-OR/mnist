import os
import tarfile


from config import DATA_ROOT, NUM_CLASSES


def maybe_extract(filename, num_classes=NUM_CLASSES, force=False):
    """Extract mnist image folders from .tar.gz files"""

    # Remove .tar.gz
    root = os.path.splitext(os.path.splitext(filename)[0])[0]

    if os.path.isdir(root) and not force:
        print("{} already present - skipping extraction of {}".
              format(root, filename))
    else:
        print("Extracting data from {}. This may take a while. Please wait.".
              format(filename))
        with tarfile.open(filename) as tar:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar, DATA_ROOT)
        print("Extraction completed!")

    data_folders = [os.path.join(root, d) for d in os.listdir(root)
                    if os.path.isdir(os.path.join(root, d))]
    if len(data_folders) != num_classes:
        raise Exception("Expected {} folders, one per classes. Found {} "
                        "folders instead".format(num_classes,
                                                 len(data_folders)))
    print(data_folders)
    return data_folders
