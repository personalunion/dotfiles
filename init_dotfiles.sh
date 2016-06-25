#!/bin/bash

dotfilepath=$HOME/dotfiles/home
dotfiles=".vimrc .vim .vim_runtime .zsh_favlist .zshrc .zshrc_pre-oh-my-zsh .zsh-update .oh-my-zsh  .bashrc .bash_aliases" 

cd $HOME

echo "Moving dotfiles to dotfile directory"

for i in $dotfiles; do
    mv $i $dotfilepath
    ln -s $dotfilepath/$i $i
    echo "$dotfilepath/$i -> $HOME/$i"
done
