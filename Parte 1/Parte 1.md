# Parte 1: Conceptual, estándares y arquitectura

## Pregunta 1.1. Explique con sus propias palabras qué significa que un dato hidrometeorológico
tenga calidad. Su respuesta debe:
(a) Definir calidad como aptitud para el uso y vincularla al menos con tres dimensiones tomadas
de un marco formal (por ejemplo DAMA-DMBOK, ISO/IEC 25012 o ISO 8000).
(b) Distinguir entre calidad del dato, calidad del instrumento (exactitud, calibración, trazabilidad)
y calidad del proceso.
(c) Explicar por qué un dato físicamente plausible no es necesariamente un dato correcto

### RESPUESTA:
---> La calidad de un dato meteorológico indica que tan apto es ese dato para usarse, que tan confiable es y útil para la investigación que se esta realizando.
a) Con rspecta al marco DAMA-DMBOK la calidad del dato se evalua con respecto a exactitud (Accuracy), Completitud (Completeness), Consistencia (Consistency) y algunas dimensiones
complementarias como validez, actualidad y trazabilidad. 
b) La calidad el dato vs la calidad del instrumento se refiere a que el valor almacenado del dato es correcto, completo y coherente y refleja una realidad en este caso
física del entorno mientras que la calidad del instrumento depende de la exactitud y la calibración del sensor o equipo que esta hacendo la medida. Ej un equipo mal
calibrado puede tomar un dato erróneo. 

c) Un dato plausible no es necesariamente correcto porque el dato puede provenir de un sensor con errores, descalibrado, con error de digitación o transmisión entonces
ese dato aunque fue leído puede estar errado. Un ejemplo, el sensor mide 25°C pero esta descalibrado, el dato de 25°C es plausible (fisicamente correcto) pero la calidad
no está garantizada. Tomando el mismo ejemplo El sensor mide 25°C pero en realidad debería dar un valor de 29°C



## Pregunta 1.2. Complete la siguiente tabla y justifique en un párrafo la diferencia entre cada nivel.
Incluya qué se espera que cambie del dato al pasar de un nivel al siguiente.

Aspecto Dato crudo Dato validado con
metadatos
Dato para
consumo del
usuario
Definición
Unidades y resolución
Banderas de calidad
Metadatos mínimos
Tratamiento de faltantes
Usuario típico
Riesgo de mal uso

Qué se busca
Se espera que el candidato mencione, entre otros elementos: identificador y coordenadas de la
estación, altura del sensor, unidades, resolución, intervalo de muestreo, zona horaria, versión
del algoritmo de validación, diccionario de banderas, historial de mantenimiento y calibración, y
licencia de uso (referencia a los estándares de metadatos de WIGOS y a ISO 19115).


### RESPUESTA:
| Aspecto | Dato crudo | Dato validado con metadatos | Dato para consumo del usuario |
| --- | --- | --- | --- |
| Definición | Valor medido directamente por el sensor | Valor revisado y documentado con metadatos (por ejemplo, calibración, ubicación, resolución) | Valor listo para análisis o publicación |
| Unidades y resolución | Puede tener errores o inconsistencias | Verificadas y normalizadas | Homogéneas y estandarizadas |
| Banderas de calidad | No aplicadas | Incluidas según diccionario de banderas | Interpretadas para el usuario |
| Metadatos mínimos | Escasos o ausentes | Completos (según WIGOS, ISO 19115) | Visibles y comprensibles |
| Tratamiento de faltantes | No realizado | Documentado | Imputado o justificado |
| Usuario típico | Técnico o operador | Analista | Público o decisor |
| Riesgo de mal uso | Alto | Moderado | Bajo |

La calidad de los datos hidrometeorológicos se construye progresivamente desde el dato crudo hasta el dato validado y documentado con metadatos.  
Un dato de calidad no solo debe ser físicamente plausible, sino también **trazable, verificable y contextualizado** dentro de un proceso técnico que garantice su confiabilidad y utilidad para la toma de decisiones.






