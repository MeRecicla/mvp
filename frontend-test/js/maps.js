let map;

$(document).ready(function() {
    createMap(-26.914273, -49.069485, 13);

    const address = "Rua Alberto Stein, 199 02, Blumenau";
    updateMapLocation(address);
});

function createMap(latitude, longitude, zoom) {
    map = L.map('mapid').setView([latitude, longitude], zoom);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
}

function updateMapLocation(address) {
    $.getJSON('http://nominatim.openstreetmap.org/search?format=json&limit=1&q=' + address, function(data) {
    
        console.log(data[0].lat + ", " + data[0].lon)

        const location = new L.LatLng(data[0].lat, data[0].lon);
        map.panTo(location);
    });
}

// TODO: set our own location marker on selected location
function createLocationMarker(lat, lon) {
    
}