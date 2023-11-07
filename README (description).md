## Step 1: Flask-Based RESTful API:
- Ensure and install Flask into the environment being used, in this case, Google Shell
- Then in that environment create the code for your ```app.py``` file within the project directory
- After creating the app.py file and integrating GET requests into the code, run the app locally
<img width="700" alt="Screenshot 2023-11-06 at 12 24 50 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/4939a585-8670-4008-9966-e7c6847f76d8">

## Step 2: Azure API deployment:
- When having the flask application code ready under the ```app.py``` file, I navigated into the Azure Functions Python HTTP trigger official page and followed its commands as stated below
- First, I pick the correct type of system, in my case Linux and Debian, since the environment used was Google Shell
- (curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg)
  - ```sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/debian/$(lsb_release -rs | cut -d'.' -f 1)/prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'```
  - Begin the APT source update: ```sudo apt-get update```
  - Install the Core tools: ```sudo apt-get install azure-functions-core-tools-4```
  - 
- Then proceeded by creating a virtual environment by following the rest of the commands:
  - ```python -m venv .venv```, ```source .venv/bin/activate```, If not installed the venv: [```sudo apt-get install python3-venv```]
    <img width="700" alt="Screenshot 2023-11-06 at 1 27 47 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/752e65c3-53ee-471d-b011-6ce58874607d">
<img width="700" alt="Screenshot 2023-11-06 at 1 45 45 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/36a55a10-9ca5-4405-93a6-2313284b3878">

- Then went ahead and created a local fx by doing the following:
  - Creating the fx (in this case named Local Function Proj): ```func init LocalFunctionProj --python -m V2```
    <img width="700" alt="Screenshot 2023-11-06 at 1 30 19 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/ebd32103-ec9b-4df7-8780-5ef01121494d">

  - And then directed into the project folder in which a few files and folders automatically were created
  - In that .py file we can transfer the flask app code and convert it into the HTTP format
  - Proceeded with making the recommended changes as stated on the Microsoft website.
- After that proceeded to log into Azure through Google shell by doing the following:
- In order to install in the google shell environment I used the following command  ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```
<img width="700" alt="Screenshot 2023-11-06 at 3 40 47 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/2e03f30f-2941-4e34-b4dc-fdd630f021f3">

- Then after completing that step I ran in my terminal a simple ```az``` command to make sure it was installed properly
  <img width="700" alt="Screenshot 2023-11-06 at 3 40 30 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/044ee63c-3219-4e63-a4c6-49efc58dcd19">

- Then I used the following command in order to login and link my environment to my Azure ```az login --use-device-code``` . A message of authentication popped up and chose the account I wanted to use. It was successfully linked since the message below appeared:
  <img width="500" alt="Screenshot 2023-11-06 at 3 41 34 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/e55a1479-6ded-4c07-b25d-1d640449e9a5">

- The next step was to name my application and connect it to the Azure resource group I had chosen by typing in my terminal the following: ```az webapp up --resource-group <groupname> --name <app-name> --runtime <PYTHON:3.9> --sku <B1>```
    - In this case, I named the app ```angapiflask``` within a new created resource group named ang504-6
<img width="700" alt="Screenshot 2023-11-06 at 3 46 18 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/2cb451b3-f373-4573-b328-0e5602521441">

- After allowing the command above to complete in the Google shell environment I moved into Azure to App Services where my Flask application appeared
<img width="700" alt="Screenshot 2023-11-06 at 3 48 34 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/1a128d83-f428-4163-9f97-cf9b812dfa23">

- Inside my web app in azure I was able to use the Default domain link provided from which I could access my app, indicating a successful deployment message through Azure as shown below:
  - Then we can see that we have successfully been logged in and deployed:
<img width="700" alt="Screenshot 2023-11-06 at 3 22 51 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/109e5d8e-970a-4bc4-b49d-464d2be768df">
<img width="700" alt="Screenshot 2023-11-06 at 2 16 08 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/10fd6536-ff86-48fb-8093-209260a8216b">


## Step 3: Open API
- Then edited the Flask app code to include the Swagger/OpenAPi code format by using the flagger package
- Created a ```requirements.txt``` to ensure the smooth running of the app
-   By changing and adding the argument ```?name=_____``` in this case added mine, it displayed into the flask app locally.
  
<img width="700" alt="Screenshot 2023-11-06 at 12 25 20 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/25d9dd0f-116f-4bb1-8edc-b3e5a93ac15c">

-   By doing so we can also test different endpoints that we included in the app.py file just by adding an argument at the end of the URL and navigating to the other endpoint
<img width="700" alt="Screenshot 2023-11-06 at 12 25 59 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/1583a9e7-215c-4e49-9421-6cace6fb">

<img width="700" alt="Screenshot 2023-11-06 at 12 31 48 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/a488f898-a5a5-41d8-a43e-711460a59c98">

<img width="700" alt="Screenshot 2023-11-06 at 12 37 26 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/f960d18e-01c9-4147-b957-40c02de1237e">

- Then using Flasgger we can also navigate to the app deployment it generated based on our code:

<img width="700" alt="Screenshot 2023-11-06 at 12 43 25 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/ccff67e5-4140-4485-b9ba-ed6f2251f55c">

<img width="700" alt="Screenshot 2023-11-06 at 12 40 34 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/90f570b7-724c-4042-8746-b059b9128197">

<img width="700" alt="Screenshot 2023-11-06 at 5 57 46 PM" src="https://github.com/angeliki-tzanou/flask_6_api_management/assets/141374140/5f875046-90ec-4d2c-b232-e65389c539b1">

- Deployed!
