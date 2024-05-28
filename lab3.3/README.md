# Laboratorio 3-3: Implementación de un Data Warehouse con AWS Redshift y Redshift Spectrum

## Autor
- **Nombres**: Isaac Tadina G y Santiago Ospina I 

## Objetivos
Este laboratorio tiene como objetivo implementar un data warehouse utilizando AWS Redshift, realizar cargas de datos y consultas mediante Redshift Spectrum.

## Configuración del Clúster Redshift
1. **Creación del Clúster Redshift**: 
  - Un clúster con el nombre `redshift-cluster-1` fue configurado utilizando la versión más reciente recomendada por AWS. 

  ![alt text](image.png)
  ![alt text](image-1.png)
  ![alt text](image-2.png)
  ![alt text](image-3.png)
  ![alt text](image-4.png)


2. **Configuración de Seguridad**:
   - Se configuró un rol IAM con los permisos necesarios (`AmazonS3ReadOnlyAccess`, `AWSGlueConsoleFullAccess`, `AmazonAthenaFullAccess`) para permitir que Redshift acceda a los datos almacenados en S3 y maneje esquemas de datos a través de Glue y Athena. (la creación de este rol saco error ya que estamos usando el AWS academy)

   ![alt text](image-5.png)
   ![alt text](image-6.png)
   ![alt text](zz_AR_1_IAM_3.png)
   ![alt text](zz_AR_1_IAM_4.png)
   ![alt text](zz_AR_1_IAM_5.png)
   ![alt text](zz_AR_1_IAM_6.png)
   ![alt text](zz_AR_1_IAM_ERROR.png)

   - Al obtener error usamos el IAM llamado `LabRole`
   ![alt text](zz_AR_1_IAM_LABROLE_7.png)

## Gestión de Datos
1. **Carga de Datos y Redshift**:
   - Se utilizó el dataset de ejemplo `tickit` proporcionado por AWS, cargando datos directamente en el clúster Redshift para realizar consultas SQL básicas.

   ![alt text](z_2_OpenQueryEditor.png)
   ![alt text](z_3_createSampleDatabase.png)

2. **Redshift Spectrum**:
   - Se creó un esquema externo `myspectrum_schema` y una base de datos `myspectrum_db` para gestionar los datos almacenados en S3.
   - Se definieron tablas externas en Redshift Spectrum para realizar consultas sobre datos almacenados de forma externa.

  ![alt text](zz_AR_2_CreateExternalDB.png)
  ![alt text](zz_AR_3_CreateTableWithExternalData.png)
  ![alt text](zz_AR_3_GetDataQuery.png)
  ![alt text](zz_AR_4_CreateRedshiftTableToCombine.png)

  - Carga de datos en la tabla externa creada:
  ![alt text](zz_AR_4_LoadDataInTableEvent2.png)
  ![alt text](zz_AR_4_ShowEvent2DataLoaded.png)

## Consultas y Análisis
1. **Consultas en Redshift**:
   - Se realizaron diversas consultas SQL para analizar los datos del dataset `tickit`.

   ![alt text](z_4_queries.png)
   ![alt text](z_4_salesForDateQuery.png)
   ![alt text](z_4_salesPerEventQuery.png)
   ![alt text](z_4_salesTableDefinitionQuery.png)
   ![alt text](z_4_totalQuentityBuyerQuery.png)

2. **Redshift Spectrum**:
   - Se realizó una consulta combinando datos de tablas nativas de Redshift con tablas externas en S3, proporcionando un ejemplo de cómo integrar datos en un entorno de data warehouse híbrido.

   ![alt text](zz_AR_4_ShowEvent2DataLoadedCounter.png)
   ![alt text](zz_AR_5_QueryWithExternalAndNativeTables.png)

## Comandos Utilizados
```sql
-- Crear esquema externo
CREATE EXTERNAL SCHEMA myspectrum_schema FROM DATA CATALOG DATABASE 'myspectrum_db' IAM_ROLE 'arn:aws:iam::433075868803:role/LabRole' CREATE EXTERNAL DATABASE IF NOT EXISTS;

-- Crear tabla externa
CREATE EXTERNAL TABLE myspectrum_schema.sales(
    salesid INTEGER,
    listid INTEGER,
    sellerid INTEGER,
    buyerid INTEGER,
    eventid INTEGER,
    dateid SMALLINT,
    qtysold SMALLINT,
    pricepaid DECIMAL(8,2),
    commission DECIMAL(8,2),
    saletime TIMESTAMP)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
LOCATION 's3://emontoyadatalake/datasets/tickitdb2/sales/';

-- Cargar datos en tabla nativa
COPY event2 FROM 's3://emontoyadatalake/datasets/tickitdb2/events/allevents.txt' IAM_ROLE 'arn:aws:iam::433075868803:role/LabRole' DELIMITER '|' TIMEFORMAT 'YYYY-MM-DD HH:MI:SS' REGION 'us-east-1';

-- Consulta combinando tablas externas y nativas
SELECT TOP 10 myspectrum_schema.sales.eventid, SUM(myspectrum_schema.sales.pricepaid) FROM myspectrum_schema.sales, event2 WHERE myspectrum_schema.sales.eventid = event2.eventid AND myspectrum_schema.sales.pricepaid > 30 GROUP BY myspectrum_schema.sales.eventid ORDER BY 2 DESC;
```

## Conclusión

Este laboratorio proporcionó una experiencia práctica valiosa en la configuración y manejo de un data warehouse utilizando AWS Redshift y Redshift Spectrum. A través de la implementación de un clúster Redshift y la configuración de Redshift Spectrum, hemos demostrado cómo se pueden integrar datos almacenados tanto internamente como externamente para realizar análisis complejos y consultas SQL eficientes. Este laboratorio no solo reforzó la comprensión de las tecnologías de almacenamiento y procesamiento de datos en la nube, sino que también destacó la importancia de la gestión eficaz de recursos para controlar los costos en un entorno de cloud computing. Los conocimientos adquiridos aquí son fundamentales para cualquiera que busque desarrollar, configurar y optimizar soluciones de big data en la nube.

