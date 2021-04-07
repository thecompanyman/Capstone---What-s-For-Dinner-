let app = new Vue ({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        available_vegetables: [],
        available_seasonings: [],
        selected_ingredients: [],
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
            let index = this.selected_ingredients.findIndex(a => a === name)
            if (index >= 0){
                this.selected_ingredients.splice(index, 1)
            }
            else {
                this.selected_ingredients.push(name)
            };
            // if(this.selected_ingredients.includes(name)){
            //     this.selected_ingredients.delete(name)
            // }
            // else(this.selected_ingredients.push(name));
            // // if this.selected_ingredients.includes(name) remove name else add it
            console.log(this.selected_ingredients)
        },
        selectVegetables: async function(){
            const csrftoken = Cookies.get('csrftoken')
            response = await axios({
                method: 'post',
                url: 'select_vegetables/',
                headers: {
                    'X-CSRFToken': csrftoken
                },
                data: {
                }
            })
            console.log(response.data)
            // if(response.data.message === 'ok'){
            //     this.availableVegetables()
            // }
        }
    },
    created: function (){
        this.availableVegetables()
        this.availableSeasonings()
    }
})