# -*- coding: utf-8 -*-
"""Download images and extract product cards from gvozditut.ru brand pages."""
import html as html_lib
import json
import re
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent / "assets" / "web"
OUT.mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}


def get(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def abs_url(src: str) -> str:
    if src.startswith("//"):
        return "https:" + src
    if src.startswith("/"):
        return "https://gvozditut.ru" + src
    return src


def download(url: str, dest: Path) -> bool:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        if len(data) < 800:
            return False
        dest.write_bytes(data)
        return True
    except Exception as e:
        print("fail", url, e)
        return False


PAGES = {
    "mika": "https://gvozditut.ru/brands/mika/",
    "torra": "https://gvozditut.ru/brands/torra/",
    "inall": "https://gvozditut.ru/brands/inall/",
    "stm": "https://gvozditut.ru/brands/stm/",
    "nashi": "https://gvozditut.ru/catalog/nashi-tovary/",
}

summary = {}
for key, url in PAGES.items():
    html = get(url)
    # collect image urls
    html = html_lib.unescape(html)
    imgs = re.findall(r'(?:src|data-src|data-original)=["\']([^"\']+)["\']', html, flags=re.I)
    imgs += re.findall(r'url\(([^)]+)\)', html)
    clean = []
    for i in imgs:
        i = html_lib.unescape(i).strip().strip("\"'")
        if not i or i.startswith("data:"):
            continue
        if any(x in i.lower() for x in [".svg", "sprite", "icon", "logo-footer", "favicon"]):
            continue
        if any(x in i.lower() for x in [".jpg", ".jpeg", ".png", ".webp", "resize", "upload", "storage", "media", "iblock"]):
            clean.append(abs_url(i))
    # unique preserve order
    seen = set()
    uniq = []
    for i in clean:
        if i not in seen:
            seen.add(i)
            uniq.append(i)
    folder = OUT / key
    folder.mkdir(exist_ok=True)
    saved = []
    for n, img_url in enumerate(uniq[:18], 1):
        ext = ".jpg"
        low = img_url.lower()
        if ".png" in low:
            ext = ".png"
        elif ".webp" in low:
            ext = ".webp"
        dest = folder / f"{n:02d}{ext}"
        if download(img_url, dest):
            saved.append(dest.name)
            print("ok", key, dest.name, dest.stat().st_size)
    # crude product names
    names = re.findall(r"(?:MIKA|Torra|TORRA|INALL|Inall|СТМ|CTM)[^<]{5,90}", html)
    names = [re.sub(r"\s+", " ", n).strip() for n in names]
    summary[key] = {"url": url, "images": saved, "names": names[:30]}

(OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print("done", {k: len(v["images"]) for k, v in summary.items()})
