{{ config(materialized='table') }}
SELECT 
    link,
    title,
    platform_source
FROM {{ ref('staging_title') }}
