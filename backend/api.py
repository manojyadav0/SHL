from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from backend.embeddings import recommend
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryText(BaseModel):
    query: str

@app.post("/recommend")
def get_recommendations(q: QueryText):
    results = recommend(q.query)
    return {"recommendations": results}
