# CMS_webpage

what is cms? what we are doing?

CMS is short for Content Management System. Designed to aid users, it stores their uploaded documents in a database, and can even bring up summaries of the user's specified document. It can specially search both the names and contents of documents for relevance to the search criteria.

how to clone repository?

https://github.com/kdesai58/CMS_webpage.git     Using your desired IDE (VS Code, for example), clone the repository using the preceeding link.

how to install all the dependencies?

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




how to run the frontend & how to start backend

Once the above is done, in your terminal, run the commands below:

Start the development server:

    npm start

Start the FastAPI server:

    uvicorn app.main:app --reload

then you have running application

You should now have your browser pop up with the application running smoothly on your own device. This will work without internet too, since the server is run on your device.