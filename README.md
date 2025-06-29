# AutomaticAutomatist

A comprehensive suite of Python tools for generating and combining abstract digital artwork using algorithmic techniques. This project creates abstract expressionist and surrealist-inspired digital art through procedural generation, then provides advanced tools for combining multiple artworks into complex compositions.

**Inspiration**: This project was born from a visit to the Vancouver Art Gallery and experiments with generative AI. The entire codebase was developed collaboratively with AI assistance, demonstrating the creative potential of human-AI collaboration in digital art.

## Project Overview

The AutomaticAutomatist consists of two main components:

1. **Abstract Art Generator** (`abstract_art_generator.py`) - Creates individual artworks
2. **Art Combiner** (`art_combiner.py`) - Combines multiple artworks into compositions

Together, these tools enable the creation of both individual pieces and complex multi-artwork compositions using various algorithmic and compositional techniques.

## Features

### Abstract Art Generator
- **Two Art Styles**: Generate Abstract Expressionist or Surrealist artwork
- **Customizable Parameters**: Control image dimensions, complexity, and artistic elements
- **Reproducible Results**: Use seeds to generate identical artwork
- **Command-Line Interface**: Easy-to-use CLI with comprehensive options
- **High-Quality Output**: Generate high-resolution PNG images

### Art Combiner
- **Multiple Composition Types**: Grid, layered, split, and mosaic layouts
- **Advanced Blending Modes**: Normal, multiply, screen, and overlay blending
- **Flexible Layouts**: Horizontal, vertical, diagonal, and radial splits
- **Batch Processing**: Combine multiple artworks at once
- **Creative Control**: Customizable spacing, opacity, tile sizes, and more

## Quick Start

### Generate Individual Artworks

```bash
# Activate the virtual environment
source art_env/bin/activate

# Generate an abstract expressionist piece
python abstract_art_generator.py --style expressionist --output my_art.png

# Generate a surrealist piece
python abstract_art_generator.py --style surrealist --output surreal_art.png
```

### Combine Multiple Artworks

```bash
# Create a grid composition
python art_combiner.py --input *.png --type grid --output combined.png

# Create a layered composition with blending
python art_combiner.py --input *.png --type layered --blend multiply --output layered.png
```

## Art Styles

### Abstract Expressionist
- Bold, gestural brush strokes with emotional color palettes
- Fluid dynamics overlays for organic flow
- Inspired by artists like Jackson Pollock and Willem de Kooning
- Features deep reds, blues, yellows, greens, purples, and oranges

### Surrealist
- Organic, biomorphic shapes using polar coordinate generation
- Dreamlike color combinations and unexpected palettes
- Perlin noise textures for natural, organic backgrounds
- Visual distortion effects for otherworldly compositions
- Inspired by artists like Joan Miró and Yves Tanguy

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone or download the script**:
   ```bash
   # If you have the file locally
   cd /path/to/your/directory
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv art_env
   source art_env/bin/activate  # On Windows: art_env\Scripts\activate
   ```

3. **Install required packages**:
   ```bash
   pip install numpy matplotlib pillow scipy
   ```

### Required Dependencies
- `numpy`: Numerical computing and array operations
- `matplotlib`: Color mapping and mathematical functions
- `pillow` (PIL): Image creation, manipulation, and saving
- `scipy`: Advanced image filtering and noise generation

## Usage

### Basic Usage

Generate an abstract expressionist artwork:
```bash
python abstract_art_generator.py --style expressionist
```

Generate a surrealist artwork:
```bash
python abstract_art_generator.py --style surrealist
```

### Command-Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--style` | | Art style: `expressionist` or `surrealist` | **Required** |
| `--output` | `-o` | Output filename | `artwork.png` |
| `--width` | | Image width in pixels | `1024` |
| `--height` | | Image height in pixels | `1024` |
| `--seed` | | Random seed for reproducible results | Random |
| `--shapes` | | Number of organic shapes (surrealist only) | `8` |
| `--strokes` | | Number of brush strokes (expressionist only) | `20-40` (random) |

### Examples

**Basic generation with custom output:**
```bash
python abstract_art_generator.py --style expressionist --output my_masterpiece.png
```

**Custom dimensions:**
```bash
python abstract_art_generator.py --style surrealist --width 512 --height 512 --output small_surreal.png
```

**Reproducible artwork with seed:**
```bash
python abstract_art_generator.py --style expressionist --seed 42 --output seeded_art.png
```

**Complex compositions:**
```bash
# Surrealist with many shapes
python abstract_art_generator.py --style surrealist --shapes 15 --output complex_surreal.png

# Expressionist with many brush strokes
python abstract_art_generator.py --style expressionist --strokes 80 --output busy_expressionist.png
```

**High-resolution artwork:**
```bash
python abstract_art_generator.py --style surrealist --width 2048 --height 2048 --output hires_art.png
```

