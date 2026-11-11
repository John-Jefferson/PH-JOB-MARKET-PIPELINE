{{ config(materialized='table') }}

WITH normalized AS (
    SELECT
        split_part(split_part(trim(link), '?', 1), '#', 1) AS link,
        lower(trim(platform_source)) AS platform_source,
        coalesce(nullif(trim(work_type), ''), 'unknown') AS work_type,
        coalesce(nullif(trim(location), ''), 'unknown') AS location,
        lower(
            coalesce(
                nullif(
                    trim(regexp_replace(cast(seniority_level AS text), '[{}"]', '', 'g')),
                    ''
                ),
                'unknown'
            )
        ) AS seniority_level,
        lower(
            coalesce(
                nullif(
                    trim(regexp_replace(cast(work_setup AS text), '[{}"]', '', 'g')),
                    ''
                ),
                'unknown'
            )
        ) AS work_setup
    FROM {{ ref('staging_conformed_single_val') }}
    WHERE link IS NOT NULL
      AND trim(link) <> ''
      AND split_part(split_part(trim(link), '?', 1), '#', 1) <> ''
),
ranked AS (
    SELECT
        *,
        row_number() OVER (
            PARTITION BY platform_source, link
            ORDER BY work_type, location, seniority_level, work_setup
        ) AS posting_rank
    FROM normalized
)

SELECT
    md5(platform_source || '|' || link) AS job_posting_key,
    link,
    platform_source,
    work_type,
    location,
    seniority_level,
    work_setup
FROM ranked
WHERE posting_rank = 1
