# Usar la imagen base de Python
FROM python:3.9-slim

# Instalar las dependencias necesarias (apt-get) y ODBC Driver para SQL Server
RUN apt-get update \
    && apt-get install -y \
    curl \
    gnupg \
    lsb-release \
    ca-certificates \
    unixodbc \
    unixodbc-dev \
    gcc \
    g++ \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/mssql-server/debian/mssql-server-2019.list > /etc/apt/sources.list.d/mssql-server-2019.list \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && apt-get update \
    && apt-get install -y msodbcsql17 \
    && apt-get clean

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . /app

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "app.py"]