### Help

View all available options:
```bash
python abstract_art_generator.py --help
```

## Technical Details

### Algorithms Used

1. **Perlin Noise Generation**: Creates organic, natural-looking textures
2. **Fluid Dynamics Simulation**: Generates flowing, wave-like patterns
3. **Polar Coordinate Shape Generation**: Creates biomorphic, organic shapes
4. **Color Palette Generation**: Art movement-inspired color schemes
5. **Gaussian Filtering**: Smooths and blends elements naturally
6. **Alpha Compositing**: Layers multiple elements with transparency

### Color Palettes

**Abstract Expressionist Colors:**
- Deep red, blue, golden yellow
- Forest green, purple, orange
- Bold, emotional combinations

**Surrealist Colors:**
- Lavender, turquoise, peach
- Deep purple, lime, sky blue
- Dreamlike, unexpected combinations

### File Output

- **Format**: PNG with full alpha channel support
- **Quality**: Lossless compression
- **Size**: Varies based on complexity and dimensions
  - Typical range: 50KB - 2MB
  - Higher complexity = larger file sizes

## Examples of Generated Art

The program generates unique artwork each time it runs (unless using the same seed). Here are some example command outputs:

```
Abstract Expressionist/Surrealist Image Generator
==================================================
Style: Expressionist
Dimensions: 1024x1024
Output: artwork.png

Generating Abstract Expressionist artwork...
Artwork saved as: artwork.png
File size: 94,542 bytes (92.3 KB)

Generation complete!
```

## Troubleshooting

### Common Issues

**ImportError: No module named 'numpy'**
```bash
# Make sure you've installed the dependencies
pip install numpy matplotlib pillow scipy
```

**Permission denied when saving files**
```bash
# Make sure you have write permissions in the current directory
# Or specify a different output path
python abstract_art_generator.py --style expressionist --output ~/Desktop/art.png
```

**Memory issues with large images**
```bash
# Reduce image dimensions for very large sizes
python abstract_art_generator.py --style surrealist --width 512 --height 512
```

### Performance Tips

- **Smaller dimensions** generate faster and use less memory
- **Fewer shapes/strokes** reduce generation time
- **Use seeds** to avoid regenerating the same random artwork
- **Virtual environments** prevent package conflicts

---

# Art Combiner

The Art Combiner takes multiple PNG images generated by the Abstract Art Generator and combines them into sophisticated composite artworks using various layout and blending techniques.

## Composition Types

### 1. Grid Layout (`--type grid`)
Arranges images in a rectangular grid with customizable spacing.

```bash
# Auto-calculate grid dimensions
python art_combiner.py --input *.png --type grid --output grid.png

# Specify columns and spacing
python art_combiner.py --input *.png --type grid --cols 3 --spacing 20 --output grid.png
```

### 2. Layered Composition (`--type layered`)
Layers images with advanced blending modes for complex visual effects.

```bash
# Multiply blending for darker, richer colors
python art_combiner.py --input *.png --type layered --blend multiply --output layered.png

# Screen blending for lighter, brighter effects
python art_combiner.py --input *.png --type layered --blend screen --output layered.png

# Overlay blending for high contrast
python art_combiner.py --input *.png --type layered --blend overlay --output layered.png
```

### 3. Split Composition (`--type split`)
Splits images and recombines parts in geometric patterns.

```bash
# Horizontal strips
python art_combiner.py --input *.png --type split --split-mode horizontal --output split_h.png

# Radial/pie slice split
python art_combiner.py --input *.png --type split --split-mode radial --output split_radial.png
```

### 4. Mosaic Composition (`--type mosaic`)
Creates detailed mosaics using tiles from different source images.

```bash
# Large tiles for bold patterns
python art_combiner.py --input *.png --type mosaic --tile-size 100 --output mosaic.png

# Small tiles for detailed textures
python art_combiner.py --input *.png --type mosaic --tile-size 25 --output detailed_mosaic.png
```

## Art Combiner Usage Examples

### Complete Workflow Example

```bash
# Generate source artworks
python abstract_art_generator.py --style expressionist --output exp1.png --seed 1
python abstract_art_generator.py --style expressionist --output exp2.png --seed 2
python abstract_art_generator.py --style surrealist --output sur1.png --seed 3
python abstract_art_generator.py --style surrealist --output sur2.png --seed 4

# Create different combinations
python art_combiner.py --input exp1.png exp2.png sur1.png sur2.png --type grid --cols 2 --output grid_combo.png
python art_combiner.py --input exp1.png exp2.png sur1.png sur2.png --type layered --blend multiply --output layered_combo.png
python art_combiner.py --input exp1.png exp2.png sur1.png sur2.png --type split --split-mode radial --output radial_combo.png
```

### Creative Tips for Combinations

