from subprocess import STDOUT, check_call
import os
import argparse


def read_args():
    parser = argparse.ArgumentParser\
        (description='Installs packages from package list. Needs filename.\nMust be run as root.')
    parser.add_argument('filename', help='Enter a package list filename')
    args = parser.parse_args()
    return args


def install_all(content):
    for line in content:
        check_call(['apt-get', 'install', '-y', line])#, stdout=open(os.devnull, 'wb'), stderr=STDOUT)


def main():
    args = read_args()
    f = open(args.filename, 'r')
    content = []
    for line in f:
        content.append(f.readline().strip())
    install_all(content)


main()