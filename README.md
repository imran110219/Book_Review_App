# Book Review Application

This application is designed for reviewing, rating books. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python 3.6.4
* Postgres


### Installing

A step by step series of examples that tell you have to get a development environment running

Download the python and install python.

```
https://www.python.org/downloads/
```

Download the Postgres and install it.

```
https://www.postgresql.org/download/
```

Install pip

```
$ easy_install pip
```

Create Virtual Environment

```
$ pip install virtualenv
$ cd Book_Review_App
$ virtualenv venv
$ venv\Scripts\activate
```

Install all package from requirements.txt

```
$ pip install -r requirements.txt
```

### Setup Database

Access postgres user

```
$ psql -U postgres
$ CREATE DATABASE bookreview;
```

Run migration

```
python manage.py makemigrations
python manage.py migrate
```

## Running the application

```
$ python manage.py runserver
```

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Sadman Sobhan** - *Initial work* - [imran110219](https://github.com/imran110219)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
