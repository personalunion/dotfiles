from subprocess import check_call, CalledProcessError
import os
import argparse

import errno
import sys


def read_args(cmdline=None):
    parser = argparse.ArgumentParser \
        (description='Installs packages from package list. Needs filename.\nMust be run as root for apt-get.'
                     'Not for wget option\n')
    parser.add_argument('filename', help='Enter a package list filename')
    parser.add_argument('-w', '--wget', help='Install foreign software via wget.', action='store_true')

    if cmdline is not None:
        args = parser.parse_args(cmdline.split())
    else:
        args = parser.parse_args()
    #args = parser.parse_args()
    return args


def install_all(content, dry_run=False):
    malfunctioned = []
    for line in content:
        try:
            if not dry_run:
                check_call(['apt-get', 'install', '-y', line])
                continue
            else:
                check_call(['apt-get', 'install', '-y', '-s', line])
                continue
        except CalledProcessError:
            malfunctioned.append(line)
    return malfunctioned


def install_via_wget(content):
    directory = '/home/s/tools_test'
    cur_dir = os.getcwd()
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(directory)

    err_downl = []
    for line in content:
        try:
            check_call(['wget', line])
            break
        except CalledProcessError:
            err_downl.append(line)

    err_unzip = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        try:
            check_call(['engrampa', '-h', f])
            break
        except CalledProcessError:
            err_unzip.append(f)
    os.chdir(cur_dir)

    return err_downl, err_unzip


def get_content(filename):
    f = open(filename, 'r')
    content = []
    for line in f:
        if line[0] != '#':
            content.append(line.strip())
    f.close()
    return content


def main():
    args = read_args()
    if not args.wget:
        try:
            os.rename('/etc/foo', '/etc/bar')
        except IOError as e:
            if e[0] == errno.EPERM:
                print("You need root permissions to do this, laterz!")
                sys.exit(1)
    content = get_content(args.filename)
    if not args.wget:
        mal = install_all(content)
        if mal:
            print('The following packages could not be installed:')
            for m in mal:
                print(m)
        else:
            print('All packages were installed successfully')
    else:
        err_d, err_unzip = install_via_wget(content)
        if err_d:
            print('The following packages could not be downloaded:')
            for m in err_d:
                print(m)
        elif err_unzip:
            print('The following packages could not be unzipped:')
            for m in err_unzip:
                print(m)
        else:
            print('All packages were installed successfully')

if __name__ == "__main__":
    main()
