let map;
let markersLayer;
const backendURL = 'http://localhost:5000/companies/';
const nominatimURL = 'http://nominatim.openstreetmap.org/search?format=json&limit=1&q=';

$(document).ready(function() {
    createMap(-26.914273, -49.069485, 11);

    setOnClickSearchButtonEvent();
});

function createMap(latitude, longitude, zoom) {
    map = L.map('mapid').setView([latitude, longitude], zoom);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    markersLayer = L.layerGroup().addTo(map);
}

function setOnClickSearchButtonEvent() {
    $('#search_button').click(function(){
        const searchedWord = $('#search_field').val();
        $.ajax({
            url: backendURL + searchedWord,
            type: "get",
            beforeSend: function() {
                clearTable();
                clearMapMarkers();
            },
            success: function(points) {
                if(points.length) {
                    populateTableWithPoints(points);
                    populateMapWithPoints(points);
                } else {
                    populateTableWithNotFound();
                }
            },
            error: function() {
                populateTableWithNotFound();
            }
        });
    });
}

function populateTableWithPoints(points) {
    points.forEach(point => {
        const name = point.nome;
        const address = point.endereco;

        $('#table tbody').append(`<tr><td>${name}</td><td>${address}</td></tr>`);
    });

    setOnClickTableEvent();
}

function setOnClickTableEvent() {
    $("#table tr").click(function(){
        $(this).addClass('active').siblings().removeClass('active');    
        const address = $(this).children('td').slice(1, 2).html() + ", Blumenau";
        updateMapLocation(address);
     });
}

function populateTableWithNotFound() {
    const notFoundMessage = "Foi mal fera, não achei nenhuma empresa que coleta isso aí que tu quer";
    $('#table tbody').append(`<tr><td colspan='2' align='center'>${notFoundMessage}</td></tr>`);
}

function clearTable() {
    $('#table tbody').empty();
}

function updateMapLocation(address) {
    $.getJSON(nominatimURL + address, function(data) {
        const zoom = 15;
        const location = [data[0].lat, data[0].lon];
        map.setView(location, zoom);
    });
}

function createLocationMarker(lat, lon, info) {
    const pinIcon = L.icon({
        iconUrl: './img/favicon-32x32.png',
        iconSize:     [32, 42],
        iconAnchor:   [22, 94],
        popupAnchor:  [-3, -76]
    });

    L.marker([lat, lon], {icon: pinIcon}).addTo(markersLayer).bindPopup(info);
}

function populateMapWithPoints(points) {
    points.forEach(point => {
        const url = nominatimURL + point.endereco + ", Blumenau";
        $.getJSON(url, function(location) {
            if(location.length) {
                console.log(point.nome + ": " + location[0].lat + ", " + location[0].lon);
                createLocationMarker(location[0].lat, location[0].lon, point.nome + "<br />" + point.endereco + " - " + point.bairro);
            }
        });
    });
}

function clearMapMarkers() {
    markersLayer.clearLayers();
}