# MetRem - Image and video metadata removing tool

This is not a complex tool that I put together for personal use. Yes, I could have used some existing tools, but I wanted
to check some tags and read it, so I threw together a simple script. I then added some command line interface and decided
that the code is close to being a tool. So I did. Deal with it.

## Requirements
Python packages needed:
- exif
- tqdm

## Usage
```shell
❯ python met_rem_main.py -h          
usage: met_rem_main.py [options]

Simple tool to remove metadata from image files

options:
  -h, --help            show this help message and exit
  -d INPUT_DIR, --input_dir INPUT_DIR
                        path to dir with files to clean, it will read files inside it, will not copy the dir itself
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        path to output dir, defaults to cwd
```
### Input
Tool with filter files in input_dir to only clean jpg, png and tiff files. All other will be ignored and not even moved.
It can read nested dirs and will reflect the structure of input_dir in output. Input dir defaults to ./Raw_files, cause
I wanted it that way and I cannot be asked to fill it

### Output
Files will be deposited in Clean_file dir created in the output_dir location, defaults to location where code was run
