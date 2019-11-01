.PHONY: clean train-nlu train-core cmdline server

TEST_PATH=./

help:
	@echo "    clean"
	@echo "        Remove python artifacts and build artifacts."
	@echo "    train-nlu"
	@echo "        Trains a new nlu model using the projects Rasa NLU config."
	@echo "    train-core"
	@echo "        Trains a new dialogue model using the story training data."
	@echo "    action-server"
	@echo "        Starts the server for custom action."
	@echo "    interactive"
	@echo "        Starts interactive training using the current model."
	@echo "    cmdline"
	@echo "        This will load the assistant in your terminal for you to chat."
	@echo "    run-cmdline"
	@echo "        This will load the assistant in your terminal for you to chat in debug mode."
	@echo "    telegram"
	@echo "        This will use your credentials.yml file to setup a webhook for the use with Telegram."

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf docs/_build

train-nlu:
	python3  -m rasa train nlu -c nlu_config.yml --nlu data/nlu_data.md --out models --fixed-model-name nlu --verbose

train-core:
	python3 -m rasa train core -d domain.yml -s data/core --out models/current/dialogue -c core_config.yml

interactive:
	python3 -m rasa_core.train interactive --core models/current/dialogue -d domain.yml -c core_config.yml -u models/current/nlu --endpoints endpoints.yml --debug

cmdline:
	python3 -m rasa shell

action-server:
	python3 -m rasa run actions

run-cmdline:
	python3 -m rasa shell

telegram:
	python3 -m rasa_core.run -d models/current/dialogue -u models/current/nlu --port 5005 --credentials credentials.yml --endpoints endpoints.yml
