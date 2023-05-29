from glob import glob
import shutil
import os
# pip install beautifulsoup4  - used for parsing html
from langchain.document_loaders import BSHTMLLoader, DirectoryLoader
# used for loading text data from html file
#   pip install transformers huggingface-hub
from transformers import AutoTokenizer
from langchain.text_splitter import CharacterTextSplitter
# pip install sentence_transformers - used for encoding text
from langchain.embeddings import HuggingFaceEmbeddings
# pip install chromadb - used to store vector embeddings
from langchain.vectorstores import Chroma


DATA_DIRECTORY = './data'
VECTOR_DB_PERSIST_DIRECTORY = "vector_db"
TRAINING_MODEL = "bigscience/bloomz-1b7"

def collect_all_hmtl_docs():
    files = glob("./shakespeare/**/*.html")
    return files


def move_html_files_to_common_directory(files):
    if not os.path.exists(DATA_DIRECTORY):
        os.makedirs(DATA_DIRECTORY)
    
    for html_file in files:
        destination = f'{DATA_DIRECTORY}/{os.path.basename(html_file)}'
        print(f"Moving File: {html_file} to {destination}")        
        shutil.move(html_file, destination)


def initial_setup():
    files = collect_all_hmtl_docs()
    print(f"Total files to move: {len(files)}")
    move_html_files_to_common_directory(files)  


def load_html_text_from_files():
    bshtml_dir_loader = DirectoryLoader(DATA_DIRECTORY, loader_cls=BSHTMLLoader)
    
    data = bshtml_dir_loader.load()

    return data

def tokenize_using_bloom(data):
    bloomz_tokenizer = AutoTokenizer.from_pretrained(TRAINING_MODEL)

    text_splitter = CharacterTextSplitter.from_huggingface_tokenizer(bloomz_tokenizer, chunk_size=100, chunk_overlap=0, separator="\n")

    documents = text_splitter.split_documents(data)

    return documents

def tokenize_html_files():
    html_file_data = load_html_text_from_files()

    tokenzied_documents = tokenize_using_bloom(html_file_data)

    return tokenzied_documents

def get_embeddings():    
    embeddings = HuggingFaceEmbeddings()

    return embeddings

def set_vector_db(tokenzied_documents, embeddings):
    vectordb = Chroma.from_documents(documents=tokenzied_documents, embedding=embeddings, persist_directory=VECTOR_DB_PERSIST_DIRECTORY)

    vectordb.persist()
    vectordb = None

def get_vector_db(embeddings):
    vectordb = Chroma(persist_directory=VECTOR_DB_PERSIST_DIRECTORY, embedding_function=embeddings)
     


tokenzied_documents = tokenize_html_files()
embeddings = get_embeddings()

set_vector_db(tokenzied_documents, embeddings)
get_vector_db(embeddings)





