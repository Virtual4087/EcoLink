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