# Medicare Locator built with the Rasa Stack

## 🏥 Introduction

This is an open source starter pack for developers of how to automate full conversations in healthcare

It supports the following user goals:

- Searching for an Hospital, Nursing Home or Home Health Agency in a US city
- Handling basic chitchat

## 🤖 How to install and setup Medicare Locator

To install Medicare Locator, please clone the repo:
```
git clone https://github.com/RasaHQ/medicare_locator.git
cd medicare_locator
```
The Medicare Locator uses Python 3.5 and 3.6 and has not been tested with other versions.
Use the requirements.txt file to install the appropriate dependencies
via pip. If you do not have pip installed yet first do:
```
sudo easy_install pip
```

otherwise execute directly:
```
pip install -r requirements.txt
```

You also need to install a spaCy English language model by running:
```
python -m spacy download en
```

This will install the bot and all of its requirements.

## How to run Medicare Locator

Train the core model by running:
```
make train-core
```
This will train the Rasa Core model and store it inside the `/models/current/dialogue` folder of your project directory.

Train the NLU model by running:
```
make train-nlu
```
This will train the NLU model and store it inside the `/models/current/nlu` folder of your project directory.

In a new terminal start the server for the custom action by running:
```
make action-server
```

Now to test the Medicare Locator with both these models run:
```
make run-cmdline
```

To run Medicare Locator in interactive learning mode run:
```
make interactive
```

There are some custom actions that require connections to external services,
specifically `FindHospital` and `FindHealthCareAddress`. These two actions 
connect to Medicare APIs. These APIs do no require tokens or any form of authentication.

For more information about Medicare APIs please visit [data.medicare.gov](https://data.medicare.gov/)

If you would like to run Medicare Locator on your website, follow the instructions
[here](https://github.com/mrbot-ai/rasa-webchat) to place the chat widget on
your website.


## 👩‍💻 Overview of the files

`data/core/` - contains stories for Rasa Core

`data/nlu_data.md` - contains example NLU training data

`actions.py` - contains custom action/api code

`domain.yml` - the domain file for Core

`nlu_config.yml` - the NLU config file

`core_config.yml` - the Core config file

## 🛠 Makefile overview

`train-nlu` - Train the NLU model.

`train-core` - Train the core model.

`interactive` - Run the Medicare Locator interactive learning mode.

`cmdline` - Run the Medicare Locator Bot.

`action-server` - Starts the action server.

## :gift: License
Licensed under the GNU General Public License v3. Copyright 2019 Rasa Technologies
GmbH. [Copy of the license](https://github.com/RasaHQ/rasa-demo/blob/master/LICENSE).
Licensees may convey the work under this license. There is no warranty for the work.
