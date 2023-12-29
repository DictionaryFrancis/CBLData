from lxml import html
from selenium import webdriver
import time
from reportlab.pdfgen import canvas
import subprocess

teams_in_the_league = {
    1:'helio',
    2:'longboats',
    3:'scs-crookstown-united-fc',
    4:'obs-fc',
    5:'vip-barbers',
    6:'marlboro-trust',
    7:'suro-cars',
    8:'co-council',
    9:'fishermans-rest-valley-rangers'
}

team_name = int(input("Insert the number:\n"
                      "1 - Helio\n"
                      "2 - LongBoats\n"
                      "3 - Crookstown\n"
                      "4 - OBS\n"
                      "5 - VIP Barbers Carrigaline\n"
                      "6 - Malboro Trust\n"
                      "7 - Suro Cars\n"
                      "8 - Cork County Council\n"
                      "9 - Fishermans Rest Valley\n"
                      ">>> "))

url = ''

if team_name in teams_in_the_league:
    url += f'https://corkbusinessleague.ie/team/{teams_in_the_league[team_name]}/results/'



driver = webdriver.Chrome()
driver.get(url)

time.sleep(1)

page_source = driver.page_source

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
    c.drawString(10, 10, "Welcome to it!")
    lines = [
        f"{team_home}   {match_home} X  {team_visitor}   {match_visitor}"
            for match_home, match_visitor, team_home, team_visitor in zip(array_match_home, array_match_visitor, array_team_home, array_team_visitor)
    ]
    y = 750

    for line in lines:
        c.drawString(100, y, line)

        y -= 20
    # c.showPage()
    c.save()


pdf_file = f"{team_name}.pdf"

create_pdf(pdf_file)
print(f'pdf created {pdf_file}!')
