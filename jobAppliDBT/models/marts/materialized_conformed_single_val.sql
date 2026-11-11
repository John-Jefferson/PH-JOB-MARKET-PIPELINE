{{ config(materialized='table') }}
SELECT
link,
work_type,
location,
seniority_level,
work_setup,
platform_source
FROM {{ ref('staging_conformed_single_val') }}
