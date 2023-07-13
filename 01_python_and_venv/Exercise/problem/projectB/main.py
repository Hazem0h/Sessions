from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
import uvicorn
import pandas as pd

app = FastAPI()

if pd.__version__ != "2.0.3":
    raise Exception("Wrong pandas version")

df = pd.read_csv("data.csv", sep = ",")

@app.get("/")
def root() -> HTMLResponse:
    html_content = f"""
    <html>
        <head>
            <title>Demo App</title>
        </head>
        <body>
            <h1>Project B runs smoothly 🐋</h1>
            <p> There are 4 persons in our csv file. </p>
            <ul>
                <li>{df.iloc[0]["name"]}: {df.iloc[0]["age"]} years old</li>
                <li>{df.iloc[1]["name"]}: {df.iloc[1]["age"]} years old</li>
                <li>{df.iloc[2]["name"]}: {df.iloc[2]["age"]} years old</li>
                <li>{df.iloc[3]["name"]}: {df.iloc[3]["age"]} years old</li>
            </ul>
            <h1 style="color:red"> ⚠ Check that Project A runs. </h1>
        </body>
    </html>
    """
    # highlight h1 tag of HTML

    return HTMLResponse(content = html_content, status_code = 200)

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8001)