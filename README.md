### Token Counter 
It's a simple project to count how many tokens exist in a prompt to be sent to a model. 
It can be useful when you need to verify dinamically if the prompt is too large, 
to avoid incomplete prompt as well as incomplete response You can find more details 
about models specification [here](https://platform.openai.com/docs/models)

### Models
The models tested here are from Open AI

### Library
The main library used in the project is called: Tiktoken and can found 
[here](https://pypi.org/project/tiktoken/)

### Idea
The possibility of counting tokens in a simple way was extracted from this documentation [here](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)

### Hands On

Setup on MacOS Sequoia
```
# Clone the repository 
git clone https://github.com/fernandoferreiratbe/token-counter.git

# Access the project's root directory
cd <path>
 
# Create a new virtual environment
python -m vevn venv

# Activate the virtual environment 
. .venv/bin/activate

# Upgrade pip version
pip install --upgrade pip

# Install requirment to run the app
pip install -r requirements.txt

# Install requirments to run tests
pip install -r requirements-test.txt
```

Run unit tests & check code coverage
```
# Run tests and evaluate the code coverage
pytest --cov-report term-missing --cov=. src/tests
```

### Additional info
The implemented test shows us an example using a simple prompt to be quantified 
based on the use of the GPT_3_5_TURBO model
