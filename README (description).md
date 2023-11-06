## Step 1: Flask-Based RESTful API:
- Ensure and install Flask into the environment being used, in this case, Google Shell
- Then in that environment create the code for your ```app.py``` file within the project directory
- After creating the app.py file and integrating GET requests into the code, run the app locally
-   add pics

## Step 2: Azure API deployment:
- When having the flask application code ready under the ```app.py``` file, I navigated into the Azure Functions Python HTTP trigger official page and followed its commands as stated below
- First, I pick the correct type of system, in my case Linux and Debian, since the environment used was Google Shell
- (curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg)
  - ```sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/debian/$(lsb_release -rs | cut -d'.' -f 1)/prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'```
  - Begin the APT source update: ```sudo apt-get update```
  - Install the Core tools: ```sudo apt-get install azure-functions-core-tools-4```
- Then proceeded by creating a virtual environment by following the rest of the commands:
  - ```python -m venv .venv```, ```source .venv/bin/activate```, If not installed the venv: [```sudo apt-get install python3-venv```]
- Then went ahead and created a local fx by doing the following:
  - Creating the fx (in this case named Local Function Proj): ```func init LocalFunctionProj --python -m V2```
  - And then directed into the project folder in which a few files and folders automatically were created
  - In that .py file we can transfer the flask app code and convert it into the HTTP format
  - Proceeded with making the recommended changes as stated on the Microsoft website.
- After that proceeded to log into Azure through Google shell by doing the following:
- In order to install in the google shell environment I used the following command  ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```
- Then after completing that step I ran in my terminal a simple ```az``` command to make sure it was installed properly
- Then I used the following command in order to login and link my environment to my Azure ```az login --use-device-code``` . A message of authentication popped up and chose the account I wanted to use. It was successfully linked since the message below appeared:
- The next step was to name my application and connect it to the Azure resource group I had chosen by typing in my terminal the following: ```az webapp up --resource-group <groupname> --name <app-name> --runtime <PYTHON:3.9> --sku <B1>```
    - In this case I named the app angapiflask within a new created resource group named ang504-6
- After allowing the command above to complete in the Google shell environment I moved into Azure to App Services where my Flask application appeared
- Inside my web app in azure I was able to use the Default domain link provided from which I could access my app, indicating successful deployment message through Azure as shown below:
  - Then we can see that we have successfully been logged in and deployed

## Step 3: Open API
- Then edited the Flask app code to include the Swagger/OpenAPi code format by using the flasgger package
- Created a ```requirements.txt``` to ensure smooth running of the app
-   By changing and adding the argument ```?name=_____``` in this case added mine, it displayed into the flask app locally.
-   add pic
-   By doing so we can also test different endpoints that we included in the app.py file just by adding an argument at the end of the URL and navigating to the other endpoint
-   add pic "hello from another page"
