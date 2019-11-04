# Python_Alexa_RaspberryPi_Automation
This repo tutorial is how to use Alexa to trigger a Python Script on a remote Raspberry Pi to turn on a motor. The motor is mounted on a 40lbs dog food dispenser. A user triggers Alexa to run the script by saying "Alexa, ask Raspberry Pi to feed the dogs". Amazon will send a signal to the ngrok endpoint which tunnels to our Flask app. Flask will interpet the intent response, triggering the motor to turn forward for a defined duration of time, then reversing the motor direction to stop the flow of food. This Repo is an end-to-end small scale example of combining Python and hardware for real world physical automation.  


In an ideal scenario the 'motor' script can be set to be executed by a cron job to ensure feeding happens automatically at a defined time, daily. In an ideal scenario, Alexa, Ngrok, and Flask are uneeded. This example is to 'wow your friends' and show the possiblities of creativity and a 'can do' attitude.  

## Getting Started
Make sure you have Python3.7 installed and working correctly. 



### Products Used




### Prerequisites

### Steps:


##Raspberry Pi setup


## Ngrok


### Flask_App Python Script


## Running the Flask_App File


## Deployment


## Built With

* [Jupyter](https://jupyterhub.am.lilly.com) - Web Interface to HPC Linux environments
* [Apache](https://maven.apache.org/) - Dependency Management


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

I use [GitHub](https://github.com/James-Davis-JnD/Python_Alexa_RaspberryPI_Automation) for versioning. For the versions available, see the [tags on this repository](https://github.com/James-Davis-JnD/Python_Alexa_RaspberryPI_Automation/tags). 

## Authors

* **James N. Davis** - *Initial work* - [James Nathan Davis](https://www.linkedin.com/in/james-davis-a13b4378)

## License

This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
 





