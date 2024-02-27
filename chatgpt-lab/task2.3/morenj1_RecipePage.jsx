import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

/**
 * A React component that displays detailed information about a recipe.
 * It fetches the recipe data from an external API using the recipe ID from the URL parameters.
 */
function RecipePage() {
  // Extracting the recipe ID from URL parameters
  let { id } = useParams();

  // State management for recipe data, loading status, and error handling
  const [recipe, setRecipe] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetches recipe data from the API
  useEffect(() => {
    const fetchRecipe = async () => {
      setIsLoading(true);
      setError(null);
      try {
        const response = await fetch(
          `https://api.spoonacular.com/recipes/${id}/information?apiKey=${process.env.REACT_APP_API_KEY}`
        );
        if (!response.ok) throw new Error('Failed to fetch recipe data.');
        const data = await response.json();
        setRecipe(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setIsLoading(false);
      }
    };
    fetchRecipe();
  }, [id]); // Only re-run the effect if the recipe ID changes

  // Conditional rendering based on loading state and error
  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  // Rendering the recipe data
  return (
    <div>
      <h1>{recipe.title}</h1>
      <img src={recipe.image} alt={recipe.title} />
      <div className="recipe-info">
        <div><span>Servings:</span> {recipe.servings}</div>
        <div><span>Cook Time:</span> {recipe.cookingMinutes} minutes</div>
        <div><span>Ready In:</span> {recipe.readyInMinutes} minutes</div>
      </div>
      <h2>Ingredients</h2>
      <ul>
        {recipe.extendedIngredients && recipe.extendedIngredients.map(ingredient => (
          <li key={ingredient.id}>{ingredient.original}</li>
        ))}
      </ul>
      <h2>Instructions</h2>
      <div dangerouslySetInnerHTML={{ __html: recipe.instructions }} />
    </div>
  );
}

export default RecipePage;