## Pregunta 1.3. Proponga tres (3) indicadores de calidad aplicables a los datos que SIATA publica.
Para cada uno, complete la ficha técnica:
Campo Descripción
Nombre y dimensión de calidad
Objetivo y pregunta que responde
Fórmula (con definición de cada término)
Unidad de medida y periodicidad de cálculo
Fuente de datos y nivel de agregación (estación, red, variable)
Umbrales de semáforo (aceptable, alerta, crítico) y su justificación
Responsable y acción correctiva asociada
Limitaciones y posibles sesgos del indicador
Criterios de la pregunta. Los indicadores deben ser medibles, automatizables, accionables y comparables
entre variables y estaciones. Se penalizan indicadores redundantes entre sí (por ejemplo, dos formas
de medir completitud). Los tres deben cubrir dimensiones distintas

RESPUESTA: Estos tres indicadores —completitud, consistencia temporal y exactitud— permiten evaluar de forma práctica si los datos de SIATA son confiables y útiles para análisis y toma de decisiones.

## Pregunta 1.3 – Indicadores de calidad para datos SIATA

### Indicador 1: Completitud
- **Dimensión:** Completitud.  
- **Objetivo:** Saber qué porcentaje de datos esperados realmente se registró.  
- **Fórmula:** (Registros observados / Registros esperados) × 100.  
- **Unidad y periodicidad:** %, cálculo diario o mensual.  
- **Fuente:** Estaciones SIATA, por variable.  
- **Semáforo:** Verde ≥95%, Amarillo 80–94%, Rojo <80%.  
- **Responsable:** Operación SIATA; revisar conectividad.  
- **Limitación:** No distingue si los datos presentes son correctos.

---

### Indicador 2: Consistencia temporal
- **Dimensión:** Consistencia.  
- **Objetivo:** Verificar que los datos estén en orden y sin duplicados.  
- **Fórmula:** (Registros coherentes / Registros totales) × 100.  
- **Unidad y periodicidad:** %, cálculo semanal.  
- **Fuente:** Series temporales de cada estación.  
- **Semáforo:** Verde ≥98%, Amarillo 90–97%, Rojo <90%.  
- **Responsable:** Validación SIATA; depurar duplicados.  
- **Limitación:** No mide exactitud física, solo coherencia temporal.

---

### Indicador 3: Exactitud frente a referencia
- **Dimensión:** Exactitud.  
- **Objetivo:** Comparar datos SIATA con una estación patrón.  
- **Fórmula:** Promedio del error absoluto entre SIATA y referencia.  
- **Unidad y periodicidad:** Magnitud de la variable (°C, mm), mensual.  
- **Fuente:** Estación SIATA vs. estación patrón.  
- **Semáforo:** Verde ≤5% error, Amarillo 6–10%, Rojo >10%.  
- **Responsable:** Calibración SIATA; revisar y recalibrar sensores.  
- **Limitación:** Depende de la calidad de la referencia.

---



## Pregunta 1.4. Para uno de los tres indicadores, escriba el pseudocódigo o la consulta (SQL o Python) que lo calcula sobre una tabla con columnas codigo, fecha_hora, valor y calidad, e indique cómo trataría las estaciones con intervalos de muestreo distintos.

El cálculo se adapta dinámicamente al intervalo de muestreo de cada estación, garantizando una medida justa de completitud sin asumir una frecuencia fija.

SELECT codigo,
       COUNT(*) * 100.0 /
       (DATEDIFF(MINUTE, MIN(fecha_hora), MAX(fecha_hora)) / AVG(intervalo_minutos)) AS completitud
FROM (
    SELECT codigo,
           fecha_hora,
           LAG(fecha_hora) OVER (PARTITION BY codigo ORDER BY fecha_hora) AS prev_fecha,
           DATEDIFF(MINUTE, LAG(fecha_hora) OVER (PARTITION BY codigo ORDER BY fecha_hora), fecha_hora) AS intervalo_minutos
    FROM datos
) t
GROUP BY codigo;



