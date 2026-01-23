def generate_html(spec: dict) -> str:
    components = spec.get("components", {})
    html_parts = []

    # HERO
    hero = components.get("Hero")
    if hero:
        html_parts.append(f"""
        <section>
            <h1>{hero.get('headline', 'Welcome')}</h1>
            <p>{hero.get('subtext', '')}</p>
        </section>
        """)

    # CONTACT
    contact = components.get("Contact")
    if contact:
        html_parts.append("""
        <section>
            <h2>Contact Me</h2>
            <form>
                <input placeholder="Email"><br><br>
                <textarea placeholder="Message"></textarea><br><br>
                <button>Send</button>
            </form>
        </section>
        """)

    # FALLBACK
    if not html_parts:
        html_parts.append("<h1>Website Generated</h1>")

    return "\n".join(html_parts)


# Contrast colour for background and foreground:
def generate_css(theme: str) -> str:
    bg = "#111" if theme == "dark" else "#ffffff"
    fg = "#ffffff" if theme == "dark" else "#000000"
    
    # Body, Navigation bar, Hero section, Button: 
    return f"""
body {{
  margin: 0;
  font-family: Arial, sans-serif;
  background: {bg};
  color: {fg};
}}

.navbar {{
  padding: 16px;
  background: #333;
  color: white;
}}

.hero {{
  padding: 80px;
  text-align: center;
}}

button {{
  padding: 12px 24px;
  border: none;
  cursor: pointer;
}}
"""
