# webapp-demo
demo of e-commerce web application serving autocompletion


## Work environment

### Virtual env

Create a virtual env and activate it :

    $ virtualenv workenv
    $ . workenv/bin/activate

### Requirements

Install the requirements packages by running the command below :

    $ pip install -r requirements.txt

### Docker
Install Docker and Docker-compse then you can run the stack with Flask, Mongodb & Redis :
    $ docker-compose up

## TODO 

  * Add CSS code
    index.htm :
    -----------
    * Head bar black with the search box in the middle with a button
    * The rest of the page is white and empty
    list.htmp :
    ----------
    * Show the product that the customer ask for in the middle of the page :
      * Add the product's picture
      * Space for product name, price and all other description available in the MongoDB
    search.htm :
    ------------
    * Add 'suggestion' (retrieve thanks to redis) below the search box when a user is looking for a product
    * Highligth the suggestion text when the user is naviguating on it (by mouse or keyboard - Maybe keyboard first then if time with mouse...)

  * Add JS code (AngularJS if possible)
    * Add a Buton and deal with the action 'click' and the 'press key enter'
    * Add code in order that the customer is able to naviguate in the suggestions that appear below the search box

  * Install & configure Apache using with Flask

  * Deal with the case where the user is looking for something that doesn't exist (at least catch the error ...)
