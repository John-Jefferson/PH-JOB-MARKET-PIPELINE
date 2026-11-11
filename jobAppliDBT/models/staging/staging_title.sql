SELECT 
    link,
    unnest(title::text[]) AS title,
    'jobstreet' as platform_source
FROM {{ source('bronze', 'jobstreet_raw_table') }}

UNION ALL

SELECT
    link,
    unnest(title::text[]) AS title,
    'foundit' as platform_source
FROM {{ source('bronze', 'foundit_raw_table') }}