import os
import argparse
import pathlib


parser = argparse.ArgumentParser(description="QuickCodeAnalyzer")
parser.add_argument("rootFolder", type=pathlib.Path)
args = parser.parse_args()
for subdir, dirs, files in os.walk(args.rootfolder):
    for filename in files:
        filepath = subdir + os.sep + filename

        with open(filepath, "r") as fp:
            classLines = [line for line in fp if "class" in line]
            for classLine in classLines:
                print(classLine)
