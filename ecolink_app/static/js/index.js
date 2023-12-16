const info_container = document.querySelector("#details")
const state_name = info_container.querySelector("#state_name")
const details = document.querySelector("#details")
const state_name_2 = document.querySelector("#state_name_2")
const start_campaign_button = document.querySelector("#start_campaign")

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('path').forEach((path) => {
        path.addEventListener('mouseover', () => {
            state_name.innerText = path.dataset.name
        })
    })

    document.querySelectorAll('path').forEach((path) => {
        path.addEventListener('click', () => {
            state_name_2.innerText = path.dataset.name
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

function register_view(){
    
}