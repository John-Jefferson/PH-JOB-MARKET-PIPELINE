{{ config(materialized='table') }}

WITH normalized AS (
    SELECT
        lower(trim(title)) AS title_key_value,
        min(trim(title)) AS title
    FROM {{ ref('staging_title') }}
    WHERE title IS NOT NULL
      AND trim(title) <> ''
      AND lower(trim(title)) <> 'none'
    GROUP BY lower(trim(title))
)

SELECT
    md5(title_key_value) AS title_key,
    title
FROM normalized
