let map = L.map('map').setView([38.9792, -3.9276],6)

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Función para obtener el radio del círculo basado en el número de visitas
function getCircleRadius(total) {
    // Puedes ajustar estos valores según tus datos para que los círculos sean proporcionales al número de visitas
    return total / 1000; // Dividimos por 1000 para que el radio del círculo no sea demasiado grande
}

// Función para asignar color a cada círculo según el número de visitas
function getColor(total) {
    // Puedes ajustar estos rangos de color según tus datos
    return total > 1000000 ? '#800026' :
           total > 500000  ? '#BD0026' :
           total > 200000  ? '#E31A1C' :
           total > 100000  ? '#FC4E2A' :
           total > 50000   ? '#FD8D3C' :
           total > 10000   ? '#FEB24C' :
           total > 5000    ? '#FED976' :
           '#FFEDA0'; // Color por defecto
}

// Leer los datos de la base de datos SQLite y agregar círculos al mapa
fetch('http://127.0.0.1:5000/get_data') // URL del servidor Flask que proporciona los datos
    .then(response => response.json())
    .then(data => {
        data.forEach(entry => {
            let circle = L.circle([entry.latitud, entry.longitud], {
                color: 'black',
                weight: 1,
                fillColor: getColor(entry.total),
                fillOpacity: 0.5,
                radius: getCircleRadius(entry.total)
            }).addTo(map);
            
            circle.bindPopup(`<b>${entry.comunidad}</b><br>Total de visitas: ${entry.total}`);
        });
    })
    .catch(error => console.error('Error al cargar los datos:', error));

