SELECT

F.title AS FilmTitle,
CONCAT(A.first_name, ' ', A.last_name) AS ActorName

FROM film F

LEFT JOIN film_actor FA
ON F.film_id = FA.film_id

LEFT JOIN actor A
ON A.actor_id = FA.actor_id

LIMIT 100;