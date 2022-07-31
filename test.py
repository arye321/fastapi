import os
from pathlib import Path


paths = sorted(Path("./babag").iterdir(), key=os.path.getmtime)
for i in paths:
    print(i.name)


