import matplotlib.pyplot as plt
import numpy as np
 
# ejex = [25,12,75,43,12]
ejex = ["Octubre","Noviembre", "Diciembre"]
ejey = [57.7,70.2,85]

fig, ax = plt.subplots()
plt.plot(ejex, ejey)
plt.xlabel("Año 2024")
plt.ylabel("Porcentaje inflación")

plt.title("El Observatorio Venezolano de Finanzas (OVF):\n Venezuela registró inflación de 85'%' en 2024")
plt.xticks(np.arange(0,3))
plt.yticks(np.arange(0, 105, 5))
# plt.grid(visible="Active")
plt.show()

#comparacionrubros que conforman el Índice Nacional de Precios al Consumidor
porcentaje_alimento = 16.4  
porcentaje_vestido = 15.5
porcentaje_hogar = 17.2
porcentaje_comunicacion = 20
porcentaje_restaurant_hotel = 26.5
total = 100

plt.bar(0.2, porcentaje_alimento, width=1/10, label="Alimentos")
plt.bar(0.3, porcentaje_vestido, width=1/10,label="Vestido y calzado")
plt.bar(0.4, porcentaje_hogar, width=1/10,label="Equipamiento del hogar")
plt.bar(0.5, porcentaje_comunicacion, width=1/10,label="Comunicaciones")
plt.bar(0.6, porcentaje_restaurant_hotel, width=1/10,label="Restaurantes y hoteles")
plt.xlabel("Rubros")
plt.ylabel("Porcentaje")
plt.title("Todos los rubros que conforman el Índice Nacional de Precios al Consumidor\n experimentaron aumentos significativos entre ellos")
plt.xticks(np.arange(0.8,0.8))
plt.yticks(np.arange(0, total+10, 10))
# plt.annotate(str(porcentaje_alimento)+'%', xy=(0.18,50), xytext=(0.18,50))

plt.grid(visible="Active")
plt.legend()
plt.show()

#Inflación anual por región.
porcentaje_anz = 96  
porcentaje_nvs = 86
porcentaje_zla = 84
porcentaje_csc = 80
total = 100

plt.bar(0.2, porcentaje_anz, width=1/10, label="Anzoátegui")
plt.bar(0.3, porcentaje_nvs, width=1/10,label="Nueva Esparta")
plt.bar(0.4, porcentaje_zla, width=1/10,label="Zulia")
plt.bar(0.5, porcentaje_csc, width=1/10,label="Área Metropolitana de Caracas")
plt.xlabel("Regiones")
plt.ylabel("Porcentaje")
plt.title("También mencionó que en el ámbito regional,\n la mayor tasa de inflación anual se registró por Estado")
plt.xticks(np.arange(0.8,0.8))
plt.yticks(np.arange(0, total+10, 10))
# plt.annotate(str(porcentaje_alimento)+'%', xy=(0.18,50), xytext=(0.18,50))

plt.grid(visible="Active")
plt.legend()
plt.show()