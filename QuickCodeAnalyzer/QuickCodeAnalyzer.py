import os
import argparse
import pathlib
import re

regex = r"(\n|^)(?<!\/\/)[^\n^\/\/]*class\s(?P<class>[a-zA-Z0-9_]+)(\s*:(\s*(?P<privpubl>[a-zA-Z_0-9]+)?\s*(?P<DerivedClasses>[a-zA-Z_0-9]+)?)(\s*,\s*(?P<privpubl2>[a-zA-Z_0-9]+)\s*(?P<otherDerivedClasses>[a-zA-Z_0-9]+))*)?\s*({|;)"

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
            #v2: "(\n|^)(?<!\/\/)[^\n^\/\/]*class\s(?P<class>[a-zA-Z0-9_]+)(\s*:(\s*(?P<privpubl>[a-zA-Z_0-9]+)?\s*(?P<DerivedClasses>[a-zA-Z_0-9]+)?)(\s*,\s*(?P<privpubl2>[a-zA-Z_0-9]+)\s*(?P<otherDerivedClasses>[a-zA-Z_0-9]+))*)?\s*({|;)"gs
            #TODO fix and use regex
            #classLines = [line for line in fp if "class" in line]
            #for classLine in classLines:
                #print(classLine)
            fileContent = fp.read()
            matches = re.finditer(regex, fileContent, re.DOTALL)

            for matchNum, match in enumerate(matches, start=1):
    
                print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
                for groupNum in range(0, len(match.groups())):
                    groupNum = groupNum + 1
        
                    print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

