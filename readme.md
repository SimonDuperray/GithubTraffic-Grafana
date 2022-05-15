# Github Insights Traffic - Grafana

This project aims to graphically represent some info corresponding to Github Traffic activity.

The following informations are displayed on Grafana Dashboard:

```
- Number of public repositories
- Percentage of cloned repositories
- Percentage of viewed repositories
- Max Views and Max Unique Viewers
- Max Clones and Max Unique Cloners
- Views and Unique viewers
- Clones and Unique Cloners
- Mean Views and Mean Unique Viewers
- Mean Clones and Mean Unique Cloners
- Median Views and Median Unique Viewers
- Median Clones and Median Unique Cloners
```

## Process
Firstly, run the asker.py file. This script will ask you to fill some informations, required to link Python script to InfluxDB to Grafana Database. You will have to fill the following informations:
```
- Auhentication Token
- Github Pseudo
- Host
- Port
- Grafana Username
- Grafana password
- Grafana Database Name
- Measurement
```

Once this done, the .env file will be filled.

After that, run the githubinsightstraffic.py, the following steps will be ran:

1. Fetch all repositories given Github username by iterating pagination index on url. I go through for loop (1->100) to store repositories in global list, and, as soon as the result is an empty list I go out of the loop. 
```
"https://api.github.com/users/USERNAME/repos?page="
```

2. Once all the repositories fetched, I use the repo's name to fetch traffic data corresponding to every repository with the two following URLs:
```
https://api.github.com/repos/USERNAME/REPO/traffic/views
```
```
https://api.github.com/repos/USERNAME/REPO/traffic/clones
```

3. I make the result in shape in a python dict data structure. I also created some basic function to get average, median, percentage of non 0 and sum from different lists. 
```python
result = {
    'views': sum(res['views']),
    'unique_viewers': sum(res['unique_viewers']),
    'clones': sum(res['clones']),
    'unique_cloners': sum(res['unique_cloners']),
    'max_views': max(res['views']),
    'max_clones': max(res['clones']),
    'max_unique_viewers': max(res['unique_viewers']),
    'max_unique_cloners': max(res['unique_cloners']),
    'nb_repositories': nb_repos,
    'percentage_cloned': get_percentage(res['clones']),
    'percentage_viewed': get_percentage(res['views']),
    'mean_views': avg(res['views']),
    'mean_clones': avg(res['clones']),
    'mean_unique_viewers': avg(res['unique_viewers']),
    'mean_unique_cloners': avg(res['unique_cloners']),
    'median_views': median(res['views']),
    'median_clones': median(res['clones']),
    'median_unique_viewers': median(res['unique_viewers']),
    'median_unique_cloners': median(res['unique_cloners'])
}
```

4. Wwe have to create the InfluxDB database on the machine/server by typing following commands:
```linux
$ influx
$ CREATE DATABASE <dbname>;
$ exit
```
5. The next step is to send this Python dict to InfluxDB Database using InfluxDBClient using the variables from the .env file.

## Deployment
For automated the database filling, I use cron job by typing the following commands:
```
$ crontab -e
$ 31 1 * * * /usr/bin/python /home/pi/Documents/path_to_py_script.py
```

## Grafana
You can now create a new Grafana Dashboard to display yout Github Traffic data as you want. Here, a screen of my custom dashboard:

[![readme.png](https://i.postimg.cc/jj9zWKXC/readme.png)](https://postimg.cc/KKPKV6Cy)