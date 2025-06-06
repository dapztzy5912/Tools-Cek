#!/usr/bin/env python3
import requests
import os
import time
import sys
import threading
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

class ModernUI:
    def __init__(self):
        self.width = 60
        self.colors = {
            'primary': Fore.CYAN + Style.BRIGHT,
            'secondary': Fore.MAGENTA + Style.BRIGHT,
            'success': Fore.GREEN + Style.BRIGHT,
            'error': Fore.RED + Style.BRIGHT,
            'warning': Fore.YELLOW + Style.BRIGHT,
            'info': Fore.BLUE + Style.BRIGHT,
            'text': Fore.WHITE + Style.BRIGHT,
            'dim': Fore.WHITE + Style.DIM,
            'accent': Fore.LIGHTCYAN_EX + Style.BRIGHT
        }
    
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def center_text(self, text, width=None):
        if width is None:
            width = self.width
        return text.center(width)
    
    def gradient_line(self, char='─', length=60):
        colors = [Fore.BLUE, Fore.CYAN, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.LIGHTCYAN_EX, Fore.CYAN, Fore.BLUE]
        line = ""
        for i in range(length):
            color_index = int((i / length) * (len(colors) - 1))
            line += colors[color_index] + char
        return line + Style.RESET_ALL
    
    def loading_animation(self, text="Loading", duration=2):
        chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        end_time = time.time() + duration
        while time.time() < end_time:
            for char in chars:
                sys.stdout.write(f'\r{self.colors["primary"]}{char} {text}...')
                sys.stdout.flush()
                time.sleep(0.1)
        sys.stdout.write('\r' + ' ' * 20 + '\r')
    
    def premium_box(self, content, title="", box_type="default"):
        box_chars = {
            'premium': ['╔', '╗', '╚', '╝', '═', '║'],
            'modern': ['┌', '┐', '└', '┘', '─', '│'],
            'rounded': ['╭', '╮', '╰', '╯', '─', '│'],
            'double': ['╔', '╗', '╚', '╝', '═', '║']
        }
        
        chars = box_chars.get(box_type, box_chars['premium'])
        top_left, top_right, bottom_left, bottom_right, horizontal, vertical = chars
        
        lines = content.strip().split('\n')
        max_width = max(len(line) for line in lines) if lines else 0
        box_width = max(max_width + 4, len(title) + 4, 40)
        
        result = []
        
        # Top border with title
        if title:
            title_padded = f" {title} "
            title_pos = (box_width - len(title_padded)) // 2
            top_line = (self.colors['primary'] + top_left + 
                       horizontal * title_pos + 
                       self.colors['accent'] + title_padded + 
                       self.colors['primary'] + horizontal * (box_width - title_pos - len(title_padded) - 1) + 
                       top_right)
        else:
            top_line = self.colors['primary'] + top_left + horizontal * (box_width - 2) + top_right
        
        result.append(top_line)
        
        # Content lines
        for line in lines:
            padded_line = f" {line.ljust(box_width - 3)} "
            result.append(self.colors['primary'] + vertical + 
                         self.colors['text'] + padded_line + 
                         self.colors['primary'] + vertical)
        
        # Bottom border
        result.append(self.colors['primary'] + bottom_left + horizontal * (box_width - 2) + bottom_right)
        
        return '\n'.join(result)

