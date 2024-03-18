# NoMail


## Table of Contents

* **[Description](#description)**
* **[Why?](#why)**
* **[Usage](#usage)**
* **[Contributing](#contributing)**


## Description

Customizable email filter for Gmail with Python.


## Why?

I wanted to make a customizable email filter to extract
pertinent information and ignore the rest.


## Installation

```bash
pip install nomail
```

## Usage

`nomail` can be used move emails to your trash:

```python
import nomail

# by default, email addresses in blacklist.csv will be moved to your trash folder
nomail.filter()
```


## Contributing

1. Clone repo and create a new branch: `$ git checkout https://github.com/aidencullo/nomail -b name_for_new_branch`.
2. Make changes and test
3. Submit pull request with description of proposed changes


## License

`nomail` was created by Aiden Cullo. It is licensed under the terms of the MIT license.