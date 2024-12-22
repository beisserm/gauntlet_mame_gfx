
def invert_bits(byte):
    """Invert the bits of a single byte."""
    return ~byte & 0xFF

def load_plane(file_path):
    """Load a plane from the specified file path."""
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
            print(f"Loaded {len(data)} bytes from {file_path}")
            return data
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return None

def combine_planes(planes, is_inverted):
    """Combine bit planes into a single byte array."""
    combined_data = bytearray()
    num_bytes = len(planes[0])  # Assuming all planes are the same length

    for i in range(num_bytes):
        combined_byte = 0
        for plane_index in range(len(planes)):
            # Reverse bits if necessary
            value = reverse_bits(planes[plane_index][i]) if is_inverted else planes[plane_index][i]
            bit = (value >> 0) & 0x01  # Take the least significant bit
            combined_byte |= (bit << plane_index)

        combined_data.append(combined_byte)

    return combined_data

def main():
    # Define the paths to the EEPROM files
    first_set_paths = [
        '../rom/gauntlet/136037-111.1a',
        '../rom/gauntlet/136037-112.1b',
        '../rom/gauntlet/136037-113.1l',
        '../rom/gauntlet/136037-114.1mn',
    ]

    second_set_paths = [
        '../rom/gauntlet/136037-115.2a',
        '../rom/gauntlet/136037-116.2b',
        '../rom/gauntlet/136037-117.2l',
        '../rom/gauntlet/136037-118.2mn',
    ]

    # Set whether the ROM data is inverted
    is_inverted = True  # Change to False if the data is not inverted

    # Load the planes for each set
    first_set = [load_plane(path) for path in first_set_paths]
    second_set = [load_plane(path) for path in second_set_paths]

    # Combine the planes for the first set (4 files)
    combined_first_set = None
    try:
        combined_first_set = combine_planes(first_set, is_inverted)
        print("Successfully combined first set of planes.")
    except ValueError as e:
        print(f"Error during combining first set of planes: {e}")

    # Combine the planes for the second set (4 files)
    combined_second_set = None
    try:
        combined_second_set = combine_planes(second_set, is_inverted)
        print("Successfully combined second set of planes.")
    except ValueError as e:
        print(f"Error during combining second set of planes: {e}")

    # Append the second set to the first
    if combined_first_set is not None and combined_second_set is not None:
        combined_data = combined_first_set + combined_second_set  # Append second set to the first set

        # Save the combined data to a file
        with open('combined_graphics.bin', 'wb') as f:
            f.write(combined_data)
        print("Successfully saved the combined data.")

if __name__ == "__main__":
    main()