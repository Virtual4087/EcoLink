const info_container = document.querySelector("#details")
const city_name = info_container.querySelector("#city_name")
const details = document.querySelector("#details")
const city_name_2 = document.querySelector("#city_name_2")
const start_campaign_button = document.querySelector("#start_campaign")
const login = document.querySelector("#login_view")
const register = document.querySelector("#register_view")

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('path').forEach((path) => {
        path.addEventListener('mouseover', () => {
            city_name.innerText = path.dataset.name
        })
    })

    document.querySelectorAll('path').forEach((path) => {
        path.addEventListener('click', () => {
            city_name_2.innerText = path.dataset.name
        })
    })
    maptilersdk.config.apiKey = '9cfqlXmXBJySAgiNxGqW';
    
    const map = new maptilersdk.Map({
      container: 'map',
      style: "efba20d3-8d89-4a7d-828a-1956aded28fa",
      center: [85.25, 27.7], 
      zoom: 12
    });

    map.on('style.load', function () {
        fetch('/static/json/kirtipurPoly.json')
            .then(response => response.json())
            .then(data => {
                map.addLayer({
                    'id': 'kirtipurPoly',
                    'type': 'fill',
                    'source': {
                        'type': 'geojson',
                        'data': data
                    },
                    'layout': {},
                    'paint': {
                        'fill-color': '#00ff00',
                        'fill-opacity': 0.25
                    }
                });
            })
    .catch(error => console.error('Error loading GeoJSON:', error));
        });

    map.on('mouseover', 'kirtipurPoly', function () {
        map.getCanvas().style.cursor = 'pointer';
    });
        
    map.on('click', 'kirtipurPoly', function(){
        console.log("Kiritpur")
    });
    
    map.on('mouseleave', 'kirtipurPoly', function () {
        map.getCanvas().style.cursor = '';
      });

    map.on('style.load', function () {
        fetch('/static/json/lalitpurPoly.json')
            .then(response => response.json())
            .then(data => {
                map.addLayer({
                    'id': 'lalitpurPoly',
                    'type': 'fill',
                    'source': {
                        'type': 'geojson',
                        'data': data
                    },
                    'layout': {},
                    'paint': {
                        'fill-color': '#fff000',
                        'fill-opacity': 0.25
                    }
                });
            })
    .catch(error => console.error('Error loading GeoJSON:', error));
    });

    map.on('mouseover', 'lalitpurPoly', function () {
        map.getCanvas().style.cursor = 'pointer';
    });
        
    map.on('click', 'lalitpurPoly', function(){
        console.log("Lalitpur")
    });
    
    map.on('mouseleave', 'lalitpurPoly', function () {
        map.getCanvas().style.cursor = '';
    });


    map.on('style.load', function () {
        fetch('/static/json/kathmanduPoly.json')
        .then(response => response.json())
        .then(data => {
            map.addLayer({
                'id': 'kathmanduPoly',
                'type': 'fill',
                'source': {
                    'type': 'geojson',
                    'data': data
                },
                'layout': {},
                'paint': {
                    'fill-color': '#f00f00',
                    'fill-opacity': 0.25
                }
            });
        })
        .catch(error => console.error('Error loading GeoJSON:', error));
    });

    map.on('mouseover', 'kathmanduPoly', function () {
        map.getCanvas().style.cursor = 'pointer';
    });
        
    map.on('click', 'kathmanduPoly', function(){
        console.log("Kathmandu")
    });

    map.on('mouseleave', 'kathmanduPoly', function () {
        map.getCanvas().style.cursor = '';
    });

})

function start_campaign(){
    start_campaign_button.classList.remove("hidden")
}

function submit_campaign(event){
    start_campaign_button.classList.add("hidden")
    event.preventDefault();
}

function cancel_create_campaign(){
    start_campaign_button.classList.add("hidden")
}

function login_view(){
    register.classList.add("hidden")
    login.classList.remove("hidden")
}
function register_view(){
    login.classList.add("hidden")
    register.classList.remove("hidden")
}