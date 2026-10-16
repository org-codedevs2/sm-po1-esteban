<div align="center">

# 🚀 Multi-App Python & Actions

### Aplicaciones de **Suma** y **Resta** con Python y FastAPI

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Tests-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

[![Ver API en Render](https://img.shields.io/badge/🌐_Ver_API_en_Render-000000?style=for-the-badge)](https://sm-po1-esteban.onrender.com)
[![Documentación](https://img.shields.io/badge/📘_Documentación_/docs-009688?style=for-the-badge)](https://sm-po1-esteban.onrender.com/docs)
[![GitHub Pages](https://img.shields.io/badge/📄_GitHub_Pages-222222?style=for-the-badge&logo=github&logoColor=white)](https://org-codedevs2.github.io/sm-po1-esteban/)

</div>

---

## 🎬 Demo

<div align="center">

![Demo de la aplicación](docs/demo.gif)

</div>

> 💡 Guarda tu GIF o captura como `docs/demo.gif` (o cambia la ruta de arriba) para que se vea aquí.

## 🌐 Enlaces

| Servicio | Enlace |
|---|---|
| 🖥️ API desplegada en Render | [sm-po1-esteban.onrender.com](https://sm-po1-esteban.onrender.com) |
| 📘 Documentación de la API (Swagger) | [sm-po1-esteban.onrender.com/docs](https://sm-po1-esteban.onrender.com/docs) |
| 📄 Página en GitHub Pages | [org-codedevs2.github.io/sm-po1-esteban](https://org-codedevs2.github.io/sm-po1-esteban/) |

> ⚠️ La API está en el plan gratuito de Render. Si lleva un tiempo sin uso, la primera visita puede tardar cerca de 50 segundos en responder.

## 🛠️ Tecnologías

<div align="center">

<img src="https://skillicons.dev/icons?i=python,fastapi,html,css,js,github,githubactions,git,idea&perline=9" alt="Tecnologías" />

</div>

- 🐍 Python 3
- ⚡ FastAPI
- 🦄 Uvicorn
- 🧪 Pytest
- ⚙️ GitHub Actions (CI)
- 📄 GitHub Pages
- ☁️ Render

## 📁 Estructura del proyecto

```
sm-po1-esteban/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/python-ci.yml
│   ├── CODEOWNERS
│   └── PULL_REQUEST_TEMPLATE.md
├── app_suma/
│   ├── public/
│   └── src/
│       ├── main.py
│       ├── index.html
│       └── test_main.py
├── app_resta/
│   ├── templates/
│   ├── resta_logic.py
│   ├── test_resta.py
│   └── views.py
├── docs/
├── public/
├── requirements.txt
└── README.md
```

## ▶️ Cómo ejecutarlo en local

1. Clona el repositorio:

```bash
git clone https://github.com/org-codedevs2/sm-po1-esteban.git
cd sm-po1-esteban
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Inicia la API de suma:

```bash
uvicorn app_suma.src.main:app --reload
```

4. Abre en el navegador `http://127.0.0.1:8000/docs`.

## 🧪 Pruebas

```bash
pytest
```

Las pruebas también se ejecutan automáticamente con GitHub Actions.

## ☁️ Despliegue en Render

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn app_suma.src.main:app --host 0.0.0.0 --port $PORT`

## 👨‍💻 Autor

<div align="center">

**Angel Esteban Rivera Camayo**

Aprendiz de Análisis y Desarrollo de Software, SENA

[![GitHub](https://img.shields.io/badge/GitHub-angelcamayojm--wq-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/angelcamayojm-wq)

</div>
