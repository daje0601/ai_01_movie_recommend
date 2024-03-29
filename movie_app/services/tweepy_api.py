import tweepy

api_key = "SvFSgQxeXSTIB9Xd4jSdB2L7v"
api_secret = "gb7HogfzFldxG4lFlmXbgF5UpuOBwHhd3TrsZtU1dAGrw49gx0"

access_token = "1372384598361960449-9q9R3Rw0F1WsG1HkFp6IQCaSjBwRU8"
access_secret = "5Js2zj4kucA4WjnxD2tH5M512iW0VGstjB5wwYUCUtskF"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def get_user(screen_name):
    """
    `get_user` 함수는 트위터의 `screen_name` 이 주어지면 tweepy 를 통해 해당
    트위터 유저를 조회한 객체를 그대로 리턴합니다.
    """
    raw_user = api.get_user(screen_name=screen_name)

    return raw_user


def get_tweets(screen_name):
    """
    `get_tweets` 함수는 트위터의 `screen_name` 이 주어지면 tweepy 를 통해 해당 트위터 유저의 트윗들을 조회한 리스트를 리턴합니다.
     - 리턴되는 트윗에는 리트윗 (retweet) 을 포함하지 않습니다.
     - 140 글자가 넘는 경우에도 다 가져올 수 있어야 합니다.
     - 답변 트윗 (retweet) 들은 포함하지 않습니다.
     - 한 페이지당 50 개의 트윗을 가져오도록 설정해야 합니다.

    Hint:

     - get_tweets 는 tweepy 의 user_timeline 함수를 사용합니다.
     - 다음 파라미터들을 어떻게 사용하는지 찾아보세요.
         - 'screeen_name'
         - 'tweet_mode'
         - 'include_rts'
         - 'count'
         - 'exclude_replies'
    """

    raw_tweets = api.user_timeline(
        screen_name=screen_name,
        tweet_mode="extended",
        include_rts=False,
        count=50,
        exclude_replies=True,
    )

    return raw_tweets
