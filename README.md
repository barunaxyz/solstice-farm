# ðŸŒ¾ Solstice Farm

> A mini Harvest Moon-style farming game set on the longest day of the year.

Built for the [June Solstice Game Jam](https://dev.to/challenges/june-game-jam-2026-06-03) on DEV Community.

---

## ðŸŽ® About the Game

It's the **Summer Solstice** â€” the longest day of the year. You've inherited an old farm from your grandfather, and you have one extraordinary, sun-drenched day to bring it back to life.

Plant seeds, till the soil, water your crops, and harvest them before the solstice sun sets. Sell your harvest at the shop to buy better seeds. Every second of sunlight counts â€” crops grow fastest at midday when the sun is at its peak!

---

## âœ¨ Features

- ðŸ§‘â€ðŸŒ¾ **Top-down player character** â€” Walk around your farm with WASD/Arrow keys
- ðŸ—ºï¸ **Tile-based world** â€” Explore your farm, the shop, and the water well
- ðŸŒ± **Full farming cycle** â€” Till â†’ Water â†’ Plant â†’ Grow â†’ Harvest
- ðŸŒ» **5 crop types** â€” Lettuce, Tomato, Corn, Sunflower, Strawberry
- â˜€ï¸ **Solstice sun mechanic** â€” Crops grow faster during peak sunlight hours
- ðŸ’° **Economy system** â€” Sell crops and buy seeds at the shop
- ðŸŒ¤ï¸ **Dynamic sky cycle** â€” Sunrise â†’ Midday â†’ Golden Hour â†’ Sunset
- âœ¨ **Particle effects** â€” Water splash, harvest sparkle, dirt puff
- ðŸŽ¨ **Retro 16-bit pixel art** â€” All sprites generated procedurally via code
- ðŸ† **Score & rating system** â€” How much can you earn in one solstice day?

---

## ðŸ› ï¸ Tech Stack

- **Python 3.x**
- **Pygame**

---

## ðŸš€ Getting Started

### Prerequisites

```bash
pip install pygame
```

### Run the Game

```bash
python main.py
```

---

## ðŸ•¹ï¸ Controls

| Action | Key |
|---|---|
| Move | WASD or Arrow Keys |
| Use Tool | Space |
| Select Hoe | 1 |
| Select Water Can | 2 |
| Select Seeds | 3 |
| Select Harvest | 4 |
| Change Seed Type | Q / E |
| Open Shop | Space or Tab while facing shop |
| Close Shop | Escape |

---

## ðŸŒ± How to Play

1. **Till the soil** â€” Select the Hoe (1) and press Space facing a dirt tile
2. **Water the soil** â€” Select the Water Can (2) and press Space
3. **Plant seeds** â€” Select Seeds (3), choose type with Q/E, press Space on watered soil
4. **Wait for growth** â€” Crops grow in real-time, faster during midday!
5. **Water again** â€” Some crops need multiple waterings during growth
6. **Harvest** â€” Select Hands (4) and press Space on a fully grown crop
7. **Sell at shop** - Face the shop, press Space or Tab, then sell your harvest for gold
8. **Buy more seeds** â€” Use gold to buy seeds for more valuable crops
9. **Refill water** â€” Visit the well to refill your watering can

---

## ðŸŒ» Crops

| Crop | Grow Time | Sell Price | Seed Cost | Waters |
|---|---|---|---|---|
| ðŸ¥¬ Lettuce | 40s | 15g | 5g | 1 |
| ðŸ… Tomato | 70s | 35g | 12g | 2 |
| ðŸŒ½ Corn | 100s | 60g | 20g | 2 |
| ðŸ“ Strawberry | 90s | 80g | 25g | 2 |
| ðŸŒ» Sunflower | 120s | 100g | 35g | 3 |

---

## ðŸ“ Project Structure

```
solstice-farm/
â”œâ”€â”€ main.py           # Entry point
â”œâ”€â”€ settings.py       # Global constants & config
â”œâ”€â”€ game.py           # Central game state & scenes
â”œâ”€â”€ world.py          # Tile map & rendering
â”œâ”€â”€ player.py         # Player movement & tools
â”œâ”€â”€ farming.py        # Crop growth system
â”œâ”€â”€ inventory.py      # Inventory & economy
â”œâ”€â”€ shop.py           # Shop UI overlay
â”œâ”€â”€ hud.py            # Heads-up display
â”œâ”€â”€ sky.py            # Day/night sky cycle
â”œâ”€â”€ camera.py         # 2D camera follow
â”œâ”€â”€ sprites.py        # Procedural pixel art
â”œâ”€â”€ particles.py      # Visual effects
â”œâ”€â”€ menu.py           # Title & game over screens
â””â”€â”€ README.md
```

---

## ðŸŒ Theme Connection

The game is directly inspired by the **June Solstice** â€” the moment when the sun reaches its highest point and the day is at its longest. The core mechanic revolves around this: **crops grow faster when the sun is at its peak**, creating a natural rhythm of urgency and reward tied to the solstice day cycle.

---

## ðŸ‘¥ Team / Developers

1. **Baruna**
2. **Bastian Heskia Silaban**

Made for the DEV June Solstice Game Jam 2026.

---

## ðŸ“„ License

MIT License â€” feel free to fork and build on this!

