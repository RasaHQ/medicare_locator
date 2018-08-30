# Rasa Stack starter-pack

Looked through the [Rasa NLU](http://rasa.com/docs/nlu/) and [Rasa Core](http://rasa.com/docs/core/) documentation and ready to build your first chatbot? We have some resources to help you get started! This repository contains the foundations of your first custom bot. Just by using the files of this repo you can build a simple assistant capable of cheering you up with Chuck Norris jokes.


Clone this repo to get started:

```
git clone https://github.com/RasaHQ/starter-pack-rasa-stack.git
```

After you clone the repository, a directory called starter-pack-rasa-stack will be downloaded to your local machine. It contains all the files of this repo and you should refer to this directory as your 'project directory'.


## Setup and installation

If you haven’t installed Rasa NLU and Rasa Core yet, you can do it by navigating to the project directory and running:  
```
pip install -r requirements.txt
```
This will install Rasa NLU and Rasa Core as well as all the dependencies you need to successfully build your first bot.  


## What’s in this starter-pack?

This starter-pack contains some training data and the main files which you can use as the basis of your first custom bot. It also has the usual file structure of the assistant built with Rasa Stack. This starter-pack consists of the following files:

### Files for Rasa NLU model

- **data/nlu_data.json** file contains training examples of six intents: 
	- greet
	- goodbye
	- thanks
	- deny
	- joke
	- name (examples of this intent contain an entity called 'name')
	
- **nlu_cofing.yml** file contains configuration of the Rasa NLU pipeline:  
```text
language: "en"

pipeline: spacy_sklearn
```	

### Files for Rasa Core model

- **data/stories.md** file contains some training stories whic respresent the conversations between a user and the assistant. 
- **domain.yml** file describes the domain of the assistant which includes intents, entities, slots, templates and actions the assistant should be aware of.  
- **actions.py** file contains a code of a custom action which retrieves a Chuck Norris joke by making an external API call.  

## How to use this starter-pack?
1. You can train the Rasa NLU model by running:  
```make train-nlu```  
This will train the Rasa NLU model and store it inside the `/models/current/nlu` folder of your project directory.

2. Train the Rasa Core model by running:  
```make train-core```  
This will train the Rasa Core model and store it inside the `/models/current/dialogue` folder of your project directory.

3. Test the assistant by running:  
```make cmdline```  
This will load the assitant in your terminal for you to chat.

## What's next?
This starter-pack lets you build a simple assistant which can tell Chuck Norris jokes. It's pretty fun, but there is so much more you can do to make a really engaging and cool assistant. Here are some ideas of what you can do to take this assistant to the next level:  
- Enrich `data/nlu_data.md` file with the intents you would like your bot to understand. Retrain the NLU model using the command above and see you assistant improving with every run!  
- Enrich `data/stories.md` file with more training stories with different dialogue turns, intents and actions.  
- Implement more custom action inside the `actions.py` file and add them to stories data as well as the domain file.   
- If you need more inspiration we have a really cool Rasa NLU [training data file](https://forum.rasa.com/t/rasa-starter-pack/704) which you can find on Rasa Community Forum. This dataset contains quite a few interesting intents. To use it, append the training examples to `data/nlu_data.md` file, retrain the NLU model and see how your bot learns new skills.

Let us know who you are getting on with Rasa Stack and what have you built! Join the [Rasa Community Forum](https://forum.rasa.com) and share you experience with us!
