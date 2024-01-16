import argparse
import os
import re

"""This script will rename files in the "image" and "label" folders
and will replace the filenames with a zero-padded
version of the original filename.
Example:
train02.jpg to 0000000002.jpg
train1943.jpg to 0000001943.jpg
val761.txt to 0000000761.txt
test327.txt to 0000000327.txt
"""


def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert file names")
    parser.add_argument(
        "--image-base-path",
        default="./datasets/bdss20k/images",
        type=str,
        help="base path of images",
    )
    parser.add_argument(
        "--label-base-path",
        default="./datasets/bdss20k/labels",
        type=str,
        help="base path of labels",
    )
    return parser.parse_args()


patterns = [
    {
        "pattern": "train(\\d+)\\.jpg",
    },
    {
        "pattern": "train(\\d+)\\.txt",
    },
    {
        "pattern": "val(\\d+)\\.jpg",
    },
    {
        "pattern": "val(\\d+)\\.txt",
    },
    {
        "pattern": "test(\\d+)\\.jpg",
    },
    {
        "pattern": "test(\\d+)\\.txt",
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

                # Determine the number of zeros based
                # on the length of the numeric part
                num_zeros = 10 - len(numeric_part)
                zero_padding = "0" * num_zeros

                new_filename = zero_padding + numeric_part

                if pattern == "train(\\d+)\\.jpg":
                    new_filename += ".jpg"

                if pattern == "val(\\d+)\\.jpg":
                    new_filename += ".jpg"

                if pattern == "test(\\d+)\\.jpg":
                    new_filename += ".jpg"

                if pattern == "train(\\d+)\\.txt":
                    new_filename += ".txt"

                if pattern == "val(\\d+)\\.txt":
                    new_filename += ".txt"

                if pattern == "test(\\d+)\\.txt":
                    new_filename += ".txt"

                os.rename(
                    os.path.join(directory, filename),
                    os.path.join(directory, new_filename),
                )
                break


def main():
    args = parse_arguments()
    for category in ["train", "val", "test"]:
        image_directory = os.path.join(args.image_base_path, category)
        label_directory = os.path.join(args.label_base_path, category)
        rename_files(image_directory, patterns)
        rename_files(label_directory, patterns)
        print(f"Renamed files in {category} image and label directories.")


if __name__ == "__main__":
    main()
