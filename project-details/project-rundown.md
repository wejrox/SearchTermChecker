# Search Term Checker
Hits an endpoint and scrapes the result for a term specified. Repeats periodically (minimum 1 minute intervals).

## Reason for creation
In the year of this projects inception, a new computer part was being released at an undisclosed time. I didn't want to check myself to see when it was released, so instead I created this little app to do the checking for me and send me a message when it was found.

## Method
1. The user sets up their email details for the app to run.
1. The user passes in the term, the URL, and how often in minutes to check the result.
2. Html get request is made to the URL.
3. Checks based on regex to see if the term is present in the response regardless of case.
4. Sends an email to the user if it is found.
5. Exit, or wait for the check interval and return to step 2.

## Tech used
- Python3.6
- Visual Studio Code
- Intellij Idea

## Definition of done
This project will be defined as completed when it:
- [x] Retrieves the URL response of an endpoint.
- [x] Checks the result for a specific string.
- [x] Informs on success.
- [x] Retries until found.

## Stretch goals
- [x] Send an email to the user on success so that they can receive a notification from anywhere.