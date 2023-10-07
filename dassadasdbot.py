import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def metodlar(ctx):
    await ctx.send("""Başlıca Geri Dönüşüm Yolları: Kendi Geleceğimizi Şekillendirmek

Günümüz dünyasında, çevremizin ve doğanın kıymetini bilmek, sadece bir seçenek değil, bir zorunluluktur. İşte bu noktada geri dönüşüm, önemli bir rol üstleniyor. Geri dönüşüm, kullanılmış malzemeleri tekrar işleyerek yeni ürünlere dönüştürme işlemidir.

Geri dönüşüm, sadece atıklarımızı azaltmakla kalmaz, aynı zamanda doğal kaynakları korumamıza yardımcı olur. Bu süreç, doğanın bize sunduğu nimetlere saygı göstermenin bir yoludur. Pet şişelerden, kağıt ve karton ürünlere, camdan elektronik ekipmanlara kadar her şeyi geri dönüştürmek mümkündür.

Bu sadece bir çevre meselesi değil, aynı zamanda ekonomik bir faydadır. Geri dönüşüm, yeni ürünlerin üretiminde kullanılan hammaddelerin tükenmesini önler. Bu da ekonomik olarak daha sürdürülebilir bir gelecek anlamına gelir.

Ancak geri dönüşüm sadece maddelerin tekrar kullanılmasıyla sınırlı değildir. İnsanlar için geri dönüşüm, hatalarımızdan ders çıkarmak, geçmişteki kararlarımızı gözden geçirmek ve daha iyi bir gelecek için adımlar atmaktır. Geçmişte yaptığımız hatalardan ders alarak, gelecekte daha bilinçli ve sürdürülebilir kararlar alabiliriz.

Geri dönüşüm, her bireyin ve toplumun sorumluluğudur. Küçük adımlarla büyük değişiklikler başlatılabilir. Atıkların doğru şekilde ayrılması, geri dönüşüm tesislerine teslim edilmesi ve geri dönüştürülebilir malzemelerin yeniden kullanılması, hepimizin yapabileceği önemli adımlardır.

Unutmayalım ki, geri dönüşüm sadece çöplerimizi azaltmakla kalmaz, aynı zamanda daha yaşanabilir bir dünya için atılmış önemli bir adımdır. Bu yolculukta hepimizin katkısı önemlidir. Geleceğimizi şekillendiren kişiler olarak, geri dönüşümün değerini kavramalı ve bu değeri yaşamımızın her alanında yansıtmalıyız.""")


bot.run("TOKEN")
