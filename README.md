# txid-address-scraper
This is a Tool and API to traverse the Bitcoin Blockchain based off a Transaction Hash and specified depth. 
It gathers the inputs and relevant data to transactions.

## Pre-requisites

1. Node.js `v8.10.0` or later and Python 'v3.6' or later.
2. Serverless CLI `v1.9.0` or later. You can run 
`npm install -g serverless` to install it.
3. An AWS account. If you don't already have one, you can sign up for a [free trial](https://aws.amazon.com/s/dm/optimization/server-side-test/free-tier/free_np/) that includes 1 million free Lambda requests per month.
4. **Set-up your [Provider Credentials](./credentials.md)**. [Watch the video on setting up credentials](https://www.youtube.com/watch?v=HSd9uYj2LJA)

1. Clone the Repo
2. Run npm install 

## To Deploy API

Ensure you have credentials setup.
Run the following 
`serverless deploy -v` 
to deploy your very own api.

APIs deployed on here have a 30 second timeout.

# To integrate Python script
Include class in project.
`from scraper import Scraper`

Initiate a Scraper Object
`s = Scraper(txid, depth)`

Get Results
`print(s.getResults())`

If issues with Python2 being install I recommend looking into Virtualenv
I run the following..

`virtualenv venv --python=python3`

`source venv/bin/activate`

