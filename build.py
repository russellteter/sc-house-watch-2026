import re, pathlib
here = pathlib.Path(__file__).parent
svg = (here / "house-districts.svg").read_text()
svg = re.sub(r"<\?xml[^>]*\?>\s*", "", svg)
html = (here / "template.html").read_text().replace("<!--SVG-->", svg)
(here / "index.html").write_text(html)
print("index.html", len(html))
