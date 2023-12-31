from lxml import html
from selenium import webdriver
import time
from reportlab.pdfgen import canvas
from datetime import date
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import letter
from PIL import Image

pdf_name = str(input('Insert the title for the PDF file: '))

teams_in_the_league = {
    1: 'helio',
    2: 'longboats',
    3: 'scs-crookstown-united-fc',
    4: 'obs-fc',
    5: 'vip-barbers',
    6: 'marlboro-trust',
    7: 'suro-cars',
    8: 'co-council',
    9: 'fishermans-rest-valley-rangers'
}

team_name = int(input("Insert the number:\n"
                      "1 - Helio Inter Cork\n"
                      "2 - LongBoats\n"
                      "3 - SCS Crookstown Utd\n"
                      "4 - OBS\n"
                      "5 - VIP Barbers Carrigaline Town\n"
                      "6 - Malboro Trust\n"
                      "7 - Suro Cars\n"
                      "8 - Cork County Council\n"
                      "9 - Fisherman's Rest Valley Rangers\n"
                      ">>> "))

url = ''
url_table = ''

if team_name in teams_in_the_league:
    url += f'https://corkbusinessleague.ie/team/{teams_in_the_league[team_name]}/results/'
    url_table += f'https://corkbusinessleague.ie/team/{teams_in_the_league[team_name]}/'

# Open first Window
driver = webdriver.Chrome()


####
# Team table position
# Open Second Window
driver.get(url_table)
time.sleep(1)

page_source = driver.page_source
table_info = html.fromstring(page_source)


array_club_name = []
array_club_position = []
array_club_matches = []
array_club_win = []
array_club_draw = []
array_club_loss = []

# pegando posicao
target_club_name = {
    1: 'Helio Inter Cork',
    2: 'Longboats',
    3: 'SCS Crookstown Utd',
    4: 'OBS',
    5: 'VIP Barbers Carrigaline Town',
    6: 'Marlboro Trust',
    7: 'Suro Cars',
    8: 'Cork County Council',
    9: "Fisherman’s Rest Valley Rangers"
}

target_club_key = target_club_name.get(team_name)
print(target_club_key)

# Number of rows in the table
num_rows = len(table_info.xpath('//*[@id="DataTables_Table_0"]/tbody/tr'))

# Iterate through each row in the table
for i in range(1, num_rows + 1):
    # Construct XPath expressions for each piece of information
    xpath_club_name = f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td[2]/a/text()'
    xpath_club_position = f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td[1]/text()'
    xpath_club_matches = f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td[3]/text()'
    xpath_club_win = f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td[4]/text()'
    xpath_club_draw = f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td[5]/text()'
    xpath_club_loss = f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td[6]/text()'
    # ... Add XPath expressions for other pieces of information

     # Collect data for each club
    club_name = [result.strip("['']") for result in table_info.xpath(xpath_club_name)]
    club_position = [result.strip("['']") for result in table_info.xpath(xpath_club_position)]
    club_matches = [result.strip("['']") for result in table_info.xpath(xpath_club_matches)]
    club_win = [result.strip("['']") for result in table_info.xpath(xpath_club_win)]
    club_draw = [result.strip("['']") for result in table_info.xpath(xpath_club_draw)]
    club_loss = [result.strip("['']") for result in table_info.xpath(xpath_club_loss)]
    # ... Collect other pieces of information

    # Append collected data to the arrays
    array_club_name.extend(club_name)
    array_club_position.extend(club_position)
    array_club_matches.extend(club_matches)
    array_club_win.extend(club_win)
    array_club_draw.extend(club_draw)
    array_club_loss.extend(club_loss)
    # ... Append other pieces of information to their respective arrays

# Print the collected data (for verification)
for name, position, matches, win, draw, loss in zip(array_club_name, array_club_position, array_club_matches,array_club_win,array_club_draw,array_club_loss):
    # print(f"Club: {name}, Position: {position}, Matches : {matches}, Win : {win}, Draw : {draw}, Loss : {loss}")

    if name == target_club_key:
         print(f'{name},{position},{matches},{win}')

####


driver.get(url)
time.sleep(1)

page_source = driver.page_source
# page_took_table = driver.page_source

driver.quit()

# webbrowser.open('https://corkbusinessleague.ie/team/helio/results/')
tree = html.fromstring(page_source)

match_home = ''
match_visitor = ''
team_home = ''
team_visitor = ''
test = []
array_match_home = []
array_match_visitor = []
array_team_home = []
array_team_visitor = []
x = 0

##

for i in range(1, 6):
    # test = tree.xpath('/html/body/div[3]/div[3]/div/div/div/h1/text()')
    match_home = tree.xpath(f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td/div/div/div[3]/a/span[{1}]/text()')
    match_visitor = tree.xpath(f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td/div/div/div[3]/a/span[3]/text()')
    team_home = tree.xpath(f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td/div/div/div[1]/div/h5/text()')
    team_visitor = tree.xpath(f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td/div/div/div[2]/div/h5/text()')
#################

    array_match_home.append(match_home[x].strip("['\n']"))
    array_match_visitor.append(match_visitor[x].strip("['\n']"))
    array_team_home.append(team_home[x].strip("['']"))
    array_team_visitor.append(team_visitor[x].strip("['']"))

# Create PDF
#####
#print(team_home[0].strip("['']"))
def create_pdf(file_path):
    c = canvas.Canvas(file_path)

    image_path = "Helio-picture.png"  # Replace with the actual path to your image
    x_position = 255
    y_position = 655
    image_width = 100
    image_height = 100
    c.drawImage(image_path,x_position,y_position,width=image_width,height=image_height)
    c.drawString(105, 600, f"LAST 5 RESULTS : {target_club_key}")
    c.drawString(95, 595, "_______________________________________________________________")

    # Create a table style
    style = [
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]

    data = [['', 'HOME', '', 'VISITOR']]


    for match_home, match_visitor, team_home, team_visitor in zip(array_match_home, array_match_visitor, array_team_home, array_team_visitor):
        data.append([match_home,team_home, match_visitor, team_visitor])

    # Create the table
    table = Table(data, colWidths=[20, 200, 20, 200])

    # Apply the table style
    table.setStyle(TableStyle(style))

    # Draw the table on the canvas
    table.wrapOn(c, 85, 350)
    table.drawOn(c, 85, 450)

    # SECOND TABLE
     # Create a table style
    style = [
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]

    data_position = [['TEAM NAME', 'POSITION', 'MATCHES', 'WON', 'DRAWN', 'LOST']]



    for name, position, matches, win, draw, loss in zip(array_club_name, array_club_position, array_club_matches,array_club_win,array_club_draw,array_club_loss):
        if name == target_club_key:
             data_position.append([name,position,matches,win,draw,loss])

    # Create the table
    table_position = Table(data_position, colWidths=[150, 80, 80, 40, 70, 40])

    # Apply the table style
    table_position.setStyle(TableStyle(style))

    # Draw the table on the canvas
    table_position.wrapOn(c, 75, 450)
    table_position.drawOn(c, 75, 350)

    c.save()


pdf_file = f"{pdf_name}--{date.today()}.pdf"

create_pdf(pdf_file)
print(f'pdf created {pdf_file}!')
