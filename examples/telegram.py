# # Example of how use it with Pyrogram

# We start importing pyrogram client and our PyWars stuff
from pyrogram import Client as Telegram 
from PyWars import *

# We create a telegram and a chat wars client
telegram  = Telegram("my_account")
chat_wars = Client(loglevel='info', )

# A bucket of deals
bucket = {}

# Now we start the agents creation for fill a bucket
@chat_wars.agent(Deal)
async def bucket_builder(stream: Stream[Deal]):
    async for deal in stream:
        msg = f"{deal.buyerName} buy {deal.qty} from  {deal.sellerName} a {deal.price} $"
        if deal.item in bucket:
            bucket[deal.item].append(msg)
        else:
            bucket[deal.item] = [msg]

# And a timer for post the bucket every 10 seconds
@chat_wars.timer(10)
async def post_deals():
    me = await telegram.get_me()
    # And late we build a post for that bucket   
    post = ""
    for item, lines in bucket.items():
        post += f"{item}:\n\n"
        post += "\n".join(lines)
        post += "\n"
    if post:
        await telegram.send_message(me.id, post)
    bucket.clear()

telegram.start()
chat_wars.run()