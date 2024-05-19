document.getElementById('recipeForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const ingredients = document.getElementById('ingredients').value;
    const diet = document.getElementById('diet').value;

    // Here you would typically make an AJAX request to your server
    // For demonstration, we'll just display the input values
    //document.getElementById('recipeOutput').innerHTML = `Ingredients: ${ingredients}<br>Diet: ${diet}`;

    fetch('https://1395-34-105-9-109.ngrok-free.app/generate-recipe', {
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
            document.getElementById('recipeOutput').innerHTML = `Recommended Recipe: ${data.recipe}`;
        })
        .catch(error => console.error('Error:', error));

});
