#!/bin/bash
# Installer untuk Multi Tools by XdpzQ

echo "Installing dependencies..."
pkg install python -y
pip install requests colorama

echo "Menjalankan tools.py..."
python tools.py
