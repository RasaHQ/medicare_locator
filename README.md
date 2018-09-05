# Rasa Stack starter-pack

Looked through the [Rasa NLU](http://rasa.com/docs/nlu/) and [Rasa Core](http://rasa.com/docs/core/) documentation and ready to build your first intelligent assistant? We have some resources to help you get started! This repository contains the foundations of your first custom assistant.  

**The training data is here in the [forum](https://forum.rasa.com/t/rasa-starter-pack/704)** 

We would recommend downloading this before getting started, although the tutorial will also work with just the data in this repo. 

The initial version of this starter-pack lets you build a simple assistant capable of cheering you up with Chuck Norris jokes.


<p align="center">
  <img src="./rasa-stack-mockup.gif">
</p>


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

You also need to install a spaCy English language model. You can install it by running:

```
python -m spacy download en
```


## What’s in this starter-pack?

This starter-pack contains some training data and the main files which you can use as the basis of your first custom assistant. It also has the usual file structure of the assistant built with Rasa Stack. This starter-pack consists of the following files:

### Files for training the Rasa NLU model

- **data/nlu_data.json** file contains training examples of six intents: 
	- greet
	- goodbye
	- thanks
	- deny
	- joke
	- name (examples of this intent contain an entity called 'name')
	
- **nlu_cofing.yml** file contains the configuration of the Rasa NLU pipeline:  
```text
language: "en"

pipeline: spacy_sklearn
```	

### Files for training the Rasa Core model

- **data/stories.md** file contains some training stories which represent the conversations between a user and the assistant. 
- **domain.yml** file describes the domain of the assistant which includes intents, entities, slots, templates and actions the assistant should be aware of.  
- **actions.py** file contains the code of a custom action which retrieves a Chuck Norris joke by making an external API call.
- **endpoints.yml** file contains the webhook configuration for custom action.

## How to use this starter-pack?
1. You can train the Rasa NLU model by running:  
```make train-nlu```  
This will train the Rasa NLU model and store it inside the `/models/current/nlu` folder of your project directory.

2. Train the Rasa Core model by running:  
```make train-core```  
This will train the Rasa Core model and store it inside the `/models/current/dialogue` folder of your project directory.

3. Start the server for the custom action by running:  
```make action-server```  
This will start the server for emulating the custom action.

4. Test the assistant by running:  
```make cmdline```  
This will load the assistant in your terminal for you to chat.

## What's next?
This starter-pack lets you build a simple assistant which can tell Chuck Norris jokes. It's pretty fun, but there is so much more you can do to make a really engaging and cool assistant. Here are some ideas of what you can do to take this assistant to the next level:  
- **Use the Rasa NLU [training data file](https://forum.rasa.com/t/rasa-starter-pack/704) which you downloaded previously from the Rasa Community Forum**. This dataset contains quite a few interesting intents which will enable your assistant to handle small talk. To use it, append the training examples to `data/nlu_data.md` file, retrain the NLU model and see how your assistant learns new skills.
- Enrich `data/nlu_data.md` file with the custom intents you would like your assistant to understand. Retrain the NLU model using the command above and see you assistant improving with every run!  
- Enrich `data/stories.md` file with more training stories with different dialogue turns, intents and actions.  
- Implement more custom action inside the `actions.py` file and add them to stories data as well as the domain file.   


Let us know how you are getting on with Rasa Stack and what have you built! Join the [Rasa Community Forum](https://forum.rasa.com) and share your experience with us!