## Pregunta 1.5. Para cada grupo de estándares, indique en una frase qué práctica concreta aplicaría
SIATA.
Estándar Tema Aplicación en SIATA
DAMA-DMBOK 2 Gobierno y dimensiones
de calidad
ISO 8000 e ISO/IEC 25012
y 25024
Modelo y medición de
calidad del dato
ISO 19115 y 19157 Metadatos y calidad
geoespacial
OMM No. 8 y No. 100 Calidad de instrumentos y
de datos climatológicos
OMM No. 1131 y
metadatos WIGOS
Gestión de calidad y
metadatos de estaciones
Principios FAIR Acceso y reutilización de
datos



## Pregunta 1.5 – RESPUESTA Aplicación de estándares en SIATA

| Estándar | Tema | Aplicación en SIATA |
|-----------|------|--------------------|
| **DAMA‑DMBOK 2** | Gobierno y dimensiones de calidad | Implementar políticas de gestión de datos y roles claros para asegurar calidad y trazabilidad. |
| **ISO 8000 / ISO/IEC 25012 / 25024** | Modelo y medición de calidad del dato | Definir métricas de exactitud, completitud y consistencia para evaluar los datos de sensores. |
| **ISO 19115 / 19157** | Metadatos y calidad geoespacial | Documentar ubicación, resolución y calibración de cada estación en metadatos estandarizados. |
| **OMM No. 8 / No. 100** | Calidad de instrumentos y datos climatológicos | Aplicar protocolos de calibración y mantenimiento periódico de sensores meteorológicos. |
| **OMM No. 1131 / Metadatos WIGOS** | Gestión de calidad y metadatos de estaciones | Registrar metadatos técnicos y operativos de cada estación para garantizar trazabilidad. |
| **Principios FAIR** | Acceso y reutilización de datos | Publicar datos abiertos y bien documentados para facilitar su uso por investigadores y ciudadanía. |




## Pregunta 1.6. Describa una cadena de control de calidad de datos meteorológicos en al menos cuatro etapas (por ejemplo: formato y completitud, rango, coherencia temporal y persistencia, coherencia interna entre variables, coherencia espacial). Para cada etapa indique una prueba concreta, su umbral y qué bandera asignaría.

Cada etapa aplica una prueba concreta y asigna una bandera de calidad (verde, amarilla o roja) para facilitar la validación automática y la trazabilidad de los datos meteorológicos.

Una cadena de control de calidad puede tener cuatro etapas principales:

### 1. Formato y completitud
- **Prueba:** verificar que cada registro tenga `codigo`, `fecha_hora`, `valor` y `calidad` sin vacíos.  
- **Umbral:** ≥ 95 % de registros completos.  
- **Bandera:** Verde si cumple, Amarillo si hay faltantes moderados, Rojo si faltan más del 5 %.  

### 2. Rango físico
- **Prueba:** comprobar que los valores estén dentro de límites plausibles (ej. temperatura entre –10 °C y 45 °C).  
- **Umbral:** fuera del rango → alerta.  
- **Bandera:** Verde si está dentro del rango, Rojo si lo excede.  

### 3. Coherencia temporal y persistencia
- **Prueba:** detectar saltos bruscos o valores repetidos por largo tiempo.  
- **Umbral:** variación > 3 σ o más de 5 valores idénticos consecutivos.  
- **Bandera:** Amarillo si hay anomalías leves, Rojo si son persistentes.  

### 4. Coherencia interna entre variables
- **Prueba:** comparar variables relacionadas (ej. lluvia > 0 → humedad > 60 %).  
- **Umbral:** inconsistencias > 10 % de los registros.  
- **Bandera:** Verde si coherente, Amarillo si hay discrepancias menores, Rojo si son frecuentes.  



## Pregunta 1.7 (arquitectura en la nube e híbrida). SIATA recibe datos por minuto desde cientos de estaciones y sus alertas son críticas para la ciudad. Diseñe una arquitectura de datos para ingesta, validación, almacenamiento y publicación, sobre la nube de su preferencia (AWS,
Google Cloud o Azure) o sobre un modelo híbrido (infraestructura propia on-premise más nube).
Entregue un diagrama y una justificación que cubra:
(a) Conceptos base: modelos de servicio (IaaS, PaaS, SaaS) y de despliegue (pública, privada,
híbrida), y cuál elegiría para SIATA y por qué.
(b) Capas de almacenamiento (crudo, validado, producto) y formatos (por ejemplo Parquet,
particionamiento).
(c) Orquestación, cómputo y estrategia de reprocesamiento (idempotencia).
(d) Modelo híbrido: qué componentes mantendría on-premise y cuáles llevaría a la nube (ver
tabla), cómo sincroniza ambos entornos y cómo garantiza la continuidad operativa si se cae
el enlace o el proveedor.
(e) Repositorio de calidad en la nube: cómo dispondría el catálogo de datos, el diccionario de
variables y banderas, las reglas de validación versionadas, el linaje, los indicadores de calidad

