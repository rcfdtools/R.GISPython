# -*- coding: UTF-8 -*-
# Name: CNEStationDictionary.py
# Description: Catálogo nacional de estaciones hidroclimatológicas del IDEAM - Colombia - Diccionario.
# Requirements: PyCharm 2021.3+, Python 3.10.0 (instalación independiente)
# Source: IDEAM Colombia - Clasificación de los climas (clima-text.pdf), http://atlas.ideam.gov.co/basefiles/clima-text.pdf
# Es: Español, En: English

stationCategoryDictEs = [
                    ['Estación Agrometeorológica','En esta estación se realizan observaciones meteorológicas y otras observaciones que ayudan a determinar las relaciones entre el clima, por una parte y la vida de las plantas y los animales por la otra. Incluye el mismo programa de observaciones de la estación climatológica principal, más registros de temperatura a varias profundidades (hasta un metro) y en la capa cercana al suelo (0, 10 y 20 cm sobre el suelo).'],
                    ['Estación Climatológica Ordinaria','Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros y humedad primordialmente. Poseen muy poco instrumental registrador. Algunas llevan instrumentos adicionales tales como tanque de evaporación, heliógrafo y anemómetro.'],
                    ['Estación Climatológica Principal','Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros, humedad, viento, radiación, brillo solar, evaporación, temperaturas extremas del tanque de evaporación, cantidad de nubes y fenómenos especiales. Gran parte de estos parámetros se obtienen de instrumentos registradores.'],
                    ['Estación Limnigráfica','Estación donde se mide el nivel de una corriente hídrica mediante un aparato registrador de nivel y que grafica una curva llamada limnigrama.'],
                    ['Estación Limnimétrica','Estación donde se mide el nivel de una corriente hídrica mediante un aparato (mira dividida en centímetros) que mide altura del agua, sin registrarla. Una persona toma el dato y lo registra en una libreta.'],
                    ['Estación Mareográfica','Estaciones para observación del estado del mar. Mide nivel, temperatura y salinidad de las aguas marinas.'],
                    ['Estación meteorológica especial','Estación instalada para realizar seguimiento a un fenómeno o un fin específico, por ejemplo, las heladas.'],
                    ['Estación Pluviográfica','Es aquella que registra en forma mecánica y continua la precipitación, en una gráfica que permite conocer la cantidad, duración, intensidad y periodo en que ha ocurrido la lluvia. Actualmente se utilizan los pluviógrafos de registro diario.'],
                    ['Estación Pluviométrica','Es una estación meteorológica dotada de un pluviómetro o recipiente que permite medir la cantidad de lluvia caída entre dos observaciones consecutivas.'],
                    ['Estación Radio Sonda','La estación de radiosonda tiene por finalidad la medición directa de parámetros atmosféricos tales como temperatura del aire, presión atmosférica, humedad relativa y dirección y velocidad del viento en las capas altas de la atmósfera (tropósfera y baja estratósfera), mediante el rastreo, por medios electrónicos, de la trayectoria de un globo meteorológico que asciende libremente y que lleva un dispositivo con los sensores que miden y transmiten la señal con los datos.'],
                    ['Estación Sinóptica Principal','En este tipo de estación se efectúan observaciones de los principales elementos meteorológicos en horas convenidas internacionalmente. Los datos se toman horariamente y corresponden a nubosidad, dirección y velocidad de los vientos, presión atmosférica, temperatura del aire, tipo y altura de las nubes, visibilidad, fenómenos especiales, características de humedad, precipitación, temperaturas extremas, capas significativas de nubes, recorrido del viento y secuencia de los fenómenos atmosféricos.'],
                    ['Estación Sinóptica Secundaria','Al igual que en la estación anterior, las observaciones se realizan a horas convenidas internacionalmente y los datos corresponden comúnmente a visibilidad, fenómenos especiales, tiempo atmosférico, nubosidad, estado del suelo, precipitación, temperatura del aire, humedad del aire, presión y viento.']]

stationStatusDictEs = [
                    ['Activa','Estación que se encuentra en operación y registra datos automáticos o tomados por un observador.'],
                    ['En mantenimiento','Estación que se encuentra en operación pero que temporalmente no registra datos automáticos o tomados por un observador por problemas en los equipos o como consecuencia de un siniestro.'],
                    ['Suspendida','Estación que se encuentra fuera de servicio de manera definitiva y no registra datos automáticos o tomados por un observador. Solo se puede consultar datos históricos en estas estaciones.']]

stationTechnologyDictEs = [
                    ['Convencional','Estación donde la toma del dato la efectúa un observador y la registra en una libreta para luego enviarla a los técnicos para que se capture y procesen estos datos.'],
                    ['Automática con telemetría','Estación que obtiene los datos de manera automática mediante sensores de diferente tipo y que tiene la capacidad de enviarlos de manera automática al centro de recepción por diferentes medios de transmisión (satelital, radiofrecuencia, GPRS, etc.)'],
                    ['Automática sin telemetría','Estación que obtiene los datos de manera automática mediante sensores de diferente tipo y que tiene la capacidad de almacenarlos en un dispositivo dentro de la misma estación. No puede enviar los datos de manera automática. Los datos debes ser obtenidos por una persona que se conecta al sitio donde la estación almacena los datos.']]