- **Multiply blending**: Creates darker, richer colors - great for dramatic effects
- **Screen blending**: Creates lighter, brighter colors - good for ethereal effects  
- **Overlay blending**: High contrast with vivid colors - creates striking compositions
- **Grid layouts**: Perfect for comparing different artworks or creating gallery walls
- **Split compositions**: Great for creating abstract patterns and geometric designs
- **Mosaic layouts**: Excellent for creating textured, detailed compositions

## Advanced Usage for Abstract Art Generator

### Batch Generation Script

Create multiple variations:
```bash
#!/bin/bash
for i in {1..5}; do
    python abstract_art_generator.py --style expressionist --output "expressionist_$i.png" --seed $i
    python abstract_art_generator.py --style surrealist --output "surrealist_$i.png" --seed $i
done
```

### Integration with Other Tools

The generated PNG files can be used with:
- Image editing software (Photoshop, GIMP)
- Web applications and websites
- Print media and physical artwork
- NFT and digital art platforms
- Social media and digital galleries

---

# Project Files

## Main Scripts

- **`abstract_art_generator.py`** - Core art generation tool
- **`art_combiner.py`** - Art composition and combination tool  

## Documentation

- **`README.md`** - This comprehensive guide
- **`ART_COMBINER_README.md`** - Detailed Art Combiner documentation

## Environment

- **`art_env/`** - Pre-configured virtual environment with all dependencies

## Installation and Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Quick Setup (Recommended)

The repository includes a pre-configured virtual environment:

```bash
# Clone or navigate to the repository
cd /path/to/AutomaticAutomatist

# Activate the included virtual environment
source art_env/bin/activate

# Start creating art immediately!
python abstract_art_generator.py --style expressionist --output my_first_art.png
```

### Manual Setup

If you prefer to set up your own environment:

```bash
# Create a new virtual environment
python3 -m venv my_art_env
source my_art_env/bin/activate  # On Windows: my_art_env\Scripts\activate

# Install required packages
pip install numpy matplotlib pillow scipy
```

### Required Dependencies
- **`numpy`**: Numerical computing and array operations
- **`matplotlib`**: Color mapping and mathematical functions
- **`pillow` (PIL)**: Image creation, manipulation, and saving
- **`scipy`**: Advanced image filtering and noise generation

## Contributing and Extending

This project demonstrates the creative potential of human-AI collaboration. You can extend it by:

1. **Adding new art styles**: Implement additional generation algorithms
2. **Expanding composition types**: Create new ways to combine artworks
3. **New blending modes**: Add more sophisticated image blending techniques
4. **Interactive features**: Add real-time preview or GUI interfaces
5. **Output formats**: Add support for SVG, PDF, or other formats
6. **Animation**: Create animated sequences from static artworks

## Creative Applications

The generated artwork can be used for:
- **Digital Art Collections**: Create unique pieces for galleries or personal collections
- **Print Media**: High-resolution outputs suitable for physical printing
- **Web Design**: Backgrounds, headers, and decorative elements
- **NFT Creation**: Unique digital assets for blockchain platforms
- **Social Media**: Eye-catching visuals for posts and profiles
- **Interior Design**: Custom artwork for homes and offices
- **Educational Projects**: Demonstrations of algorithmic art and procedural generation

This is a standalone script, but you can extend it by:

1. **Adding new art styles**: Implement new generation methods
2. **Expanding color palettes**: Add more art movement-inspired colors
3. **New algorithms**: Implement additional procedural generation techniques
4. **Output formats**: Add support for SVG, PDF, or other formats
5. **Interactive features**: Add real-time preview or GUI interface

## Acknowledgments

**Artistic Inspiration:**
- **Abstract Expressionists**: Jackson Pollock, Willem de Kooning, Mark Rothko
- **Surrealists**: Joan Miró, Yves Tanguy, Salvador Dalí
- **Algorithmic Art**: Pioneers in computational creativity and generative art
- **Vancouver Art Gallery**: The spark that ignited this creative journey

**Technical Inspiration:**
- **Generative AI**: This entire project was developed through human-AI collaboration
- **Open Source Community**: The Python ecosystem that makes creative coding accessible
- **Procedural Generation**: The mathematical beauty of algorithmic creativity

## Project Philosophy

AutomaticAutomatist represents a fusion of traditional artistic movements with modern computational techniques. By combining the emotional expressiveness of Abstract Expressionism with the dreamlike qualities of Surrealism, and then providing tools to create complex compositions, this project explores how algorithms can be used as creative partners rather than mere tools.

The collaborative development process with AI demonstrates that technology can enhance rather than replace human creativity, opening new possibilities for artistic expression in the digital age.

---

*Each generated artwork is unique and reflects the random, expressive nature of abstract and surrealist art movements, while the combination tools allow for infinite creative possibilities in composition and presentation.*
