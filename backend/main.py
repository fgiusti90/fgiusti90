import os
from fastapi import FastAPI
from pydantic import BaseModel
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import SupabaseVectorStore
from langchain.chains import ConversationalRetrievalChain
from supabase import create_client

app = FastAPI()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# Inicializa cliente Supabase
supabase = create_client(supabase_url, supabase_key)

# Configura LLM y embeddings
llm = OpenAI(model="gpt-4")
embeddings = OpenAIEmbeddings()
vector_store = SupabaseVectorStore(client=supabase, embedding=embeddings)

# Cadena de conversaci\u00f3n con RAG
chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever())

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    result = chain({"question": req.message, "chat_history": []})
    return ChatResponse(response=result["answer"])
