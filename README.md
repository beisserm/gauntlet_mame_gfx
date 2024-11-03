# gauntlet_mame_gfx

In *Gauntlet* (1985), the sprites were designed in a pixelated, low-resolution format typical of arcade games from that era. Here’s an overview of their format and characteristics:

1. **Pixel Dimensions and Resolution**:
   - The sprites were generally small and used low-resolution graphics to fit the hardware limitations. Commonly, character sprites were around **16x16 pixels** or **32x32 pixels** for larger, more detailed characters like bosses.
   
2. **Limited Color Palette**:
   - Due to hardware constraints, the sprites used a limited color palette. Most sprites had **8–16 colors** to stay within the limits of 16-bit color space or similar graphics hardware of the time.

3. **Tile-Based Structure**:
   - Sprites in *Gauntlet* were often **tile-based**; this meant they were made of multiple smaller blocks (tiles) arranged to create the larger character or item sprites.
   - This approach saved memory, as common tile patterns could be reused across different sprites and game objects.

4. **Orientation and Animation Frames**:
   - The character sprites had **directional sprites** for facing different directions (left, right, up, down) to allow for smooth character movement.
   - Sprites had **minimal animation frames** (around 2-4 frames per action) to conserve memory while still giving the illusion of movement, especially for walking and attacking.

5. **Transparencies**:
   - Transparent pixels were used to allow the background to show through, as characters and items needed to move across various terrains. This transparency was achieved by designating certain color indexes as “invisible.”

6. **Character Distinctiveness**:
   - Each player character had a unique color scheme (e.g., Red for Thor, Blue for Merlin, Green for Thyra, and Yellow for Questor) to differentiate them easily, while enemy sprites were typically uniform with slight variations in color to indicate different types or difficulty levels.

The combination of these factors made the *Gauntlet* sprites efficient and visually distinct, even with the era's limitations on graphical fidelity.

In *Gauntlet* (1985), the sprites were likely designed with **4 bits per pixel** (4bpp), allowing each pixel to be represented by one of **16 possible colors**. This bit depth aligns with the arcade hardware of the time, which often used limited color palettes to conserve memory.

Here’s how 4bpp worked in *Gauntlet*:

- **Color Palette**: The sprites could select from a palette of 16 colors, which was stored in memory separately and applied across all sprites and backgrounds.
- **Efficient Memory Use**: Using 4bpp meant each sprite used half a byte (4 bits) per pixel, which allowed for a good balance between color variety and low memory usage.
- **Transparency Handling**: Typically, one color index in the palette would be set aside to represent transparency, allowing the background to show through without storing extra data for transparent regions.

The 4bpp approach made *Gauntlet*'s sprites colorful and efficient, essential for the game's fast-paced action and need for smooth performance on arcade hardware.

Yes, *Gauntlet* (1985) used **4bpp planar graphics**, where each bitplane was stored separately in a dedicated EPROM chip. Here’s how that worked:

1. **4bpp Planar Format**:
   - In 4bpp planar graphics, each pixel’s color is determined by combining bits from four separate planes.
   - Each plane represented one bit of color information across the entire sprite, and when combined, the four planes could produce 16 different colors (2^4 = 16).

2. **Storage in Separate EPROMs**:
   - Each bitplane was stored in its own EPROM chip. For example, Plane 0 would be in one EPROM, Plane 1 in another, and so on up to Plane 3.
   - The arcade hardware would read the data from each EPROM simultaneously, combining the bit values from each plane to produce the final color index for each pixel.

3. **Efficient Rendering**:
   - This approach was efficient for arcade systems of the time, as it allowed for parallel reading from the EPROMs, speeding up the rendering of graphics on screen.
   - By storing each plane in separate EPROMs, it was easier to replace or update specific graphical elements without affecting the entire sprite set.

4. **Transparency and Color Masking**:
   - As mentioned, one of the color values (often the 0 index) was used for transparency, so any pixel with a 0 in all four bitplanes would be rendered as transparent.

This bitplane setup was a common technique in the 1980s arcade games, optimizing both storage and processing for the hardware while still allowing colorful and distinctive sprites.

Mapping the EPROMs in *Gauntlet*’s hardware schematic to the MAME ROM files involves identifying which EPROMs correspond to specific sections of the game data (e.g., graphics, sound, program code). MAME emulates these components based on how they were physically organized in the original arcade hardware.

Here's a general approach for mapping:

