# Medicare Locator built with the Rasa Stack

## 🏥 Introduction

This is an open source starter pack for developers of how to automate full conversations in healthcare

It supports the following user goals:

- Searching for an Hospital, Nursing Home or Home Health Agency in a city
- Handling basic chitchat

## 🤖 How to install and run Medicare Locator

To install Medicare Locator, please clone the repo and run:

```
cd medicare_locator
pip install -r requirements.txt
```
This will install the bot and all of its requirements.
Note that it was written in Python 3 so might not work with PY2.

To train the core model: `make train-core`. 

To train the NLU model: `make train-nlu`.

To run Medicare Locator with both these models:
```
make action-server &
make run-cmdline
```

To run Medicare Locator in interactive learning mode: 
```
make action-server &
make interactive
```

There are some custom actions that require connections to external services,
specifically `FindHospital` and `FindHealthCareAddress`. These two actions 
connect to Medicare APIs. These APIs do no require tokens or any form of authentication.

For more informations about Medicare APIs please visit [data.medicare.gov](https://data.medicare.gov/)

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
