# 🐍 Ejecutor de Código Python

## 📋 Descripción

**Ejecutor de Código Python** es una aplicación web moderna que permite escribir y ejecutar código Python directamente desde el navegador, sin necesidad de instalar herramientas locales. Ideal para estudiantes, principiantes y desarrolladores que quieren practicar lógica de programación de forma rápida y sencilla.

### Características principales

- ✅ Interfaz intuitiva y responsiva
- ✅ Ejecución segura de código Python
- ✅ Captura de salida y errores en tiempo real
- ✅ Soporte para múltiples tipos de scripts
- ✅ Almacenamiento del código ejecutado en la sesión

---

## 🛠️ Tecnologías Utilizadas

### Backend

- **Python 3.12** - Lenguaje de programación
- **FastAPI** - Framework web moderno y de alto rendimiento
- **Uvicorn** - Servidor ASGI

### Frontend

- **HTML5** - Estructura semántica
- **CSS3** - Estilos responsivos con diseño moderno

---

## 🚀 Cómo Usar

### Opción 1: En Línea (Recomendado)

Accede a la versión desplegada en Replit sin necesidad de instalar nada:

[Ejecutor-Python](https://ejecutor-python--juantrillini.replit.app/)

### Opción 2: Ejecución Local

#### Requisitos previos

- Python 3.9+
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

#### Pasos de instalación

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
   python -m uvicorn main:app --reload
   ```

4. **Accede a la aplicación**
   Abre tu navegador e ingresa a: `http://127.0.0.1:8000`

---

## 📁 Estructura del Proyecto

``` bash
ejecutor-python/
├── main.py                 # Aplicación principal (FastAPI)
├── requirements.txt        # Dependencias del proyecto
├── templates/
│   └── index.html         # Página principal
└── styles/
    └── style.css          # Estilos de la aplicación
```

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Imprime un saludo

```python
print("¡Hola, mundo!")
```

### Ejemplo 2: Operaciones matemáticas

```python
numero = 10
resultado = numero * 2
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

- **Host:** `127.0.0.1`
- **Puerto:** `8000`
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
