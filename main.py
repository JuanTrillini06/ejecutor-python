import os
import io
import sys
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
current_dir = os.path.dirname(os.path.realpath(__file__))

# Montar archivos estáticos PRIMERO
styles_path = os.path.join(current_dir, "styles")
templates_path = os.path.join(current_dir, "templates")

app.mount("/static", StaticFiles(directory=styles_path), name="static")
templates = Jinja2Templates(directory=templates_path)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Renderiza la página inicial
    return templates.TemplateResponse("index.html", {"request": request, "resultado": ""})

@app.get("/como-funciona", response_class=HTMLResponse)
async def how_to_use(request: Request):
    return templates.TemplateResponse("howuse.html", {"request": request})

@app.post("/ejecutar", response_class=HTMLResponse)
async def ejecutar_codigo(request: Request, codigo: str = Form(...)):
    if not codigo.strip():
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "resultado": "Por favor, introduzca código.",
            "codigo_previo": ""
        })

    # Capturar output del código ejecutado
    output_capturado = io.StringIO()
    namespace = {}
    
    try:
        # Redirigir stdout para capturar prints
        sys.stdout = output_capturado
        
        # Ejecutar el código en un namespace aislado
        exec(codigo, namespace)
        
        # Restaurar stdout
        sys.stdout = sys.__stdout__
        
        # Obtener el resultado
        resultado_final = output_capturado.getvalue()
        if not resultado_final:
            resultado_final = "Código ejecutado exitosamente (sin output)."
            
    except Exception as e:
        # Restaurar stdout en caso de error
        sys.stdout = sys.__stdout__
        resultado_final = f"Error: {type(e).__name__}: {str(e)}"

    return templates.TemplateResponse("index.html", {
        "request": request, 
        "resultado": resultado_final,
        "codigo_previo": codigo
    })