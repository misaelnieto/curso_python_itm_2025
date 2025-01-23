# Alcancía

Hecha en Flask

# Instalación

- Instalar UV desde https://docs.astral.sh/uv/getting-started/installation/
- Instalar virtualenv:
    ```
    uv venv
    ```
- Inicializar la base de datos SQLite
    ```
    uv run -- flask initdb
    ```
- Correr aplicación Flask en modo debug
    ```
    uv run -- flask run --debug
    ```
