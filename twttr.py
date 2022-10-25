tweet = input("Tweet: ")
for i in tweet:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        tweet = tweet.replace(i,'')
    if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        tweet = tweet.replace(i,'')
print(tweet)