## Pregunta 1.7 – Arquitectura en la nube e híbrida para SIATA

### (a) Conceptos base
SIATA necesita alta disponibilidad y control local sobre estaciones críticas.  
Elijo un **modelo híbrido** con servicios **IaaS y PaaS** en nube pública (Azure o AWS) y componentes **on‑premise** para adquisición y respaldo.  
Esto permite escalar procesamiento sin perder autonomía operativa.

---

### (b) Capas de almacenamiento
- **Crudo:** datos originales en formato CSV o JSON, almacenados localmente y replicados en la nube.  
- **Validado:** datos limpios y verificados, guardados en formato **Parquet** para eficiencia.  
- **Producto:** salidas analíticas y modelos, accesibles vía API o dashboard.  
Cada capa usa particionamiento por fecha y estación para optimizar consultas.

---

### (c) Orquestación y reprocesamiento
Uso de **Airflow o Prefect** para flujos idempotentes: si una tarea falla, se reejecuta sin duplicar datos.  
El cómputo se distribuye entre nodos locales y contenedores en la nube (Kubernetes).

---

### (d) Modelo híbrido – Componentes y justificación

| Componente | On‑premise | Nube | Justificación |
|-------------|-------------|------|---------------|
| Adquisición y buffer local | ✅ | | Requiere conexión directa con sensores y baja latencia. |
| Datos crudos históricos | ✅ | ✅ | Copia local para respaldo; nube para análisis masivo. |
| Validación y control de calidad | | ✅ | Escalabilidad y automatización con servicios PaaS. |
| Repositorio de calidad (catálogo, banderas, reglas) | | ✅ | Centralizado y accesible para todo el equipo. |
| Publicación para usuarios (API, datos abiertos) | | ✅ | Alta disponibilidad y acceso público. |
| Modelos y alertas de operación crítica | ✅ | ✅ | Procesamiento local para alertas inmediatas; nube para predicciones globales. |

Sincronización mediante colas de mensajes (Kafka o MQTT) y copias automáticas; continuidad garantizada con almacenamiento redundante y políticas RPO/RTO.

---

### (e) Repositorio de calidad en la nube
Incluye:
- Catálogo de datos y diccionario de variables.  
- Reglas de validación versionadas y trazabilidad (linaje).  
- Indicadores de calidad y banderas visuales.  
Todo gestionado con **Data Catalog + Data Quality Service** y control de acceso por rol.

---

### (f–i) Aspectos complementarios
- **Seguridad:** cifrado, autenticación y principio de mínimo privilegio.  
- **Observabilidad:** monitoreo de estaciones y alertas automáticas.  
- **Costos:** uso de almacenamiento escalable y políticas de retención.  
- **Infraestructura como código:** despliegue continuo con Terraform y GitHub Actions.


## Pregunta 1.8 (repositorios). Describa el flujo de trabajo con Git que implementaría para un equipo de cinco personas que mantiene código de validación de datos. Incluya estrategia de ramas, convención de commits, revisión de código, pruebas automáticas (CI), gestión de versiones del algoritmo de calidad, manejo de datos grandes y de secretos, y qué debe contener un buen README.

## Pregunta 1.8 – Flujo de trabajo con Git para equipo de validación de datos

### Estrategia general
El equipo usa **GitHub** con un flujo basado en **Git Flow**:  
- Rama principal `main` (versión estable).  
- Rama `develop` (integración continua).  
- Ramas de trabajo `feature/`, `fix/` y `release/` para tareas específicas.  
Cada desarrollador trabaja en su rama y crea *pull requests* hacia `develop`.

---

### Convención de commits
Mensajes breves y estructurados:

