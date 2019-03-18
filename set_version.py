
import argparse
import sys
import os
import codecs

import PyInstaller.utils.win32.versioninfo


def main():
    parser = argparse.ArgumentParser(
        epilog='This script accepts the following input')
    parser.add_argument('-c', '--CompanyName')
    parser.add_argument('-f', '--FileDescription')
    parser.add_argument('-v', '--FileVersion', nargs=4, type=int)
    parser.add_argument('-i', '--InternalName')
    parser.add_argument('-cp', '--Copyright')
    parser.add_argument('-p', '--ProductName')
    parser.add_argument('-u', '--ProductVersion')

    # Parse our args as a dictionary which we will iterate through for string structs creation
    args = vars(parser.parse_args())

    # We need the Fileversion value for FixedFileInfo values
    versionno = args.get('FileVersion')
    ffi = PyInstaller.utils.win32.versioninfo.FixedFileInfo()
    ffi.__init__(filevers=versionno, prodvers=versionno)
    ffi.__unicode__()

    # Define our output file
    output = 'versionFile.py'

    # Convert our Fileversion list to a string, we need this to iterate over the dict
    versionString = str(args.get('FileVersion'))
    replacements = {'[':'', ']':'', ',':'.'}
    args['FileVersion'] = "".join([replacements.get(c, c) for c in versionString])

    # Define our kids
    kids = []
    #Iterate through our dict and create for every argument a string struct
    for key, value in args.items():
        stringstr = PyInstaller.utils.win32.versioninfo.StringStruct()
        stringstr.__init__(name=key, val=value)
        stringstr.__unicode__()
        kids.append(stringstr)

    # Create the varstruct object
    varStr = PyInstaller.utils.win32.versioninfo.VarStruct()
    # We pass some pre-defined info, this should not differ for our program
    varStr.__init__(name='Translation', kids=[1033, 1200])
    varStr.__unicode__()

    # Create the varfileinfo object and insert varstruct into it
    varfile = PyInstaller.utils.win32.versioninfo.VarFileInfo()
    varfile.__init__(kids=[varStr])
    varfile.__unicode__()

    # Create stringtable object
    strTable = PyInstaller.utils.win32.versioninfo.StringTable()
    strTable.__init__(name='040904B0', kids=kids)
    strTable.__unicode__()

    # Create StringFileInfo object
    sfi = PyInstaller.utils.win32.versioninfo.StringFileInfo()
    sfi.__init__(kids=[strTable])
    sfi.__unicode__()
    kids = [sfi]
    kids.append(varfile)
    print(kids)

    # Create VSVersionInfo object
    vs = PyInstaller.utils.win32.versioninfo.VSVersionInfo()
    vs.__init__(ffi=ffi, kids=kids)
    vs.__unicode__()

    # Write the result to a file
    with codecs.open(output, 'w+', 'utf8') as fp:
        fp.write(u"%s" % (vs,))


if __name__ == '__main__':
    main()


