import webbrowser
import uvicorn

webbrowser.open("http://127.0.0.1:8000/chat")
uvicorn.run("health_web.main:app", host="127.0.0.1", port=8000, reload=True)