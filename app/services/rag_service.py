from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

print("RAG packages working")
def get_embeddings():

    return OllamaEmbeddings(
        model="nomic-embed-text"
    )


def create_resume_vector_store(
    resume_text: str,
    resume_id: int
):

    # 1. Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(
        resume_text
    )


    # 2. Create embeddings
    embeddings = get_embeddings()


    # 3. Store vectors in Chroma
    vector_store = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        collection_name=f"resume_{resume_id}",
        persist_directory="./chroma"
    )


    return vector_store



def get_resume_retriever(
    resume_id: int
):

    embeddings = get_embeddings()


    vector_store = Chroma(
        collection_name=f"resume_{resume_id}",
        embedding_function=embeddings,
        persist_directory="./chroma"
    )


    return vector_store.as_retriever(
        search_kwargs={
            "k": 5
        }
    )