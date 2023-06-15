import fitz
from PIL import Image

def pdf_to_jpg(input_path, output_path):
    pdf_file = fitz.open(input_path)
    
    # Iterar sobre as páginas do PDF
    for page_number in range(pdf_file.page_count):
        page = pdf_file.load_page(page_number)
        pix = page.get_pixmap()
        
        # Criar objeto de imagem PIL a partir dos dados do pixmap
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Salvar a imagem como arquivo JPG
        output_file = f"{output_path}_{page_number+1}.jpg"
        image.save(output_file, "JPEG")

# Caminho para o arquivo PDF de entrada
input_file = "caminho_para_o_arquivo.pdf"

# Caminho para a pasta de saída (onde as imagens JPG serão salvas)
output_folder = "caminho_da_pasta_de_saida"

# Chamando a função para converter o arquivo PDF em imagens JPG
pdf_to_jpg(input_file, output_folder)