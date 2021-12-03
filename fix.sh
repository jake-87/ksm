sed --in-place "s/\;.*//g" $1 && sed "s/[[:space:]]*//g" --in-place $1 && tr --delete '\n' < $1 | cat > example-fixed.ksm
