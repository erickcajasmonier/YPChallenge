# YPChallenge

## Task #1: Exploratory Testing Challenge
Please find the exploratory testing challenge markdown file [here](/Exploratory_Charters.md)

## Task #2: RESTful API Automation Testing
Python version:
- Python 3.9

In case you are using a Macbook and have two versions of python (python 2 and python 3), please execute the following command to have python 3 as the default python version runner: `ln -s -f /usr/local/bin/python3.# /usr/local/bin/python`, replease # with the python version number.
Then reopen the terminal and execute `python --version` to check the correct latest default version.

You must install the pip packages in order to run the automation testing, please execute `pip install -r requirements.txt` in your terminal.

Python Packages used for this AUT project:
- pytest v6.2.5
- requests v2.27.1
- Faker v11.3.0
- python-dotenv v0.19.2

#### Important: There is a **.env.template** file, this file must be name changed to **.env** file.

To run all tests you need to go to the main project folder for example: `cd /Users/CodeChallenge/YPChallenge` and execute the command `pytest` or `pytest -s` using the terminal.

### Test Cases:
In all test cases were verified the response status codes, response bodies (json and xml), and response texts.
#### PET
- Add a new pet to the store:
  - Add pet successfully with available status.
  - Add pet successfully with not available status.
  - Verify invalid input.
  - Perform a bad request.
- Upload pet image:
  - Upload pet image successfully.
  - Pet not found.
- Update an existing pet:
  - Update an existing pet successfully.
  - Pet not found.
  - Perform a bad request
- Find pets by status:
  - Find pet by available status.
  - Find pet with pending status.
  - Find pet with sold status.
  - Perform a bad request.
- Find pet by id:
  - Find pet with id successfully.
  - Pet not found.
  - Perform a bad request.
- Delete a pet:
  - Delete a pet successfully.
  - Perform a bad request.
- Update and existing pet with form data:
  - Update an existing pet successfully.
  - Pet not found.
  - Perform a bad request

#### STORE
- Place an order for a pet:
  - Place an order for a pet successfully.
  - Verify invalid input.
  - Perform a bad request.
- Return pet inventories by status:
  - Return pet inventories by approved status.
  - Return pet inventories by placed status.
  - return pet inventories by delivered status.
- Find purcharse order by id:
  - Find purchase order by id successfully.
  - Id not found.
  - Perform a bad request.
- Delete purchase order by id:
  - Delete purchase order by id successfully.
  - Perform a bad request.

#### USER
- Create a new user:
  - Create a new user successfully.
  - Verify invalid input.
  - Perform a bad request.
- Log user into the system:
  - Log the user into the system successfully.
  - Verify incorrect username/password.
- Get user by username:
  - Get user by username successfully.
  - Invalid username.
- Update user:
  - Update user successfully.
  - Perform a bad request.
- Log out current logged in user session:
  - Log out current logged in user session successfully.
- Delete user:
  - Delete user successfully.
  - User not found.

### Python Automation Results:
![Automation Results](/automation_result.png?raw=true)

### Notes:
- The test relies in random generated data, there is no need to add or change anything before executing the automation tests.
- There are some tests that were skipped due to some current issues with the API behaviors, you can check the reason of the skipped tests seaching for `@pytest.mark.skip`.

### Problems faced during local execution of swagger-petstore project:
- After having the swagger-petstore project in my local, I needed to update the war dependency in the pom file because I had the latest Maven version and there were some conflicts building all the dependencies, after doing that I could deploy the Maven project to my local using mvn or docker commands without any problems.