# Tweety
**Uses "Twitter Streaming API" to get the target tweets(real-time) for a recent high traffic event(s). Later, tweets can be filtered using REST API**

## Requirements
Python 2.7+, pip, mysql, Twitter developer app

> Note: For creating `Twitter developer app`, visit [Twitter Application Management](https://apps.twitter.com/) page
> In the current project i have incorporated my twitter account.

## How to run?
1. Move to ```<project-dir>```, create virual environment and then activate it as


```sh
$ cd <project-dir>
$ virtualenv .environment
$ source .environment/bin/activate
```

2. Add mysql username and password to ```settings.py```.

3. Run a bash file ```do_clean_start```.

```sh
$ ./do_clean_start
```


3. Add mysql username and password to ```settings.py```.
```
> Now you can access the application by visiting ```{protocol}://{host}:{port}```. By default it run on ```http://localhost:8000```.
> If you want to run it manually use.
```

```sh
$ cd <project-dir>
$ source .environment/bin/activate
$ python manage.py runserver
```


## Operators

**Operators**: Following operators are available in order to filter/query data/tweets -

* _```equals```_ : Facilitates exact match, or **=** operator for numeric/datetime values.

* _```contains```_ : Facilitates full-text search.

* ```startswith``` : <var> (Starts with <var>),

* ```endswith``` : <var> (Ends with <var>),

* _```gte```_ : **>=** operator for numeric/datetime values.

* _```gt```_ : **>** operator for numeric/datetime values.

* _```lte```_ : **<=** operator for numeric/datetime values.

* _```lt```_ : **<** operator for numeric/datetime values.

* _```range```_ : **<= =>** operator for numeric/datetime values.


## API's/Endpoints

### For WOEID

```sh
GET /get-woeid/
```
It will give all the woeid along with other meta details of the countries.

*Response*
```javascript
[
    {
        "name": "Worldwide",
        "countryCode": null,
        "url": "http://where.yahooapis.com/v1/place/1",
        "country": "",
        "parentid": 0,
        "placeType": {
            "code": 19,
            "name": "Supername"
        },
        "woeid": 1
    },
    {
        "name": "Winnipeg",
        "countryCode": "CA",
        "url": "http://where.yahooapis.com/v1/place/2972",
        "country": "Canada",
        "parentid": 23424775,
        "placeType": {
            "code": 7,
            "name": "Town"
        },
        "woeid": 2972
    },
    {.....},
    ..
    ..
]
```
### Streaming

```sh
GET /start-stream/?woeid=1
```
> Note-: If nothing is supplied as a woeid then by default it will taken it as 1

It will start streaming real-time tweets for ```woied```. And tweets will get stored in the database.

*Response*

```javascript
{
  "status": "success",
  "message": "Started streaming tweets with woeid 1"
}
```

### API/Filtering

```sh
POST /get-filter-data?page=1&no_records=30
```

> Note: ```page``` & ```no_records```  can be used for limit/pagination, but are optional, default ```page``` is 1 and default ```no_records``` is 20.


*Request body*

```javascript
{
   "sort":[
      "-reply_count"        // Use '-' sign for 'desc' order.
   ],
   "criteria":{
      "AND":[

         {
            "fields":"hash_tags__name",  // for hastags field should be 'hash_tags__name'
            "operator":"contains",
            "query":"FMLA25"
         }
      ],
      "OR":[
         {
            "fields":"screen_name",
            "operator":"equals",
            "query":"cricket"
         },
         {
            "fields":"hash_tags__name",
            "operator":"",
            "query":"hockey"
         }
      ],
      "NOT":[
         {
            "fields":"retweet_count",
            "operator":"range",
            "query":"0|1"       // for range the values should be sperated with a '|'
         }
      ]
   }
}

```

*Response*

```javascript

{
    "tweets": [
        {
            "screen_name": "Emy02701199",
            "user_name": "Emy v-rat",
            "location": "Eysines, France ",
            "source_device": "Twitter Lite",
            "is_retweeted": false,
            "retweet_count": 0,
            "country": "",
            "country_code": "",
            "reply_count": 0,
            "favorite_count": 0,
            "tweet_text": "On t'écoute choisis moi pour mes 30 ans  #CauetOffreMoiDisney",
            "created_at": "2018-02-05T19:24:59",
            "timestamp_ms": "1517858699300",
            "lang": "fr",
            "tweet_id": "960595124366594049",
            "hash_tags": [
                "CauetOffreMoiDisney"
            ]
        },
        {
            "screen_name": "YoongiSaah",
            "user_name": "Sarah Ama Kai",
            "location": "Seoul,Coreia do Sul",
            "source_device": "Twitter for Android",
            "is_retweeted": false,
            "retweet_count": 0,
            "country": "",
            "country_code": "",
            "reply_count": 0,
            "favorite_count": 0,
            "tweet_text": "RT @JuriHobi: #ARMYSelcaDay Canino com o Tae Tae bias. https://t.co/Bd1LUmHIDb",
            "created_at": "2018-02-05T18:57:13",
            "timestamp_ms": "1517857033166",
            "lang": "pt",
            "tweet_id": "960588136094027777",
            "hash_tags": [
                "ARMYSelcaDay"
            ]
        },
        {
            "screen_name": "JokesRicardo",
            "user_name": "Ricardo",
            "location": "Maiquetia, Venezuela",
            "source_device": "Twitter for iPhone",
            "is_retweeted": false,
            "retweet_count": 0,
            "country": "",
            "country_code": "",
            "reply_count": 0,
            "favorite_count": 0,
            "tweet_text": "RT @SAbbasi3010: #GustavoPetroEnLaW, por motivos electoreros, niega ser chavista y dice que no quiere llevar a Colombia al mismo desastre d…",
            "created_at": "2018-02-05T19:25:05",
            "timestamp_ms": "1517858705946",
            "lang": "es",
            "tweet_id": "960595152241811456",
            "hash_tags": [
                "GustavoPetroenlaW"
            ]
        },
        {......},
        {......},
    ],
    "per_page_records": "5",
    "total_no_records": 83431,
    "total_pages": 16687,
    "current_page": "1"
}

```

