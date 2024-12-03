import exif
import argparse
import utils
from pathlib import Path
from tqdm import tqdm

arg_parser = argparse.ArgumentParser(prog='MetRem', description='Simple tool to remove metadata from image files',
									usage='met_rem_main.py [options]', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
arg_parser.add_argument('-d', '--input_dir', default='Raw_files',
						help='path to dir with files to clean, it will read files inside it, will not copy the dir itself')
arg_parser.add_argument('-o', '--output_dir', default='cwd/Clean_files', help='path to output dir, defaults to cwd')

args = arg_parser.parse_args()
output_dir = args.output_dir
if output_dir == 'cwd/Clean_files':
	output_dir = Path(Path.cwd(), 'Clean_files')
input_dir = args.input_dir
paths = utils.dir_to_paths(input_dir)

clean_files_path = Path(output_dir)
clean_files_path.mkdir(exist_ok=True)

pbar = tqdm(total=len(paths), desc='Cleaning metadata: ', ascii=True)
for path in paths:
	image = exif.Image(path)
	if not image.has_exif:
		print(f'File {path} does not have EXIF data')
		continue
	image.delete_all()
	
	new_name = path.relative_to(input_dir)
	new_name_filename = f'{new_name.stem}_clean.{str(new_name.name).split(".")[-1]}'
	new_path = Path(clean_files_path, new_name.parent, new_name_filename)
	new_path.parent.mkdir(parents=True, exist_ok=True)
	new_image = open(new_path, mode='wb')
	new_image.write(image.get_file())
	new_image.close()
	pbar.update(1)
