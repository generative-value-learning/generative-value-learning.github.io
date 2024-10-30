import fitz  # PyMuPDF
from PIL import Image
import io

def pdf_to_png(pdf_path, dpi=300):
    """
    Convert a PDF file to PNG image.
    
    Args:
        pdf_path (str): Path to the PDF file
        dpi (int): DPI for the output image (default: 300)
        
    Returns:
        PIL.Image: The converted PNG image
    """
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Get the first page
    page = pdf_document[0]
    
    # Set the zoom factor based on DPI
    zoom = dpi / 72  # 72 is the default PDF DPI
    
    # Create a matrix for rendering
    mat = fitz.Matrix(zoom, zoom)
    
    # Get the page's pixmap using the matrix
    pix = page.get_pixmap(matrix=mat)
    
    # Convert pixmap to PIL Image
    img_data = pix.tobytes("png")
    img = Image.open(io.BytesIO(img_data))
    
    # Close the PDF document
    pdf_document.close()
    
    return img

def save_pdf_as_png(pdf_path, dpi=300):
    """
    Convert a PDF file to PNG and save it.
    
    Args:
        pdf_path (str): Path to the PDF file
        dpi (int): DPI for the output image (default: 300)
    """
    output_path = pdf_path.replace('.pdf', '.png')
    img = pdf_to_png(pdf_path, dpi)
    img.save(output_path, "PNG")

if __name__ == "__main__":
    save_pdf_as_png("./static/images/icv/icv_01_shot.pdf")
    save_pdf_as_png("./static/images/icv/icv_shots_average.pdf")
