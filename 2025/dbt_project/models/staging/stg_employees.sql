-- models/staging/stg_employees.sql
-- TODO: clean, cast, and normalize columns from raw_employees
select *
from {{ source('employees', 'raw_employees') }} 