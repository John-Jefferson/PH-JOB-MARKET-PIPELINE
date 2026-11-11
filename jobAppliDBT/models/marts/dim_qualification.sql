{{ config(materialized='table') }}

WITH normalized AS (
    SELECT
        lower(trim(qualification)) AS qualification_key_value,
        min(trim(qualification)) AS qualification
    FROM {{ ref('staging_qualifications') }}
    WHERE qualification IS NOT NULL
      AND trim(qualification) <> ''
      AND lower(trim(qualification)) <> 'none'
    GROUP BY lower(trim(qualification))
)

SELECT
    md5(qualification_key_value) AS qualification_key,
    qualification
FROM normalized
