#!/bin/bash

#     Plane 0: 136037-111.1a
#     Plane 1: 136037-112.1b
#     Plane 2: 136037-113.1l
#     Plane 3: 136037-114.1mn

# Second Set of Planes (for the second part):

#     Plane 0: 136037-115.2a
#     Plane 1: 136037-116.2b
#     Plane 2: 136037-117.2l
#     Plane 3: 136037-118.2mn

# Define input and output files
set1=("136037-111.1a" "136037-112.1b" "136037-113.1l" "136037-114.1mn")
set2=("136037-115.2a" "136037-116.2b" "136037-117.2l" "136037-118.2mn")
output_file="combined_graphics_output.bin"

# Temporary files for interleaved sets
temp1="set1_interleaved.bin"
temp2="set2_interleaved.bin"

cd ../rom/gauntlet

# Function to interleave 4 files
interleave_files() {
    local files=("$@")
    local output="${files[-1]}"
    rm -f "$output"

    # Get the size of the smallest file
    file_size=$(stat -c%s "${files[0]}")

    # Interleave bytes from all input files
    for ((i=0; i<file_size; i++)); do
        for file in "${files[@]::${#files[@]}-1}"; do
            dd if="$file" of="$output" bs=1 skip="$i" count=1 conv=notrunc oflag=append status=none
        done
    done
}

# Interleave first set of files
interleave_files "${set1[@]}" "$temp1"

# Interleave second set of files
interleave_files "${set2[@]}" "$temp2"

# Combine the two interleaved files into the final output
cat "$temp1" "$temp2" > "$output_file"

# Clean up temporary files
rm -f "$temp1" "$temp2"

cd -

echo "Combined and interleaved ROM data written to $output_file"