import os
import argparse
import pathlib


parser = argparse.ArgumentParser(description="QuickCodeAnalyzer")
parser.add_argument("rootFolder", type=pathlib.Path)
args = parser.parse_args()
for subdir, dirs, files in os.walk(args.rootFolder):
    for filename in files:
        if not filename.endswith(".h"):
            continue
        filepath = subdir + os.sep + filename

        with open(filepath, "r") as fp:
            #regex: (?<!//[^\n])class\s(?P<class>[a-zA-Z0-9_]+)(\s*:(\s*([a-zA-Z_0-9]+)?\s*(?P<DerivedClasses>[a-zA-Z_0-9]+)?)(,\s*([a-zA-Z_0-9]+)?\s*(?P<OtherDerivedClasses>[a-zA-Z_0-9]+)?)*)?\s*({|;)
            #TODO fix and use regex
            classLines = [line for line in fp if "class" in line]
            for classLine in classLines:
                print(classLine)
