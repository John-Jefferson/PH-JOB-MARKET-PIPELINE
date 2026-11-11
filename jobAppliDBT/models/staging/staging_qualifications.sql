SELECT
    link,
    unnest(qualifications::text[]) AS qualification,
    'jobstreet' as platform_source
FROM {{ source('bronze', 'jobstreet_raw_table') }}

UNION ALL

SELECT 
    link,
    unnest(qualifications::text[]) AS qualification,
    'foundit' as platform_source
FROM {{ source('bronze', 'foundit_raw_table') }}