# Update protocol

This protocol is thought to guide the Jenkins instance update for the Wikidata bots

## Installation

Prerequisites:

*   Python (3.8 was used in our case)
*   Pip:
 `sudo apt-get update`
 `sudo apt-get install pip`
*   Java (e.g.: Open Java Development Kit (OpenJDK))


Jenkins and virtualenv:
*   Jenkins (https://www.jenkins.io/doc/book/installing/linux/)

*   `sudo pip install virtualenv`


## Testing the workspace

*   Set up a Ghostbot in Jenkins with https://github.com/ernestoab/wikibots and check whether it produces results

## Setup working environment

*   Set up Jenkins jobs in accordance to the original Wikibots (e.g.: with the [Jenkins Import Plugin](https://www.coachdevops.com/2020/06/migrate-jenkins-jobs-from-one-server-to.html)) and the desired GitHub repo
*   

## Troubleshooting

*  make sure python version for virtualenv in the Jenkins Job's execute shell alings with the python version on the server
*  check OS, commands like "source" needed to be changed to "."
*  In case "virtualenv -p python38 venv" leads to permission errors, run:
```
cd /var/lib/jenkins/workspace/ 
sudo chwon -R jenkins:jenkins *

```
