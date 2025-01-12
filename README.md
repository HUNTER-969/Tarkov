twitch nightbot  

用 Tarkov.json  
!editcom !123 \\$(eval const api = $(urlfetch json https://raw.githubusercontent.com/HUNTER-969/Tarkov/refs/heads/main/Tarkov.json); const responses = api.responses; responses[Math.floor(Math.random() * responses.length)])  

用 Tarkov2.json  
!addcom !123 $(eval const api = $(urlfetch json https://raw.githubusercontent.com/HUNTER-969/Tarkov/refs/heads/main/Tarkov2.json); api["故事" + (Math.floor(Math.random() * 7) + 1)])
