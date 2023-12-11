# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# User specific aliases and functions
PATH=$PATH:$HOME/bin:$HOME/php/bin:$HOME/nginx/sbin:$HOME/memcached/bin:$HOME/redis/bin
export PATH

alias supervisorctl='supervisorctl -c /etc/supervisor/supervisord.conf'
alias ll='ls -lh --color=auto --time-style="+%Y-%m-%d %H:%M"'
