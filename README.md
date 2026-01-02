# ♟️ Grandmaster Chess Suite - Premium Edition

A premium, feature-rich chess game built with pure HTML, CSS, and JavaScript. Experience the royal game with stunning visuals, advanced AI, and professional-grade features.

![Chess Master](https://img.shields.io/badge/Chess-Master-gold) ![Version](https://img.shields.io/badge/version-2.0-blue) ![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

### 🎮 Core Gameplay
- **Full Chess Rules Implementation**
  - Castling (Kingside & Queenside)
  - En Passant capture
  - Pawn promotion with piece selection
  - Check, Checkmate, and Stalemate detection
  - 50-move rule enforcement

### 🤖 AI Opponent
- **5 Difficulty Levels**: Beginner to Grandmaster
- Advanced minimax algorithm with alpha-beta pruning
- Adjustable AI strength for all skill levels

### ⏱️ Game Features
- **Game Timers**: 5, 10, 15, 30 minutes, or unlimited
- **Move History**: Full game history with undo/redo functionality
- **PGN Export**: Export games in standard PGN format
- **Move Hints**: Get suggestions for your next move
- **Evaluation Bar**: Visual position evaluation
- **Game Statistics**: Track moves and captures

### 🎨 Premium UI/UX
- **4 Beautiful Themes**: Onyx, Ivory, Sapphire, Ruby
- **Coordinate Labels**: Optional file/rank indicators
- **Move Assist Mode**: Visual indicators for legal moves
- **Sound Effects**: Immersive audio feedback
- **Responsive Design**: Works on desktop and mobile
- **Smooth Animations**: Polished visual transitions

### 📊 Advanced Features
- **Algebraic Notation**: Professional move notation
- **Clickable Move History**: Navigate through game history
- **Visual Highlights**: Last move, check, and selection indicators
- **Premium Glassmorphism Design**: Modern, elegant interface

## 🚀 Getting Started

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/chess-master.git
   cd chess-master
   ```

2. **Open in browser**
   - Simply open `chess.html` in your web browser
   - No build process or dependencies required!

### Usage

1. **Start a Game**
   - Click "Start Match" from the main menu
   - White pieces move first (you play as White)

2. **Make Moves**
   - Click on a piece to select it
   - Click on a highlighted square to move
   - Legal moves are shown when a piece is selected

3. **Settings**
   - Adjust AI difficulty level
   - Enable/disable timers
   - Change board theme
   - Toggle sound effects and move assist

4. **Game Controls**
   - **⌂** - Return to main menu
   - **↻** - Reset game
   - **⚙** - Open settings
   - **⮐** - Undo move
   - **⮒** - Redo move
   - **📄** - Export PGN

## 🎯 Game Rules

### Special Moves

**Castling**
- Move your king two squares toward a rook
- The rook moves to the square the king crossed
- Available when: king and rook haven't moved, no pieces between, king not in check

**En Passant**
- Capture a pawn that just moved two squares
- Must be done immediately after the two-square move

**Pawn Promotion**
- When a pawn reaches the 8th rank, choose: Queen, Rook, Bishop, or Knight

## 🛠️ Technical Details

### Technologies
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with CSS variables, animations, and glassmorphism
- **Vanilla JavaScript**: No frameworks or dependencies
- **Web Audio API**: Sound generation

### Browser Compatibility
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

### File Structure
```
chess-master/
├── chess.html          # Main game file
├── cover.avif          # Menu background image
├── server.py           # Optional Python server
├── README.md           # This file
├── LICENSE             # MIT License
└── .gitignore         # Git ignore rules
```

## 🎨 Customization

### Themes
The game includes 4 premium themes. To add your own:

1. Add a new theme class in the CSS:
```css
body.theme-yourname {
    --board-light: #color1;
    --board-dark: #color2;
    --highlight: rgba(r, g, b, a);
    --check-pulse: rgba(r, g, b, a);
    --bg-overlay: linear-gradient(...);
}
```

2. Add option to theme selector in settings modal

### AI Difficulty
Adjust AI strength by modifying the `aiDifficulty` value in settings or directly in code.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Support

If you encounter any issues or have suggestions, please open an issue on GitHub.

## 🙏 Acknowledgments

- Chess piece symbols: Unicode chess symbols
- Design inspiration: Modern chess applications
- Sound effects: Web Audio API synthesis

## 📈 Roadmap

- [ ] Online multiplayer support
- [ ] Opening book database
- [ ] Endgame tablebase integration
- [ ] Tournament mode
- [ ] Puzzle mode
- [ ] Analysis engine integration
- [ ] Mobile app version

---

**Made with ♟️ and ❤️**

Enjoy your games of chess!
