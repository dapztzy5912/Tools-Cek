#!/bin/bash

# Premium Multi Tools Installer v2.0
# Created by XdpzQ

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
BOLD='\033[1m'
DIM='\033[2m'
NC='\033[0m' # No Color

# Animation function
loading_animation() {
    local duration=$1
    local text=$2
    local chars="⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    local end=$((SECONDS + duration))
    
    while [ $SECONDS -lt $end ]; do
        for (( i=0; i<${#chars}; i++ )); do
            printf "\r${CYAN}${chars:$i:1} ${text}...${NC}"
            sleep 0.1
        done
    done
    printf "\r${GREEN}✅ ${text}... Done!${NC}\n"
}

# Gradient line function
gradient_line() {
    local length=${1:-60}
    local line=""
    local colors=("${BLUE}" "${CYAN}" "${WHITE}" "${CYAN}" "${BLUE}")
    
    for (( i=0; i<length; i++ )); do
        local color_index=$((i * ${#colors[@]} / length))
        line+="${colors[$color_index]}═"
    done
    echo -e "${line}${NC}"
}

# Clear screen
clear

# Premium banner
echo -e "${BOLD}${CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║  ██████╗ ██████╗ ███████╗███╗   ███╗██╗██╗   ██╗███╗   ███╗    ████████╗ ██████╗  ██████╗ ██╗     ║
║  ██╔══██╗██╔══██╗██╔════╝████╗ ████║██║██║   ██║████╗ ████║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ║
║  ██████╔╝██████╔╝█████╗  ██╔████╔██║██║██║   ██║██╔████╔██║       ██║   ██║   ██║██║   ██║██║     ║
║  ██╔═══╝ ██╔══██╗██╔══╝  ██║╚██╔╝██║██║██║   ██║██║╚██╔╝██║       ██║   ██║   ██║██║   ██║██║     ║
║  ██║     ██║  ██║███████╗██║ ╚═╝ ██║██║╚██████╔╝██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝███████╗║
║  ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝ ╚═════╝ ╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝║
║                                                                               ║
║                           🚀 INSTALLER v2.0 - PREMIUM EDITION 🚀              ║
║                                  Made by XdpzQ                                ║
╚═══════════════════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

gradient_line 80
echo

# Welcome message
echo -e "${BOLD}${WHITE}Welcome to Premium Multi Tools Installer!${NC}"
echo -e "${DIM}This installer will set up all required dependencies and launch the application.${NC}"
echo

gradient_line 80
echo

# Check if running on Termux
if [[ -n "$PREFIX" ]] && [[ "$PREFIX" == *"com.termux"* ]]; then
    echo -e "${GREEN}🤖 Termux environment detected!${NC}"
    PACKAGE_MANAGER="pkg"
    PYTHON_CMD="python"
else
    echo -e "${YELLOW}🐧 Standard Linux environment detected${NC}"
    if command -v apt &> /dev/null; then
        PACKAGE_MANAGER="apt"
        PYTHON_CMD="python3"
    elif command -v yum &> /dev/null; then
        PACKAGE_MANAGER="yum"
        PYTHON_CMD="python3"
    elif command -v pacman &> /dev/null; then
        PACKAGE_MANAGER="pacman"
        PYTHON_CMD="python3"
    else
        echo -e "${RED}❌ Unsupported package manager${NC}"
        exit 1
    fi
fi

echo

# Installation steps
echo -e "${BOLD}${BLUE}📦 Starting installation process...${NC}"
echo

# Step 1: Update package list
echo -e "${CYAN}Step 1/4: Updating package list${NC}"
loading_animation 2 "Updating repositories"

if [[ "$PACKAGE_MANAGER" == "pkg" ]]; then
    pkg update -y &> /dev/null
elif [[ "$PACKAGE_MANAGER" == "apt" ]]; then
    sudo apt update -y &> /dev/null
fi

# Step 2: Install Python
echo -e "${CYAN}Step 2/4: Installing Python${NC}"
if command -v python3 &> /dev/null || command -v python &> /dev/null; then
    echo -e "${GREEN}✅ Python is already installed${NC}"
else
    loading_animation 3 "Installing Python"
    if [[ "$PACKAGE_MANAGER" == "pkg" ]]; then
        pkg install python -y &> /dev/null
    elif [[ "$PACKAGE_MANAGER" == "apt" ]]; then
        sudo apt install python3 python3-pip -y &> /dev/null
    fi
fi

# Step 3: Install pip packages
echo -e "${CYAN}Step 3/4: Installing Python dependencies${NC}"
loading_animation 3 "Installing required packages"

# Install packages
if [[ "$PYTHON_CMD" == "python" ]]; then
    pip install requests colorama &> /dev/null
else
    pip3 install requests colorama &> /dev/null
fi

# Step 4: Verify installation
echo -e "${CYAN}Step 4/4: Verifying installation${NC}"
loading_animation 2 "Running system checks"

# Check if all dependencies are available
python_check=$($PYTHON_CMD -c "import requests, colorama; print('OK')" 2>/dev/null)
if [[ "$python_check" == "OK" ]]; then
    echo -e "${GREEN}✅ All dependencies verified successfully!${NC}"
else
    echo -e "${RED}❌ Dependency verification failed${NC}"
    echo -e "${YELLOW}⚠️  Please check your Python installation${NC}"
    exit 1
fi

echo

# Success message
gradient_line 80
echo -e "${BOLD}${GREEN}"
cat << "EOF"
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║    ✅ INSTALLATION COMPLETED SUCCESSFULLY! ✅         ║
║                                                       ║
║    🎉 Premium Multi Tools is ready to use!           ║
║    🚀 All dependencies have been installed            ║
║    💎 Premium features are now available              ║
║                                                       ║
║    📝 Features included:                              ║
║    • 🌤️ Advanced Weather Checker                      ║
║    • 👤 Social Media Username Checker                 ║
║    • 💻 Premium UI with animations                     ║
║    • 🎨 Modern gradient design                         ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

gradient_line 80
echo

# Launch prompt
echo -e "${BOLD}${WHITE}🚀 Ready to launch Premium Multi Tools?${NC}"
echo -e "${DIM}Press Enter to start the application or Ctrl+C to exit...${NC}"
read -r

echo
echo -e "${PURPLE}🎬 Launching Premium Multi Tools...${NC}"
loading_animation 2 "Starting application"

echo
gradient_line 80

# Launch the application
if [[ -f "tools.py" ]]; then
    $PYTHON_CMD tools.py
else
    echo -e "${RED}❌ tools.py not found in current directory${NC}"
    echo -e "${YELLOW}💡 Please make sure you're in the correct directory${NC}"
    exit 1
fi

# Goodbye message
echo
echo -e "${BOLD}${CYAN}Thank you for using Premium Multi Tools!${NC}"
echo -e "${DIM}Created with ❤️ by XdpzQ${NC}"
gradient_line 80
