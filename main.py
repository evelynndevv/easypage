from flask import Flask, render_template

app = Flask(__name__)

# SWITCHES
discordSwitch = True
twitterSwitch = True

# switch specific details
discordID = "1248689798445666416"
twitterProfile= "iHave40KilosOfKetamine"

# details
name = "meow"
background = "#282828"
foreground = "#ebdbb2"
font = "Comic Sans MS"
title = "testing"
pfp = "pfp.png"

@app.route('/')
def home():
    return render_template('index.html',
                           bg=background,
                           t=title,
                           fg=foreground,
                           font=font,
                           name=name,
                           image_filename=pfp,
                           discord="https://discord.com/users/" + discordID,
                           discordSwitch=discordSwitch,
                           twitter=twitterProfile,
                           twitterSwitch=twitterSwitch)

if __name__ == '__main__':
    app.run(debug=True)
