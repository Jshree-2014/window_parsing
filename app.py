from flask import Flask

app = Flask(__name__)

# Define the YouTube live stream iframe code


youtube_embed_code = """
<iframe width="930" height="523" src="https://aplus-evolution.systems88.com/frontend/evo/r2/#category=baccarat&game=baccarat&table_id=p63cmvmwagteemoy&lobby_launch_id=cfacb89210144c32a137e483321cad6a" 
title="Aaj Tak LIVE TV: Delhi Air Pollution | Assembly Election 2023 | CM Nitish | Shopian Encounter News" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
allowfullscreen>
</iframe>"""

youtube_embed_code1 = """
<iframe width="930" height="523" src="https://aplus-evolution.systems88.com/frontend/evo/r2/#category=baccarat&game=baccarat&table_id=onokyd4wn7uekbjx&lobby_launch_id=8ce45ceeff2c4161823bf1ad89f4fdb8" 
title="Aaj Tak LIVE TV: Delhi Air Pollution | Assembly Election 2023 | CM Nitish | Shopian Encounter News" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
allowfullscreen>
</iframe>"""

youtube_embed_code2 = """
<iframe width="930" height="523" src="https://aplus-evolution.systems88.com/frontend/evo/r2/#category=baccarat&game=baccarat&table_id=qgdk6rtpw6hax4fe&lobby_launch_id=d94916babb5b4c3c8e5f85067348ce81" 
title="Aaj Tak LIVE TV: Delhi Air Pollution | Assembly Election 2023 | CM Nitish | Shopian Encounter News" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
allowfullscreen>
</iframe>"""


@app.route('/')
def home():
    # Include the YouTube iframe code within your HTML content
    return f"""
    <html>
    <head>
        <title>Simple One-Page Website</title>
        <style>
            /* Define a class to add margin between iframes */
            .iframe-container {{
                margin-bottom: 20px; /* Adjust the value to create desired space */
            }}
        </style>
    </head>
    <body>
        <h1>Welcome to My One-Page Website</h1>
        <p>This is a simple one-page website created using Python and Flask.</p>

        <!-- Embed the YouTube live stream video -->
        <div class="iframe-container">
            {youtube_embed_code}
        </div>
        <div class="iframe-container">
            {youtube_embed_code1}
        </div>
        <div class="iframe-container">
            {youtube_embed_code2}
        </div>

    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)
