from pathlib import Path


def dir_to_paths(dir_path: str) -> list[Path]:
	"""
	Function that takes dir with raw files and returns list of path to files in dir. Can be nested dict, can be flat, can have files
	that aren't images (not signed .jpg, .png, .tiff) - those will be ignored

	:dir_path: path to dir with raw files with metadata
	:return: list of Paths pointing to files to be cleaned up of metadata
	"""
	
	raw_files_dir_path = Path(dir_path)
	if not raw_files_dir_path.exists():
		print('Input dir does not exist')
		exit(8)
	raw_files_list = list(raw_files_dir_path.rglob('*.jpg'))
	raw_files_list.extend(list(raw_files_dir_path.rglob('*.png')))
	raw_files_list.extend(list(raw_files_dir_path.rglob('*.tiff')))
	
	return raw_files_list
