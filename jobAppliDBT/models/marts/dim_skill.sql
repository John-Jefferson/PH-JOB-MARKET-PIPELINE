{{ config(materialized='table') }}

WITH normalized AS (
    SELECT
        lower(trim(skill)) AS skill_key_value,
        min(trim(skill)) AS skill
    FROM {{ ref('staging_skills') }}
    WHERE skill IS NOT NULL
      AND trim(skill) <> ''
      AND lower(trim(skill)) <> 'none'
    GROUP BY lower(trim(skill))
)

SELECT
    md5(skill_key_value) AS skill_key,
    skill
FROM normalized
