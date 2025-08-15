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
         - Pledge (donate)
         - Create 
         - Sign in tab (user account)
    - possible about information on this page or as seperate tab
  - Featured Kickstarters
- Pledge page
    - Menu??? 
        - Poems
        - Short Story
        - Limericks
    - Information about pledges/fundraisers that have been created
        - categories 
        - 
    - Some way of pledging 
        - pledge amount
        - way to complete line of poem/story
        - anon or leave name
        - tracking to see when poem is complete
        - additional comments
    
- Create Page
    - user - log in (to be at top of each page) but would be good to have seperate on this page too.
    - form to complete with details
      - title
      - description
      - image
      - target amount
      - open/closed status
      - creation date
        - category
            - poem
            - short story
            - limerick
        - information about the poem/shortstory/limerick
            - Basics
                - Name of project
                - Theme or picture
                - Starting Line, or paragraph
            - Pledges 
                - How Many per entry
                - Feedback of pledge to project 
     
- Log in Page (user account capability)
  - user account 
    - email
    - password
    - name 
    - basic demographics (maybe)

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------------ | --------------------- | ---------------------------- |
| fundraiser/    |GET          |Fetch all fundraisers    |  N/A            |     200                  |   None        |
|fundraiser/ | POST | Creat a new fundraiser | JSON Payload | 201 | Any logged user


### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )