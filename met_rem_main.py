import exif
import argparse
import utils
from pathlib import Path
from tqdm import tqdm

arg_parser = argparse.ArgumentParser(prog='MetRem', description='Simple tool to remove metadata from image files',
									usage='met_rem_main.py [options]')
arg_parser.add_argument('-d', '--input_dir', type=utils.dir_to_paths, default='Raw_files')

args = arg_parser.parse_args()

paths = args.input_dir

clean_files_path = Path('Clean_files')
clean_files_path.mkdir(exist_ok=True)

pbar = tqdm(total=len(paths), desc='Cleaning metadata: ', ascii=True)
for path in paths:
	image = exif.Image(path)
	if not image.has_exif:
		print(f'File {path} does not have EXIF data')
		continue
	image.delete_all()
	
	new_name = path.name.split('.')
	new_name = f'{new_name[0]}_clean.{new_name[1]}'
	new_path = Path(clean_files_path, Path(*path.parts[1:-1]), new_name)
	new_path.parent.mkdir(parents=True, exist_ok=True)
	new_image = open(new_path, mode='wb')
	new_image.write(image.get_file())
	new_image.close()
	pbar.update(1)
