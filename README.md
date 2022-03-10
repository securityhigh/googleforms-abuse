# googleforms-abuse
The program for flooding Google Forms.

## Using
First - edit config.ini, adding parameters from POST request. You need to take this data from the browser (**DevTools -> Network -> Request for /responseForm**; for this you need to fill out a test questionnaire).
All required query parameters start with **"entry"**.
You also need to fill in the **"url"** field in the config, which contains a link to the profile without a slash and **"viewForm"** at the end.
Example on file **config.ini**

```
> pip3 install requests
> python3 formshack.py
# Enter requests count
```
