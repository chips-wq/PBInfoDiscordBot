# PBInfo Discord Bot

A Discord bot that fetches and displays programming problems from PBInfo.ro with their solutions. The bot can scrape problem statements, examples, and find corresponding source code solutions from GitHub repositories or online tutorials.

## Features

- 🔍 **Problem Fetching**: Retrieve programming problems from PBInfo.ro by problem code
- 📝 **Rich Embeds**: Display problems with formatted descriptions, examples, and constraints
- 💻 **Source Code Integration**: Automatically find and display solutions from:
  - Personal GitHub repository
  - Rezolvari-PBInfo tutorials
- 🗄️ **Database Storage**: SQLite database for caching GitHub file information
- 🎵 **Voice Features**: Connect to voice channels and play audio

## Project Structure

```
├── run.py                    # Main entry point
├── init_DB.py               # Database initialization
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker configuration
├── bot/
│   ├── config.py           # Configuration and environment variables
│   ├── db.py               # Database connection
│   ├── util.py             # GitHub API utilities
│   ├── bot/
│   │   ├── cavou_bot.py    # Discord bot client setup
│   │   ├── main.py         # Main bot commands
│   │   ├── troll.py        # Voice channel features
│   │   └── util.py         # Discord utilities and embed generation
│   ├── models/
│   │   └── models.py       # Data models (Problem, Source, Example)
│   └── scrape/
│       ├── scrape_PBInfo.py # PBInfo problem scraper
│       └── get_sursa.py    # Source code finder
```

## Commands

- `-problema <problem_code>` - Fetch and display a problem from PBInfo.ro
- `-test` - Test GitHub API connection
- `-refresh` - Refresh the GitHub files database
- `-name` - Display server name and ID
- `-speak` - Connect to voice channel and play audio

## Setup

### Prerequisites

- Python 3.x
- Discord Bot Token
- GitHub Personal Access Token (for source code fetching)

### Environment Variables

Set the following environment variables:

```bash
export username_github="your-github-username"
export token_github="your-github-token"
export base_dir_github="https://api.github.com/repos/your-username/your-repo/contents"
export token_bot="your-discord-bot-token"
```

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize the database:
   ```bash
   python init_DB.py
   ```
4. Run the bot:
   ```bash
   python run.py
   ```

### Docker Deployment

Build and run using Docker:

```bash
docker build -t pbinfo-discord-bot .
docker run pbinfo-discord-bot
```

## Dependencies

Key dependencies include:
- `discord.py` - Discord API wrapper
- `requests` - HTTP requests
- `beautifulsoup4` - Web scraping
- `markdownify` - HTML to Markdown conversion
- `sqlite3` - Database operations

## How It Works

1. **Problem Fetching**: When a user runs `-problema <code>`, the bot:
   - Scrapes the problem page from PBInfo.ro
   - Extracts problem statement, examples, and constraints
   - Creates a [`Problema_PBInfo`](bot/models/models.py) object

2. **Source Code Finding**: The bot attempts to find solutions by:
   - Searching the GitHub repository database for matching files
   - Falling back to scraping from Rezolvari-PBInfo tutorials

3. **Display**: Problems are displayed using Discord embeds with:
   - Formatted problem statement
   - Input/output specifications
   - Examples with explanations
   - Source code solutions (if found)

## Models

The bot uses several data models defined in [`bot/models/models.py`](bot/models/models.py):

- **`Problema_PBInfo`**: Represents a complete programming problem
- **`Source`**: Represents source code with language and author info
- **`Exemplu`**: Represents problem examples with optional explanations

## Contributing

Feel free to contribute by:
- Adding new scraping sources
- Improving error handling
- Adding new Discord commands
- Enhancing the problem display format

## License

This project is for educational purposes. Please respect PBInfo.ro's terms of service when scraping their content.
