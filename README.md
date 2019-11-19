## CI/CD for research multiple ways
[![License: MIT](https://img.shields.io/badge/License-MIT-c886e5.svg)](https://opensource.org/licenses/MIT)

## Requirements

💻 Laptop with WiFi access

✨ GitHub Account

🚇 _[Azure DevOps account](https://azure.microsoft.com/services/devops/?WT.mc_id=rse19-github-taallard)_

### Using Azure pipelines
The workshop hands on session materials for using Azure pipelines can be found 👉🏼 [here](./az-pipeline-vm.md)

### Running the application locally

You will need the requirements above as well as the following steps:

1. Install Python > 3.6 (3.7 preferred)
2. Fork this repo 
3. Clone your fork of the repo
```
git clone https://github.com/{your-user}/rse19-ms-workshop.git

cd rse19-ms-workshop
```
3. Install dependencies - we recommend using virtual environments or conda environments

_Virtual env_
```
# MAC or Linux 
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

```
# Windows
py -m venv .env
.\env\Scripts\activate
pip install -r requirements.txt
```

_Anaconda_
```
conda env create -n rse19
conda activate rse19
conda install --file requirements.txt
```

To run the bokeh apps you can run the following command:

```
bokeh serve iris

#or
bokeh serve boston
```