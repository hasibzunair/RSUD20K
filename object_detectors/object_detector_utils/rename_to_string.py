import argparse
import os
import re

"""This script will rename files in the "image" and "label" folders
and will replace the filenames with a zero-padded
version of the original filename.
Example:
0000000002.jpg to train02.jpg 
0000001943.jpg to train1943.jpg
t0000000761.txt to val761.txt 
0000000327.txt to test327.txt
"""
def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert file names")
    parser.add_argument(
        "--image-base-path",
        default="./save_test_images",
        type=str,
        help="base path of images",
    )
    # parser.add_argument(
    #     "--label-base-path",
    #     default="./datasets/rsud20k/labels",
    #     type=str,
    #     help="base path of labels",
    # )
    return parser.parse_args()

patterns = [
    {
        "pattern": "(\\d+)\\.jpg",
    },
]

# Function to rename files based on the patterns
def rename_files(directory, pattern_data):
    for filename in os.listdir(directory):
        for pattern_info in pattern_data:
            pattern = pattern_info["pattern"]

            match = re.match(pattern, filename)
            if match:
                numeric_part = match.group(1)
                if numeric_part != '0':
                    os.rename(
                        os.path.join(directory, filename),
                        os.path.join(directory, "test" + numeric_part + ".jpg"),
                    )

                # Determine the number of zeros based
                # on the length of the numeric part
                num_zeros = 10 - len(numeric_part)
                zero_padding = "0" * num_zeros

                new_filename = zero_padding + numeric_part