usage:

1- go to 'https://my.telegram.org/auth' and login  
2- go to API 'development tools'  
3- copy 'api_id' and 'api_hash'  
4- create a '.env' file and put the above variables like this:
```
api_id=1234567
api_hash=123456789abcdefghijklmnopqrstuvwxyz
```
5- run python file in terminal like bellow:  
``` python main.py --source-chat='xxxxx' --target-chat='xxxxx' --sleep-time=1  ```

TODO:  
add filters for audio, photo, text, video, etc.
add Docker configuratioin