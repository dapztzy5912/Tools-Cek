# 🚀 Premium Multi Tools - Termux CLI

<div align="center">

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗    ║
║    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║    ║
║    ██╔████╔██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║    ║
║    ██║╚██╔╝██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║    ║
║    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████║
║    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
║                                                                               ║
║                           🚀 PREMIUM EDITION v2.0 🚀                          ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

**✨ A premium CLI toolkit for Termux with modern UI and advanced features ✨**

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python)](https://python.org)
[![Termux Compatible](https://img.shields.io/badge/Termux-Compatible-green?style=for-the-badge&logo=android)](https://termux.com)
[![Premium Edition](https://img.shields.io/badge/Edition-Premium-gold?style=for-the-badge&logo=star)](https://github.com/dapztzy5912/Tools-Cek)

</div>

---

## 🌟 Features Overview

<table>
<tr>
<td width="50%">

### 🌤️ **Advanced Weather Checker**
- Real-time weather data from wttr.in API
- Detailed information including temperature, humidity, wind speed
- Support for cities worldwide
- Premium UI with loading animations
- Error handling with user-friendly messages

</td>
<td width="50%">

### 👤 **Social Media Username Checker**
- Check username availability across multiple platforms:
  - 🐙 **GitHub**
  - 📸 **Instagram** 
  - 🎵 **TikTok**
- Real-time availability status
- Color-coded results with icons
- Fast concurrent checking

</td>
</tr>
<tr>
<td width="50%">

### 💻 **Premium User Interface**
- Modern gradient designs
- Smooth loading animations
- Beautiful ASCII art banners
- Color-coded status messages
- Responsive box layouts
- Professional typography

</td>
<td width="50%">

### 🚀 **Developer Information**
- About the creator
- Contact information
- Development philosophy
- Contribution guidelines
- Support channels

</td>
</tr>
</table>

---

## 🎨 Screenshots

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         🌤️  WEATHER CHECKER  ⛅                              ║
╚═══════════════════════════════════════════════════════════════════════════════╝

╭─────────────────────────────────────────────╮
│                📍 Location Input             │
│                                             │
│ Enter city name below:                      │
╰─────────────────────────────────────────────╯

🏙️  City: Surabaya

⠋ Fetching weather data...

╔═══════════════════════════════════════════════════════════════════════╗
║                     🌍 Weather in Surabaya                           ║
║                                                                       ║
║ 🌡️  Temperature: 28°C (82°F)                                         ║
║ 💨 Wind: 15 km/h E                                                   ║
║ 💧 Humidity: 75%                                                     ║
║ ☁️  Condition: Partly cloudy                                         ║
║ 👁️  Visibility: 10 km                                               ║
║ 📊 Pressure: 1013 mb                                                ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---

## ⚡ Quick Installation

### 🤖 For Termux Users

```bash
# Clone the repository
git clone https://github.com/dapztzy5912/Tools-Cek.git

# Navigate to directory
cd Tools-Cek

# Run the premium installer
bash install.sh
```

### 🐧 For Linux Users

```bash
# Clone the repository
git clone https://github.com/dapztzy5912/Tools-Cek.git

# Navigate to directory
cd Tools-Cek

# Install dependencies
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install requests colorama

# Run the application
python3 tools.py
```

---

## 🔧 Manual Installation

If you prefer to install manually:

### Prerequisites
- Python 3.6 or higher
- Internet connection for API calls

### Dependencies
```bash
pip install requests colorama
```

### Launch
```bash
python tools.py
```

---

## 🎯 Usage Guide

### 1. 🌤️ Weather Checker
- Select option `[1]` from the main menu
- Enter any city name when prompted
- Get detailed weather information instantly
- Supports international cities

### 2. 👤 Username Checker
- Select option `[2]` from the main menu
- Enter the username you want to check
- See availability across GitHub, Instagram, and TikTok
- Results are color-coded for easy reading

### 3. 👨‍💻 Developer Information
- Select option `[3]` to learn about the creator
- Contact information and social links
- Development philosophy and mission

### 4. 🚪 Exit
- Select option `[4]` to safely exit the application
- Animated goodbye message

---

## 🎨 UI Features

### Color Coding
- 🔵 **Blue/Cyan**: Primary interface elements
- 🟢 **Green**: Success messages and available usernames
- 🔴 **Red**: Error messages and taken usernames
- 🟡 **Yellow**: Warning messages and unknown status
- 🟣 **Purple/Magenta**: Secondary highlights
- ⚪ **White**: Text content

### Animations
- ⠋ Loading spinners with multiple frames
- 🎬 Smooth text rendering
- 🌈 Gradient line separators
- ✨ Animated banners

### Box Styles
- **Premium**: Double-line borders with titles
- **Modern**: Single-line clean borders
- **Rounded**: Curved corner aesthetics

---

## 🛠️ Technical Details

### Architecture
```
Premium Multi Tools/
├── tools.py           # Main application with premium UI
├── install.sh         # Automated installer script
├── README.md          # This documentation
└── requirements.txt   # Python dependencies (optional)
```

### Dependencies
- **requests**: HTTP library for API calls
- **colorama**: Cross-platform colored terminal text
- **os**: System operations
- **time**: Time-related functions
- **sys**: System-specific parameters
- **threading**: Concurrent operations

### API Endpoints
- **Weather**: `https://wttr.in/{city}?format=j1`
- **GitHub**: `https://github.com/{username}`
- **Instagram**: `https://www.instagram.com/{username}/`
- **TikTok**: `https://www.tiktok.com/@{username}`

---

## 🔒 Privacy & Security

- **No Data Storage**: No user data is stored locally or remotely
- **HTTPS Only**: All API calls use secure connections
- **No Authentication**: No login or personal information required
- **Open Source**: Full source code available for review

---

## 🐛 Troubleshooting

### Common Issues

**1. Import Error - Module not found**
```bash
# Solution: Install dependencies
pip install requests colorama
```

**2. Connection Error**
```bash
# Check your internet connection
# Some networks may block certain APIs
```

**3. Permission Denied (Linux)**
```bash
# Make installer executable
chmod +x install.sh
```

**4. Python Command Not Found**
```bash
# Try alternative commands
python3 tools.py
# or
python tools.py
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🎯 Ways to Contribute
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 🎨 Improve UI/UX design
- 📚 Enhance documentation
- 🔧 Submit bug fixes
- ⭐ Add new social media platforms

### 📝 Contribution Guidelines
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### 🏆 Contributors
- **XdpzQ** - Creator and lead developer
- **Community** - Ideas and feedback

---

## 📊 Project Stats

- **Language**: Python 3
- **Lines of Code**: ~400+
- **Features**: 4 main functions
- **Platforms Supported**: GitHub, Instagram, TikTok
- **UI Elements**: 20+ visual components
- **API Integrations**: 4 different services

---

## 🎯 Roadmap

### Version 2.1 (Coming Soon)
- [ ] 📱 Twitter/X username checking
- [ ] 🎨 Custom color themes
- [ ] 💾 Configuration file support
- [ ] 📊 Usage statistics

### Version 2.2 (Future)
- [ ] 🌍 Multi-language support
- [ ] 🔄 Auto-update functionality
- [ ] 📧 Email availability checker
- [ ] 🎵 Spotify username checker

### Version 3.0 (Long-term)
- [ ] 🌐 Web interface
- [ ] 📱 Mobile app
- [ ] 🤖 Discord bot integration
- [ ] ☁️ Cloud synchronization

---

## 📞 Support & Contact

### 🆘 Get Help
- **GitHub Issues**: [Report bugs or request features](https://github.com/dapztzy5912/Tools-Cek/issues)
- **Documentation**: Check this README for detailed information
- **Community**: Join discussions in the repository

### 👨‍💻 Developer Contact
- **Name**: XdpzQ
- **Location**: Surabaya, East Java, Indonesia
- **GitHub**: [@dapztzy5912](https://github.com/dapztzy5912)
- **Status**: Wa😂

---

## 📜 License

This project is open source and available under the MIT License.

```
MIT License

Copyright (c) 2024 XdpzQ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

### Special Thanks
- **Termux Community** - For the amazing Android terminal
- **wttr.in** - For the excellent weather API
- **Python Community** - For the powerful programming language
- **Open Source Contributors** - For inspiration and tools

### Libraries Used
- [Requests](https://requests.readthedocs.io/) - HTTP library
- [Colorama](https://pypi.org/project/colorama/) - Terminal colors

---

<div align="center">

### ⭐ Star this repository if you found it helpful!

**Made with ❤️ by XdpzQ in Surabaya, Indonesia**

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║                    🚀 Thank you for using Premium Multi Tools! 🚀             ║
║                                                                               ║
║                          ✨ Keep coding, keep creating! ✨                    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

[⬆️ Back to Top](#-premium-multi-tools---termux-cli)

</div>
