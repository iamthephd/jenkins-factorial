from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Factorial API")

# Create a model for the request body
class NumberInput(BaseModel):
    number: int

# Function to calculate factorial
def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n-1)

# API route to calculate factorial
@app.post("/api/factorial")
def get_factorial(input: NumberInput):
    try:
        result = calculate_factorial(input.number)
        return {"number": input.number, "factorial": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RecursionError:
        raise HTTPException(status_code=400, detail="Input too large, resulting in recursion limit exceeded")

# Serve the home page
@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("static/index.html", "r") as file:
        return file.read()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=9000, reload=True)