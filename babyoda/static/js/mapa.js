
let map;

function initMap() {

    var coordenadas = {lat: -15.80762866191734, lng: -48.09639308638717};

    map = new google.maps.Map(document.getElementById("map"), {
        center: coordenadas,
        zoom: 18,
        zoomControl: false,
        mapTypeControl: false,

    });
}