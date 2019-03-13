# Medicare Locator built with the Rasa Stack

## 🏥 Introduction

This is an open source starter pack for developers, to show how to automate full conversations in healthcare.

It supports the following user goals:

- Searching for a hospital, nursing home or home health agency in a US city
- Handling basic chitchat

## 💾 How to install and setup Medicare Locator

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

## 🤖 How to run Medicare Locator

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

Now to test the Medicare Locator with both these models you can run:
```
make cmdline
```
After the bot has loaded you can start chatting to it. If you start by saying `Hi` for example,
the bot will reply by asking you what you are looking for and show you a number of options in form of buttons.
Since those buttons do not show when testing the bot in the command line, you can imitate a button click by copy
and pasting the intent of the button of your choice as your input (illustrated in the example below).

An example conversation in the command line could look something like this:
```
Your input ->  Hi
Hi. What are you looking for ?
Buttons:
1: Hospital (/inform{"selected_type_slot": "rbry-mqwu"})
2: Nursing Home (/inform{"selected_type_slot": "b27b-2uc7"})
3: Home Health Agency (/inform{"selected_type_slot": "9wzi-peqs"})
Your input ->  /inform{"selected_type_slot": "rbry-mqwu"}
What is you current city?
Your input ->  Seattle
...
```

Try out different conversations and see what the current state of the bot can do!
After playing around a bit you can try to modify and extend the bot by adding custom actions and intents for example.
Find help for this in the [Rasa Docs](https://rasa.com/docs/).

A helpful option to extend training data and get to know your bot is interactive learning,
here you can correct your bot at every step in the conversation and automatically save the data for future training.

To run Medicare Locator in interactive learning mode run:
```
make interactive
```

## More about the Medicare Locator demo bot
There are some custom actions that require connections to external services,
specifically `FindHospital` and `FindHealthCareAddress`. These two actions 
connect to Medicare APIs. These APIs do not require tokens or any form of authentication.

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
