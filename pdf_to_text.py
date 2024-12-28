
import os
import pdfplumber

# Abrir o arquivo PDF
with pdfplumber.open('ebook2.pdf') as arquivo_pdf:
    # Extrair o texto de cada página do PDF
    paginas = []
    for pagina in arquivo_pdf.pages:
        paginas.append(pagina.extract_text())

# Juntar o texto de todas as paginas em um unico string
texto_completo = '\nNEW_PAGE\n'.join(paginas)

# Salvar o texto em um arquivo de texto
with open('ebook2.txt', 'w') as arquivo_txt:
    arquivo_txt.write(texto_completo)
    
