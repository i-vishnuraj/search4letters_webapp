# search4letters_webapp
Basic project with Python and Flask

## The repository and files were adapted from Head First : Python Second Edition

As part of learning or relearning Python :snake:, the repository walks through below components:
- Python Functions 
- DocString & Annotations
- Set methods
- setup file for installing custom modules
- Flask module for Minor Web App Deployment
- Jinja2 Template Engine
- HTML & CSS file structure
- Context management Protocol
- mySQL connector for logging and retrieve log contents

mySQL queries for some common data questions:
- How many requests have been responded to?
> select count(*) from log;

- What's the most common list of letters?
> select count(letters) as 'count', letters from log
> group by letters
> order by count desc
> limit 1;

- Which IP addresses are the requests coming from?
> select distinct ip from log;

- Which browser is being used the most?
> select browser_string, count(browser_string) as 'count'
> from log
> group by browser_string
> order by count desc
> limit 1;
