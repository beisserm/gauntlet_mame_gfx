import os

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

def combine_planes(planes):
    num_planes = len(planes)
    combined_data = bytearray()
    num_bytes = len(planes[0])  # Assuming all planes are the same length

    for i in range(num_bytes):
        combined_byte = 0
        for plane_index in range(num_planes):
            # Ensure to mask and combine correctly
            if i < len(planes[plane_index]):
                value = (planes[plane_index][i] >> 0) & 0x01  # Assuming 1bpp for this plane
                combined_byte |= (value << plane_index)

        if combined_byte < 0 or combined_byte > 255:
            raise ValueError(f"Byte value out of range: {combined_byte} at index {i}")
        
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

    # Load the planes
    first_set = [load_plane(path) for path in first_set_paths]
    second_set = [load_plane(path) for path in second_set_paths]

    combined_first_set = None
    combined_second_set = None

    # Combine the planes and handle potential errors
    try:
        combined_first_set = combine_planes(first_set)
        print("Successfully combined first set of planes.")
    except ValueError as e:
        print(f"Error during combining first set of planes: {e}")

    try:
        combined_second_set = combine_planes(second_set)
        print("Successfully combined second set of planes.")
    except ValueError as e:
        print(f"Error during combining second set of planes: {e}")

    # Save combined data to file if they were successfully combined
    if combined_first_set is not None:
        with open('combined_first_set.bin', 'wb') as f:
            f.write(combined_first_set)
    
    if combined_second_set is not None:
        with open('combined_second_set.bin', 'wb') as f:
            f.write(combined_second_set)

if __name__ == "__main__":
    main()