class WeatherChecker:
    def __init__(self, ui):
        self.ui = ui
    
    def check_weather(self):
        self.ui.clear_screen()
        
        # Header
        print(self.ui.gradient_line('═', 80))
        print(self.ui.colors['primary'] + self.ui.center_text("🌤️  WEATHER CHECKER  ⛅", 80))
        print(self.ui.gradient_line('═', 80))
        print()
        
        # Input box
        city_prompt = self.ui.premium_box(
            "Enter city name below:",
            "📍 Location Input",
            "rounded"
        )
        print(city_prompt)
        print()
        
        city = input(self.ui.colors['accent'] + "🏙️  City: " + self.ui.colors['text'])
        
        if not city.strip():
            print(self.ui.colors['error'] + "❌ City name cannot be empty!")
            self.wait_for_enter()
            return
        
        print()
        self.ui.loading_animation("Fetching weather data", 2)
        
        try:
            url = f"https://wttr.in/{city}?format=j1"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                current = data['current_condition'][0]
                
                weather_info = f"""
🌡️  Temperature: {current['temp_C']}°C ({current['temp_F']}°F)
💨 Wind: {current['windspeedKmph']} km/h {current['winddir16Point']}
💧 Humidity: {current['humidity']}%
☁️  Condition: {current['weatherDesc'][0]['value']}
👁️  Visibility: {current['visibility']} km
📊 Pressure: {current['pressure']} mb
                """.strip()
                
                result_box = self.ui.premium_box(
                    weather_info,
                    f"🌍 Weather in {city.title()}",
                    "premium"
                )
                print(result_box)
                
            else:
                error_box = self.ui.premium_box(
                    "❌ City not found or service unavailable\n🔄 Please check the city name and try again",
                    "⚠️ Error",
                    "modern"
                )
                print(self.ui.colors['error'] + error_box)
                
        except requests.exceptions.RequestException:
            error_box = self.ui.premium_box(
                "🌐 Network connection error\n📡 Please check your internet connection",
                "🚫 Connection Error",
                "modern"
            )
            print(self.ui.colors['error'] + error_box)
        except Exception as e:
            error_box = self.ui.premium_box(
                f"💥 Unexpected error occurred\n🔧 Error details: {str(e)}",
                "❌ System Error",
                "modern"
            )
            print(self.ui.colors['error'] + error_box)
        
        self.wait_for_enter()
    
    def wait_for_enter(self):
        print()
        input(self.ui.colors['dim'] + "Press Enter to continue..." + self.ui.colors['text'])

class UsernameChecker:
    def __init__(self, ui):
        self.ui = ui
        self.platforms = {
            "GitHub": {
                "url": "https://github.com/{}",
                "icon": "🐙",
                "color": self.ui.colors['info']
            },
            "Instagram": {
                "url": "https://www.instagram.com/{}/",
                "icon": "📸",
                "color": self.ui.colors['secondary']
            },
            "TikTok": {
                "url": "https://www.tiktok.com/@{}",
                "icon": "🎵",
                "color": self.ui.colors['primary']
            }
        }
    
    def check_username(self):
        self.ui.clear_screen()
        
        # Header
        print(self.ui.gradient_line('═', 80))
        print(self.ui.colors['secondary'] + self.ui.center_text("👤 USERNAME AVAILABILITY CHECKER 🔍", 80))
        print(self.ui.gradient_line('═', 80))
        print()
        
        # Input
        username_prompt = self.ui.premium_box(
            "Enter the username you want to check:",
            "📝 Username Input",
            "rounded"
        )
        print(username_prompt)
        print()
        
        username = input(self.ui.colors['accent'] + "👤 Username: " + self.ui.colors['text'])
        
        if not username.strip():
            print(self.ui.colors['error'] + "❌ Username cannot be empty!")
            self.wait_for_enter()
            return
        
        print()
        self.ui.loading_animation("Checking username availability", 3)
        
        results = []
        for platform, config in self.platforms.items():
            try:
                url = config['url'].format(username)
                response = requests.get(url, timeout=5)
                
                if response.status_code == 200:
                    status = "❌ TAKEN"
                    color = self.ui.colors['error']
                elif response.status_code == 404:
                    status = "✅ AVAILABLE"
                    color = self.ui.colors['success']
                else:
                    status = "⚠️ UNKNOWN"
                    color = self.ui.colors['warning']
                
                results.append(f"{config['icon']} {platform:<12} {color}{status}")
                
            except:
                results.append(f"{config['icon']} {platform:<12} {self.ui.colors['warning']}🔌 CONNECTION ERROR")
        
        # Display results
        result_content = "\n".join(results)
        result_box = self.ui.premium_box(
            result_content,
            f"🎯 Results for '@{username}'",
            "premium"
        )
        print(result_box)
        
        self.wait_for_enter()
    
    def wait_for_enter(self):
        print()
        input(self.ui.colors['dim'] + "Press Enter to continue..." + self.ui.colors['text'])

