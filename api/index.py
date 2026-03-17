import os
import io
import sys
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import html

app = FastAPI()

# Obtener el CSS como string
STYLE_CSS = """
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.pagina {
    font-family: Arial, sans-serif;
    background-color: #1E293B;
    padding: 20px;
    display: grid;
    grid-template-columns:  1fr min-content;
    grid-template-rows: repeat(2, 1fr);
    grid-column-gap: 10px;
    min-height: 100vh;
}

.pagina .contenido{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;
    padding: 20px;
    grid-area: 1/1/3/2;
}

.pagina .contenido .titulo {
    color: #FFD43B;
    margin-bottom: 20px;
    font-size: 2.5em;
    text-shadow: #fddc64 0px 0px 7px;
}

.pagina .contenido .contenedor-editor {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.pagina .contenido .contenedor-editor .editor {
    width: 150%;
    max-width: 800px;
    height: 300px;
    padding: 10px;
    border: 1px solid #3776AB;
    border-radius: 5px;
    box-shadow: 0 0 10px #3776AB;
    background-color: #0F172A;
    font-family: 'Courier New', Courier, monospace;
    font-size: 1em;
    color:  #F8FAFC;
}

.pagina .contenido .contenedor-editor .boton-enviar {
    margin-top: 10px;
    padding: 10px 20px;
    background-color: #FFD43B;
    color: #0F172A;
    border: none;
    cursor: pointer;
    font-size: 1em;
    align-items: center;
    border-radius: 5px;
    transition: 0.3s ease;
}

.pagina .contenido .contenedor-editor .boton-enviar:hover {
    background-color: #FFC107;
    scale: 1.05;
}

.pagina .contenido .resultado-contenido {
    padding: 20px;
    border: 1px solid #3776AB;
    border-radius: 5px;
    box-shadow: 0 0 10px #3776AB;
    background-color: #0F172A;
    width: 80%;
    max-width: 800px;
    margin-top: 20px;
}

.pagina .contenido .resultado-contenido .resultado{
    color: #F8FAFC;
    text-align: center;
}

.pagina .contenido .resultado-contenido pre{
    color: #4ADE80;
    font-family: 'Courier New', Courier, monospace;
    font-size: 1em;
}

.pagina .cabecera {
    grid-area: 1/2/3/3;
    display: flex;
    align-items: start;
    justify-content: center;
    background-color: #FFD43B;
    border-radius: 5px;
    box-shadow: 0 0 10px #FFC107;
    position: relative;
}

.pagina .cabecera .menu-toggle {
    display: none;
    background: none;
    border: none;
    font-size: 1.8em;
    cursor: pointer;
    color: #F8FAFC;
    padding: 10px 15px;
    width: 100%;
    text-align: center;
}

.pagina .cabecera .navegacion ul {
    list-style: none;
    display: flex;
    flex-direction: column;
    text-align: center;
    padding: 5px;
    gap: 20px;
}

.pagina .cabecera .navegacion li a {
    color: #F8FAFC;
    text-decoration: none;
    font-size: 1.2em;
    transition: 0.3s ease;
}

.pagina .cabecera .navegacion li a:hover {
    color: #1E293B;
}

.pagina .como-funciona-contenido{
    display: flex;
    flex-direction: column;
    align-items: start;
    justify-content: start;
    padding: 20px;
}

.pagina .como-funciona-contenido .titulo {
    color: #FFD43B;
    margin-bottom: 20px;
    font-size: 2.5em;
    text-shadow: #fddc64 0px 0px 7px;
}

.pagina .como-funciona-contenido .parrafo {
    color: #F8FAFC;
    text-align: start;
    margin-top: 20px;
}

.pagina .como-funciona-contenido .lista{
    color: #F8FAFC;
    text-align: start;
    margin-top: 20px;
    list-style: none;
}

.pagina .como-funciona-contenido .lista li{
    margin-bottom: 10px;
    font-size: 1.2em;
}

.pagina .como-funciona-contenido .lista-secundaria{
    color: #F8FAFC;
    text-align: start;
    margin-top: 20px;
    list-style: none;
}

.pagina .como-funciona-contenido .lista-secundaria li{
    margin-bottom: 10px;
    font-size: 1.2em;
}

@media (max-width: 768px) {
    .pagina {
        padding: 10px;
        display: grid;
        grid-template-columns: min-content;
        grid-template-rows: min-content 1fr;
        grid-row-gap: 10px;
    }
    
    .pagina .contenido {
        grid-area: 2/1/3/3;
        padding-left: 10px;
        padding-right: 10px;
    }
    
    .pagina .contenido .titulo {
        font-size: 1.8em;
    }
    
    .pagina .contenido .contenedor-editor .editor {
        width: 100% !important;
        font-size: small;
    }
    
    .pagina .contenido .contenedor-editor .boton-enviar {
        font-size: 0.9em;
        padding: 8px 16px;
    }
    
    .pagina .contenido .resultado-contenido {
        width: 100%;
    }
    
    .pagina .contenido .resultado-contenido .resultado{
        font-size: 1.2em;
    }
    
    .pagina .contenido .resultado-contenido pre{
        font-size: small;
    }
    
    .pagina .como-funciona-contenido{
        grid-area: 2/1/3/3;
        padding-left: 10px;
        padding-right: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    
    .pagina .como-funciona-contenido .titulo {
        font-size: 1.8em;
    }
    
    .pagina .como-funciona-contenido .parrafo {
        color: #F8FAFC;
        text-align: start;
        margin-top: 20px;
        font-size: 0.8em;
    }

    .pagina .como-funciona-contenido .lista{
        color: #F8FAFC;
        text-align: start;
        margin-top: 20px;
        list-style: none;
    }
    
    .pagina .como-funciona-contenido .lista li{
        margin-bottom: 10px;
        font-size: 1em;
    }
    
    .pagina .como-funciona-contenido .lista-secundaria{
        color: #F8FAFC;
        text-align: start;
        margin-top: 20px;
        list-style: none;
    }
    
    .pagina .como-funciona-contenido .lista-secundaria li{
        margin-bottom: 10px;
        font-size: 1em;
    }
    
    .pagina .cabecera {
        grid-area: 1/1/2/3;
        padding-left: 10px;
        padding-right: 10px;
        display: flex;
        align-items: end;
        flex-direction: column;
    }

    .pagina .cabecera .menu-toggle {
        display: block;
        color: #1E293B;
    }

    .pagina .cabecera .navegacion {
        display: none;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background-color: #FFD43B;
        border-radius: 0 0 5px 5px;
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
        z-index: 1000;
    }

    .pagina .cabecera .navegacion.active {
        display: block;
    }

    .pagina .cabecera .navegacion ul {
        flex-direction: column;
        gap: 0;
        padding: 15px 0;
    }

    .pagina .cabecera .navegacion li {
        padding: 10px 0;
        border-bottom: 1px solid rgba(248, 250, 252, 0.2);
    }

    .pagina .cabecera .navegacion li:last-child {
        border-bottom: none;
    }

    .pagina .cabecera .navegacion li a {
        color: #1E293B;
    }
    
    .pagina .cabecera .navegacion li a:hover {
        color: #0F172A;
    }
}
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect fill='%23FFD43B' width='100' height='100'/><text x='50' y='75' font-size='60' font-weight='bold' text-anchor='middle' fill='%231E293B' font-family='Arial'>P</text></svg>">
    <style>
        {css}
    </style>
    <title>Ejecutor python</title>
</head>
<body class = "pagina">
    <header class = "cabecera">
        <button class="menu-toggle" id="menuToggle">☰</button>
        <nav class = "navegacion" id="menuNav">
            <ul>
                <li><a href="/">Inicio</a></li>
                <li><a href="/como-funciona">¿Cómo usarlo?</a></li>
                <li><a href="https://docs.python.org/es/3/" target="_blank">Documentacion Python</a></li>
            </ul>
        </nav>
    </header>
    <main class = "contenido">
        <h1 class = "titulo">Editor de código Python</h1>
    
        <form class = "contenedor-editor" action="/ejecutar" method="post">
            <textarea class="editor" name="codigo" rows="10" cols="50" required placeholder="Escribe tu código aquí...">{codigo_previo}</textarea>
            <br>
            <button class="boton-enviar" type="submit">Evaluá tu código</button>
        </form>

        {resultado_html}
    </main>
    <script>
        document.getElementById('menuToggle').addEventListener('click', function() {{
            const menuNav = document.getElementById('menuNav');
            menuNav.classList.toggle('active');
        }});

        // Cerrar menú al hacer clic en un enlace
        document.querySelectorAll('.navegacion a').forEach(link => {{
            link.addEventListener('click', function() {{
                document.getElementById('menuNav').classList.remove('active');
            }});
        }});
    </script>
</body>
</html>
"""

