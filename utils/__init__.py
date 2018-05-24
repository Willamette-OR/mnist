import os


from config import DATA_ROOT


if not os.path.exists(DATA_ROOT):
    os.mkdir(DATA_ROOT)
