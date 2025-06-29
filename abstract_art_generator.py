#!/usr/bin/env python3
"""
Abstract Expressionist/Surrealist Image Generator

This program creates abstract and surrealist-inspired digital artwork using
various algorithmic techniques including noise functions, fluid dynamics
simulation, and organic shape generation.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import random
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from scipy.ndimage import gaussian_filter
import colorsys
import math

class AbstractArtGenerator:
    def __init__(self, width=1024, height=1024):
        self.width = width
        self.height = height
        self.num_shapes = 8  # Default for surrealist
        self.num_strokes = None  # Default for expressionist (will be random)
        
    def generate_color_palette(self, style="expressionist"):
        """Generate color palettes inspired by different art movements"""
        if style == "expressionist":
            # Bold, emotional colors
            base_colors = [
                (0.8, 0.1, 0.1),  # Deep red
                (0.1, 0.1, 0.8),  # Deep blue
                (0.9, 0.7, 0.1),  # Golden yellow
                (0.1, 0.6, 0.1),  # Forest green
                (0.6, 0.1, 0.6),  # Purple
                (0.9, 0.4, 0.1),  # Orange
            ]
        else:  # surrealist
            # Dreamlike, unexpected color combinations
            base_colors = [
                (0.7, 0.3, 0.8),  # Lavender
                (0.3, 0.8, 0.7),  # Turquoise
                (0.9, 0.6, 0.3),  # Peach
                (0.4, 0.2, 0.7),  # Deep purple
                (0.8, 0.8, 0.2),  # Lime
                (0.2, 0.5, 0.8),  # Sky blue
            ]
        
        # Add variations to base colors
        palette = []
        for color in base_colors:
            for i in range(3):
                variation = tuple(max(0, min(1, c + random.uniform(-0.2, 0.2))) 
                                for c in color)
                palette.append(variation)
        
        return palette

    def perlin_noise_2d(self, shape, scale=100, octaves=6, persistence=0.5):
        """Generate 2D Perlin noise for organic textures"""
        def fade(t):
            return t * t * t * (t * (t * 6 - 15) + 10)
        
        def lerp(t, a, b):
            return a + t * (b - a)
        
        def gradient(h, x, y):
            vectors = np.array([[0,1], [1,1], [1,0], [1,-1], 
                               [0,-1], [-1,-1], [-1,0], [-1,1]])
            g = vectors[h % 8]
            return g[:,:,0] * x + g[:,:,1] * y
        
        noise = np.zeros(shape)
        frequency = 1
        amplitude = 1
        max_value = 0
        
        for _ in range(octaves):
            x = np.arange(shape[1]) * frequency / scale
            y = np.arange(shape[0]) * frequency / scale
            
            # Simple noise approximation
            layer = np.random.random(shape) * amplitude
            layer = gaussian_filter(layer, sigma=scale/frequency/4)
            
            noise += layer
            max_value += amplitude
            amplitude *= persistence
            frequency *= 2
        
        return noise / max_value

    def create_fluid_dynamics(self):
        """Simulate fluid-like patterns"""
        # Create velocity field
        x = np.linspace(0, 4*np.pi, self.width)
        y = np.linspace(0, 4*np.pi, self.height)
        X, Y = np.meshgrid(x, y)
        
        # Multiple wave interference
        wave1 = np.sin(X) * np.cos(Y)
        wave2 = np.sin(X*2 + np.pi/3) * np.cos(Y*1.5)
        wave3 = np.sin(X*0.5) * np.cos(Y*3 + np.pi/2)
        
        fluid = wave1 + 0.5*wave2 + 0.3*wave3
        
        # Add turbulence
        noise = self.perlin_noise_2d((self.height, self.width), scale=50)
        fluid += 0.3 * noise
        
        return fluid

    def create_organic_shapes(self, num_shapes=None):
        """Generate organic, biomorphic shapes"""
        if num_shapes is None:
            num_shapes = self.num_shapes
            
        img = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        palette = self.generate_color_palette("surrealist")
        
        for _ in range(num_shapes):
            # Random center point
            cx = random.randint(self.width//4, 3*self.width//4)
            cy = random.randint(self.height//4, 3*self.height//4)
            
            # Generate organic shape using polar coordinates
            angles = np.linspace(0, 2*np.pi, 50)
            radii = []
            
            for angle in angles:
                # Base radius with organic variation
                base_radius = random.randint(50, 200)
                variation = 30 * np.sin(angle * random.randint(2, 8)) * \
                           np.cos(angle * random.randint(1, 5))
                radii.append(base_radius + variation)
            
            # Convert to cartesian coordinates
            points = []
            for angle, radius in zip(angles, radii):
                x = cx + radius * np.cos(angle)
                y = cy + radius * np.sin(angle)
                points.append((x, y))
            
            # Choose color and transparency
            color = random.choice(palette)
            color_rgba = tuple(int(c * 255) for c in color) + (random.randint(100, 200),)
            
            draw.polygon(points, fill=color_rgba)
        
        return img

    def create_gestural_strokes(self):
        """Create expressive, gestural brush strokes"""
        img = Image.new('RGB', (self.width, self.height), 'white')
        draw = ImageDraw.Draw(img)
        
        palette = self.generate_color_palette("expressionist")
        
        # Use specified number of strokes or random range
        num_strokes = self.num_strokes if self.num_strokes is not None else random.randint(20, 40)
        
        for _ in range(num_strokes):
            # Random starting point
            start_x = random.randint(0, self.width)
            start_y = random.randint(0, self.height)
            
            # Create curved stroke path
            points = [(start_x, start_y)]
            x, y = start_x, start_y
            
            # Random direction and curvature
            direction = random.uniform(0, 2*np.pi)
            curvature = random.uniform(-0.1, 0.1)
            
            stroke_length = random.randint(100, 400)
            step_size = random.randint(5, 15)
            
            for i in range(0, stroke_length, step_size):
                direction += curvature + random.uniform(-0.2, 0.2)
                x += step_size * np.cos(direction)
                y += step_size * np.sin(direction)
                
                # Keep within bounds
                x = max(0, min(self.width, x))
                y = max(0, min(self.height, y))
                
                points.append((x, y))
            
            # Draw stroke with varying width
            color = random.choice(palette)
            color_rgb = tuple(int(c * 255) for c in color)
            width = random.randint(3, 20)
            
            if len(points) > 1:
                for i in range(len(points)-1):
                    draw.line([points[i], points[i+1]], fill=color_rgb, width=width)
        
        return img

    def apply_surreal_effects(self, img):
        """Apply surreal visual effects"""
        # Convert to PIL if numpy array
        if isinstance(img, np.ndarray):
            img = Image.fromarray((img * 255).astype(np.uint8))
        
        # Random distortions
        effects = [
            lambda x: x.filter(ImageFilter.GaussianBlur(radius=random.uniform(1, 3))),
            lambda x: ImageEnhance.Color(x).enhance(random.uniform(0.5, 2.0)),
            lambda x: ImageEnhance.Contrast(x).enhance(random.uniform(0.7, 1.5)),
            lambda x: x.filter(ImageFilter.EDGE_ENHANCE),
        ]
        
        # Apply random effects
        for _ in range(random.randint(1, 3)):
            effect = random.choice(effects)
            img = effect(img)
        
        return img

    def generate_abstract_expressionist(self):
        """Generate an abstract expressionist style image"""
        print("Generating Abstract Expressionist artwork...")
        
        # Start with gestural strokes
        base_img = self.create_gestural_strokes()
        
        # Add fluid dynamics overlay
        fluid = self.create_fluid_dynamics()
        fluid_normalized = (fluid - fluid.min()) / (fluid.max() - fluid.min())
        
        # Convert fluid to color image
        palette = self.generate_color_palette("expressionist")
        fluid_colored = np.zeros((self.height, self.width, 3))
        
        for i in range(self.height):
            for j in range(self.width):
                color_idx = int(fluid_normalized[i, j] * (len(palette) - 1))
                fluid_colored[i, j] = palette[color_idx]
        
        fluid_img = Image.fromarray((fluid_colored * 255).astype(np.uint8))
        fluid_img = fluid_img.convert('RGBA')
        
        # Make fluid overlay semi-transparent
        alpha = fluid_img.split()[-1]
        alpha = alpha.point(lambda p: p * 0.3)  # 30% opacity
        fluid_img.putalpha(alpha)
        
        # Composite images
        base_img = base_img.convert('RGBA')
        result = Image.alpha_composite(base_img, fluid_img)
        
        return result.convert('RGB')

    def generate_surrealist(self):
        """Generate a surrealist style image"""
        print("Generating Surrealist artwork...")
        
        # Create base with organic shapes
        organic_img = self.create_organic_shapes()
        
        # Create background with noise
        noise = self.perlin_noise_2d((self.height, self.width), scale=80)
        noise_normalized = (noise - noise.min()) / (noise.max() - noise.min())
        
        # Apply dreamlike color mapping
        palette = self.generate_color_palette("surrealist")
        background = np.zeros((self.height, self.width, 3))
        
        for i in range(self.height):
            for j in range(self.width):
                # Use noise to select colors
                color_idx = int(noise_normalized[i, j] * (len(palette) - 1))
                background[i, j] = palette[color_idx]
        
        bg_img = Image.fromarray((background * 255).astype(np.uint8))
        
        # Composite organic shapes over background
        bg_img = bg_img.convert('RGBA')
        result = Image.alpha_composite(bg_img, organic_img)
        
        # Apply surreal effects
        result = self.apply_surreal_effects(result)
        
        return result.convert('RGB')

def main():
    """Main function to generate and save artwork"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Generate abstract expressionist or surrealist artwork",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python abstract_art_generator.py --style expressionist --output my_art.png
  python abstract_art_generator.py --style surrealist --width 512 --height 512
  python abstract_art_generator.py --style expressionist --seed 42 --output seeded_art.png
        """
    )
    
    parser.add_argument(
        '--style', 
        choices=['expressionist', 'surrealist'], 
        required=True,
        help='Art style to generate (expressionist or surrealist)'
    )
    
    parser.add_argument(
        '--output', '-o',
        default='artwork.png',
        help='Output filename (default: artwork.png)'
    )
    
    parser.add_argument(
        '--width',
        type=int,
        default=1024,
        help='Image width in pixels (default: 1024)'
    )
    
    parser.add_argument(
        '--height',
        type=int,
        default=1024,
        help='Image height in pixels (default: 1024)'
    )
    
    parser.add_argument(
        '--seed',
        type=int,
        help='Random seed for reproducible results (optional)'
    )
    
    parser.add_argument(
        '--shapes',
        type=int,
        default=None,
        help='Number of organic shapes for surrealist style (default: 8)'
    )
    
    parser.add_argument(
        '--strokes',
        type=int,
        default=None,
        help='Number of brush strokes for expressionist style (default: random 20-40)'
    )
    
    args = parser.parse_args()
    
    # Set random seed if provided
    if args.seed is not None:
        random.seed(args.seed)
        np.random.seed(args.seed)
        print(f"Using random seed: {args.seed}")
    
    print("Abstract Expressionist/Surrealist Image Generator")
    print("=" * 50)
    print(f"Style: {args.style.title()}")
    print(f"Dimensions: {args.width}x{args.height}")
    print(f"Output: {args.output}")
    
    # Create generator with specified dimensions
    generator = AbstractArtGenerator(width=args.width, height=args.height)
    
    # Override default parameters if specified
    if args.shapes is not None:
        generator.num_shapes = args.shapes
    if args.strokes is not None:
        generator.num_strokes = args.strokes
    
    # Generate artwork based on style
    if args.style == 'expressionist':
        print("\nGenerating Abstract Expressionist artwork...")
        artwork = generator.generate_abstract_expressionist()
    else:  # surrealist
        print("\nGenerating Surrealist artwork...")
        artwork = generator.generate_surrealist()
    
    # Save the artwork
    artwork.save(args.output)
    print(f"Artwork saved as: {args.output}")
    
    # Display file info
    import os
    file_size = os.path.getsize(args.output)
    print(f"File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
    print("\nGeneration complete!")

if __name__ == "__main__":
    # Install required packages if not available
    try:
        import numpy as np
        import matplotlib.pyplot as plt
        from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
        from scipy.ndimage import gaussian_filter
    except ImportError as e:
        print(f"Missing required package: {e}")
        print("Install with: pip install numpy matplotlib pillow scipy")
        exit(1)
    
    main()
