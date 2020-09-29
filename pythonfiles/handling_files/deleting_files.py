import os
from pathlib import Path

p = Path.home()/'Desktop'

print(p)

os.unlink(p/'Dadaji_dadi_12.png')
