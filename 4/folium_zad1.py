import folium

mapa = folium.Map(location=[52.15, 21.00], zoom_start=13)
folium.Marker(location=[52.15, 21.00], popup='Warszawa').add_to(mapa)
mapa.save('mapa.html')
