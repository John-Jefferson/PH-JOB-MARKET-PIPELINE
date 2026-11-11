SELECT 
    link,
    unnest(skills::text[]) AS skill,
    'jobstreet' as platform_source
FROM {{ source('bronze', 'jobstreet_raw_table') }}

UNION ALL

SELECT 
    link,
    unnest(skills::text[]) AS skill,
    'foundit' as platform_source
FROM {{ source('bronze', 'foundit_raw_table') }}