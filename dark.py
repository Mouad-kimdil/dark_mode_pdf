import fitz
import os
import sys
from pathlib import Path

def convert_pdf_to_dark_mode(input_path, output_path, brightness=0.08, contrast=1.4):
    try:
        doc = fitz.open(input_path)
        print(f"Processing {len(doc)} pages...")
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            print(f"Processing page {page_num + 1}/{len(doc)}")
            
            mat = fitz.Matrix(3.0, 3.0)
            pix = page.get_pixmap(matrix=mat, alpha=False, annots=True)
            
            for y in range(pix.height):
                for x in range(pix.width):
                    pixel = pix.pixel(x, y)
                    if len(pixel) >= 3:
                        r, g, b = pixel[0], pixel[1], pixel[2]
                        if r + g + b > 600:
                            new_r = int(brightness * 255)
                            new_g = int(brightness * 255)
                            new_b = int(brightness * 255)
                        else:
                            new_r = min(255, int((255 - r) * contrast))
                            new_g = min(255, int((255 - g) * contrast))
                            new_b = min(255, int((255 - b) * contrast))
                        
                        if len(pixel) == 4:
                            pix.set_pixel(x, y, (new_r, new_g, new_b, pixel[3]))
                        else:
                            pix.set_pixel(x, y, (new_r, new_g, new_b))
            
            page.clean_contents()
            page.insert_image(page.rect, pixmap=pix)
            pix = None
        
        doc.save(output_path, garbage=4, deflate=True, clean=True, pretty=True)
        doc.close()
        print(f"Dark mode PDF saved to: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

def get_pdf_path():
    while True:
        path = input("Enter the PDF file path: ").strip().strip('"\'')
        if not path:
            print("Please enter a valid path.")
            continue
        
        path = os.path.expanduser(path)
        if not os.path.exists(path):
            print(f"File not found: {path}")
            continue
        
        if not path.lower().endswith('.pdf'):
            print("Please select a PDF file.")
            continue
        
        return path

def get_output_path(input_path):
    default_dir = os.path.dirname(input_path)
    filename = os.path.splitext(os.path.basename(input_path))[0]
    default_output = os.path.join(default_dir, f"{filename}_dark.pdf")
    
    print(f"Default output: {default_output}")
    output = input("Enter output path (or press Enter for default): ").strip().strip('"\'')
    
    if not output:
        return default_output
    
    output = os.path.expanduser(output)
    if os.path.isdir(output):
        output = os.path.join(output, f"{filename}_dark.pdf")
    elif not output.lower().endswith('.pdf'):
        output += '.pdf'
    
    os.makedirs(os.path.dirname(output), exist_ok=True)
    return output

def main():
    print("PDF Dark Mode Converter")
    print("=" * 30)
    
    input_path = get_pdf_path()
    print(f"Input: {input_path}")
    
    output_path = get_output_path(input_path)
    print(f"Output: {output_path}")
    
    print("\nQuality Settings:")
    try:
        brightness = float(input("Background brightness (0.05-0.2, default 0.08): ") or "0.08")
        contrast = float(input("Text contrast (1.0-2.0, default 1.4): ") or "1.4")
    except ValueError:
        brightness, contrast = 0.08, 1.4
        print("Using default settings.")
    
    print("\n🔄 Converting to dark mode...")
    success = convert_pdf_to_dark_mode(input_path, output_path, brightness, contrast)
    
    if success:
        print(f"\nConversion completed successfully!")
        print(f"File size: {os.path.getsize(output_path) / 1024 / 1024:.1f} MB")
    else:
        print("\nConversion failed.")

if __name__ == "__main__":
    main()
