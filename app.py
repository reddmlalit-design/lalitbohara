from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# डेटाबेस की जगह एक छोटा स्टोर
url_database = {}
url_counter = 1

HTML_TEMPLATE = '''
<html>
<head>
    <title>Lalit Gaming Tools & URL Shortener</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="background-color: #111; color: #fff; text-align: center; font-family: Arial; padding: 20px;">
    
    <h1 style="color: #ff4500; font-size: 32px; margin-bottom: 5px;">LALIT GAMING TOOLS</h1>
    <p style="color: #00ff00; margin-top: 0; font-weight: bold;">[ प्रो-गेमिंग टूल्स और यूआरएल शॉर्टनर ]</p>
    <hr style="width: 80%; border-color: #ff4500; margin-bottom: 30px;">

    <!-- टूल 1: यूआरएल शॉर्टनर -->
    <div style="background: #222; border: 1px solid #ff4500; padding: 20px; border-radius: 10px; max-width: 400px; margin: 0 auto 30px auto;">
        <h3 style="color: #ff4500; margin-top: 0;">🔗 VIP URL Shortener</h3>
        <p style="color: #ccc; font-size: 14px;">अपने बड़े गेमिंग या यूट्यूब लिंक्स को यहाँ छोटा करें:</p>
        <form method="POST" action="/shorten">
            <input type="url" name="long_url" placeholder="https://example.com" required 
                   style="width: 80%; padding: 10px; border-radius: 5px; border: none; margin-bottom: 10px;"><br>
            <button type="submit" style="background: #ff4500; color: #fff; border: none; padding: 10px 20px; border-radius: 5px; font-weight: bold; cursor: pointer;">लिंक छोटा करें</button>
        </form>
        {% if short_url %}
            <div style="margin-top: 15px; background: #333; padding: 10px; border-radius: 5px;">
                <p style="margin: 0; color: #00ff00;">आपका छोटा लिंक तैयार है:</p>
                <a href="{{ short_url }}" target="_blank" style="color: #ff4500; font-weight: bold;">{{ short_url }}</a>
            </div>
        {% endif %}
    </div>

    <!-- टूल 2: फ्री फायर डायमंड/XP कैलकुलेटर -->
    <div style="background: #222; border: 1px solid #00ff00; padding: 20px; border-radius: 10px; max-width: 400px; margin: 0 auto;">
        <h3 style="color: #00ff00; margin-top: 0;">🎮 FF Level Up Calculator</h3>
        <p style="color: #ccc; font-size: 14px;">अगले लेवल पर जाने के लिए ज़रूरी मैच का हिसाब लगाएं:</p>
        <input type="number" id="current_lvl" placeholder="वर्तमान लेवल (उदा. 50)" style="width: 80%; padding: 10px; border-radius: 5px; border: none; margin-bottom: 10px;"><br>
        <button onclick="calculateLevel()" style="background: #00ff00; color: #000; border: none; padding: 10px 20px; border-radius: 5px; font-weight: bold; cursor: pointer;">हिसाब लगाएं</button>
        <p id="calc_result" style="margin-top: 15px; color: #ff4500; font-weight: bold;"></p>
    </div>

    <script>
    function calculateLevel() {
        var lvl = document.getElementById('current_lvl').value;
        if(lvl) {
            var matches = (parseInt(lvl) * 12);
            document.getElementById('calc_result').innerText = "आपको अगले लेवल के लिए लगभग " + matches + " फुल मैच खेलने होंगे!";
        } else {
            document.getElementById('calc_result').innerText = "कृपया अपना लेवल दर्ज करें।";
        }
    }
    </script>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_TEMPLATE, short_url=None)

@app.route('/shorten', methods=['POST'])
def shorten():
    global url_counter
    long_url = request.form['long_url']
    short_id = str(url_counter)
    url_database[short_id] = long_url
    url_counter += 1
    # लोकल होस्ट के हिसाब से लिंक बनाना
    full_short_url = f"http://{request.host}/{short_id}"
    return render_template_string(HTML_TEMPLATE, short_url=full_short_url)

@app.route('/<short_id>')
def redirect_to_url(short_id):
    long_url = url_database.get(short_id)
    if long_url:
        return redirect(long_url)
    return "<h1>लिंक नहीं मिला!</h1>", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
