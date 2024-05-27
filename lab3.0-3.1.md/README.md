```markdown
# Documentación del Laboratorio de Gestión de Archivos en HDFS y S3

## Configuración Inicial del Clúster EMR

### Creación del Clúster
- **Nombre del Clúster**: emr-sospinai-cluster-final
- **Versión del Clúster**: 6.14.0
- **Tipo de Instancia**: m4.xlarge
- **Aplicaciones Instaladas**: Hadoop 3.3.3, Hive 3.1.3, Spark 3.4.1, Hue 4.11.0, JupyterHub 1.5.0
- **Configuración de Software**:
  ```json
  {
    "Classification": "jupyter-s3-conf",
    "Properties": {
      "s3.persistence.enabled": "true",
      "s3.persistence.bucket": "sospinainotebooks"
    }
  }
  ```

### Configuración de Seguridad y Conectividad
- **Puertos Abiertos en el Clúster**:
  - Puertos 22, 14000, 9870, 8888, 9443, 8890 habilitados para facilitar el acceso y la funcionalidad de las aplicaciones.

## Acceso y Configuración de Servicios
### Creación del Clúster
- **Nombre del Clúster**: emr-sospinai-cluster-final
- **Versión del Clúster**: 6.14.0
- **Tipo de Instancia**: m4.xlarge
- **Aplicaciones Instaladas**: Hadoop 3.3.3, Hive 3.1.3, Spark 3.4.1, Hue 4.11.0, JupyterHub 1.5.0
- **Configuración de Software**:
  ```json
  {
    "Classification": "jupyter-s3-conf",
    "Properties": {
      "s3.persistence.enabled": "true",
      "s3.persistence.bucket": "sospinainotebooks"
    }
  }


### HUE
- **Usuario**: hadoop
- **Contraseña**: Hadoop2024*
- **Problema Encontrado**:
  Al intentar acceder a los archivos de HDFS, se encontró con el error: "Cannot access: /user/hadoop. The HDFS REST service is not available."
- **Solución**:
  Se editó el archivo `/etc/hue/conf/hue.ini` cambiando el puerto de 14000 a 9870 y se reinició el servicio con `systemctl restart hue.service`.

### JupyterHub
- **Usuario**: jovyan
- **Contraseña**: jupyter
- Se creó y probó un notebook para validar las configuraciones de las variables `spark` y `sc`.

![alt text](image.png)

## Gestión de Datasets
A continuación se mostraran imagenes de como se practico la gestión y creación de archivos.

### Copiar (gestión) de archivos hacia el HDFS vía HUE.
- Los datasets fueron cargados en HDFS bajo el directorio `/user/hadoop/datasets`, asegurando que estén disponibles para análisis y procesamiento.


## Conclusión

Este laboratorio demostró la configuración efectiva y la gestión de un entorno EMR para el procesamiento de big data, incluyendo la configuración de seguridad, la resolución de problemas de acceso y la gestión eficiente de datos a gran escala.

## Comandos Útiles

- Conectar vía SSH al nodo master: `ssh -i <your-key>.pem hadoop@<master-node-ip>`
- Reiniciar servicio HUE: `systemctl restart hue.service`
- Listar archivos en HDFS: `hdfs dfs -ls /user/hadoop/datasets`

```