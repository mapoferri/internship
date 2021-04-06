# Internship

Here there are the codes used for the containerization of apps [PredGPI](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-9-392) and [BaCeLlo](https://academic.oup.com/bioinformatics/article/22/14/e408/228072).

# Requirements

Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) on your machine.
Python3 and all other dependecies of the applications are already in the personalized image.

These infrastructure has been organized to work on input multifasta files, as dowloaded from Uniprot database. 
To specify the path of your input directory, you would need to modify the .env file in the same directory as the docker-compose.yml script. 
The rest of the redirecting no needs to be modified, otherwise all scripts need to be updated. 

To run the first application (PredGPI), run the command: 
```
docker-compose -f docker-compose-predgpi.yml up --build
```

The results will appear as output directory in the input local one. 

For the BaCelLo app, all the codes necessary for the containerized infrastructure to run are in the [bacello] subdirectory. 
To run the second application so, run the command:

```
docker-compose -f docker-compose.yml up --build
```