1. **Identify EPROM Designations in the Schematic**:
   - In the *Gauntlet* schematic, each EPROM chip should have a label (e.g., **136037-1045** for *Gauntlet*). The labeling convention often includes a prefix (for the game board set) and a numeric suffix indicating its function or sequence.
   - Look for indications of where these EPROMs are connected. The graphics EPROMs are usually connected to the video subsystem, while sound and program EPROMs connect to their respective parts of the circuit.

2. **Match EPROMs to MAME ROM Files**:
   - In MAME, the ROM files are usually named based on the original EPROM labels from the arcade PCB schematics. For example, a graphics ROM file might be named **136037.1045** or **gauntlet.1045** in the MAME ROM set, directly matching the EPROM label.
   - You can cross-reference the EPROM label in the schematic with MAME’s **ROM definitions** in its driver file for *Gauntlet* (found in the source code under `mame/src/mame/drivers/gauntlet.cpp` or similar paths). The driver file defines the ROMs used and their memory locations.

3. **Planar Graphics ROM Mapping**:
   - For graphics, the 4bpp planar format means each bitplane is stored in separate EPROMs. In the MAME ROM set, these will appear as sequential files for each plane. For example:
     - **gauntlet.1045** for Plane 0
     - **gauntlet.1046** for Plane 1
     - **gauntlet.1047** for Plane 2
     - **gauntlet.1048** for Plane 3
   - Each file corresponds to one bitplane, so MAME combines these files at runtime to render each sprite with the correct colors.

4. **Confirming with MAME Tools**:
   - MAME has tools and logs that help verify the correct ROM loading. Running MAME with verbose logging (`mame -verbose gauntlet`) shows how each ROM is mapped in memory.
   - Additionally, using a utility like `romcmp` (for comparing ROM files) or examining the **checksum/hash** in the MAME ROM definition can help ensure each ROM file correctly matches the expected EPROM content.

5. **Check for Additional ROM Details in the MAME Driver Documentation**:
   - Sometimes, the MAME driver source file includes comments with further mapping details, such as which EPROM corresponds to specific game assets (e.g., sprites, tilemaps, or sound).
   - This information helps validate that the right ROM files are mapped to the expected EPROMs and hardware functions.

With this approach, you should be able to map the EPROMs in the schematic to their corresponding files in the MAME ROM set accurately. If you have a specific schematic or MAME ROM set, I can provide more tailored guidance.

*Gauntlet* (1985) by Atari used multiple EPROMs for its program code, graphics, and sound, with each one labeled for specific functions. Here’s a list of commonly identified EPROMs used for the original *Gauntlet* arcade board:

### Program ROMs
- **136037-1050** to **136037-1053**: These contain the main game code and are connected to the CPU.
- **136037-2050** to **136037-2053**: Alternate program set; often used for different regional versions or revisions.

### Graphics ROMs (Planar Graphics Data)
- **136037-1045**: Graphics Plane 0
- **136037-1046**: Graphics Plane 1
- **136037-1047**: Graphics Plane 2
- **136037-1048**: Graphics Plane 3

These four ROMs collectively hold the sprite data in 4bpp planar format, with each plane corresponding to one of the ROMs above.

### Sound ROMs
- **136037-1011**: Sound effects
- **136037-1012**: Additional sound effects
- **136037-1013**: Speech samples or additional effects (varies by board revision)

### Other ROMs
- **136037-1049**: Tilemap data, which includes background and environmental details.
- **136037-1010**: Often used for palette or color lookup tables (CLUT), to map the 4-bit pixel data to RGB values on screen.

### Notes for MAME Users
In MAME, these ROM files are typically named according to these labels (e.g., **gauntlet.1045** for the first graphics ROM). MAME may combine some of these files in sets to accurately emulate the original board layout. Different versions (such as *Gauntlet II* or regional variants) may have additional ROM files, or the program ROMs might differ slightly in labeling.

If you have any questions about the ROMs for a specific revision of *Gauntlet*, I can help with more detailed mapping!

The code snippet you provided is part of the graphics definitions in the MAME driver for *Gauntlet*. Let's break down what each section does:

### Overview of the Code

1. **gfx_layout Structure**: 
   - The `gfx_layout` structure defines how graphics are organized and stored in memory for the game's sprites and tilemaps. It specifies parameters such as size, color depth, and the arrangement of pixel data.

### Specific Layouts

