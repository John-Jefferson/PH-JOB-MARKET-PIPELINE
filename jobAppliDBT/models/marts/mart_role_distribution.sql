{{ config(materialized='table') }}

SELECT
    titles.title_key,
    titles.title,
    jobs.platform_source,
    count(DISTINCT bridge.job_posting_key) AS job_posting_count
FROM {{ ref('bridge_job_title') }} AS bridge
INNER JOIN {{ ref('dim_title') }} AS titles
    ON bridge.title_key = titles.title_key
INNER JOIN {{ ref('fct_job_postings') }} AS jobs
    ON bridge.job_posting_key = jobs.job_posting_key
GROUP BY
    titles.title_key,
    titles.title,
    jobs.platform_source
