import exif
import argparse
import utils
from pathlib import Path

arg_parser = argparse.ArgumentParser(prog='MetRem', description='Simple tool to remove metadata from image files',
									usage='met_rem_main.py [options]')
arg_parser.add_argument('-d', '--input_dir', type=utils.dir_to_paths, default='Raw_files')

args = arg_parser.parse_args()

paths = args.input_dir

clean_files_path = Path('Clean_files')
clean_files_path.mkdir(exist_ok=True)

for path in paths:
	image = exif.Image(path)
	if not image.has_exif:
		print(f'File {path} does not have EXIF data')
		continue
	all_tags = image.list_all()
	for tag in all_tags:
		print(tag, image.get(tag, ''), sep=' --- ')
