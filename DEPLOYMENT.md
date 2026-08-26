# ⚡ CYBERPUNK 2077 NETRUNNER GITHUB PROFILE // DEPLOYMENT GUIDE

Welcome to **Swarup D's (@SwarupRock)** Cyberpunk 2077 Netrunner GitHub Profile repository setup guide.

---

## 📁 REPOSITORY FOLDER STRUCTURE

```text
SwarupRock/
├── .github/
│   └── workflows/
│       └── spaceship.yml              # GitHub Action for automated Spaceship graph generation
├── assets/
│   ├── header_banner.svg              # Arasaka Netrunner Animated HUD Banner
│   ├── terminal_status.svg            # System Status Diagnostics Panel
│   ├── skyline_footer.svg             # Night City Animated Skyline Footer with AV Flying Vehicles
│   └── spaceship.svg                  # Neon Yellow Spaceship Contribution Graph SVG
├── scripts/
│   └── generate_spaceship_svg.py      # Python script generating spaceship matrix SVG
├── DEPLOYMENT.md                      # Deployment & documentation guide
└── README.md                          # Cyberpunk 2077 Netrunner Profile Page
```

---

## 🚀 AUTOMATED GITHUB MCP DEPLOYMENT

The files in this repository are deployed directly to your GitHub profile repository: `https://github.com/SwarupRock/SwarupRock` using the connected **GitHub MCP Server**.

### How the Components Work:

1. **Header Banner (`assets/header_banner.svg`)**:
   - Styled with pure SVG CSS keyframe glitch animations, scanning line lasers, and Arasaka clearance metrics.

2. **System Status Panel (`assets/terminal_status.svg`)**:
   - Displays real-time status gauges for CPU, Neural Network, Machine Learning Core, AI Vision Module, and 99.99% system uptime.

3. **Spaceship Contribution Graph (`assets/spaceship.svg`)**:
   - Replaces standard contribution charts with a neon yellow Cyberpunk spacecraft patrolling contribution grid cells.
   - Updated automatically every 24 hours via `.github/workflows/spaceship.yml`.

4. **Night City Animated Footer (`assets/skyline_footer.svg`)**:
   - Features animated flying AV vehicles (Aerodynes) with glowing thrusters over Night City megabuildings and the iconic quote `"SEE YOU IN NIGHT CITY."`.

---

## 🛠️ LOCAL TESTING & RE-GENERATION

To manually regenerate the `spaceship.svg` contribution matrix locally:

```bash
python scripts/generate_spaceship_svg.py
```

This updates `assets/spaceship.svg` with your latest contribution matrix!
