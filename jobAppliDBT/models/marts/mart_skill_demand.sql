{{ config(materialized='table') }}

SELECT
    skills.skill_key,
    skills.skill,
    jobs.platform_source,
    count(DISTINCT bridge.job_posting_key) AS job_posting_count
FROM {{ ref('bridge_job_skill') }} AS bridge
INNER JOIN {{ ref('dim_skill') }} AS skills
    ON bridge.skill_key = skills.skill_key
INNER JOIN {{ ref('fct_job_postings') }} AS jobs
    ON bridge.job_posting_key = jobs.job_posting_key
GROUP BY
    skills.skill_key,
    skills.skill,
    jobs.platform_source
