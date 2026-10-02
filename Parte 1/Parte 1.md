Parte 1: Conceptual, estándares y arquitectura

Pregunta 1.1. Explique con sus propias palabras qué significa que un dato hidrometeorológico
tenga calidad. Su respuesta debe:
(a) Definir calidad como aptitud para el uso y vincularla al menos con tres dimensiones tomadas
de un marco formal (por ejemplo DAMA-DMBOK, ISO/IEC 25012 o ISO 8000).
(b) Distinguir entre calidad del dato, calidad del instrumento (exactitud, calibración, trazabilidad)
y calidad del proceso.
(c) Explicar por qué un dato físicamente plausible no es necesariamente un dato correcto


---> La calidad de un dato meteorológico indica que tan apto es ese dato para usarse, que tan confiable es y útil para la investigación que se esta realizando.
a) Con rspecta al marco DAMA-DMBOK la calidad del dato se evalua con respecto a exactitud (Accuracy), Completitud (Completeness), Consistencia (Consistency) y algunas dimensiones
complementarias como validez, actualidad y trazabilidad. 
b) La calidad el dato vs la calidad del instrumento se refiere a que el valor almacenado del dato es correcto, completo y coherente y refleja una realidad en este caso
física del entorno mientras que la calidad del instrumento depende de la exactitud y la calibración del sensor o equipo que esta hacendo la medida. Ej un equipo mal
calibrado puede tomar un dato erróneo. 

c) Un dato plausible no es necesariamente correcto porque el dato puede provenir de un sensor con errores, descalibrado, con error de digitación o transmisión entonces
ese dato aunque fue leído puede estar errado. Un ejemplo, el sensor mide 25°C pero esta descalibrado, el dato de 25°C es plausible (fisicamente correcto) pero la calidad
no está garantizada. Tomando el mismo ejemplo El sensor mide 25°C pero en realidad debería dar un valor de 29°C



Pregunta 1.2. Complete la siguiente tabla y justifique en un párrafo la diferencia entre cada nivel.
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






Pregunta 1.3. Proponga tres (3) indicadores de calidad aplicables a los datos que SIATA publica.
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




Pregunta 1.4. Para uno de los tres indicadores, escriba el pseudocódigo o la consulta (SQL o
Python) que lo calcula sobre una tabla con columnas codigo, fecha_hora, valor y calidad, e indique
cómo trataría las estaciones con intervalos de muestreo distintos.
4



Pregunta 1.5. Para cada grupo de estándares, indique en una frase qué práctica concreta aplicaría
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
Pregunta 1.6. Describa una cadena de control de calidad de datos meteorológicos en al menos
cuatro etapas (por ejemplo: formato y completitud, rango, coherencia temporal y persistencia,
coherencia interna entre variables, coherencia espacial). Para cada etapa indique una prueba
concreta, su umbral y qué bandera asignaría.



Pregunta 1.7 (arquitectura en la nube e híbrida). SIATA recibe datos por minuto desde
cientos de estaciones y sus alertas son críticas para la ciudad. Diseñe una arquitectura de datos
para ingesta, validación, almacenamiento y publicación, sobre la nube de su preferencia (AWS,
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
