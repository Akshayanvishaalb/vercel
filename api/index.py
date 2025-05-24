from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

# Load data from JSON file
with open("marks.json", "r") as f:
    data = json.load(f)

# Convert list to dict for faster access
marks_dict = {item["name"]: item["marks"] for item in data}

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api")
def get_marks(name: list[str] = []):
    result = [marks_dict.get(n, None) for n in name]
    return {"marks": result}
