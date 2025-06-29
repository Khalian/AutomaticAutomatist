# Abstract Art Generator

A Python program that creates abstract expressionist and surrealist-inspired digital artwork using algorithmic techniques including noise functions, fluid dynamics simulation, and organic shape generation.

I got the idea from visiting Vancouver Art Gallery and my experiments with Gen AI. I wrote this entire package with gen AI.

## Features

- **Two Art Styles**: Generate Abstract Expressionist or Surrealist artwork
- **Customizable Parameters**: Control image dimensions, complexity, and artistic elements
- **Reproducible Results**: Use seeds to generate identical artwork
- **Command-Line Interface**: Easy-to-use CLI with comprehensive options
- **High-Quality Output**: Generate high-resolution PNG images

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

## Advanced Usage

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

## Contributing

This is a standalone script, but you can extend it by:

1. **Adding new art styles**: Implement new generation methods
2. **Expanding color palettes**: Add more art movement-inspired colors
3. **New algorithms**: Implement additional procedural generation techniques
4. **Output formats**: Add support for SVG, PDF, or other formats
5. **Interactive features**: Add real-time preview or GUI interface

## Acknowledgments

Inspired by the works of:
- **Abstract Expressionists**: Jackson Pollock, Willem de Kooning, Mark Rothko
- **Surrealists**: Joan Miró, Yves Tanguy, Salvador Dalí
- **Algorithmic Art**: Pioneers in computational creativity and generative art

*Generated artwork is unique each time and reflects the random, expressive nature of abstract and surrealist art movements.*
