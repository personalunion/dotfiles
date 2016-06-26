#!/bin/bash

dotfilepath=$HOME/dotfiles/home
dotfiles=".vimrc .vim .vim_runtime .zsh_favlist .zshrc .zshrc_pre-oh-my-zsh .zsh-update .oh-my-zsh  .bashrc .bash_aliases" 

init=0

print_usage ()
{
    echo "Linking script for dotfiles."
    echo "Usage:"
    echo -e "\t-h or --help prints this help message"
    echo -e "\t-i or --init for copying all dotfiles defined in this script and linking them. \n\t\tDefault is just linking"
}

while [ "$1" != "" ];do
    case "$1" in 
    -i|--init) init=1  ;; 
    -h|--help) (print_usage); exit 0 ;;
    *) init=0 ;;
    esac
    shift
done


cd $HOME

echo "Moving dotfiles to dotfile directory"

for i in $dotfiles; do
    if [ $init eq 1]; then
        mv $i $dotfilepath
    fi
    ln -s $dotfilepath/$i $i
    echo "$dotfilepath/$i -> $HOME/$i"
done