#### 1. `anlayout`
```cpp
static const gfx_layout anlayout =
{
    8, 8,                       // Width and height of each sprite (8x8 pixels)
    RGN_FRAC(1, 1),            // Number of regions: 1 region (all data in one plane)
    2,                          // Number of bits per pixel (2 bpp, allowing for 4 colors)
    { 0, 4 },                  // Offsets to the bit planes in the data
    { 0, 1, 2, 3, 8, 9, 10, 11 }, // X offsets for pixel data
    { 0*16, 1*16, 2*16, 3*16, 4*16, 5*16, 6*16, 7*16 }, // Y offsets for pixel data
    8*16                       // Total size of one sprite (16 bytes)
};
```
- **8x8 Pixels**: Each sprite is 8x8 pixels.
- **1 Region**: All sprite data is stored in a single region.
- **2 Bits per Pixel**: This allows for 4 different colors (2^2).
- **Bit Plane Offsets**: The `{0, 4}` array indicates where the bit planes are stored in the data, meaning the first color data comes from the first half of the sprite data.
- **Pixel Offsets**: The `{0, 1, 2, 3, 8, 9, 10, 11}` array determines how pixels are arranged horizontally, while the Y offsets indicate how rows are arranged vertically in the memory.
- **Total Size**: The total size of one sprite is 16 bytes.

#### 2. `pfmolayout`
```cpp
static const gfx_layout pfmolayout =
{
    8, 8,                       // Width and height of each tile (8x8 pixels)
    RGN_FRAC(1, 4),            // Number of regions: 4 regions (data is divided into 4 planes)
    4,                          // Number of bits per pixel (4 bpp, allowing for 16 colors)
    { RGN_FRAC(3, 4), RGN_FRAC(2, 4), RGN_FRAC(1, 4), RGN_FRAC(0, 4) }, // Offsets for each bit plane
    { 0, 1, 2, 3, 4, 5, 6, 7 }, // X offsets for pixel data
    { 0*8, 1*8, 2*8, 3*8, 4*8, 5*8, 6*8, 7*8 }, // Y offsets for pixel data
    8*8                        // Total size of one tile (8 bytes)
};
```
- **8x8 Pixels**: Each tile is also 8x8 pixels.
- **4 Regions**: The data is split into 4 regions (bit planes), suitable for 4 bits per pixel.
- **4 Bits per Pixel**: This allows for 16 different colors (2^4).
- **Bit Plane Offsets**: The `{RGN_FRAC(3, 4), RGN_FRAC(2, 4), RGN_FRAC(1, 4), RGN_FRAC(0, 4)}` array specifies how to read each of the four bit planes, which are arranged sequentially in memory.
- **Pixel and Y Offsets**: Similar to the previous layout, it specifies how to access the pixel data.
- **Total Size**: The total size of one tile is 8 bytes.

### GFXDECODE_START and GFXDECODE_ENTRY

```cpp
static GFXDECODE_START( gfx_gauntlet )
    GFXDECODE_ENTRY( "gfx2", 0, pfmolayout,  256, 32 )
    GFXDECODE_ENTRY( "gfx1", 0, anlayout,      0, 64 )
GFXDECODE_END
```
- **GFXDECODE_START**: This macro begins the definition of a graphics decoding table for *Gauntlet*.
- **GFXDECODE_ENTRY**:
  - The first argument is the tag for the ROM (e.g., `"gfx2"` or `"gfx1"`), which corresponds to the ROM file names defined in the driver.
  - The second argument is the starting offset in the ROM data (usually 0).
  - The third argument specifies the layout (e.g., `pfmolayout` or `anlayout`) defined earlier.
  - The fourth argument specifies the color base (e.g., 256 or 0), which determines the starting color index for the graphics.
  - The fifth argument specifies the total number of colors to use for the graphics (e.g., 32 or 64).

### Summary
Overall, this code defines how the sprite and tile graphics for *Gauntlet* are structured in memory and how they are decoded from ROM data during emulation. The layouts define the pixel organization and how many bits are used per pixel, while the `GFXDECODE` section ties this information to specific ROM files to facilitate accurate rendering of graphics in the game.

To map the MAME ROM entries you provided to the graphics ROMs used in *Gauntlet*, you can follow the information in the code snippet regarding the ROM regions, sizes, and associated layouts. Here's how to do that step-by-step:

### Understanding the MAME Code

1. **ROM_REGION Definitions**:
   - The `ROM_REGION` macro defines a memory region in the emulated hardware. Each region is associated with a specific part of the graphics or game data.
   - The `"gfx1"` and `"gfx2"` labels correspond to the graphics layouts defined earlier in the driver.

2. **ROM_LOAD Entries**:
   - Each `ROM_LOAD` statement specifies a ROM file to be loaded into the corresponding region, along with its starting offset, size, and CRC/SHA1 checksums for validation.

### Mapping the ROMs

