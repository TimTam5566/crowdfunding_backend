# crowdfunding_backend
Django
# Crowdfunding Back End
Tammy Healy

## Planning:
### Concept/Name
Poetry Site where for each pledge you add a line/paragraph to a poem or short story

### Intended Audience/User Stories
Anyone whow would like to be creative, but does not want to write a whole poem or short story.? 

### Front End Pages/Functionality

- Home Page
    - Title of website (Plot Twist - your the author, or Inkvestors, or Pledge for your thoughts)
    - Menu to additional pages (fixed in header to repeat on each page)
    - About information
    - Featured Kickstarters
- Create Page
    - user - log in/register (owner)
    - form to complete fundraising details
    - Ability to submit form
    - Include the following
        - Owner (a user)
        - Description
        - Image
        - Target amount to raise
        - Whether it is currently open to accepting new supporters or not
        - When the fundraiser was created
- Pledge page/section
    - user login/register (pledger)
    - form to complete details
      - pledge amount
      - comment for line of poem
      - anonymous or named
      - fundraiser pledge is for

- User account 
    - username
    - email
    - password
    - basic demographics (maybe)???????

- Update Functionality
- Delete Functionality
- implement suitable Permission for who can do certain things - eg delete pledge

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL         | HTTP Method | Purpose                          | Request Body | Success Response Code | Authentication/Authorisation |
| ----------- | ----------- | -------------------------------- | ------------ | --------------------- | ---------------------------- |
| fundraiser/ | GET         | Fetch all fundraisers            | N/A          | 200                   | None                         |
| fundraiser/ | POST        | Create a new fundraiser          | JSON Payload | 201                   | Any logged user              |
| user/       | GET         | Fetch all users - a single user? | N/A?         | 200                   | None                         |
| user/       | POST        | Create new user                  | JSON Payload | 201                   | Any logged user              |
| pledge/     | GET         | Fetch all pledges                | N/A          | 200                   | none                         |
| pledge/     | POST        | Create/add pledge                | JSON Payload | 201                   | Any 
logged user              |


- Handle failed requests gracefully (e.g. you should have a custom 404 page rather than the default error page).

- Return the relevant status codes for both successful and unsuccessful requests to the API.

- Use Token Authentication, including an endpoint to obtain a token along with the current user's details.

- 

### DB Schema

![]( {{ ./relative/path/to/your/schema/image.png }} )