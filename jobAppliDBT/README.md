# JobAppli dbt models

This project transforms the JobStreet and FoundIt bronze tables into a gold-layer dimensional model.

## Model layout

- `fct_job_postings`: one row per source platform and canonical posting URL; includes work type, location, seniority, and work setup.
- `dim_title`, `dim_skill`, `dim_qualification`: unique normalized labels.
- `bridge_job_title`, `bridge_job_skill`, `bridge_job_qualification`: many-to-many relationships from postings to their extracted labels.
- `mart_skill_demand`: current posting counts by skill and platform.
- `mart_role_distribution`: current posting counts by matched title and platform.
- `mart_location_summary`: current posting counts and attribute variety by location and platform.

The title bridge is intentional: title extraction matches a set of title keywords, so one posting can match more than one title. Qualifications are also multi-valued, so they use a qualification dimension plus a job-qualification bridge.

These are current-snapshot marts, not historical trend models. The source data does not currently include a reliable scrape timestamp or posting date.

## Run

Configure the `jobAppliDBT` profile for PostgreSQL, then run:

```shell
dbt build --project-dir jobAppliDBT
```

`dbt build` creates the models and runs the tests declared in `models/marts/marts.yml`.
