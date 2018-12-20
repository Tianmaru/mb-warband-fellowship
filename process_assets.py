import string
import os
import shutil

from module_info import *

# Lav's export_dir tweak
export_dir = '%s/' % export_dir.replace('\\', '/').rstrip('/')

print "Exporting assets..."

files = ["main.bmp", "icon.png"]

for filename in files:
    if os.path.isfile(filename):
        dest = os.path.join(export_dir, filename)
        shutil.copy(filename, dest)

srcs = ["Data", "Music", "Resource", "SceneObj", "Sounds", "Textures"]

for src in srcs:
	if os.path.isdir(src):
		dest = os.path.join(export_dir, src)
		src_files = os.listdir(src)
		for file_name in src_files:
    			file_path = os.path.join(src, file_name)
	    		if (os.path.isfile(file_path)):
        			shutil.copy(file_path, dest)

