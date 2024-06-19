![Multi_Color_Bar](https://github.com/Walkoud/CS2-Auto-Accept/assets/38588921/3f57ad10-c80c-457a-9f49-679558eb2f79)

# media-downloader-ez
A npm package to download video from url (insta, youtube, tiktok, X...) to discord.


## Exemple for discord js : 
```js
const MediaDownloader = require('media-downloader-ez');



const Discord = require('discord.js-v11-stable');
const client = new Discord.Client({
    disableEveryone: true
  });

client.on('message', async (message) => {
  try {
    if(message.content.startsWith('!download') && message.content.includes('http')){
        let attachment = await MediaDownloader(message.content);
        message.channel.send({ content: `Téléchargé par: \`${message.author.username}\``, files: [attachment] });
    }



  } catch (error) {
    console.error('Erreur lors du téléchargement de la vidéo :', error);
    message.reply('Une erreur est survenue lors du téléchargement de la vidéo.').then((m) => { deleteMessage(m); });
  }
});



client.login("your token").catch((err) => {
    console.log('INCORECT TOKEN LOGIN !')
  })

```

![Multi_Color_Bar](https://github.com/Walkoud/CS2-Auto-Accept/assets/38588921/3f57ad10-c80c-457a-9f49-679558eb2f79)
