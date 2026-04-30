#!/usr/bin/env python3
"""
🛡️ AegisX Command Center - Generate PDF Guide
Quick script to create a professional PDF from HTML
"""

import subprocess
import sys
import os

def generate_pdf():
    """Generate PDF from HTML guide."""
    
    print("\n" + "="*60)
    print("🛡️  AegisX PDF Guide Generator")
    print("="*60 + "\n")
    
    # Check if weasyprint is installed
    try:
        import weasyprint
        print("✅ weasyprint found")
    except ImportError:
        print("❌ weasyprint not found")
        print("\n📦 Installing weasyprint...\n")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "weasyprint"])
        print("\n✅ weasyprint installed\n")
    
    # Generate PDF
    html_file = "AEGISX_GUIDE.html"
    pdf_file = "AEGISX_GUIDE.pdf"
    
    if not os.path.exists(html_file):
        print(f"❌ {html_file} not found!")
        print("\nFirst, run: python generate_pdf_guide.py")
        return False
    
    print(f"📄 Converting {html_file} to {pdf_file}...\n")
    
    try:
        from weasyprint import HTML
        HTML(html_file).write_pdf(pdf_file)
        print(f"✅ PDF created: {pdf_file}\n")
        
        # Get file size
        size_kb = os.path.getsize(pdf_file) / 1024
        print(f"📊 File size: {size_kb:.1f} KB\n")
        
        print("=" * 60)
        print("🎉 Success!")
        print("=" * 60)
        print(f"\n📋 Your guide is ready: {pdf_file}")
        print("\n📧 You can now:")
        print(f"   1. Email {pdf_file} to your hackathon judge")
        print(f"   2. Print {pdf_file} as a reference")
        print(f"   3. Share on GitHub or Google Drive")
        print(f"   4. Use as documentation\n")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}\n")
        print("💡 Alternatives to generate PDF:")
        print("   1. Open AEGISX_GUIDE.html in Chrome/Firefox")
        print("   2. Press Ctrl+P → Save as PDF")
        print("   3. Upload HTML to https://cloudconvert.com\n")
        return False

if __name__ == "__main__":
    generate_pdf()
