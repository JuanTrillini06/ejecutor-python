# 🐍 Ejecutor de Código Python

## 📋 Descripción

**Ejecutor de Código Python** es una aplicación web moderna que permite escribir y ejecutar código Python directamente desde el navegador, sin necesidad de instalar herramientas locales. Ideal para estudiantes, principiantes y desarrolladores que quieren practicar lógica de programación de forma rápida y sencilla.

### Características principales

- ✅ Interfaz intuitiva y responsiva
- ✅ Ejecución segura de código Python
- ✅ Captura de salida y errores en tiempo real
- ✅ Soporte para múltiples tipos de scripts
- ✅ Almacenamiento del código ejecutado en la sesión
- ✅ Menú hamburguesa responsive para dispositivos móviles

---

## 🛠️ Tecnologías Utilizadas

### Backend

- **Python 3.11+** - Lenguaje de programación
- **FastAPI** - Framework web moderno y de alto rendimiento
- **Uvicorn** - Servidor ASGI

### Frontend

- **HTML5** - Estructura semántica
- **CSS3** - Estilos responsivos con diseño moderno y animaciones

### Hosting

- **Vercel** - Plataforma de deployment para funciones serverless

---

## 🚀 Despliegue en Vercel (Recomendado)

---

## 💻 Ejecución Local

### Requisitos previos

- Python 3.9+
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clona el repositorio**

   ```bash
   git clone https://github.com/JuanTrillini06/ejecutor-python.git
   cd ejecutor-python
   ```

2. **Instala las dependencias**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta el servidor**

   ```bash
   python -m uvicorn api.index:app --reload --host 0.0.0.0 --port 3000
   ```

4. **Accede a la aplicación**
   Abre tu navegador e ingresa a: `http://localhost:3000`

---

## 📁 Estructura del Proyecto

``` bash
ejecutor-python/
├── api/
│   └── index.py              # Aplicación principal (FastAPI) - Para Vercel
├── main.py                   # Versión local de la app
├── requirements.txt          # Dependencias del proyecto
├── vercel.json              # Configuración de Vercel
├── vercel.txt               # Guía completa de deploy
├── .gitignore               # Archivos ignorados por Git
├── templates/               # Templates HTML (opcional)
│   ├── index.html
│   └── howuse.html
└── styles/                  # Estilos CSS (opcional)
    └── style.css
```

---

## 📖 Cómo Usar

1. **Escribe tu código Python** en el área de texto
2. **Haz clic en "Evaluá tu código"** para ejecutarlo
3. **Ve el resultado** en la sección de resultados

### Características de código soportadas

- ✅ Funciones y clases
- ✅ Bucles (for, while)
- ✅ Condicionales (if, else)
- ✅ Operaciones matemáticas
- ✅ Manipulación de strings
- ✅ Listas y diccionarios
- ✅ Importación de módulos estándar de Python

### Limitaciones

- ⚠️ No se pueden ejecutar operaciones que requieran interacción del usuario
- ⚠️ No se pueden instalar paquetes externos durante la ejecución
- ⚠️ Timeout de ejecución para prevenir bucles infinitos

---

## Ejemplo 1: Hola mundo

```python
print("hola mundo!")
```

## Ejemplo 2: Operacion suma

``` python
numUno = 1
numDos = 2
resultado = numUno + numDos
print(f"El resultado es: {resultado}")
```

### Ejemplo 3: Listas y bucles

```python
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(num ** 2)
```

---

## ⚙️ Configuración

No se requiere configuración adicional. La aplicación funciona con los siguientes parámetros predeterminados:

- **Host:** `localhost`
- **Puerto:** `3000`
- **Modo de recarga:** Habilitado para desarrollo

---

## 🔒 Seguridad

El código se ejecuta en un namespace aislado respetando los siguientes principios:

- Ejecución en entorno contenido
- Manejo robusto de errores
- Sin acceso a funciones peligrosas del sistema

---

## 📝 Licencia

Este proyecto está disponible bajo licencia libre para uso educativo.

---

## 👤 Autor

Desarrollado como herramienta educativa para iniciarse en Python.
