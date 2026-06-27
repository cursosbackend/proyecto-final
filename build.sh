#!/usr/bin/env bash
set -o errexit

echo "--- Iniciando proceso de instalación de dependencias ---"
pip install -r requirements.txt

echo "--- Compilando archivos estáticos de la aplicación ---"
python manage.py collectstatic --noinput

echo "--- Aplicando migraciones estructurales a SQLite3 ---"
python manage.py migrate

echo "--- Cargando catálogo base desde archivos de fixture ---"
if [ -f "productos_iniciales.json" ]; then
    python manage.py loaddata productos_iniciales.json
else
    echo "Aviso: No se encontró el archivo productos_iniciales.json para precarga."
fi

echo "--- Creando usuarios iniciales ---"
python manage.py seed_data

echo "--- Proceso de construcción finalizado con éxito ---"
