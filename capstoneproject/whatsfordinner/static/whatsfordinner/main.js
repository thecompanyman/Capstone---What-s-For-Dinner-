let app = new Vue ({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        available_vegetables: [],
        available_seasonings: [],
        selected_ingredients: [],
        recipes: [],
        submitted_ingredients: '',
    },
    methods: {
        availableVegetables: async function(){
            let response = await axios({
                method: 'get',
                url: 'available_vegetables/',
            })
            this.available_vegetables = response.data
        },
        availableSeasonings: async function(){
            let response = await axios({
                method: 'get',
                url: 'available_seasonings/',
            })
            // console.log(response.data)
            this.available_seasonings = response.data
        },
        displaySelected: function(name){
            let index = this.selected_ingredients.findIndex(el => el === name) //arrow function searching over the array, each element is the a, returns true when a = name
            if (index >= 0){
                this.selected_ingredients.splice(index, 1)
            }
            else {
                this.selected_ingredients.push(name)
            };
            // console.log(this.selected_ingredients)
        },
        // getRecipes: async function(){
        //     let response = await axios({
        //         method: 'get',
        //         url: 'get_recipes/',
        //     })
        //     console.log(response.data)
        //     this.recipes = response.data
        // },
        findRecipes: async function(){
            const csrftoken = Cookies.get('csrftoken')
            response = await axios({
                method: 'post',
                url: 'find_recipes/',
                headers: {
                    'X-CSRFToken': csrftoken
                },
                data: {
                    submittedIngredients: this.selected_ingredients
                }
            })
            console.log(response.data)
            // if(response.data.message === 'ok'){
            //     // this.getRecipes()
            // }
            // this.displaySelected()
            this.recipes = response.data
        }
    },
    created: function (){
        this.availableVegetables()
        this.availableSeasonings()
    }
})