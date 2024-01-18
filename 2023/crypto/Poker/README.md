## Poker

### Description

Let's play Poker! I'll give you an advantage by letting you draw the first five cards first.

With that, can you figure out the rest of the deck?

To make sure it's a fair game, I have released the source codes.

Access the server: nc host port

### Solution

1. Identify that random seed generated is based on unix timestamp in miliseconds synced to a NTP server
2. The number of possible unique shuffle from 52! to only 1000
3. Use included `test.py` to generate 1000 possible shuffles based on unix timestamp and filter the shuffles based on the five issued cards

## Flag

`WH2023{UsE_GoOD_RANdOm_NumBErs}`

## Running locally

```bash
docker build -t poker .
docker run -p 1337:1337 poker
```

Access the server: nc localhost 1337