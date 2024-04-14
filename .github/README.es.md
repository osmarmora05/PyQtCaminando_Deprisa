# Estado
**Progreso**

# Descripción del proyecto
"PyQtCaminando_Deprisa", es una aplicación CRUD (Crear, Leer, Actualizar, Eliminar) basada en PyQt5 fácil de usar, diseñada específicamente para integrarse perfectamente con bases de datos MySQL. Este proyecto sirve como una implementación práctica para la clase de Ingenieria de softaware en el que se abordaba el siguiente caso:

La empresa Caminando de Prisa,  está teniendo serios problemas, debido a que se realiza la facturación manualmente, por lo que ha decidido contratarlo a usted como Ingeniero de Sistemas para que desarrolle un software de facturación a su medida.

En la entrevista, el Director de la empresa, le informa, con que cuenta y que desea para su empresa:

1. La empresa es vendedora de artículos de oficina.
2. El presupuesto es limitado dado que es una institución pequeña.
3. No se cuenta con computadoras, habrá que obtenerlas para la implantación y desarrollo del  software.
4. El software se necesita esté listo en un mes a partir de la fecha.
5. El sistema llevará el control de facturas numeradas secuencialmente.
6. Tendrá opción para calcular y facturar con IVA o sin él.
7. Tendrá opción para aplicar descuento, donde el cajero pueda digitar el porcentaje de descuento a aplicar, de acuerdo a algunas normas establecidas por la empresa.
8. Los artículos a facturar deberán ser obtenidos desde una BD, que la empresa proporcionará.
9. Al concluir el día, se genera un formato de arqueo en pantalla, donde el cajero introducirá los datos  y el sistema realizará la sumatoria de las facturas consecutivas e imprima el arqueo del día.
10. Se desea que se genere un  reporte de las ventas semanales y quincenales.
11. Que cuente con contraseñas para acceso al sistema.

## Prerrequisitos
Antes de comenzar, asegúrese de que MySQL Server esté instalado en su sistema. Si aún no está instalado, puedes descargarlo desde el sitio web oficial de MySQL.


# Guía de instalación
Para comenzar con "PyQtCaminando_Deprisa", siga estos sencillos pasos de instalación:

1. **Abre tu terminal:**
    Comience abriendo su terminal o símbolo del sistema.

2. **Clonar el repositorio:**
    Utilice el siguiente comando para clonar el repositorio del proyecto y navegar al directorio del proyecto:
    
    ```sh
   git clone https://github.com/osmarmora05/PyQtCaminando_Deprisa && cd PyQtCaminando_Deprisa
   ```

3. **Configurar un entorno virtual:**
    Cree un entorno virtual para gestionar las dependencias del proyecto por separado:

    ```sh
   python -m venv venv
   ```

4. **Activar el entorno virtual:**
    Dependiendo de su sistema operativo, active el entorno virtual usando uno de estos comandos:

    - Windows:

     ```sh
     .\venv\Scripts\activate
     ```

   - Unix/Linux:
     ```sh
     source ./venv/bin/activate
     ```

5. **Instalar dependencias requeridas:**
    Instale todos los paquetes de Python necesarios como se enumeran en el archivo `requirements.txt`:

    ```sh
    python main.py
    ```