# League of Legends Mock Match MCP

🎮 **AI-powered League of Legends mock match simulator and summoner comparison tool**

This Model Context Protocol (MCP) server provides comprehensive League of Legends summoner analysis and mock match simulations based on historical performance data from the last 10 games.

## Features

- **🔍 Summoner Analysis**: Get detailed statistics including KDA, damage dealt, and win rates
- **⚔️ Mock Match Simulation**: AI-powered 10-phase match progression simulation
- **🌍 Multi-language Support**: Available in 7 languages
- **📊 Performance Comparison**: Side-by-side summoner comparisons
- **🎯 Match Prediction**: Outcome prediction based on historical data

## Supported Languages

- English (EN/ENGLISH)
- Korean (한국어)
- Traditional Chinese (繁體中文)
- Japanese (日本語)
- Spanish (ESPAÑOL)
- Bengali (বাংলা)
- Punjabi (ਪੰਜਾਬੀ)

## Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/onepersonunicorn/lolgpt.git
   cd lolgpt
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (optional):
   ```bash
   export LOL_API_URL="https://1tier.xyz"
   export LOL_DEFAULT_LANGUAGE="EN"
   export LOL_API_TIMEOUT="30"
   ```

4. **Run the server**:
   ```bash
   python main.py
   ```

## Usage

### Available Tools

The MCP server provides 6 different tools for various League of Legends simulation needs:

#### 1. `league_of_legends_summoner_vs_match`
Main tool for comprehensive match simulation.

**Parameters:**
- `uidA` (required): Riot ID of first summoner
- `tagA` (required): Tag of first summoner  
- `uidB` (required): Riot ID of second summoner
- `tagB` (required): Tag of second summoner
- `lang` (optional): Language for simulation (default: "EN")

#### 2. `lol_summoner_mock_battle`
Simplified battle simulation interface.

#### 3. `league_summoner_comparison`
Compare two summoners with detailed analysis.

#### 4. `summoners_rift_simulation`
Focused on Summoner's Rift match simulation.

#### 5. `lol_player_vs_player_match`
PvP-focused match simulation.

#### 6. `league_match_predictor`
Match outcome prediction tool.

### Example Usage

```python
# Example API call
await league_of_legends_summoner_vs_match(
    uidA="Hide on bush",
    tagA="KR1", 
    uidB="Zeus",
    tagB="KR1",
    lang="EN"
)
```

### Sample Output

```
🎮 **League of Legends Mock Match Simulation**
════════════════════════════════════════════

📊 Summoner A (PlayerOne#KR1) - Last 10 Games Statistics:
• Average Kills: 8.2
• Average Assists: 12.5
• Average Deaths: 4.1
• Average KDA: 5.05
• Average Damage Dealt: 28,450
• Win Rate: 70%

📊 Summoner B (PlayerTwo#NA1) - Last 10 Games Statistics:
• Average Kills: 6.8
• Average Assists: 9.2
• Average Deaths: 5.3
• Average KDA: 3.02
• Average Damage Dealt: 22,100
• Win Rate: 55%

🎯 Mock Match Simulation - Summoner's Rift:
════════════════════════════════════════════

Phase 1: Welcome to the Snowdown Showdown.
Phase 2: Thirty seconds until minions spawn.
Phase 3: Minions have spawned!
Phase 4: First blood! Zeus has been slain.
Phase 5: Hide on bush has slain an enemy!
Phase 6: Hide on bush has destroyed a turret.
Phase 7: Zeus Quadrakill!
Phase 8: Hide on bush is legendary!
Phase 9: Hide on bush has destroyed a inhibitor.
Phase 9: Hide on bush victory!

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `LOL_API_URL` | Base URL for League of Legends API | `https://1tier.xyz` |
| `LOL_DEFAULT_LANGUAGE` | Default language for simulations | `EN` |
| `LOL_API_TIMEOUT` | API request timeout in seconds | `30` |

### Smithery Configuration

The server supports Smithery configuration via `smithery.yaml`:

```yaml
startCommand:
  type: stdio
  configSchema:
    properties:
      debug:
        type: boolean
        default: false
      apiUrl:
        type: string
        default: "https://1tier.xyz"
      language:
        type: string
        default: "EN"
      timeout:
        type: number
        default: 30
```

## API Integration

The server integrates with the 1tier.xyz API endpoint which provides:

- **Summoner Statistics**: Last 10 games performance data
- **Match Simulation**: AI-generated match progression
- **Multi-language Support**: Localized simulation text
- **Real-time Data**: Current summoner performance metrics

## Error Handling

The server includes comprehensive error handling for:

- **Network Issues**: Connection timeouts and API failures
- **Invalid Parameters**: Missing or incorrect summoner IDs/tags
- **API Rate Limits**: Graceful handling of rate limit responses
- **Data Parsing**: JSON parsing and validation errors

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

League of Legends mock match simulations are for entertainment purposes only. Results are based on historical performance data and do not guarantee actual match outcomes. League of Legends is a trademark of Riot Games, Inc.

## Support

For issues and questions:
- Create an issue on GitHub
- Contact the development team

## Acknowledgments

- **Riot Games** for League of Legends
- **1tier.xyz** for providing the API infrastructure
- **MCP Community** for the Model Context Protocol framework

---

Made with ❤️ for the League of Legends community