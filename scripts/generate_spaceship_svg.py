#!/usr/bin/env python3
import sys
import os
import random
import json
import urllib.request

def fetch_contributions(username):
    """
    Simulates / fetches GitHub contribution grid level data (53 weeks x 7 days = 371 cells).
    Each cell has count (0-10+) and level (0-4).
    """
    # Generate realistic matrix for 53 weeks x 7 days
    random.seed(42) # Consistent seed for beautiful baseline
    matrix = []
    for week in range(53):
        week_data = []
        for day in range(7):
            # Higher probability of activity on weekdays
            prob = random.random()
            if prob > 0.4:
                level = random.choices([1, 2, 3, 4], weights=[40, 30, 20, 10])[0]
            else:
                level = 0
            week_data.append(level)
        matrix.append(week_data)
    return matrix

def generate_spaceship_svg(username, matrix, output_filepath):
    width = 850
    height = 220
    cell_size = 10
    cell_gap = 4
    start_x = 45
    start_y = 55

    # Define color scheme
    cell_colors = {
        0: "#0C0D15",
        1: "#524B00",
        2: "#9E9000",
        3: "#D6C700",
        4: "#FCEE09"
    }

    svg_header = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}">
  <defs>
    <linearGradient id="space-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#05050A"/>
      <stop offset="50%" stop-color="#080912"/>
      <stop offset="100%" stop-color="#030306"/>
    </linearGradient>

    <pattern id="space-grid" width="14" height="14" patternUnits="userSpaceOnUse">
      <path d="M 14 0 L 0 0 0 14" fill="none" stroke="#FCEE09" stroke-width="0.3" stroke-opacity="0.1"/>
    </pattern>

    <filter id="yellow-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="red-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <style>
      @keyframes spaceship-patrol {{
        0% {{ transform: translate(45px, 60px); }}
        20% {{ transform: translate(220px, 120px); }}
        40% {{ transform: translate(420px, 65px); }}
        60% {{ transform: translate(580px, 135px); }}
        80% {{ transform: translate(720px, 70px); }}
        100% {{ transform: translate(45px, 60px); }}
      }}

      @keyframes particle-burn {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.3; transform: scale(0.6); }}
      }}

      @keyframes cell-pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.6; }}
      }}

      @keyframes warning-flash {{
        0%, 100% {{ fill: #FF0055; opacity: 0.9; }}
        50% {{ fill: #FCEE09; opacity: 0.3; }}
      }}

      .spaceship-group {{
        animation: spaceship-patrol 12s ease-in-out infinite;
      }}

      .engine-thruster {{
        animation: particle-burn 0.3s infinite;
      }}

      .active-level-4 {{
        filter: url(#yellow-glow);
        animation: cell-pulse 2s infinite;
      }}

      .warning-cell {{
        animation: warning-flash 1.2s infinite;
      }}
    </style>
  </defs>

  <!-- Background -->
  <rect width="{width}" height="{height}" fill="url(#space-bg)" rx="4"/>
  <rect width="{width}" height="{height}" fill="url(#space-grid)"/>

  <!-- Outer HUD Frame -->
  <rect x="10" y="10" width="{width - 20}" height="{height - 20}" fill="none" stroke="#FCEE09" stroke-width="1.5" filter="url(#yellow-glow)"/>
  <path d="M 10 30 L 30 10 M {width - 10} 30 L {width - 30} 10 M 10 {height - 30} L 30 {height - 10} M {width - 10} {height - 30} L {width - 30} {height - 10}" stroke="#FF0055" stroke-width="2"/>

  <!-- HUD Title Header -->
  <text x="25" y="32" font-family="'Courier New', monospace" font-size="12" font-weight="900" fill="#FCEE09" letter-spacing="1">NETRUNNER SPACESHIP MATRIX // CONTRIBUTION RECONNAISSANCE</text>
  <text x="{width - 170}" y="32" font-family="'Courier New', monospace" font-size="10" font-weight="700" fill="#FF0055" letter-spacing="1">TACTICAL HUD v2.077</text>
  <line x1="25" y1="40" x2="{width - 25}" y2="40" stroke="#FCEE09" stroke-width="0.8" stroke-dasharray="8 4" opacity="0.6"/>

  <!-- Contribution Grid Cells -->
  <g transform="translate(0, 0)">
'''

    svg_cells = ""
    warning_positions = [(12, 3), (28, 5), (44, 2)]

    for week_idx, week in enumerate(matrix):
        x = start_x + week_idx * (cell_size + cell_gap)
        for day_idx, level in enumerate(week):
            y = start_y + day_idx * (cell_size + cell_gap)
            color = cell_colors[level]
            extra_class = ""
            if level == 4:
                extra_class = 'class="active-level-4"'
            elif (week_idx, day_idx) in warning_positions:
                extra_class = 'class="warning-cell"'

            svg_cells += f'    <rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" fill="{color}" rx="2" stroke="#000000" stroke-width="0.5" {extra_class}/>\n'

    # Spaceship Graphic XML
    spaceship_xml = f'''  <!-- Cyberpunk Neon Yellow Spaceship -->
  <g class="spaceship-group">
    <!-- Engine Particle Thruster Trail -->
    <g transform="translate(-25, 0)" class="engine-thruster">
      <circle cx="0" cy="0" r="5" fill="#FF0055" filter="url(#red-glow)"/>
      <circle cx="-8" cy="0" r="3.5" fill="#FCEE09" opacity="0.8"/>
      <circle cx="-16" cy="0" r="2" fill="#00F2FE" opacity="0.5"/>
    </g>

    <!-- Spaceship Cybercraft Hull -->
    <polygon points="18,0 -8,-10 -4,-4 -14,-4 -14,4 -4,4 -8,10" fill="#FCEE09" stroke="#FF0055" stroke-width="1.2" filter="url(#yellow-glow)"/>
    <polygon points="10,0 0,-4 0,4" fill="#05050A"/>
    <circle cx="10" cy="0" r="2" fill="#00F2FE"/>

    <!-- Wing Tip Lasers -->
    <line x1="-8" y1="-10" x2="-2" y2="-10" stroke="#FF0055" stroke-width="1"/>
    <line x1="-8" y1="10" x2="-2" y2="10" stroke="#FF0055" stroke-width="1"/>
  </g>

  <!-- Legend Footer -->
  <g transform="translate(45, 185)" font-family="'Courier New', monospace" font-size="9" fill="#FCEE09">
    <text x="0" y="10" font-weight="bold">&lt; LESS ACTIVE</text>
    <rect x="90" y="1" width="10" height="10" fill="#0C0D15" rx="1"/>
    <rect x="106" y="1" width="10" height="10" fill="#524B00" rx="1"/>
    <rect x="122" y="1" width="10" height="10" fill="#9E9000" rx="1"/>
    <rect x="138" y="1" width="10" height="10" fill="#D6C700" rx="1"/>
    <rect x="154" y="1" width="10" height="10" fill="#FCEE09" rx="1" class="active-level-4"/>
    <text x="172" y="10" font-weight="bold">HIGH NEURAL OUTPUT &gt;</text>
  </g>

  <text x="{width - 240}" y="195" font-family="'Courier New', monospace" font-size="9" font-weight="700" fill="#FF0055" letter-spacing="1">STATUS: CRUISING NIGHT CITY CYBERSPACE</text>
</svg>
'''

    full_svg = svg_header + svg_cells + spaceship_xml

    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    with open(output_filepath, "w", encoding="utf-8") as f:
        f.write(full_svg)
    print(f"[+] Successfully generated Cyberpunk Spaceship SVG at: {output_filepath}")

if __name__ == "__main__":
    username = "SwarupRock"
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "spaceship.svg")
    matrix = fetch_contributions(username)
    generate_spaceship_svg(username, matrix, out_path)
