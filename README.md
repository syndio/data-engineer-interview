# Data Engineer Interview Take Home Exercise

This exercise is about creating a relational schema to support provided data, applying ETL logic to ingest the provided data into your relational schema, and then deriving data from your relational schema via a SQL query.

Three CSV files are provided in the `sample_customer_data` folder. Your task is to ingest these files into a reasonably simple relational schema. It may be important to note:
- These files represent uploads from three (fictionalized) Syndio clients. They contain data about (also fictionalized) employees at each client.
- You can assume the `employee_id` column is a globally-specific ID (if two rows have the same `employee_id`, they are referring to the same person).
- These files are denormalized; for the purposes of this exercise, please implement a simple normalized schema.
- These fictionalized companies may have included typing/naming errors when uploading their data.

Once you have created your full relational schema and ingested the provided data, please develop a query to display the following:
- Our internal teams would like to see the average employee compensation for each job group by gender. 

You may choose to implement this exercise in either Golang or Python; the skeleton exercise for each language is provided
here alongside this readme. Pick one of them and implement the transform of the incoming data files and insert the records
into your provided sqlite schema.

The result of the exercise is the completed ETL code logic, the sqlite db file which contains the applied schema (table created) as well as a SQL query.

The next interview will build on your solution to this exercise, so be ready to talk through your solution and enhance it!

## Not Required
- Tests
- Documentation
- Logging or anything more than basic error handling

## Submission
- Respond to the email you received for completing this exercise with:
  - Zip file containing the ETL code, sqlite db file of your relation schema, and your query as well as any additional files you believe might be necessary or helpful
- We'll run it and prepare feedback for the next part of the interview (if applicable)

## Notes
- We expect this to take no more than 120 minutes, please try and limit your effort to that window.
- Anything extra (tests, other logic outside of the basic ETL) is not worth bonus points
- We truly value your time and just want a basic benchmark and common piece of code to use in future interviews.
- If we bring you in for in-person interviews we'll expand on this submission; don't spend too much time on individual minor decisions, as your overall thought process / architecture are most important.
