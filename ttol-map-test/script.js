var LeafIcon = L.Icon.extend({
    options: {
        shadowUrl: '',
        iconSize:     [48, 49],
        shadowSize:   [0, 0],
        iconAnchor:   [17, 43],
        shadowAnchor: [17, 43],
        popupAnchor:  [0, -50]
    }
});

var userMarker   = new LeafIcon({iconUrl: 'gfx/marker-user.png', iconAnchor:[24,24]}),
    barMarker   = new LeafIcon({iconUrl: 'gfx/marker-bar.png'}),
    barArtifactMarker   = new LeafIcon({iconUrl: 'gfx/marker-bar-artifact.png'}),
    barGhostMarker   = new LeafIcon({iconUrl: 'gfx/marker-bar-ghost.png'}),
    restaurantMarker = new LeafIcon({iconUrl: 'gfx/marker-restaurant.png'}),
    restaurantArtifactMarker = new LeafIcon({iconUrl: 'gfx/marker-restaurant-artifact.png'}),
    restaurantGhostMarker = new LeafIcon({iconUrl: 'gfx/marker-restaurant-ghost.png'}),
    hotelMarker = new LeafIcon({iconUrl: 'gfx/marker-hotel.png'}),
    hotelArtifactMarker = new LeafIcon({iconUrl: 'gfx/marker-hotel-artifact.png'}),
    hotelGhostMarker = new LeafIcon({iconUrl: 'gfx/marker-hotel-ghost.png'}),
    clubMarker  = new LeafIcon({iconUrl: 'gfx/marker-club.png'}),
    clubArtifactMarker  = new LeafIcon({iconUrl: 'gfx/marker-club-artifact.png'}),
    clubGhostMarker  = new LeafIcon({iconUrl: 'gfx/marker-club-ghost.png'}),
    homeMarker  = new LeafIcon({iconUrl: 'gfx/marker-home.png'}),
    homeArtifactMarker  = new LeafIcon({iconUrl: 'gfx/marker-home-artifact.png'}),
    homeGhostMarker  = new LeafIcon({iconUrl: 'gfx/marker-home-ghost.png'}),
    theaterMarker  = new LeafIcon({iconUrl: 'gfx/marker-theater.png'}),
    theaterArtifactMarker  = new LeafIcon({iconUrl: 'gfx/marker-theater-artifact.png'}),
    theaterGhostMarker  = new LeafIcon({iconUrl: 'gfx/marker-theater-ghost.png'}),
    musicMarker  = new LeafIcon({iconUrl: 'gfx/marker-music.png'}),
    musicArtifactMarker  = new LeafIcon({iconUrl: 'gfx/marker-music-artifact.png'}),
    musicGhostMarker  = new LeafIcon({iconUrl: 'gfx/marker-music-ghost.png'}),
    gamblingMarker  = new LeafIcon({iconUrl: 'gfx/marker-gambling.png'}),
    gamblingArtifactMarker  = new LeafIcon({iconUrl: 'gfx/marker-gambling-artifact.png'}),
    gamblingGhostMarker  = new LeafIcon({iconUrl: 'gfx/marker-gambling-ghost.png'}),
    brothelMarker  = new LeafIcon({iconUrl: 'gfx/marker-brothel.png'}),
    brothelArtifactMarker  = new LeafIcon({iconUrl: 'gfx/marker-brothel-artifact.png'}),
    brothelGhostMarker  = new LeafIcon({iconUrl: 'gfx/marker-brothel-ghost.png'}),
    otherMarker  = new LeafIcon({iconUrl: 'gfx/marker-other.png'});
    otherArtifactMarker  = new LeafIcon({iconUrl: 'gfx/marker-other-artifact.png'});
    otherGhostMarker  = new LeafIcon({iconUrl: 'gfx/marker-other-ghost.png'});

function handlePopup(marker) {
  itemIdx = marker.itemIdx;
  marker.unbindPopup();
  marker.bindPopup(mapItems[itemIdx].cap).openPopup(); 
}

function success(position) {
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;
  getMap(latitude, longitude);
}
function error() {
  const latitude = 40.724648803426604;
  const longitude = -73.99681448936464;
  getMap(latitude, longitude);
}

function onMapClick(e) {
    window.console.log(e.latlng);
}

// initializing the live user marker in the middle of Washington Square
const liveUserMarker = L.marker([40.73073856023451, -73.99746894836427], {icon: userMarker});

var homeLat = 40.73073856023451;
var homeLng = -73.99746894836427;

function onLocationFound(e) {
  liveUserMarker.setLatLng(e.latlng);
  homeLat = e.latlng.lat;
  homeLng = e.latlng.lng;
  // window.console.log('locationfound:', e.latlng);
}

function getMap(latitude, longitude) {
  const map = L.map("map").setView([latitude, longitude], 2  );
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);
  
  map.locate({setView: false,
             maxZoom: 16,
             watch:true
           });

  liveUserMarker.addTo(map);

  for (i=0 ; i < mapItems.length ; i++){
    item = mapItems[i];
    lat = item.pos[0];
    lng = item.pos[1];
    status = item.status

    switch (item.type) {
      case 'Bar':
        icon = barMarker;
        if (status=='artifact') { icon = barArtifactMarker };
        if (status=='ghost') { icon = barGhostMarker };
        break;
      case 'Restaurant':
        icon = restaurantMarker;
        if (status=='artifact') { icon = restaurantArtifactMarker };
        if (status=='ghost') { icon = restaurantGhostMarker };
        break;
      case 'Hotel':
        icon = hotelMarker;
        if (status=='artifact') { icon = hotelArtifactMarker };
        if (status=='ghost') { icon = hotelGhostMarker };
        break;
      case 'Social club':
        icon = clubMarker;
        if (status=='artifact') { icon = clubArtifactMarker };
        if (status=='ghost') { icon = clubGhostMarker };
        break;
      case 'Theater':
        icon = theaterMarker;
        if (status=='artifact') { icon = theaterArtifactMarker };
        if (status=='ghost') { icon = theaterGhostMarker };
        break;
      case 'Music venue':
        icon = musicMarker;
        if (status=='artifact') { icon = musicArtifactMarker };
        if (status=='ghost') { icon = musicGhostMarker };
        break;
      case 'Gambling':
        icon = gamblingMarker;
        if (status=='artifact') { icon = gamblingArtifactMarker };
        if (status=='ghost') { icon = gamblingGhostMarker };
        break;
      case 'Brothel':
        icon = brothelMarker;
        if (status=='artifact') { icon = brothelArtifactMarker };
        if (status=='ghost') { icon = brothelGhostMarker };
        break;
      default:
        icon = otherMarker;
        if (status=='artifact') { icon = otherArtifactMarker };
        if (status=='ghost') { icon = otherGhostMarker };
    }

    marker = new L.Marker(new L.LatLng(lat, lng), {icon: icon}).addTo(map);
    marker.itemIdx = i;
    marker.on('click', function (e) {              
      handlePopup(this); 
    });

  }

  map.on('click', onMapClick);
  map.on('locationfound', onLocationFound);

  const centerButton = document.querySelector('#centerButton');

  centerButton.addEventListener('click', (event) => {
    window.console.log('center on ',homeLat,homeLng)
    map.flyTo(L.latLng(homeLat,homeLng));
  });

  // centerButton = document.getElementById('centerButton');
  // centerButton.on('click', function() { map.panTo(homeLat,homgLng) });

}

(() => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(success, error);
  } else {
    alert("Geolocation is not supported by this browser");
  }

})();

