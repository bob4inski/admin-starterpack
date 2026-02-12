# Конфигурационные файлы для настройки терминала

## .bashrc - конфигурация для Bash

```bash
# ~/.bashrc: executed by bash(1) for non-login shells.

# Если не работает в интерактивном режиме, ничего не делать
case $- in
    *i*) ;;
      *) return;;
esac

# Настройка истории команд
HISTCONTROL=ignoreboth
HISTSIZE=1000
HISTFILESIZE=2000
shopt -s histappend

# Настройка окна
shopt -s checkwinsize

# Настройка промпта
PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

# Включение цветной поддержки ls
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# Полезные алиасы
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias grep='grep --color=auto'
alias mkdir='mkdir -pv'
alias wget='wget -c'

# Функции для быстрой навигации
mkcd() {
    mkdir -p "$1" && cd "$1"
}

extract() {
    if [ -f $1 ]; then
        case $1 in
            *.tar.bz2)   tar xjf $1     ;;
            *.tar.gz)    tar xzf $1     ;;
            *.bz2)       bunzip2 $1     ;;
            *.rar)       unrar e $1     ;;
            *.gz)        gunzip $1      ;;
            *.tar)       tar xf $1      ;;
            *.tbz2)      tar xjf $1     ;;
            *.tgz)       tar xzf $1     ;;
            *.zip)       unzip $1       ;;
            *.Z)         uncompress $1  ;;
            *.7z)        7z x $1        ;;
            *)           echo "'$1' cannot be extracted via extract()" ;;
        esac
    else
        echo "'$1' is not a valid file"
    fi
}
```

## .zshrc - конфигурация для Zsh

```zsh
# ~/.zshrc

# Настройка истории
HISTSIZE=1000
SAVEHIST=1000
setopt HIST_IGNORE_DUPS
setopt HIST_IGNORE_ALL_DUPS
setopt HIST_FIND_NO_DUPS
setopt HIST_SAVE_NO_DUPS

# Настройка автодополнения
autoload -Uz compinit
compinit
zstyle ':completion:*' menu select
setopt COMPLETE_ALIASES

# Настройка промпта
autoload -Uz promptinit
promptinit
prompt adam1

# Настройка цветов
autoload -U colors
colors

# Полезные алиасы
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias grep='grep --color=auto'
alias mkdir='mkdir -pv'
alias wget='wget -c'

# Функции
mkcd() {
    mkdir -p "$1" && cd "$1"
}

extract() {
    if [ -f $1 ]; then
        case $1 in
            *.tar.bz2)   tar xjf $1     ;;
            *.tar.gz)    tar xzf $1     ;;
            *.bz2)       bunzip2 $1     ;;
            *.rar)       unrar e $1     ;;
            *.gz)        gunzip $1      ;;
            *.tar)       tar xf $1      ;;
            *.tbz2)      tar xjf $1     ;;
            *.tgz)       tar xzf $1     ;;
            *.zip)       unzip $1       ;;
            *.Z)         uncompress $1  ;;
            *.7z)        7z x $1        ;;
            *)           echo "'$1' cannot be extracted via extract()" ;;
        esac
    else
        echo "'$1' is not a valid file"
    fi
}
```

## .tmux.conf - конфигурация для tmux

```bash
# ~/.tmux.conf

# Установка префикса на Ctrl-a
unbind C-b
set -g prefix C-a

# Настройка панели статуса
set -g status-bg black
set -g status-fg white
set -g status-left '#[fg=green]#H'

# Настройка окон
setw -g window-status-current-bg red
setw -g window-status-current-fg white

# Настройка панелей
set -g pane-border-fg green
set -g pane-border-bg black
set -g pane-active-border-fg white
set -g pane-active-border-bg yellow

# Включение мыши
setw -g mouse on

# Удобные сочетания клавиш
bind r source-file ~/.tmux.conf \; display "Reloaded!"
bind | split-window -h
bind - split-window -v
```

## .vimrc - конфигурация для Vim

```vim
" ~/.vimrc

" Настройка синтаксиса и отступов
syntax on
set tabstop=4
set shiftwidth=4
set expandtab
set autoindent
set smartindent

" Настройка номеров строк
set number
set relativenumber

" Настройка поиска
set hlsearch
set incsearch
set ignorecase
set smartcase

" Настройка отображения
set showmatch
set ruler
set laststatus=2

" Настройка цветов
colorscheme default

" Полезные сочетания клавиш
let mapleader = ","
nnoremap <leader>w :w<CR>
nnoremap <leader>q :q<CR>
nnoremap <leader>e :e<Space>
```

## Инструкции по установке

### Для Bash
1. Скопируйте содержимое в файл `~/.bashrc`
2. Перезапустите терминал или выполните `source ~/.bashrc`

### Для Zsh
1. Установите Zsh: `sudo apt install zsh` (Ubuntu/Debian) или `brew install zsh` (macOS)
2. Скопируйте содержимое в файл `~/.zshrc`
3. Сделайте Zsh оболочкой по умолчанию: `chsh -s $(which zsh)`
4. Перезапустите терминал

### Для tmux
1. Установите tmux: `sudo apt install tmux` (Ubuntu/Debian) или `brew install tmux` (macOS)
2. Создайте файл `~/.tmux.conf` и скопируйте в него содержимое
3. Запустите tmux: `tmux`

### Для Vim
1. Создайте файл `~/.vimrc` и скопируйте в него содержимое
2. Запустите Vim для применения настроек

## Дополнительные рекомендации

### Установка Oh My Zsh (опционально)
```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Полезные плагины для Zsh
- zsh-autosuggestions
- zsh-syntax-highlighting
- zsh-completions

### Рекомендуемые шрифты для терминала
- Fira Code
- JetBrains Mono
- Source Code Pro
- Hack
