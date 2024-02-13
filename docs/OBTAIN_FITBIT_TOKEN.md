This is what I used for getting the access token required for the backend to access my fitbit data. Note that it is dependant on the `Implicit Grant Flow` (see https://dev.fitbit.com/build/reference/web-api/developer-guide/authorization/), which may become unavailable sometime in the future.

1. Start registering your own fitbit app at https://dev.fitbit.com/apps/new
2. Set `OAuth 2.0 Application Type` to personal, type in any URL in all URL-related fields **except `Redirect URL`**
3. In `Redirect URL`, use http://localhost
4. Finish registration
5. Select the newly registered app on https://dev.fitbit.com/apps
6. Copy the value from the OAuth 2.0 Client ID
7. Replace the `<CLIENT_ID>` in the URL below with the copied client ID from previous step:
 ```https://www.fitbit.com/oauth2/authorize?client_id=<CLIENT_ID>&response_type=token&redirect_uri=http://localhost&scope=activity%20cardio_fitness%20electrocardiogram%20heartrate%20location%20nutrition%20oxygen_saturation%20profile%20respiratory_rate%20settings%20sleep%20social%20temperature%20weight```
 8. Use this URL in browser, then select for how long you want the access to be and allow the desired scopes
 9. You will then be redirected to something like:
  ``` http://localhost/#access_token=<ACCESS_TOKEN>&user_id=<USER_ID>&scope=social+settings+profile+activity+location+nutrition+heartrate+weight+sleep&token_type=Bearer&expires_in=<SOME_MILISECONDS>```
  This redirect will fail, but the redirection URL in your browser contains the needed access token after `access_token=` until the first `&` character. This is all that is required for the backend to fetch your data from the web API. Never share or upload it anywhere, as it will give anyone that has it access to your fitbit data!