#### GFX1 Region
```cpp
ROM_REGION( 0x04000, "gfx1", 0 )
ROM_LOAD( "136037-104.6p",   0x000000, 0x004000, CRC(6c276a1d) SHA1(ec383a8fdcb28efb86b7f6ba4a3306fea5a09d72) ) // 27128, second half 0x00
```
- **Region Size**: `0x04000` (16 KB)
- **File Loaded**: `136037-104.6p`
- **Details**: This ROM contains the graphics data for the layout `anlayout` (8x8 sprites). It is loaded into the `gfx1` region, which corresponds to character graphics. This specific ROM is likely used for the player character sprites.

#### GFX2 Region
```cpp
ROM_REGION( 0x40000, "gfx2", ROMREGION_INVERT )
ROM_LOAD( "136037-111.1a",   0x000000, 0x008000, CRC(91700f33) SHA1(fac1ce700c4cd46b643307998df781d637f193aa) )
ROM_LOAD( "136037-112.1b",   0x008000, 0x008000, CRC(869330be) SHA1(5dfaaf54ee2b3c0eaf35e8c17558313db9791616) )
ROM_LOAD( "136037-113.1l",   0x010000, 0x008000, CRC(d497d0a8) SHA1(bb715bcec7f783dd04151e2e3b221a72133bf17d) )
ROM_LOAD( "136037-114.1mn",  0x018000, 0x008000, CRC(29ef9882) SHA1(91e1465af6505b35cd97434c13d2b4d40a085946) )
ROM_LOAD( "136037-115.2a",   0x020000, 0x008000, CRC(9510b898) SHA1(e6c8c7af1898d548f0f01e4ff37c2c7b22c0b5c2) )
ROM_LOAD( "136037-116.2b",   0x028000, 0x008000, CRC(11e0ac5b) SHA1(729b7561d59d94ef33874a134b97bcd37573dfa6) )
ROM_LOAD( "136037-117.2l",   0x030000, 0x008000, CRC(29a5db41) SHA1(94f4f5dd39e724570a0f54af176ad018497697fd) )
ROM_LOAD( "136037-118.2mn",  0x038000, 0x008000, CRC(8bf3b263) SHA1(683d900ab7591ee661218be2406fb375a12e435c) )
```
- **Region Size**: `0x40000` (256 KB)
- **Files Loaded**: 
  - `136037-111.1a`
  - `136037-112.1b`
  - `136037-113.1l`
  - `136037-114.1mn`
  - `136037-115.2a`
  - `136037-116.2b`
  - `136037-117.2l`
  - `136037-118.2mn`
  
- **Details**: These ROMs are likely used for the tilemap graphics and environmental elements in the game. The `pfmolayout` defined in the driver indicates that these tiles are organized in a 4bpp planar format.

### Mapping to Graphics ROMs

- **gfx1 (anlayout)**:
  - **ROM**: `136037-104.6p` 
  - **Use**: Contains the sprite graphics for player characters (8x8 pixel sprites, 2bpp).

- **gfx2 (pfmolayout)**:
  - **ROMs**: 
    - `136037-111.1a`
    - `136037-112.1b`
    - `136037-113.1l`
    - `136037-114.1mn`
    - `136037-115.2a`
    - `136037-116.2b`
    - `136037-117.2l`
    - `136037-118.2mn`
  - **Use**: Contains the tile graphics for the game environment and backgrounds (8x8 pixel tiles, 4bpp).

### Conclusion

To summarize, the mapping you are looking for is as follows:

- The **gfx1 region** with the single ROM `136037-104.6p` is used for the character sprites.
- The **gfx2 region** with multiple ROMs (`136037-111.1a` to `136037-118.2mn`) contains the tilemap graphics and background elements, suitable for use with the `pfmolayout`.

This understanding allows MAME to properly render graphics during gameplay by loading the necessary data from the specified ROMs based on the defined graphics layouts.

Yes, that's correct! For the `gfx2` region in the *Gauntlet* MAME driver, you have multiple ROMs that are organized in a way that requires reading multiple files to reconstruct the sprite data for the graphics.

### Breakdown of the GFX2 Region

The **`gfx2` region** has the following ROM files loaded:

1. **ROMs Loaded**:
   - `136037-111.1a` (0x000000)
   - `136037-112.1b` (0x008000)
   - `136037-113.1l` (0x010000)
   - `136037-114.1mn` (0x018000)
   - `136037-115.2a` (0x020000)
   - `136037-116.2b` (0x028000)
   - `136037-117.2l` (0x030000)
   - `136037-118.2mn` (0x038000)

### Understanding the Planar Graphics Layout