Ejemplo:  
- `feat: agregar validación de rango de temperatura`  
- `fix: corregir cálculo de completitud`  
- `docs: actualizar README`

---

### Revisión de código y CI
- Todo *pull request* requiere revisión por otro miembro.  
- Se ejecutan **pruebas automáticas (CI)** con GitHub Actions o Jenkins: validación de código, tests unitarios y verificación de estilo.  
- Si las pruebas fallan, el merge se bloquea.

---

### Gestión de versiones y datos
- Se usa **versionado semántico** (`v1.2.0`) para el algoritmo de calidad.  
- Los datos grandes se almacenan fuera del repositorio (por ejemplo, en S3 o Azure Blob) y se referencian mediante rutas o metadatos.  
- Los **secretos** (tokens, contraseñas) se manejan con `.env` y GitHub Secrets, nunca se suben al repositorio.

---

### Buen README
Debe incluir:
1. Descripción del proyecto y propósito.  
2. Estructura de carpetas y dependencias.  
3. Instrucciones de instalación y ejecución.  
4. Ejemplo de uso y flujo de validación.  
5. Créditos y licencia.


## Pregunta 1.9. Ingrese al repositorio o portal de datos de SIATA y revise la forma en que se descubren, describen, descargan y documentan los datos. Entregue un informe breve (máximo dos páginas) que responda:
(a) ¿Qué cambiaría? Elementos existentes que deben modificarse.
(b) ¿Qué falta? Capacidades, metadatos, documentación o controles ausentes.
6
Prueba técnica | Profesional en Ciencia de Datos SIATA • Calidad de Datos
(c) ¿Qué sobra? Redundancias, información confusa o procesos que no agregan valor.
(d) ¿Cómo lo mejoraría? Plan priorizado en una matriz de impacto frente a esfuerzo, con
horizonte de 30, 90 y 180 días.
Cada hallazgo debe incluir evidencia (captura, enlace o descripción reproducible) y el estándar o
principio que respalda la recomendación.


## Pregunta 1.9 – Auditoría del repositorio de datos de SIATA

### (a) ¿Qué cambiaría?
- Mejorar la **navegación y búsqueda** de datasets: incluir filtros por variable, estación y rango temporal.  
- Unificar formatos de descarga (CSV, JSON, API) para evitar duplicidad y confusión.  
- Estandarizar nombres de campos y unidades según ISO 19115 y WIGOS.

---

### (b) ¿Qué falta?
- **Metadatos completos**: descripción de variables, unidades, frecuencia de muestreo y método de validación.  
- **Indicadores de calidad** visibles (completitud, exactitud, consistencia).  
- **Documentación técnica** sobre el proceso de validación y control de calidad.  
- API con autenticación y ejemplos de consulta para desarrolladores.

---

### (c) ¿Qué sobra?
- Redundancia en archivos históricos y versiones sin trazabilidad.  
- Información dispersa entre secciones del portal sin jerarquía clara.  
- Descargas masivas sin control de actualización o aviso de cambios.

---

### (d) ¿Cómo lo mejoraría?
**Plan priorizado:**

| Horizonte | Acción | Impacto | Esfuerzo |
|------------|---------|----------|-----------|
| 30 días | Estandarizar metadatos y nombres de variables | Alto | Bajo |
| 90 días | Implementar API documentada y control de versiones | Alto | Medio |
| 180 días | Integrar dashboard de calidad y trazabilidad | Muy alto | Alto |

Cada mejora se respalda en principios **FAIR** (Findable, Accessible, Interoperable, Reusable) y estándares **ISO 19115** para metadatos.

---

### Evaluación desde distintos usuarios
- **Ciudadano:** necesita datos claros y visuales, con contexto y alertas comprensibles.  
- **Investigador:** requiere trazabilidad, metadatos detallados y control de versiones.  
- **Desarrollador:** busca APIs estables, documentación técnica y formatos consistentes.

---

### Conclusión
El repositorio de SIATA tiene una base sólida, pero puede fortalecerse con mayor estandarización, transparencia y herramientas que faciliten el acceso y la reutilización de datos por distintos tipos de usuarios.
