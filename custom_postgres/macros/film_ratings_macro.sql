{% macro generate_film_ratings() %}

WITH films_with_ratings AS (
    SELECT 
        film_id,
        title,
        release_date,
        price,
        rating,
        user_rating,
        CASE
            WHEN user_rating >= 4.5 THEN 'Excellent'
            WHEN user_rating >= 4 THEN 'Good'
            WHEN user_rating >= 3.5 THEN 'Average'
            WHEN user_rating >= 3 THEN 'Poor'
            ELSE 'Terrible'
        END AS user_rating_category
    FROM {{ ref('films') }}
),

films_with_actors AS (
    SELECT 
        f.film_id,
        f.title,
        STRING_AGG(a.actor_name, ', ') AS actors
    FROM {{ ref('films') }} f
    JOIN {{ ref('film_actors') }} fa ON f.film_id = fa.film_id
    JOIN {{ ref('actors') }} a ON fa.actor_id = a.actor_id
    GROUP BY f.film_id, f.title
)

SELECT
    fwf.*,
    fwa.actors
FROM films_with_ratings fwf
JOIN films_with_actors fwa ON fwf.film_id = fwa.film_id

{% endmacro %}