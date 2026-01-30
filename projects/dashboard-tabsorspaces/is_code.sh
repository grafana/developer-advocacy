#!/bin/bash

code_mimes=(
  "text/x-c"
  "text/x-c++"
  "text/x-java"
  "text/x-csharp"
  "text/x-go"
  "text/x-rust"
  "text/x-swift"
  "text/x-kotlin"
  "text/x-python"
  "text/x-script.python"
  "text/x-perl"
  "text/x-ruby"
  "text/x-php"
  "text/x-bash"
  "text/x-shellscript"
  "text/x-tcl"
  "text/x-lua"
  "text/x-r"
  "text/x-julia"
  "text/x-elixir"
  "text/x-erlang"
  "text/x-clojure"
  "text/x-ocaml"
  "text/x-lisp"
  "text/x-haskell"
  "text/x-ada"
  "text/x-assembly"
  "text/x-visual-basic"
  "text/x-scheme"
  "text/css"
  "application/javascript"
  "application/x-javascript"
  "application/typescript"
  "application/x-typescript"
  "application/json"
  "application/xml"
  "application/x-toml"
  "application/x-yaml"
  "application/x-properties"
)

# Look for all files in the given path, but ignore hidden directories (to skip things like .git)
find "$1" -type f -path '*/.*' -prune -o -print0 | while IFS= read -r -d '' file 
do
  mime=$(file --brief --mime-type "$file")
  for code_type in "${code_mimes[@]}"
  do
    if [[ "$mime" == *"$code_type"* ]]
    then
      echo "$file"
      break
    fi
  done
done
