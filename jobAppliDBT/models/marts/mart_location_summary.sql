{{ config(materialized='table') }}

SELECT
    location,
    platform_source,
    count(DISTINCT job_posting_key) AS job_posting_count,
    count(DISTINCT work_type) FILTER (WHERE work_type <> 'unknown') AS work_type_count,
    count(DISTINCT seniority_level) FILTER (WHERE seniority_level <> 'unknown') AS seniority_level_count,
    count(DISTINCT work_setup) FILTER (WHERE work_setup <> 'unknown') AS work_setup_count
FROM {{ ref('fct_job_postings') }}
GROUP BY
    location,
    platform_source
