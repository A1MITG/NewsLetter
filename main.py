from src.newsletter_export import get_word_response

from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
from src.newsletter import generate_newsletter
import traceback

app = FastAPI()


@app.get("/newsletter")
def get_newsletter():
    try:
        return {"markdown": generate_newsletter()}
    except Exception as e:
        tb = traceback.format_exc()
        return JSONResponse(status_code=500, content={"error": str(e), "traceback": tb})

# Executive HTML endpoint
# Executive HTML endpoint
@app.get("/newsletter/html", response_class=HTMLResponse)
def get_newsletter_html():
    try:
        from src.newsletter_html import generate_newsletter_html
        return generate_newsletter_html()
    except Exception as e:
        tb = traceback.format_exc()
        return HTMLResponse(f"<h2>Error</h2><pre>{str(e)}</pre><pre>{tb}</pre>", status_code=500)

# Word download endpoint
@app.get("/newsletter/word")
def download_word():
    return get_word_response()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
