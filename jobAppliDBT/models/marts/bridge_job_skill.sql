{{ config(materialized='table') }}

SELECT DISTINCT
    jobs.job_posting_key,
    skills.skill_key
FROM {{ ref('staging_skills') }} AS staged
INNER JOIN {{ ref('fct_job_postings') }} AS jobs
    ON split_part(split_part(trim(staged.link), '?', 1), '#', 1) = jobs.link
   AND lower(trim(staged.platform_source)) = jobs.platform_source
INNER JOIN {{ ref('dim_skill') }} AS skills
    ON lower(trim(staged.skill)) = lower(skills.skill)
WHERE staged.skill IS NOT NULL
  AND trim(staged.skill) <> ''
  AND lower(trim(staged.skill)) <> 'none'
