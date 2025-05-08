-- models/marts/employees.sql
-- TODO: build a clean employee dimension model from stg_employees
select *
from {{ ref('stg_employees') }}
limit 0; 