The **`pfmolayout`** defined in the driver indicates that the graphics data for tiles is stored in a **4bpp (bits per pixel)** format, meaning that each pixel is represented by 4 bits (allowing for 16 colors). Since it's a planar format, the data is divided into separate planes for each bit.

#### For Each Tile (8x8 Pixels):
- **Four Bit Planes**: Each tile's pixel data is divided into four separate planes:
  - Plane 0
  - Plane 1
  - Plane 2
  - Plane 3

### Mapping ROMs to Planes

Typically, for a 4bpp planar layout, the ROMs are organized such that you might have pairs of ROMs to represent the different planes, depending on how the graphics data is structured. Here’s a common organization:

1. **First Set of Planes** (for the first part of the graphics):
   - **Plane 0**: `136037-111.1a`
   - **Plane 1**: `136037-112.1b`
   - **Plane 2**: `136037-113.1l`
   - **Plane 3**: `136037-114.1mn`

2. **Second Set of Planes** (for the second part):
   - **Plane 0**: `136037-115.2a`
   - **Plane 1**: `136037-116.2b`
   - **Plane 2**: `136037-117.2l`
   - **Plane 3**: `136037-118.2mn`

### To Recreate Sprite Data:
To reconstruct a full set of sprite data or tile graphics, you would typically need to read from all four files corresponding to a specific tile or sprite:

- For each tile:
  - Read 8 bytes from each of the four ROMs (for example, if you are combining tiles from `136037-111` to `136037-114` or `136037-115` to `136037-118`).
  - Combine the data according to the planar layout to create a complete representation of that tile.

### Conclusion

Yes, you would indeed need to read the four files corresponding to each bit plane to recreate the complete sprite or tile graphics data for the `gfx2` region in *Gauntlet*. This method allows MAME to accurately emulate the way the original hardware would have rendered these graphics, taking advantage of the 4bpp planar storage method used in the game's ROMs.

Yes, the values in parentheses in the **Breakdown of the GFX2 Region** section represent the **offsets** within the specified ROM region. Here’s a more detailed explanation:

### ROM_LOAD Entries Breakdown

The syntax for each `ROM_LOAD` entry looks like this:

```cpp
ROM_LOAD( "filename", offset, size, CRC(checksum) SHA1(hash) )
```

- **`filename`**: The name of the ROM file being loaded.
- **`offset`**: The starting position in the memory region where this ROM data will be loaded. This is specified in bytes.
- **`size`**: The size of the ROM data being loaded, also specified in bytes.
- **`CRC`** and **`SHA1`**: These are checksums used for verifying the integrity of the ROM data.

### Example from GFX2 Region

Using the example from the GFX2 region you provided earlier:

```cpp
ROM_LOAD( "136037-111.1a",   0x000000, 0x008000, CRC(91700f33) SHA1(fac1ce700c4cd46b643307998df781d637f193aa) )
```
- **`"136037-111.1a"`**: This is the ROM file name.
- **`0x000000`**: This indicates that this ROM file starts at offset 0 in the `gfx2` memory region.
- **`0x008000`**: This indicates that the size of the ROM data being loaded is 8,000 bytes (or 32 KB).
  
The subsequent entries in the GFX2 region will have their own offsets that indicate where each ROM file's data will be loaded in relation to the start of the `gfx2` region.

### Full GFX2 Region Breakdown

Here’s how the offsets look for the other ROMs:

1. `136037-111.1a` (Offset: **0x000000**, Size: **0x008000**)
2. `136037-112.1b` (Offset: **0x008000**, Size: **0x008000**)
3. `136037-113.1l` (Offset: **0x010000**, Size: **0x008000**)
4. `136037-114.1mn` (Offset: **0x018000**, Size: **0x008000**)
5. `136037-115.2a` (Offset: **0x020000**, Size: **0x008000**)
6. `136037-116.2b` (Offset: **0x028000**, Size: **0x008000**)
7. `136037-117.2l` (Offset: **0x030000**, Size: **0x008000**)
8. `136037-118.2mn` (Offset: **0x038000**, Size: **0x008000**)

### Conclusion

In summary, the values in parentheses are indeed offsets that determine where each ROM file's data is loaded within the `gfx2` region in memory. This structured loading allows the emulator to accurately reconstruct the graphics data used in the game.

Yes, you can use the `dd` command in Linux to extract data from each of the ROM files and combine the planes into a single file. Since the graphics data in the *Gauntlet* ROMs is stored in a planar format, you will need to read each plane from the corresponding files and interleave the data as needed.

### Steps to Use `dd` for Extracting Planar Data

1. **Identify the ROM Files**: Make sure you have the ROM files you need to work with.

