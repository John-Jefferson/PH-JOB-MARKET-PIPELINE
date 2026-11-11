{{ config(materialized="table") }}
SELECT 
    link,
    skill,
    platform_source
FROM {{ ref('staging_skills') }}
