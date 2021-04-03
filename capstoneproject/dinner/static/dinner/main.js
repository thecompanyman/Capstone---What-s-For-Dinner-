// refer to todo list, sending data from one spot to another

// event listener for click, grab the items selected in veggies list

// 



// const container = document.querySelector("#list-container")
// const saveButton = container.querySelector(".save-ingredients")
// const selectedIngredients = container.querySelector(".selected-ingredients")
// const savedIngredients = container.querySelector("#saved-ingredients")

// saveButton.addEventListener('click', function() {
//     addSelectedIngredients();
// }) 

// function addSelectedIngredients() {
//     let addIngredient = document.createElement('li')
//     addIngredient.innerText = selectedIngredients.value
//     savedIngredients.appendChild(addIngredient)
// }


const container = document.querySelector("#list-container")
const saveVeggies = container.querySelector("#save-veggies")
const selectedVeggies = container.querySelector("#selected-veggies")
const saveSeasonings = container.querySelector("#save-seasonings")
const selectedSeasonings = container.querySelector("#selected-seasonings")
const savedIngredients = container.querySelector("#saved-ingredients")

saveVeggies.addEventListener('click', function() {
    addSelectedVeggies();
}) 

saveSeasonings.addEventListener('click', function() {
    addSelectedSeasonings();
}) 

function addSelectedVeggies() {
    let addVeggie = document.createElement('li')
    // let saveAllVeggies = Array.from(saveVeggies.options)
    addVeggie.innerText = selectedVeggies.value
    savedIngredients.appendChild(addVeggie)
}

function addSelectedSeasonings() {
    let addSeasoning = document.createElement('li')
    addSeasoning.innerText = selectedSeasonings.value
    savedIngredients.appendChild(addSeasoning)
}


// you can axios here to have the recipe list update as user selects ingredients

// use mouse down or click on ingredients to select ingredients and add to ingredient list, won't need submit button