# CMS_webpage

**What is CMS all about?**

CMS is stands for Content Management System. Designed to aid users, it stores their uploaded documents in a database, and can even bring up summaries of the user's specified document. It can specially search both the names and contents of documents for relevance to the search criteria.

***How to get yourself a working copy of CMS***
Below are the instructions to get yourself a working copy of the CMS app on your laptop.

*How to clone a copy of the repository:*

https://github.com/kdesai58/CMS_webpage.git     Using your desired IDE (VS Code, for example), clone the repository using the preceeding link.

*How to install all the dependencies needed:*

Start a new terminal and run the installation codes below to set up your environment to run the webpage and ensure you have all the components needed:

    npx create-react-app my-cms-frontend
    cd my-cms-frontend
    npm install react-router-dom
    pip install fastapi
    pip install uvicorn
    pip install sqlalchemy
    pip install fastapi[all]
    pip install faiss-cpu
    pip install pypdf2
    pip install numpy


*How to start the backend and frontend in order to run the program:*

Once the above is done, in your terminal, run the commands below:

Start the development server:

    npm start

Start the FastAPI server:

    uvicorn app.main:app --reload

**You should now have a running application**

You should now have your browser pop up with the application running smoothly on your own device. 
Depending on your device's specifications, the summary and search features may take some time to return results as it will run the AI behind the scenes... This will work without internet too, since the server is run on your device.

***Improvements next in line***

While this is a fully functional program, there are a few updates in line to make this an even better experience:

    Modifying the number of search results given to the user...