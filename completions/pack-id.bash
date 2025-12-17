# Bash completion for pack-id
# Install: Copy to /usr/local/etc/bash_completion.d/ or source directly

_pack_id_completion() {
    local cur prev words cword
    _init_completion || return

    # First argument: complete .crbl files
    if [[ $cword -eq 1 ]]; then
        COMPREPLY=($(compgen -f -X '!*.crbl' -- "$cur"))
        return 0
    fi

    # Second argument: suggest naming conventions
    if [[ $cword -eq 2 ]]; then
        # Provide naming convention suggestions
        local suggestions=("cc-" "cribl-")
        COMPREPLY=($(compgen -W "${suggestions[*]}" -- "$cur"))
        
        # Show hint about naming conventions (if compopt is available)
        if type compopt &>/dev/null; then
            compopt -o nospace
        fi
        
        return 0
    fi
}

complete -F _pack_id_completion pack-id

