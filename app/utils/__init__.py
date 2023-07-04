from fastapi import FastAPI

# Import your microservice modules
from app.services.pdf_to_word import convert_pdf_to_word


app = FastAPI()

# Define your API routes and corresponding endpoints
@app.post("/api/user/info")
async def get_user_info():
    # Implementation for getting user info
    ...

@app.post("/api/process-job")
async def process_job(job_type: str):
    # Determine the appropriate microservice based on the job type
    if job_type == "pdf-to-word":
        return await convert_pdf_to_word()
    else:
        return {"error": "Invalid job type"}
