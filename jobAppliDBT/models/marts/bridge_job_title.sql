{{ config(materialized='table') }}

SELECT DISTINCT
    jobs.job_posting_key,
    titles.title_key
FROM {{ ref('staging_title') }} AS staged
INNER JOIN {{ ref('fct_job_postings') }} AS jobs
    ON split_part(split_part(trim(staged.link), '?', 1), '#', 1) = jobs.link
   AND lower(trim(staged.platform_source)) = jobs.platform_source
INNER JOIN {{ ref('dim_title') }} AS titles
    ON lower(trim(staged.title)) = lower(titles.title)
WHERE staged.title IS NOT NULL
  AND trim(staged.title) <> ''
  AND lower(trim(staged.title)) <> 'none'
