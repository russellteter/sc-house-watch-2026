import re, json, pathlib
here = pathlib.Path(__file__).parent
svg = re.sub(r"<\?xml[^>]*\?>\s*", "", (here / "house-districts.svg").read_text())
house = json.loads((here / "house.json").read_text())
prec = json.loads((here / "precincts.json").read_text())
assert len(prec) == 46, len(prec)
assert len(house) == 124, len(house)
html = (here / "app.html").read_text()
assert "<!--SVG-->" in html and "/*HOUSE*/[]" in html and "/*PRECINCTS*/{}" in html
html = html.replace("<!--SVG-->", svg).replace("/*HOUSE*/[]", json.dumps(house, separators=(",", ":"))).replace("/*PRECINCTS*/{}", json.dumps(prec, separators=(",", ":")))
(here / "index.html").write_text(html)
print("index.html", len(html))
