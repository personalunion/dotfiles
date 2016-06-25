#aliases
#git
copu() {
   git add --all 
   RET=`git commit -m "$1"`
   if [ "$RET" == "" ]
	then echo "Tell 'em what you did";
   	else git push
   fi
}

co() {
   git add --all 
   git commit -m "$1"
}

pp() {
    evince $1 &
}

alias commit='git add --all && git commit'
alias st='git status'
alias code='cd /home/miraculix/code'

#studies
alias ma='cd /home/miraculix/master'

#other
alias ll='ls -al'
alias o='gnome-open'
alias rr='retext'
s() {
    if [ $2 == ""]
    	then grep -rn "$1" *
	else grep -rn "$1" * --after-context=$2
    fi
}
