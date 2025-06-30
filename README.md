# ChecklistBot for Solana Coins

## What it does:
- Responds to `/scan <CA>` and gives a full breakdown based on your market cap entry/exit criteria
- Whitelisted access only, clean output, no logging
- Deployed via Railway

## Setup Instructions

1. Create a Telegram bot with @BotFather and get your token
2. Fork this repo or upload to your own GitHub
3. Go to [https://railway.app](https://railway.app)
   - "New Project" → "Deploy from GitHub"
   - Add environment variable: `TELEGRAM_TOKEN` = your token
4. Deploy and you’re live

## Commands
- `/start` — confirms bot is online
- `/scan <CA>` — scans a contract address (Solana only)