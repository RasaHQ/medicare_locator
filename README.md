# Medicare Locator built with the Rasa Stack

## 🏥 Introduction

This is an open source starter pack for developers to show how to automate full conversations in healthcare sector.

It supports the following user goals:

- Searching for a hospital, nursing home or home health agency in a US city.
- Handling basic chitchat.

## 💾 How to install and setup Medicare Locator

**Step 1**: To install Medicare Locator, please clone the repo:
```
git clone https://github.com/RasaHQ/medicare_locator.git
cd medicare_locator
```
The Medicare Locator uses **Python 3.5 and 3.6** and has not been tested with other versions.
Use the requirements.txt file to install the appropriate dependencies
via pip. If you do not have pip installed yet first do:
```
sudo easy_install pip
```
otherwise move to the next step directly.

**Step 2**: Install requirements:
```
pip install -r requirements.txt
```

**Step 3**: Install the spaCy English language model by running:
```
python3 -m spacy download en
```

This will install the bot and all of its requirements.

## 🤖 How to run Medicare Locator

**Step 1**: Train the core model by running:
```
make train-core
```
This will train the Rasa Core model and store it inside the `/models/current/dialogue` folder of your project directory.

**Step 2**: Train the NLU model by running:
```
make train-nlu
```
This will train the NLU model and store it inside the `/models/current/nlu` folder of your project directory.

**Step 3**: In a new terminal start the server for the custom action by running:
```
make action-server
```

**Step 4**: Now to test the Medicare Locator with both these models you can run:
```
make cmdline
```
After the bot has loaded you can start chatting to it. If you start by saying `Hi` for example,
the bot will reply by asking you what you are looking for and show you a number of options in form of buttons.
Since those buttons do not show when testing the bot in the command line, you can imitate a button click by copy
and pasting the intent of the button of your choice as your input.

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

**Step 5**: To run Medicare Locator in interactive learning mode run:
```
make interactive
```

## 📱 Use Telegram as Chat platform
In order to chat to the Medicare Locator through Telegram you can do the following:

**Step 1**: First if you don't already use Telegram, download it and set it up with your phone.
Once you are registered with Telegram you start by setting up a Telegram bot.

**Step 2**: To setup your own bot go to the [Telegram BotFather](https://web.telegram.org/#/im?p=@BotFather),
enter `/newbot` and follow the instructions.
You should get your `access_token`, and the username you set will be your `verify`. Save this information as you will need it later.

**Step 3**: Now you will need to connect to Telegram via a webhook. To create a local webhook from your machine you can use [Ngrok](https://ngrok.com/). Follow the instructions on their site to
set it up on your computer. Move `ngrok` to your working directory and in a new terminal run:
```
./ngrok http 5005
```
Ngrok will create a https address for your computer. For Telegram you need the address in this format:
`https://xxxxxx.ngrok.io/webhooks/telegram/webhook`

**Step 4**: Go to the *credentials.yml* file that you downloaded from the repo and input your personal `access_token`, `verify` and `webhook_url`.
You will have to update the `webhook_url` everytime you do redo Step 3, the `access_token` and `verify` will stay the same.

**Step 5**: In a new terminal start the server for the custom action by running:
```
make action-server
```

**Step 6**: In a new terminal connect to Telegram by running:
```
make telegram
```

**Step 7**: Now you and anyone on Telegram are able to chat to your bot. You can find it by searching for its name on Telegram.

Detailed information about this can also be found in the [Rasa Docs](https://rasa.com/docs/core/connectors/#telegram-connector).


## More about the Medicare Locator demo bot
There are some custom actions that require connections to external services,
specifically `FacilityForm` and `FindHealthCareAddress`. These two actions
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

`credentials.yml` - contains credentials for the use with Telegram

`endpoints.yml` - contains url for endpoint

## 🛠 Makefile overview
Run `make help` to see an overview of all make commands available.

`train-nlu` - Train the NLU model.

`train-core` - Train the Core model.

`interactive` - Run the Medicare Locator interactive learning mode.

`cmdline` - Run the bot on the command line.

`action-server` - Start the action server.

`telegram` - Run the bot in the Telegram channel.

## :gift: License
Licensed under the GNU General Public License v3. Copyright 2019 Rasa Technologies
GmbH. [Copy of the license](https://github.com/RasaHQ/rasa-demo/blob/master/LICENSE).
Licensees may convey the work under this license. There is no warranty for the work.