2. **Determine the Offsets and Sizes**: You already know the offsets and sizes for each ROM. For example, each file in the `gfx2` region has a size of `0x008000` (32 KB).

3. **Use `dd` to Extract Data**:
   - You can extract data from each ROM file and write it to a temporary file.
   - After extracting all the necessary planes, you can then combine them into a single file for planar graphics manipulation.

### Example Commands

Assuming you have the ROM files in your current directory:

#### Extracting Plane Data

Here's an example of how to use `dd` to extract the planar data:

1. **Extracting Each Plane**:

```bash
# Extract Plane 0 from 136037-111.1a
dd if=136037-111.1a of=plane0.bin bs=1 count=32768 skip=0

# Extract Plane 1 from 136037-112.1b
dd if=136037-112.1b of=plane1.bin bs=1 count=32768 skip=0

# Extract Plane 2 from 136037-113.1l
dd if=136037-113.1l of=plane2.bin bs=1 count=32768 skip=0

# Extract Plane 3 from 136037-114.1mn
dd if=136037-114.1mn of=plane3.bin bs=1 count=32768 skip=0
```

2. **Combining the Planes**:

After extracting the planes into separate files, you will need to interleave the data. This can be done with a script or a binary file manipulation tool, as `dd` itself does not support complex interleaving directly.

### Interleaving Example Script (Bash)

You can write a small script to interleave the extracted data:

```bash
#!/bin/bash

# Output file
output_file="combined.bin"
# Clear the output file
> "$output_file"

# Number of pixels per tile (8x8) = 64 pixels
# Loop through each byte for the number of tiles
for ((i=0; i<32768; i++)); do
    # Read each plane and output to the combined file in the right order
    for plane in {0..3}; do
        # Use dd to read a byte from each plane file
        dd if=plane"$plane".bin bs=1 count=1 skip=$i 2>/dev/null >> "$output_file"
    done
done
```

### Running the Script

1. Save the script to a file, e.g., `combine_planes.sh`.
2. Make it executable:
   ```bash
   chmod +x combine_planes.sh
   ```
3. Run the script:
   ```bash
   ./combine_planes.sh
   ```

### Conclusion

Using the `dd` command in conjunction with a script allows you to efficiently extract and combine planar graphics data from the *Gauntlet* ROM files. After combining, you will have a single file that you can use in a ROM hacking tool to work with the sprite data.


# Gauntlet Game PCB Assembly Parts List

