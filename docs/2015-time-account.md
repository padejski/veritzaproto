## Veritza 2015 Time Accounting

---

This document describes tasks and time spent on them on Veritza in 2015.

### Summary

---

The major work categories are:

* Serbia app
* Federal app
* Project wide changes
* Corex app
* California app


### Serbia App

---

Total time spent: 168 hrs

Time shared amongst the following components:

* scrapers: 63 hrs
    - This time is divided across 5 scrapers
    - Each scraper job involved writing a scraper and design a database model for it.
    - REASON: some scrapers underwent several iterations e.g. the company scrapers trying to auto generate IDs.

* Data Integrations: 48 hrs
    - This time is divided across 5 integrations.
    - Each integration involves a database model design, data comparison logic, user subscription logic and a frontend view.
    - REASON: the data comparison logic underwent several iterations. First with string matching (borrowed from Montenegro) then fuzzy string matching with integration hooks on data models to allow automatic data integration when new data rows are added.
    - REASON: also the initial logic was in the `corex` app under commands but eventually moved to an `integration.py` file in serbia app. This refactor reduced clutter.

* Views and Frontend: 41 hrs
    - time spent on frontend views of scraped data and integration views.

* Debug and error fixes: 16 hrs
    - time spent fixing scraping errors, fronted views errors and integration errors.



### Federal app

---

Total time spent: 83 hrs

Time shared amongst the following components:

* scrapers: 55 hrs
    - This time is divided across 8 scrapers.

* Views and Frontend: 24 hrs
    - time spent on frontend views of scraped data.

* Debug: 4 hrs
    - time spent on fixing errors.


### Project wide changes

---

Total time spent: 30 hrs

Time shared amongst the following components:

* Project initial setup, structure and documentation: 11 hrs
    - this involved local project repository setup, git branch and heroku app setup.

* Full text search: 18 hrs
    - implemented full text search on serbia and federal applications.


### Corex app

---

This is the core application module having common used functionalities and management commands.

The time spent on this app interleaves with time spent on other apps since the are dependent on the core module. The base scrapers for instance are implemented in the corex app.



### California app

---

Total time spent: 6 hrs

Barely began on California. Two scrapers have been implemented but are yet to me committed to the project since most focus has been on serbia and federal apps so far.
