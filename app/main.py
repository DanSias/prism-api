from fastapi import FastAPI

app = FastAPI(title="PrismAPI", description="AI Prompt Execution with Google Gemini")

@app.get("/")
def read_root():
    return {"message": "Welcome to PrismAPI"}

# Add routes here
