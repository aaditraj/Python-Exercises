import zipfile, os

from pathlib import Path

p = Path.home()/'Desktop'/'SCHOOL DRIVE DOWNLOAD 1'

scienceZip = zipfile.ZipFile(p/'Science study guide.zip')

print(scienceZip.namelist())

study_guide_info = scienceZip.getinfo('Science study guide.html')

print(study_guide_info.file_size)

print(study_guide_info.compress_size)