| Designator | Description                              | Part No.     |
|------------|------------------------------------------|--------------|
| 1A         | Integrated Circuit, EPROM, 300ns         | 136037-111   |
| 1B         | Integrated Circuit, EPROM, 300ns         | 136037-112   |
| 1K         | Integrated Circuit, Custom, SLAGS        | 137415-101   |
| 1L         | Integrated Circuit, EPROM, 300ns         | 136037-113   |
| 1M/N       | Integrated Circuit, EPROM, 300ns         | 136037-114   |
| 1W         | Integrated Circuit, RAM, 2149H-2         | 137199-002   |
| 1X         | Integrated Circuit, RAM, 2149H-2         | 137199-002   |
| 2A         | Integrated Circuit, EPROM, 300ns         | 136037-115   |
| 2B         | Integrated Circuit, EPROM, 300ns         | 136037-116   |
| 2K         | Integrated Circuit, Custom, SLAGS        | 137415-101   |
| 2L         | Integrated Circuit, EPROM, 300ns         | 136037-117   |
| 2M/N       | Integrated Circuit, EPROM, 300ns         | 136037-118   |
| 2W         | Integrated Circuit, RAM, 2149H-2         | 137199-002   |
| 2X         | Integrated Circuit, RAM, 2149H-2         | 137199-002   |
| 3C         | Integrated Circuit, 74LS374              | 37-74LS374   |
| 3D         | Integrated Circuit, 74LS244              | 37-74LS244   |
| 3E         | Integrated Circuit, 74LS157              | 37-74LS157   |
| 3F         | Integrated Circuit, 74LS138              | 137177-001   |
| 3J         | Integrated Circuit, 74LS244              | 37-74LS244   |
| 3K         | Integrated Circuit, 74LS273              | 37-74LS273   |
| 3L         | Integrated Circuit, 74LS283              | 137204-001   |
| 3M         | Integrated Circuit, 74LS283              | 137204-001   |
| 3N         | Integrated Circuit, 74LS174              | 37-74LS174   |
| 3P         | Integrated Circuit, 74LS175              | 37-74LS175   |
| 3R         | Integrated Circuit, 74LS163A             | 37-74LS163A  |
| 3S         | Integrated Circuit, 74LS163A             | 37-74LS163A  |
| 3T         | Integrated Circuit, 74LS163A             | 37-74LS163A  |
| 3U         | Integrated Circuit, 74LS163A             | 37-74LS163A  |
| 3W         | Integrated Circuit, 74LS163A             | 37-74LS163A  |
| 3X         | Integrated Circuit, 74LS163A             | 37-74LS163A  |
| 4C         | Integrated Circuit, 74LS273              | 37-74LS273   |
| 4D         | Integrated Circuit, 74LS175              | 37-74LS175   |
| 4E         | Integrated Circuit, 74LS378              | 137305-001   |
| 4F         | Integrated Circuit, 74LS163A             | 37-74LS163A  |
| 4J         | Integrated Circuit, 74LS86               | 37-74LS86    |
| 4K         | Integrated Circuit, 74LS374              | 37-74LS374   |
| 4L         | Integrated Circuit, 74LS169              | 137109-001   |
| 4M         | Integrated Circuit, 74LS169              | 137109-001   |
| 4N         | Integrated Circuit, 74LS273              | 37-74LS273   |
| 4P         | Integrated Circuit, 74LS174              | 37-74LS174   |
| 4R         | Integrated Circuit, PROM, 82S129         | 136037-103   |
| 4S         | Integrated Circuit, 74LS32               | 37-74LS32    |
| 4T         | Integrated Circuit, 74LS86               | 37-74LS86    |
| 7S         | Integrated Circuit, 74LS174              | 37-74LS174   |
| 7T         | Integrated Circuit, 74LS08               | 37-74LS08    |
| 7U         | Integrated Circuit, PROM, 82S147         | 136037-101   |
| 7W         | Integrated Circuit, 74LS04               | 37-74LS04    |
| 7X         | Integrated Circuit, 74LS32               | 37-74LS32    |
| 8C         | Integrated Circuit, 74LS253              | 37-74LS253   |
| 8D         | Integrated Circuit, 74LS253              | 37-74LS253   |
| 8E         | Integrated Circuit, 74LS253              | 37-74LS253   |
| 8F         | Integrated Circuit, 74LS378              | 137305-001   |
| 8J         | Integrated Circuit, 74LS378              | 137305-001   |
| 8K         | Integrated Circuit, 74LS153              | 37-74LS153   |
| 8L         | Integrated Circuit, 74LS153              | 37-74LS153   |
| 8M         | Integrated Circuit, 74LS244              | 37-74LS244   |
| 8P         | Integrated Circuit, Custom, SYNGEN       | 137419-103   |
| 8T         | Integrated Circuit, 74LS139              | 37-74LS139   |
| 8U         | Integrated Circuit, 74LS253              | 37-74LS253   |
| 9A         | Integrated Circuit, EPROM, 200ns         | 136037-107   |
| 9B         | Integrated Circuit, EPROM, 200ns         | 137037-108   |
| 9C         | Integrated Circuit, 74S139               | 37-74S139    |
| 9D         | Integrated Circuit, 74S157               | 37-74S157    |
| 9E         | Integrated Circuit, 74LS245              | 37-74LS245   |
| 9F         | Integrated Circuit, 74LS244              | 37-74LS244   |
| 9J         | Integrated Circuit, 74LS373              | 37-74LS373   |
| 9K         | Integrated Circuit, 74LS245              | 37-74LS245   |
| 9L         | Integrated Circuit, RAM, 2149H-3         | 137199-001   |
| 9M         | Integrated Circuit, RAM, 2149H-3         | 137199-001   |
| 9N         | Integrated Circuit, 74LS273              | 37-74LS273   |
| 9P         | Integrated Circuit, 74LS260              | 137332-001   |
| 9R         | Integrated Circuit, 74S04                | 37-74S04     |
| 9S         | Integrated Circuit, 74S74                | 37-74S74     |
| 9T         | Integrated Circuit, 7406                 | 37-7406      |
| 10A        | Integrated Circuit, EPROM, 200ns         | 136037-105   |
| 10B        | Integrated Circuit, EPROM, 200ns         | 136037-106   |
| 10C        | Integrated Circuit, SLAPSTIC             | 137412-104   |
| 10D        | Integrated Circuit, 74LS138              | 137177-001   |
| 10E        | Integrated Circuit, 74LS245              | 37-74LS245   |
| 10F        | Integrated Circuit, 74LS244              | 37-74LS244   |
| 10J        | Integrated Circuit, 74LS373              | 37-74LS373   |
| 10K        | Integrated Circuit, 74LS245              | 37-74LS245   |
| 10L        | Integrated Circuit, RAM, 2149H-3         | 137199-001   |
| 10M        | Integrated Circuit, RAM, 2149H-3         | 137199-001   |
| 10N        | Integrated Circuit, 74LS273              | 37-74LS273   |
| 10P        | Integrated Circuit, 74LS260              | 137332-001   |
| 10T        | Integrated Circuit, 7406                 | 37-7406      |
| 14U        | Integrated Circuit, 4066B                | 37-4066      |
| 14/15O     | Integrated Circuit, 4066B                | 37-4066      |
| 15L        | Integrated Circuit, POKEY                | 137430-001   |
| 15P        | Integrated Circuit, 74LS245              | 37-74LS245   |
| 15R        | Integrated Circuit, YM2151               | 137401-001   |
| 15S        | Integrated Circuit, 74LS273              | 37-74LS273   |
| 15T        | Integrated Circuit, YM3012               | 137402-001   |
| 15U        | Integrated Circuit, 4066B                | 37-4066      |
| 15/16L     | Integrated Circuit, Microprocessor, 6502-A | 90-6013   |
| 15/16U     | Integrated Circuit, LM324                | 37-LM324     |
| 16K        | Integrated Circuit, 74LS244              | 37-74LS244   |
| 16L        | Integrated Circuit, 74LS244              | 37-74LS244   |
| 16N/P      | Integrated Circuit, HM6116               | 137211-001   |
| 16M        | Integrated Circuit, HM6116               | 137211-001   |
| 16R        | Integrated Circuit, EPROM, 300ns         | 136037-120   |
| 16S        | Integrated Circuit, EPROM, 300ns         | 136037-119   |
| 16T/U      | Integrated Circuit, 74LS259              | 37-74LS259   |
| VR1        | Integrated Circuit, LM7812               | 37-7812      |
| VR2        | Integrated Circuit, LM7905               | 37-7905      |


