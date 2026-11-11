{{ config(materialized='table') }}
SELECT
    link,
    qualification,
    platform_source
FROM {{ ref('staging_qualifications') }}
