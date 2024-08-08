# INaturalist and its API

So INaturalist is this website that facilitates the uploading of pictures of different species of animals.
See: `https://www.inaturalist.org/observations`

This website also has an API, and apparently the API has 2 versions, V1 and V2. I used the V1 in here.  
Using the API we can communicate with the service, and get data from the website.  

The website contains pictures of different species of animals. Each species has a common name and a scientific name. I used their common names in here; for example: `Sharptail Bees`

In here we have a `pollinators.txt` file. In this file, we input the name of the species that we are interested in, so that we can extract the data related to those species from the INaturalist website.
For example, in this file, I entered `American Bumble Bee` , `Fervid Nomad Bee` and `Sharptail Bees`. These are all different bee species that INaturalist has the data for.


Here, using the `DownloadObservations.py` file, we can get the data from INaturalist, more specifically, the observations.   
This data contains a lot of different information, like the date the picture was captured, the location, the name of the species, the url of the picture and so many more.  
For an example and more info, see: `https://www.inaturalist.org/observations/export?verifiable=true&page=1&spam=false&place_id=any&user_id=&project_id=`  
When running this file, the code generates as many directories for us as needed, specified by the species names in the `pollinators.txt` file.  
Using the `per_page` variable in the `DownloadObservations.py` file, we can specify how many examples of the species we want to get the data for.  
