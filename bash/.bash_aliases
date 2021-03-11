# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# ls aliases
alias ll='ls -AlFh'

# ===== CUSTOM =====

# clear
alias cls='clear'

# clear and neofetch
alias neocls='clear; neofetch'
alias ncls='clear; neofetch'

# matrix
alias matrix='cmatrix -B -C magenta'