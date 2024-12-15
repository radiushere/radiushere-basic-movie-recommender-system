# Basic Movie Recommender System
This new project which I worked on is a Basic Movie Recommendation System using Correlation-Based Collaborative Filtering.

<br><br>

<h1><strong>Project Title:</strong> Movie Recommender System</h1>

<h2><strong>Project Description:</strong></h2>
<p>A data-driven movie recommendation system that suggests similar movies based on user rating patterns. The system uses correlation analysis to find movies with similar user rating behaviors.</p>

<br>
<h2>Elaborated Description:</h2>

<pre>
<strong>Key Technical Components:</strong>
1. <strong>Data Sources:</strong>
   - Ratings dataset (ratings.csv)
   - Movies dataset (movies.csv)

2. <strong>Key Technologies:</strong>
   - Python
   - Pandas (Data manipulation)
   - NumPy (Numerical computing)
   - Matplotlib/Seaborn (Data visualization)

<strong>Core Functionality:</strong>
- Allows users to input a movie name
- Finds movies with similar user rating patterns
- Filters recommendations by minimum number of ratings (>100)
- Ranks similar movies by correlation coefficient

<strong>Recommendation Method:</strong>
- Correlation-Based Collaborative Filtering
- Analyzes how similarly users rate the input movie and other movies
- Higher correlation suggests more similar rating patterns

<strong>Technical Implementation Details:</strong>
- Data Preprocessing
  - Convert ratings to numeric
  - Merge movies and ratings datasets
  - Handle missing values
- Create a user-movie rating matrix
- Calculate correlations between movies
- Filter and sort recommendations

<strong>Potential Improvements:</strong>
1. Add more sophisticated recommendation algorithms
2. Implement genre-based filtering
3. Create a user interface
4. Add more detailed recommendation explanations
5. Implement machine learning models like KNN or matrix factorization

<strong>Limitations:</strong>
- Relies on existing rating patterns
- May not work well for movies with few ratings
- Does not consider user preferences directly
- Correlation does not always mean similar enjoyment

<strong>Skills Demonstrated:</strong>
- Data preprocessing
- Pandas data manipulation
- Correlation analysis
- Basic recommendation system design
- Data-driven problem solving

<strong>Learning Objectives:</strong>
- Understand collaborative filtering
- Practice data analysis techniques
- Learn recommendation system basics
- Develop skills in Python data science libraries

<strong>Sample Use Case:</strong>
```
Enter a movie name (exactly as in the dataset): Star Wars: Episode IV - A New Hope (1977)
Top Correlated Movies to that movie (with more than 100 ratings):
- Raiders of the Lost Ark (1981)
- Return of the Jedi (1983)
- Empire Strikes Back, The (1980)
```
</pre>

<h3>The dataset used for this is given <a href="https://grouplens.org/datasets/movielens/latest/">here!</a></h3> 
