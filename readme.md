Crear un contenedor de SQL Server con Docker
Configurar Flask para conectarse a SQL Server
Definir los modelos en SQLAlchemy
Implementar el CRUD en Flask
Probar la API con Postman o curl

# comando docker sql server
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=TuPassword123!" \
   -p 1433:1433 --name sqlserver \
   -d mcr.microsoft.com/mssql/server:latest

ACCEPT_EULA=Y → Acepta los términos de uso.
SA_PASSWORD=TuPassword123! → Contraseña del usuario sa.
-p 1433:1433 → Expone el puerto 1433 (por defecto en SQL Server).
--name sqlserver → Nombre del contenedor.
mcr.microsoft.com/mssql/server:latest → Imagen oficial de SQL Server.

# Ejecuta la base de datos
docker exec -it sqlserver /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P 1234

