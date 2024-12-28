
#pip install fitz
#pip install pymupdf[extra]

import os
import fitz

os.chdir('C:\\Users\\ACT\\Documents\\C\\scripts_new\\pdf_to_text')

# Caminho para o diretório com os arquivos .pdf
src_dir = "files_pdf"
dest_dir = "files_txt"

# Itera sobre os arquivos no diretório
for file in os.listdir(src_dir):
    # Verifica se o arquivo tem a extensão .pdf
    if file.endswith(".pdf"):
        # Abre o arquivo .pdf
        pdf_file = fitz.open(os.path.join(src_dir, file))
        print(pdf_file)
        pages = []
        for page in pdf_file:
            text = page.get_text()
            pages.append(text)
            #Concatenar as paginas em uma unica string
            text = '\nNEW_PAGE\n'.join(pages)
            # Cria o nome do arquivo de saída
            output_file = os.path.splitext(file)[0] + ".txt"
            # Escreve o texto no arquivo de saída - equivalente function save_file convert_pdf2txt.py
            with open(os.path.join(dest_dir, output_file), "w") as txt_file:
                txt_file.write(text)

print('Processo finalizado com sucesso!')

#https://github.com/daveshap/ChatGPT_QA_Regenerative_Medicine/blob/main/step01_convert_PDFs.py
#https://github.com/daveshap/RecursiveSummarizer/blob/main/recursively_summarize.py

##
files = os.listdir(src_dir)
files = [i for i in files if '.pdf' in i]
for file in files:
    """convert pdf to txt"""


##
import glob

files=glob.glob('C:\\Users\\ACT\\Documents\\C\\scripts_new\\nlp\\files_pdf\\*.pdf')