class OwnerInfo:
    def __init__(self, ui):
        self.ui = ui
    
    def show_info(self):
        self.ui.clear_screen()
        
        # Animated header
        print(self.ui.gradient_line('═', 80))
        print(self.ui.colors['secondary'] + self.ui.center_text("👨‍💻 DEVELOPER INFORMATION 🚀", 80))
        print(self.ui.gradient_line('═', 80))
        print()
        
        # Profile card
        profile_info = f"""
🏷️  Name     : XdpzQ
🌍 Location : Surabaya, East Java
💼 Status   : Wa😂
🎯 Passion  : Creating awesome tools
⚡ Skills   : Python, Shell Scripting, CLI Tools
🌟 Mission  : Making tech accessible for everyone

🔗 GitHub   : github.com/dapztzy5912
📧 Contact  : Available on GitHub
🎨 Style    : Modern & Premium interfaces
        """.strip()
        
        profile_box = self.ui.premium_box(
            profile_info,
            "👤 Developer Profile",
            "premium"
        )
        print(profile_box)
        
        print()
        
        # Thank you message
        thanks_msg = self.ui.premium_box(
            "Thank you for using this premium CLI tool!\n🙏 Your support motivates continuous development",
            "💝 Appreciation",
            "rounded"
        )
        print(self.ui.colors['success'] + thanks_msg)
        
        print()
        input(self.ui.colors['dim'] + "Press Enter to return to main menu..." + self.ui.colors['text'])

class PremiumMultiTool:
    def __init__(self):
        self.ui = ModernUI()
        self.weather = WeatherChecker(self.ui)
        self.username = UsernameChecker(self.ui)
        self.owner = OwnerInfo(self.ui)
    
    def animated_banner(self):
        banner_art = """
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
        """
        
        lines = banner_art.strip().split('\n')
        colors = [self.ui.colors['primary'], self.ui.colors['secondary'], self.ui.colors['accent']]
        
        for i, line in enumerate(lines):
            color = colors[i % len(colors)]
            print(color + line)
            time.sleep(0.05)
    
    def show_menu(self):
        print()
        print(self.ui.gradient_line('─', 80))
        print()
        
        menu_items = [
            ("1", "🌤️", "Weather Checker", "Check real-time weather for any city"),
            ("2", "👤", "Username Checker", "Verify username availability on social platforms"),
            ("3", "👨‍💻", "Developer Info", "About the creator of this tool"),
            ("4", "🚪", "Exit", "Leave the application")
        ]
        
        for num, icon, title, desc in menu_items:
            print(f"  {self.ui.colors['accent']}[{num}] {icon} {self.ui.colors['text']}{title:<18} {self.ui.colors['dim']}• {desc}")
        
        print()
        print(self.ui.gradient_line('─', 80))
    
    def get_user_choice(self):
        print()
        choice = input(self.ui.colors['primary'] + "🎯 Select option (1-4): " + self.ui.colors['text'])
        return choice.strip()
    
    def run(self):
        while True:
            self.ui.clear_screen()
            self.animated_banner()
            self.show_menu()
            
            choice = self.get_user_choice()
            
            if choice == '1':
                self.weather.check_weather()
            elif choice == '2':
                self.username.check_username()
            elif choice == '3':
                self.owner.show_info()
            elif choice == '4':
                self.ui.clear_screen()
                
                # Goodbye animation
                goodbye_box = self.ui.premium_box(
                    "Thank you for using Premium Multi Tools! 🚀\n✨ Made with ❤️ by XdpzQ ✨\n🌟 See you next time! 🌟",
                    "👋 Goodbye",
                    "premium"
                )
                print(self.ui.colors['success'] + goodbye_box)
                
                print()
                self.ui.loading_animation("Shutting down", 2)
                print(self.ui.colors['primary'] + "\n🎉 Application closed successfully!")
                break
            else:
                print(self.ui.colors['error'] + "\n❌ Invalid option! Please select 1-4.")
                time.sleep(1.5)

def main():
    try:
        app = PremiumMultiTool()
        app.run()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\n⚠️ Application interrupted by user.")
        print(Fore.CYAN + "👋 Thanks for using Premium Multi Tools!")
    except Exception as e:
        print(Fore.RED + f"\n💥 An unexpected error occurred: {str(e)}")
        print(Fore.YELLOW + "🔧 Please report this issue to the developer.")

if __name__ == "__main__":
    main()
