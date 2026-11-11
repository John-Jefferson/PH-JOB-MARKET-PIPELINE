{{ config(materialized='table') }}

SELECT DISTINCT
    jobs.job_posting_key,
    qualifications.qualification_key
FROM {{ ref('staging_qualifications') }} AS staged
INNER JOIN {{ ref('fct_job_postings') }} AS jobs
    ON split_part(split_part(trim(staged.link), '?', 1), '#', 1) = jobs.link
   AND lower(trim(staged.platform_source)) = jobs.platform_source
INNER JOIN {{ ref('dim_qualification') }} AS qualifications
    ON lower(trim(staged.qualification)) = lower(qualifications.qualification)
WHERE staged.qualification IS NOT NULL
  AND trim(staged.qualification) <> ''
  AND lower(trim(staged.qualification)) <> 'none'
