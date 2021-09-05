# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Dependancies You Need for this Config
# zsh-syntax-highlighting - syntax highlighting for ZSH in standard repos
# autojump - jump to directories with j or jc for child or jo to open in file manager
# zsh-autosuggestions - Suggestions based on your history

# Initial Setup
# touch "$HOME/.cache/zshhistory
# Setup Alias in $HOME/zsh/aliasrc
# git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
# echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>! ~/.zshrc

# Enable colors and change prompt:
autoload -U colors && colors
PS1="%B%{$fg[magenta]%}%n%b%{$reset_color%}@%B%{$fg[cyan]%}%~%{$fg[white]%} %{$fg[magenta]%}$%{$reset_color%}%b"

# Custom Variables
EDITOR=vim

# History in cache directory:
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.cache/zshhistory
setopt appendhistory

# Basic auto/tab complete:
autoload -U compinit
zstyle ':completion:*' menu select
zmodload zsh/complist
compinit
_comp_options+=(globdots)               # Include hidden files.

# Custom ZSH Binds
bindkey '^ ' autosuggest-accept

# Load ; should be last.
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh 2>/dev/null
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 2>/dev/null
source /usr/share/autojump/autojump.zsh 2>/dev/null
#source ~/powerlevel10k/powerlevel10k.zsh-theme

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

#* Use alias definitions.
if [ -f "$ZDOTDIR/zsh_aliases" ]; then
    . "$ZDOTDIR/zsh_aliases"
fi

#* Use custom env variables.
if [ -f "$ZDOTDIR/zsh_variables" ]; then
    . "$ZDOTDIR/zsh_variables"
fi

#* ======== RUN COMMANDS AT SHELL STARTUP ========
neofetch
