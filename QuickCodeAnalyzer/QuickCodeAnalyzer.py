import os
import sys, getopt


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            rootfolder = arg

    for subdir, dirs, files in os.walk(rootfolder):
        for filename in files:
            filepath = subdir + os.sep + filename

            with open(filepath, "r") as fp:
                classLines = [line for line in fp if "class" in line]
                for classLine in classLines:
                    print(classLine)

if __name__ == "__main__":
    main(sys.argv[1:])