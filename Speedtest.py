import flet as ft
import speedtest 
from time import sleep
 
def main(page:ft.Page):
    #set page
    page.title = 'SPEEDTEST.me'
    page.theme_mode='light'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_bgcolor = 'blue'
    page.padding = 40
    page.bgcolor = '#121213'
    

    #enable scroll
    page.auto_scroll = True

    #configure fonts
    page.fonts = {
        'anydore' : 'fonts/Anydore.otf',
        'creattion' : 'fonts/Creattion.otf',
        'SPACE MISSION' : 'fonts/SPACE MISSION.otf'  ,
        'pricedown'   :'fonts/pricedown bl.otf'   ,
        'zekton': 'fonts/zekton rg.otf'
    }

    #initialize speedtest variable
    st = speedtest.Speedtest()

    #individual components
    appTitle = ft.Row(
        controls=[
            ft.Text(value='Speedtest',font_family='pricedown', style='displayLarge', color='red',),
            ft.Text(value='.me',font_family='anydore', style='displaylarge', color='#0080ff'),
        ], alignment='center'
    )

   
    #printing Text
    
    line1 = ft.Text(">press start...", font_family='consolas', color = 'white')
    line2 = ft.Text("", font_family='consolas-bold', color = '#1aff1a')
    line3 = ft.Text("", font_family='consolas', color = '#1aff1a')
    progressBar1 = ft.ProgressBar(width = 400, color='#0080ff', bgcolor = '#eeeeee',opacity = 0)
    progressText1 = ft.Text("  ",font_family='consolas',opacity = 0)
    progressRow1= ft.Row(controls=[progressText1,progressBar1])
    line4 = ft.Text("", font_family='consolas', color = 'Yellow')
    line5 = ft.Text("", font_family='consolas', color = '#1aff1a')
    line6 = ft.Text("", font_family='consolas', color = '#1aff1a')
    progressBar2 = ft.ProgressBar(width = 400, color='#0080ff', bgcolor = '#eeeeee',opacity = 0)
    progressText2 = ft.Text("  ",font_family='consolas',opacity = 0)
    progressRow2= ft.Row(controls=[progressText2,progressBar2])
    line7 = ft.Text("", font_family='consolas', color = 'yellow')
    line8 = ft.Text("", font_family='consolas', color = 'white')
    
    terminalText = ft.Column(controls=[line1,line2,line3,progressRow1,line4,line5,line6,progressRow2,line7,line8])

    speedContainer = ft.Container (
            content=terminalText,
            width=200,
            height = 100,
            bgcolor = 'black',
            

            border_radius= 40,
            padding = 40,
            animate=ft.animation.Animation(1000,"bounceOut")
    )


 

    def animateSpeedContainer(e): 
        progressRow1.opacity = 0
        progressBar1.opacity = 0
        progressBar1.value = None
        progressRow2.opacity = 0
        progressBar2.opacity = 0
        progressBar2.value = None
        line1.value = ""
        line2.value = ""
        line3.value = ""
        line4.value = ""
        line5.value = ""
        line6.value = ""
        line7.value = ""
        line8.value = ""


        speedContainer.update() 
        
        speedContainer.width = 800
        speedContainer.height = 400
        
        line1.value = '> Calculating Download speed, please wait...'  
        speedContainer.update()
        sleep(1)
        #perform download speed calculation
        idealServer = st.get_best_server() #gives best possible server in region
        city = idealServer['name']
        country = idealServer['country']
        countryCode = idealServer['cc']
        line2.value = f'> Finding best possible servers in {city}, {country} {countryCode}...'
        speedContainer.update() 
        sleep(2)
        line3.value='> Connection established, status OK, fetching download speed...'
        progressRow1.opacity = 1
        progressBar1.opacity = 1
        speedContainer.update() 

        downloadSpeed = st.download() / (2**20)
        progressBar1.value = 1

        line4.value = f'> The download speed is {str(round(downloadSpeed,2))} Mb/S'
        speedContainer.update() 

        line5.value='> Status OK, calculating upload speed, please wait...'
        line6.value ='> Fetching upload speed, please wait...'
        progressRow2.opacity = 1
        progressBar2.opacity = 1
        speedContainer.update()
        uploadSpeed = st.upload()/ (2**20)
        progressBar2.value = 1
        line7.value = f'> The upload speed is {str(round(uploadSpeed,2))} Mb/S'
        speedContainer.update() 
        sleep(1)

        line8.value = "> Task completed successfully\n\n App Developed By: Tanishq Jujgar"
        speedContainer.update() 

        






    #page components
    page.add(
        appTitle,
        speedContainer,
        ft.IconButton(icon= ft.icons.PLAY_CIRCLE_FILL_SHARP,icon_color="blue", icon_size = 40, on_click=animateSpeedContainer),
    )



ft.app(target = main,assets_dir='assets')
