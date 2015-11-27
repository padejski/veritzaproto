## Veritza Nov 2015

---

This document describes work done on Veritza as of Nov 2015.

### Summary

---

There are several updates made to the project.

The main updates are:

* Serbia app data integration
* Montenegro application decoupling
* User support
* Full Text Search support

### Serbia Data Integration

---
Aggregated serbia data integration commands into an integrator class found in
the `integration.py` file.
This allows for data integrations for all serbian datasets to be run at the
same time.



### Montenegro Application Decoupling

---

Applications are now decoupled into **montenegro**, **serbia** and **usa**.

There is now a `/montenegro` routing route for the **montenegro** app.

### User Support

---

User login support has been returned.

Testing account:
username: matt
pasword: mattadmin

### Full Text Search support

---
Full Text Search has been implemented using
[django-watson](https://github.com/etianen/django-watson).

This has been fully integrated for the serbia app.



### Contributors

---

Documentation done by [Matt Gathu](http://mattgathu.me)
