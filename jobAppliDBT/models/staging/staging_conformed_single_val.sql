SELECT
link,
work_type,
location,
seniority_level,
work_setup,
'jobstreet' as platform_source
FROM {{ source('bronze', 'jobstreet_raw_table') }}

UNION ALL

SELECT
link,
work_type,
location,
seniority_level,
work_setup,
'foundit' as platform_source
FROM {{ source('bronze', 'foundit_raw_table') }}