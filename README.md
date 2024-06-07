# AI-Project

## Problem Statement: 
In our daily life, we often want to make use of the ingredients we have at hand or sometimes encounter dishes on social media or at restaurants we wish to replicate at home. Identifying corresponding recipes online based solely on brief descriptions can be difficult and time-consuming.
## Aim:
We aim to develop a tool that uses a textual description to provide detailed recipes, including ingredients and cooking instructions. This tool will employ natural language processing to interactively refine recipe suggestions based on user-provided ingredients and preferences.
## Usage:

## prerequisite
In requirement.txt
## hyperparameters
learning_rate = 1e-4
num_epochs = 4
accumulation_steps = 4
batch_size = 8

## experiment results
For three model, we first use BELU score to evaluate the reslut. Below is experiment result
|Model|Bleu score|
|---|---|
|vegetarian| 0.3758|
|Lacto-ovo| 0.3978|
|Non-vegetarian| 0.4192|

Also consider the ingredient coverage objectives, measuring how well the generated recipes include the user-provided ingredients. The generated recipes consistently include all user-provided ingredients, demonstrating high ingredient coverage and effectively fulfilling the primary requirement of using specific ingredients. 
Below is some Analysis
### Recipe Detail and Completeness: 
The generated recipes lack detail and often include very basic instructions that might not be sufficient for users, especially those who are not experienced cooks. For example, the direction "mix all ingredients together" is too vague and does not provide adequate cooking instructions. 
### Inaccurate Ingredient Measurements: 
The ingredient measurements are overly simplistic and unrealistic (e.g., "1 c. chocolate, flour, milk, eggs"). This indicates that the model does not appropriately handle ingredient quantities and combinations. 
### Low BLEU Scores: 
The BLEU scores are relatively low, indicating that the generated recipes do not closely match the reference recipes. This suggests that while the model can include the specified ingredients, it struggles to produce recipes that are similar to those written by humans. 
### Repetitive and Generic Titles: 
The titles of the recipes are generic and repetitive (e.g., "chocolate dish", "flour dish"), which does not provide useful information about the dish. This indicates a lack of creativity and contextual understanding in naming the dishes. 
### Take-Away Messages 
#### Strengths: 
The model successfully includes user-specified ingredients in the generated recipes, meeting a key requirement. It follows a basic recipe structure, making the output somewhat usable. 
#### Weaknesses: 
The generated recipes are overly simplistic and lack the detail needed for practical cooking. Ingredient measurements and combinations are unrealistic, which could lead to poor cooking outcomes. Low BLEU scores reflect a significant deviation from reference recipes, indicating room for improvement in generating high-quality, realistic recipes. 
#### Surprises: 
The consistency in including user-specified ingredients is a positive surprise, showing the model's effectiveness in ingredient coverage. The lack of detailed instructions and accurate measurements is surprising, given the importance of these aspects in recipe generation. 
Potential Errors and Improvements 
### Tokenization and Quantity Handling: 
Errors may arise from the way ingredients and quantities are tokenized and handled by the model. Improving the model's ability to handle and generate realistic ingredient quantities and combinations would enhance recipe quality. 
### Training Data Quality: 
The model's training data might not be comprehensive enough to cover detailed and varied cooking instructions. Using a larger and more diverse dataset with detailed recipes could improve the  model's performance. 
### Enhanced Model Architecture: 
Consider using a more advanced model architecture or fine-tuning techniques to improve the quality of generated recipes. Incorporating additional context and knowledge about cooking processes could lead to more realistic and detailed recipes.
