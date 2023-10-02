
# Resume

Project to read resume data from an Restful API built in Flask


## Setup

* python3.7 or higher
* virtual enviroment recommended

```bash
  python3 -m venv env
  cd resume
  source env/bin/activate
  python3 -m pip install requirements.txt
```

## Running API

### locally
* after you have activated the virtual enviroment and installed the packages using pip

```bash
  python3 app.py
```

* view swagger doc on http://127.0.0.1:5000


## Testing

```bash
  cd resume
  source env/bin/activate
  python3 tests.py
```


    
## API Reference

#### Get contacts

```http
  GET /get_all_contacts
```

#### Get contact details

```http
  GET /get_contact_details/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of contact to fetch contact details |


```http
  GET /get_professional_experience/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of contact to fetch professional experience data |


```http
  GET /get_education/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of contact to fetch education data |





