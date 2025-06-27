- 👋 Hi, I’m @fgiusti90
- 👀 Currently developing AI Agents to develop as HR Consultants
- 📫 How to reach me: www.linkedin.com/in/federico-giusti-59bb991b

<!---
fgiusti90/fgiusti90 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

## MVP BPyME

Este repositorio incluye un ejemplo simple de backend en Python utilizando **FastAPI** y **LangChain** para orquestar agentes de IA. El backend se encuentra en `backend/main.py` y espera variables de entorno `SUPABASE_URL` y `SUPABASE_KEY` para conectarse a Supabase. El endpoint `/chat` procesa mensajes y devuelve la respuesta generada por GPT-4.

### Ejecutar localmente

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Definir variables de entorno `SUPABASE_URL` y `SUPABASE_KEY`.
3. Iniciar la aplicación:
   ```bash
   uvicorn backend.main:app --reload
   ```

### Nota

El código es un punto de partida para un MVP y requiere configuraciones adicionales de seguridad y despliegue para un entorno productivo.
