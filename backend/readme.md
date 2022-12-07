### Commands to run backend

* create virtualenv `python -m venv myenv`

* activate virtualenv `myenv\scripts\activate`

* install the dependencies `pip install -r requirements.txt`

* run the server `python manage.py runserver`

### Setting up selenium

* please refer to this <a href="https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/">guide</a> to setup selenium, once done you need to place the driver in the same place where i have put mine (replace with mine msedgedriver.exe) with the one present in the repository.

* to edit the selenium path in the try_final.py script to avoid errors

### API endpoints used in the project

To fetch Records (GET)
`http://127.0.0.1:8000/api/v1/`

To refresh records (POST)
`http://127.0.0.1:8000/api/v1/`
