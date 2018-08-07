import os
from pathlib import Path
from collections import Counter


def hardlink_check(directory_path: str) -> bool:

    directory = Path(directory_path)

    if not directory.exists():
        return False

    inodes = list()
    hardlinks = list()

    for file in directory.iterdir():
        inodes.append(os.stat(file).st_ino)

    counter = Counter(inodes)

    for key, value in counter.items():
        if value > 1:
            hardlinks.append(key)

    if hardlinks:
        return True
    else:
        return False

