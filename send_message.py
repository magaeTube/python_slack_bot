from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = ""

client = WebClient(token=slack_token)

try:
    response = client.chat_postMessage(
        channel="",
        text="Hello World"
    )

except SlackApiError as e:
    print(f"Error posting message: {e.response['error']}")
