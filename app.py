from flask import Flask, render_template, request
import datetime


# Function to generate HTML code for the dropdown with date options
def generate_date_dropdown():
    dropdown_html = '<select name="date">'

    # Generate date options for the next 30 days
    today = datetime.date.today()
    for i in range(30):
        date = today + datetime.timedelta(days=i)
        date_str = date.strftime('%Y-%m-%d')
        dropdown_html += f'<option value="{date_str}">{date_str}</option>'

    dropdown_html += '</select>'

    return dropdown_html


dropdown_code = generate_date_dropdown()
print(dropdown_code)

app = Flask(__name__)

dropdown_options = {
    'COUNTRY':[['Part of', 'P36'],
                ['image', 'P18'],
                ['Date', '#datepicker'],
                ['official name', 'P1448'],
                ['native label', 'P1705'],
                ['shortname', 'P1813'],
                ['pronunciation audio', 'P443'],
                ['ethnic group', 'P172'],
                ['religion or worldview' , 'P140'],
                ['IPA transcription' , 'P898'],
                ['participant in' ,'P1344'],
                ['life expectancy','P2250'],
                ['named after','P138'],
                ['demonym','P1549'],
                ['official language','P37']
               ],
    'TAXON': [['subclass of','P279'],
              ['image','P18'],
              ['video','P10'],
              ['pronunciation audio','P443'],
              ['mass,P2067'],
              ['taxon name','P225'],
              ['taxon rank','P105'],
              ['parent taxon','P171'],
              ['taxon common name','P1843'],
              ['original combination','P1403'],
              ['longest observed lifespan','P4214'],
              ['gestation period','P3063'],
              ['bite force quotient','P3485'],
              ['IUCN conservation status','P141'],
              ['audio','P51']],
    '3DFILM': [['part of','P361:'],
               ['logo image','154'],
               ['image','P18'],
               ['title','P1476'],
               ['named after','P138'],
               ['derivative work','P4969'],
               ['part of the series','P179'],
               ['main subject','P921'],
               ['followed by','P156'],
               ['genre','P136'],
               ['performer','P175'],
               ['country of origin','P495'],
               ['original language of film or TV show','P364'],
               ['publication date','P577'],
               ['director','P57']],
    'FILM' :[['image','P18'],
             ['vide','P10'],
             ['title','P1476'],
             ['publication date','P577'],
             ['original language of film','P364'],
             ['genre','P136'],
             ['director','P57'],
             ['cast member','P161'],
             ['director of photography','P344'],
             ['screen writer','P58'],
             ['producer','P162'],
             ['film editor','P1040'],
             ['narrative location','P840'],
             ['filming location','P915'],
             ['country of rigin','P495']],
    'CITY' :[['subclass of','P279'],
              ['image','P18'],
              ['short name','P1813'],
              ['next lower rank','P3729'],
              ['studied by','P2579'],
              ['nighttime view','P3451'],
              ['icon','P2910'],
              ['geography of topic ','P2633'],
              ['history of topic','P2184'],
              ['inception','P571'],
              ['official name','P1448'],
              ['native label','P1705'],
              ['nickname','P1449'],
              ['IPA transcription','P898'],
              ['named after','P138']]
}


@app.route('/', methods=['GET', 'POST'])
def index():
    selected_option = None
    contents = None
    if request.method == 'POST':
        selected_option = request.form.get('selected_option')
        if selected_option in dropdown_options:
            contents = dropdown_options[selected_option]

    return render_template('index.html', options=dropdown_options.keys(), selected_option=selected_option, contents=contents)

if __name__ == '__main__':
    app.run(debug=True)
