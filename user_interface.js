document.getElementById('recipeForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const ingredients = document.getElementById('ingredients').value;
    const diet = document.getElementById('diet').value;

    // Here you would typically make an AJAX request to your server
    // For demonstration, we'll just display the input values
    //document.getElementById('recipeOutput').innerHTML = `Ingredients: ${ingredients}<br>Diet: ${diet}`;

    fetch('https://99c9-34-74-110-245.ngrok-free.app/generate-recipe', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title,
            ingredients,
            diet
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);  // Log the response to see what you are actually receiving
            document.getElementById('recipeTitle').querySelector('span').textContent = data.recipe.title;
            document.getElementById('recipeIngredients').querySelector('span').textContent = data.recipe.ingredients;
            document.getElementById('recipeDirections').querySelector('span').textContent = data.recipe.directions;
        })
        
        
        .catch(error => console.error('Error:', error));

});
