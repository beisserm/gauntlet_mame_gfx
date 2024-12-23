#!/usr/bin/env python3

import datetime

def write_bitplanes_to_4bpp(set_paths, output_path, flags):
    # Open all files for reading
    set_files = [open(path, 'rb') for path in set_paths]

    # Initialize combined_byte before entering the loop
    #combined_byte = 0

    try:
        # Open output file for writing
        with open(output_path, flags) as output_file:
            while True:
                # Read one byte from each file in the set
                set_bytes = [file.read(1) for file in set_files]

                # If all files return empty bytes, we've finished processing
                if not any(set_bytes):
                    break

                # # Combine the bytes from the set files
                # for i, byte in enumerate(set_bytes):
                #     if byte:  # If byte is not empty
                #         # Combine bytes correctly based on their positions
                #         combined_byte |= ord(byte) << (i * 8)  # Shift the byte depending on the position
                        
                # # Write the combined byte to the output file
                # output_file.write(bytes([combined_byte & 0xFF]))  # Write only the least significant byte
                # combined_byte = 0  # Reset for the next iteration

                # Write the bytes from each file in sequence to the output file
                #output_file.write(b''.join(set_bytes))
                for byte in set_bytes:
                #     inverted_byte = ~byte[0] & 0xFF  # Invert the bits of the byte
                #     output_file.write(bytes([inverted_byte]))

                    #if byte:  # If byte is not empty (i.e., not EOF)
                    output_file.write(byte)

    finally:
        # Close all files
        for file in set_files:
            file.close()

def main():
    # Define the file paths for the bitplanes (first set)
    first_set_paths = [
        '../rom/gauntlet/136037-111.1a',
        '../rom/gauntlet/136037-112.1b',
        '../rom/gauntlet/136037-113.1l',
        '../rom/gauntlet/136037-114.1mn',
    ]

    # Reverse the order of the first set paths
    #first_set_paths = first_set_paths[::-1]

    # Define the file paths for the bitplanes (second set)
    second_set_paths = [
        '../rom/gauntlet/136037-115.2a',
        '../rom/gauntlet/136037-116.2b',
        '../rom/gauntlet/136037-117.2l',
        '../rom/gauntlet/136037-118.2mn',
    ]

    #second_set_paths = second_set_paths[::-1]

    # Generate timestamp in yy-mm-dd-hh-mm format
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H_%M")

    # Define the output file path with the timestamp
    output_path = f'output_4bpp_inverted_{timestamp}.bin'

    # Process the first set of files
    write_bitplanes_to_4bpp(first_set_paths, output_path, 'wb')

    # Process the second set of files and append to the same output file
    write_bitplanes_to_4bpp(second_set_paths, output_path, 'ab')

if __name__ == "__main__":
    main()
