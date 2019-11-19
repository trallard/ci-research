## CI/CD for research multiple ways

[![License: MIT](https://img.shields.io/badge/License-MIT-c886e5.svg)](https://opensource.org/licenses/MIT)
- [CI/CD for research multiple ways](#cicd-for-research-multiple-ways)
- [⚡️ About this tutorial](#%e2%9a%a1%ef%b8%8f-about-this-tutorial)
- [Requirements](#requirements)
  - [☁️ Using Azure pipelines](#%e2%98%81%ef%b8%8f-using-azure-pipelines)
  - [⚙️ Using GitHub actions](#%e2%9a%99%ef%b8%8f-using-github-actions)
  - [💻 Running the application locally](#%f0%9f%92%bb-running-the-application-locally)
  - [📓 Using the materials](#%f0%9f%93%93-using-the-materials)

## ⚡️ About this tutorial
This tutorial was originally developed for NL-RSE 2019 by Tania Allard. The whole tutorial is self contained in this repo and you should be able to follow at your own pace. 

By the end of the tutorial you should be able to start implementing your CI/CD workflows either in Azure pipelines or GitHub actions. 
Note that since it's only a 1 hour course this is meant to be a taster of the capabilities of both solutions.

## Requirements

💻 Laptop with WiFi access

✨ GitHub Account

💻 Git installed in your personal laptop

🚇 _[Azure DevOps account](https://azure.microsoft.com/services/devops/?WT.mc_id=rse-github-taallard)_

📝 A text editor. I 💜VS Code, you can get it following this link 👉🏼 [VSCode](https://code.visualstudio.com//?wt.mc_id=rse-github-taallard).

### ☁️ Using Azure pipelines
The workshop hands on session materials for using Azure pipelines can be found 👉🏼 [here](./az-pipeline-vm.md).

### ⚙️ Using GitHub actions
The workshop hands on session materials for using GitHub actions can be found 👉🏼 [here](./github-actions.md).

We will also have time for you to create your own custom actions!!!

### 💻 Running the application locally
For the tutorial we will be testing and creating containers for the bokeh app in this repo.
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

### 📓 Using the materials

You can use, remix and adapt the content here, it has a MIT license so attribution is required. 
If you also want to contribute to the tutorial or make suggestions please open an issue here or contact Tania Allard at trallard[at]bitsandchips.me 