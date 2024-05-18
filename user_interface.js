document.getElementById('recipeForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const ingredients = document.getElementById('ingredients').value;
    const diet = document.getElementById('diet').value;

    // Here you would typically make an AJAX request to your server
    // For demonstration, we'll just display the input values
    document.getElementById('recipeOutput').innerHTML = `Ingredients: ${ingredients}<br>Diet: ${diet}`;
});
