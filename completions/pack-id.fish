# Fish completion for pack-id
# Install: Copy to ~/.config/fish/completions/ or /usr/local/share/fish/vendor_completions.d/

# Complete .crbl files for the first argument
complete -c pack-id -n '__fish_is_first_arg' -F -a '(command ls *.crbl 2>/dev/null)' -d 'Input .crbl file'

# For the second argument, provide naming convention suggestions
complete -c pack-id -n '__fish_is_nth_arg 2' -a 'cc-' -d 'Community: cc-<product>-<tech>'
complete -c pack-id -n '__fish_is_nth_arg 2' -a 'cribl-' -d 'Cribl official: cribl-<product>-<tech>'

# Helper functions
function __fish_is_first_arg
    set -l cmd (commandline -opc)
    test (count $cmd) -eq 1
end

function __fish_is_nth_arg
    set -l n $argv[1]
    set -l cmd (commandline -opc)
    test (count $cmd) -eq $n
end

