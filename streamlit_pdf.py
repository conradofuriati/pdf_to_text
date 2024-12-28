import streamlit as st
import PyPDF2

def converter_pdf_para_texto(arquivo_pdf):
    # Abrir o arquivo PDF
    with open(arquivo_pdf, 'rb') as f:
        leitor_pdf = PyPDF2.PdfFileReader(f)

    # Extrair o texto de cada página do PDF
    paginas = []
    for i in range(leitor_pdf.getNumPages()):
        pagina = leitor_pdf.getPage(i)
        paginas.append(pagina.extractText())

    # Juntar o texto de todas as páginas em um único string
    texto_completo = '\n'.join(paginas)

    return texto_completo

# Criar o layout da página com o Streamlit
st.title('Conversor de PDF para Texto')
st.markdown('Selecione o arquivo PDF que você quer converter:')

# Adicionar um widget para selecionar o arquivo PDF
arquivo_pdf = st.file_uploader('', type='pdf')

if arquivo_pdf is not None:
    # Converter o arquivo PDF em texto
    texto = converter_pdf_para_texto(arquivo_pdf)

    # Mostrar o texto convertido
    st.markdown('Texto convertido:')
    st.text(texto)
