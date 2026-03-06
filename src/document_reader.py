import os 
import pdfplumber 
from docx import Document 

def read_document (filepath ):
    """
    Reads text from PDF, DOCX, or TXT files.
    """
    _ ,ext =os .path .splitext (filepath )
    ext =ext .lower ()

    try :
        if ext =='.pdf':
            return read_pdf (filepath )
        elif ext =='.docx':
            return read_docx (filepath )
        elif ext =='.txt':
            return read_txt (filepath )
        else :
            print (f"Unsupported file format: {ext }")
            return ""
    except Exception as e :
        print (f"Error reading {filepath }: {e }")
        return ""

def read_pdf (filepath ):
    text =""
    with pdfplumber .open (filepath )as pdf :
        for page in pdf .pages :
            extract =page .extract_text ()
            if extract :
                text +=extract +"\n"
    return text 

def read_docx (filepath ):
    doc =Document (filepath )
    text =[]
    for para in doc .paragraphs :
        text .append (para .text )
    return "\n".join (text )

def read_txt (filepath ):
    with open (filepath ,'r',encoding ='utf-8')as f :
        return f .read ()