Here’s the filtered list with only the EPROM entries:

```markdown
# Gauntlet Game PCB Assembly Parts List - EPROMs Only

| Designator | Description                    | Part No.     |
|------------|--------------------------------|--------------|
| 1A         | Integrated Circuit, EPROM, 300ns | 136037-111 |
| 1B         | Integrated Circuit, EPROM, 300ns | 136037-112 |
| 1L         | Integrated Circuit, EPROM, 300ns | 136037-113 |
| 1M/N       | Integrated Circuit, EPROM, 300ns | 136037-114 |
| 2A         | Integrated Circuit, EPROM, 300ns | 136037-115 |
| 2B         | Integrated Circuit, EPROM, 300ns | 136037-116 |
| 2L         | Integrated Circuit, EPROM, 300ns | 136037-117 |
| 2M/N       | Integrated Circuit, EPROM, 300ns | 136037-118 |
| 9A         | Integrated Circuit, EPROM, 200ns | 136037-107 |
| 9B         | Integrated Circuit, EPROM, 200ns | 137037-108 |
| 10A        | Integrated Circuit, EPROM, 200ns | 136037-105 |
| 10B        | Integrated Circuit, EPROM, 200ns | 136037-106 |
| 16R        | Integrated Circuit, EPROM, 300ns | 136037-120 |
| 16S        | Integrated Circuit, EPROM, 300ns | 136037-119 |
``` 

This table includes only the EPROM entries, showing each designator, description, and part number in markdown format.

Exactly! Each chip (or ROM file) contains a specific set of graphic data arranged sequentially in memory. This arrangement allows for reading from multiple chips at the same time to construct the bitplanes necessary for the sprites and graphics used in the game.

Here’s a breakdown of how this works:

    Sequential Arrangement: The ROM files for GFX2 are loaded into memory at defined offsets. Each subsequent file follows the previous one without gaps, which makes it straightforward to read them in sequence.

    Parallel Reading: Even though the files are loaded sequentially in memory, they can be accessed in parallel during the graphics rendering process. For example, when rendering 4bpp graphics (like the ones in Gauntlet), the bits from the different ROMs are combined together. This means that when drawing a single pixel, data from multiple files is interleaved—one from each plane—allowing for a richer color palette and more detailed sprites.

    Bitplane Combination: Each plane contributes a certain number of bits to the final color of a pixel. For instance, in a 4bpp setup, you might read bits from four different ROMs (each representing a plane) and combine them to get the final pixel value. The interleaving during reading allows the graphics hardware to quickly access the necessary data for rendering.

This setup is efficient for the hardware architecture and allows for more complex graphics while managing memory usage effectively.