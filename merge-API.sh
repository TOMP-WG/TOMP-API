#!/bin/bash

# Define the work directory
path="./work/"

# Create directory if it doesn't exist
if [ ! -d "$path" ]; then
    mkdir -p "$path"
fi

ask='y'
join_cmd=""

# Handle arguments
if [ "$#" -ne 0 ]; then
    # If arguments are provided, they are treated as files
    files=("$@") # Store all arguments in an array
    drafts=() # No drafts by default if files are specified directly
    ask='n'
else
    echo "fetch files"
    # Find files matching "TOMP-API-*.yaml" in current directory
    # Using find to handle spaces in filenames more robustly, though globbing usually works
    readarray -t files < <(find . -maxdepth 1 -name "TOMP-API-*.yaml" -printf '%f\n')
    # Find files in "./draft modules/"
    readarray -t drafts < <(find "./draft modules/" -maxdepth 1 -name "TOMP-API-*.yaml" -printf '%f\n')
fi

# Special handling for 'all' argument
if [ "$1" == 'all' ]; then
    echo "fetch files"
    readarray -t files < <(find . -maxdepth 1 -name 'TOMP-API-*.yaml' -printf '%f\n')
    readarray -t drafts < <(find "./draft modules/" -maxdepth 1 -name "TOMP-API-*.yaml" -printf '%f\n')
    ask='n'
fi

# Special handling for 'mp' argument
if [ "$1" == 'mp' ]; then
    echo "merge mp files"
    files=() # Empty files array
    readarray -t drafts < <(find "./MP modules/" -maxdepth 1 -name "TOMP-API-*.yaml" -printf '%f\n')
    ask='n'
fi

echo "Files to process: ${files[@]}"

# Process main files
for arg in "${files[@]}"; do
    if [ "$arg" != 'TOMP-API-1-CORE.yaml' ]; then
        if [[ "$arg" != 'TOMP-API-2-OFFERS.yaml' && "$arg" != 'TOMP-API-4-PURCHASE.yaml' ]]; then
            defaultValue='N'
            display="Add $arg [y/N]"
        else
            defaultValue='Y'
            display="Add $arg [Y/n]"
        fi

        confirmation=""
        if [ "$ask" == 'y' ]; then
            read -p "$display " confirmation
        else
            confirmation='y'
        fi

        # If confirmation is empty, use defaultValue
        if [ -z "$confirmation" ]; then
            confirmation="$defaultValue"
        fi

        if [[ "$confirmation" == 'y' || "$confirmation" == 'Y' ]]; then
            dest_file="$path$arg"
            # Replace 'TOMP-API-1-CORE.yaml' etc. with empty string
            # The PowerShell's script does three replacements on the same file in sequence.
            # This means the second and third replacements are on the already modified content.
            # We'll mimic this by piping through sed sequentially.

            # First, copy the file to the destination, then apply replacements
            cp "$arg" "$dest_file"

            # Apply replacements. Note: sed -i modifies in place.
            sed -i "s/TOMP-API-1-CORE.yaml//g" "$dest_file"
            sed -i "s/TOMP-API-2-OFFERS.yaml//g" "$dest_file"
            sed -i "s/TOMP-API-4-PURCHASE.yaml//g" "$dest_file"

            echo "Processed $dest_file"
            join_cmd+=" $dest_file"
        fi
    fi
done

# Process draft files
for arg in "${drafts[@]}"; do
    confirmation=""
    if [ "$1" == 'mp' ]; then
        confirmation='y'
    else
        read -p "Add $arg [y/N] " confirmation
    fi

    if [[ "$confirmation" == 'y' || "$confirmation" == 'Y' ]]; then
        source_dir=""
        if [ "$1" == 'mp' ]; then
            source_dir="./MP modules/"
        else
            source_dir="./draft modules/"
        fi

        dest_file="$path$arg"
        # Copy the file first
        cp "${source_dir}${arg}" "$dest_file"
        # Apply replacement
        sed -i "s|../TOMP-API-1-CORE.yaml||g" "$dest_file" # Use | as delimiter for sed due to / in path

        join_cmd+=" $dest_file"
    fi
done

# Construct the final yaml-merge command
final_merge_cmd="yaml-merge $join_cmd ./TOMP-API-1-CORE.yaml > ./TOMP-API-BOM.yaml"
echo "$final_merge_cmd"
eval "$final_merge_cmd" # Execute the command

# Handle encoding and renaming
in_file='./TOMP-API-BOM.yaml'
out_file='./TOMP-API.yaml'

if [ "$1" == 'mp' ]; then
    out_file='./TOMP-API-MP.yaml'
fi

# Convert to UTF-8 without BOM
sed '1s/^\xEF\xBB\xBF//' "$in_file" > "$out_file"

# Clean up temporary files
rm -f "$in_file"
rm -rf "$path" # Remove the work directory and its contents
