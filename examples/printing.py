# # A dummy example of printing all

# We import all basic stuff and build a dummy client for cw2 api consumtion
from PyWars import *

app = Client()


# We define an agent to process deals

@app.agent(Deal)  # this decorator define wath kind of topic we are specting for consume
async def deals(stream: Stream[Deal]):  # as we consume 'deals' topic we recieve a stream of deals
    async for deal in stream:  # we itterate over the deals
        print(deal)  # and we print every one of them


# From now on all it will be more of the same implementation


@app.agent(Offer)
async def offers(stream: Stream[Offer]):
    async for offer in stream:
        print(offer)


@app.agent(Duel)
async def duels(stream: Stream[Duel]):
    async for duel in stream:
        print(duel)


@app.agent(SexDigest)
async def sexdigest(stream: Stream[SexDigest]):
    async for sd in stream:
        print(sd)


@app.agent(YellowPage)
async def yellow_pages(stream: Stream[YellowPage]):
    async for yp in stream:
        print(yp)


@app.agent(AuctionDigest)
async def auctions(stream: Stream[AuctionDigest]):
    async for adigest in stream:
        print(adigest)


# Now we start to process and printing, easy and dummy
app.run()
