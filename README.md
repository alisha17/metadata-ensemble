## Ensemble search API

This application requires:

    Python 3.8.6

Install the requirements using:

```
pip install -r requirements.txt
```

To run the application (this will start the flask server - default port is 5000):

```
python run_server.py
```

Hit the endpoint using [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/) 
or any other API platform your prefer:

Example call:

```
http://localhost:5000/get_species_databases?species=homo_sapiens&release=100
```

You should see the response:

```
{
    "databases": [
        {
            "dbname": "homo_sapiens_cdna_100_38",
            "type": "cdna"
        },
        {
            "dbname": "homo_sapiens_core_100_38",
            "type": "core"
        },
        {
            "dbname": "homo_sapiens_funcgen_100_38",
            "type": "funcgen"
        },
        {
            "dbname": "homo_sapiens_otherfeatures_100_38",
            "type": "otherfeatures"
        },
        {
            "dbname": "homo_sapiens_rnaseq_100_38",
            "type": "rnaseq"
        },
        {
            "dbname": "homo_sapiens_variation_100_38",
            "type": "variation"
        }
    ]
}
```

To format the code, [Black](https://github.com/psf/black) formatter is used which follows PEP8 standards:

```
black .
```
#### NOTES : 
- At the moment, there is no pagination for results. But if the expected number of results is large,
it is best to paginate the results.
- The SQL credentials should ideally be passed as command line arguments or stored in a config file instead of hardcoding in the code.

### Deployment

There can be different ways to deploy this application:
1. Easiest would be to deploy this web service to AWS EC2 instance, using gunicorn for server and nginx for reverse proxy and load balancing and if there is a front-end for this web service,
that could be deployed to S3 bucket.
OR
2. The web service could be deployed to Heroku (free tier) but if we need to scale then we need a paid plan which does load balancing
to handle the number of requests. OR

3. Deploy to AWS Elastic Beanstalk - Elastic Beanstalk sets up an environment including 
EC2 instances, load balancers etc. (easier to scale if the traffic increases)

To make the solution more scalable, a more sophisticated architectural solution can be used so as to balance the load when number of requests increases.
Most of the deployment solutions above help in scaling when the load increases. For example: The auto 
scaling group in AWS Elastic Beanstalk will spawn more EC2 instances when the traffic increases.


### Testing

To test the application:

1. Use pytest to mock the API and validate
 the input and response of the API (testing the routes) for unit testing and integration testing.
 
2. If the production database is very large, it is best to create a new mock database with limited values to test the routes (for integration testing).

3. For security testing, use a tool like [Bandit](https://pypi.org/project/bandit/) - to find security
issues in the code.

3. To automate the testing, the use of CI pipelines is essential. By using a framework like CircleCI, Jenkins, Concourse etc., the tests can be automated to run on each build.