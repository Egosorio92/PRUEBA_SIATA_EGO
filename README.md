# PRUEBA_SIATA_EGO
En este repositorio se muestran los resultados del examen para Científico de Datos SIATA - 2026

🧾 Descripción del proyecto
Este repositorio contiene el desarrollo técnico y analítico del proyecto SIATA – Calidad de datos hidrometeorológicos, orientado a evaluar, validar y mejorar la confiabilidad de los registros provenientes de estaciones meteorológicas del Valle de Aburrá.
El trabajo incluye:

Parte 1: análisis conceptual sobre calidad del dato, estándares internacionales (ISO, WIGOS, FAIR) y diseño de arquitectura híbrida de datos.

Parte 2: implementación práctica en Python y Jupyter/Colab para la ingesta, validación, cálculo de indicadores y visualización de resultados mediante dashboard.
Se integran datos de estaciones de temperatura, precipitación, radiación y nivel, junto con scripts de control de calidad, correlaciones y auditoría de repositorios.


SIATA/
├── parte1/
│   └── respuestas.md
├── parte2/
│   ├── notebooks/
│   │   └── DESARROLLO_PRUEBA_SIATA.ipynb
│   ├── scripts/
│   │   ├── app.py
│   │   ├── srcquality.py
│   │   ├── test_quality.py
│   │   └── Modelo_de_Inmutabilidad_de_Datos_Crudos.py
│   ├── datos/
│   │   ├── Estacion_meteorologica_367_2025-12-01_2026-04-30.csv
│   │   ├── Estacion_nivel_803_2025-12-01_2026-04-30.csv
│   │   ├── Estacion_piranometro_6004_2025-12-01_2026-04-30.csv
│   │   └── Estacion_pluviometrica_35_2025-12-01_2026-04-30.csv
│   ├── resultados/
│   │   ├── PANTALLAZOS_DSHBOARD.pptx
│   │   └── RESUMEN_EJECUTIVO.docx
│   └── requirements.txt
└── README.md