HOWUSE_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect fill='%23FFD43B' width='100' height='100'/><text x='50' y='75' font-size='60' font-weight='bold' text-anchor='middle' fill='%231E293B' font-family='Arial'>P</text></svg>">
    <style>
        {css}
    </style>
    <title>Ejecutor python</title>
</head>
<body class = "pagina">
    <header class = "cabecera">
        <button class="menu-toggle" id="menuToggle">☰</button>
        <nav class = "navegacion" id="menuNav">
            <ul>
                <li><a href="/">Inicio</a></li>
                <li><a href="/como-funciona">¿Cómo usarlo?</a></li>
                <li><a href="https://docs.python.org/es/3/" target="_blank">Documentacion Python</a></li>
            </ul>
        </nav>
    </header>
    <main class = "como-funciona-contenido">
        <h1 class = "titulo">¿Cómo usar este editor de código Python?</h1>
    
        <p class = "parrafo">Este editor de código Python te permite escribir y ejecutar código Python directamente en tu navegador. Para usarlo, sigue estos pasos:</p>
        
        <ol class = "lista">
            <li>Escribe tu código Python en el área de texto proporcionada.</li>
            <li>Haz clic en el botón "Evaluá tu código" para ejecutar el código que has escrito.</li>
            <li>El resultado de la ejecución se mostrará debajo del botón, en la sección "Resultado".</li>
        </ol>

        <p class = "parrafo">Este editor admite caracteres comprendidos en el conjunto de caracteres UTF-8. Por ejemplo:</p>

        <ul class = "lista-secundaria">
            <li>Caracteres acentuados: á, é, í, ó, ú</li>
            <li>Caracteres especiales: ñ, ü, ç</li>
            <li>Símbolos: @, #, $, %, ^, &, *, (, )</li>
            <li>Comillas rectas: ', ". NO comillas curvas: ", "</li>
        </ul>

        <p class = "parrafo">Puedes escribir cualquier código Python válido, desde operaciones simples hasta funciones más complejas. ¡Diviértete programando!</p>
    </main>
    <script>
        document.getElementById('menuToggle').addEventListener('click', function() {{
            const menuNav = document.getElementById('menuNav');
            menuNav.classList.toggle('active');
        }});

        // Cerrar menú al hacer clic en un enlace
        document.querySelectorAll('.navegacion a').forEach(link => {{
            link.addEventListener('click', function() {{
                document.getElementById('menuNav').classList.remove('active');
            }});
        }});
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTML_TEMPLATE.format(
        css=STYLE_CSS,
        codigo_previo="",
        resultado_html=""
    )

@app.get("/como-funciona", response_class=HTMLResponse)
async def how_to_use():
    return HOWUSE_TEMPLATE.format(css=STYLE_CSS)

@app.post("/ejecutar", response_class=HTMLResponse)
async def ejecutar_codigo(codigo: str = Form(...)):
    if not codigo.strip():
        resultado_html = ""
        resultado_final = "Por favor, introduzca código."
    else:
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
        
        resultado_html = f"""<section class = "resultado-contenido">
            <h2 class = "resultado">Resultado</h2>
            <br>
            <pre>{html.escape(resultado_final)}</pre>
        </section>"""

    return HTML_TEMPLATE.format(
        css=STYLE_CSS,
        codigo_previo=html.escape(codigo) if codigo else "",
        resultado_html=resultado_html
    )
