import discord , time

async def speak_real(curr_guild):
    most_members_vc = curr_guild.voice_channels[0]
    for vc in curr_guild.voice_channels:
        if len(vc.members) > len(most_members_vc.members):
            most_members_vc = vc
    vc = await most_members_vc.connect()
    vc.play(discord.FFmpegPCMAudio(executable="/usr/bin/ffmpeg" , source=source_name))
    # Sleep while audio is playing.
    while vc.is_playing():
        time.sleep(.1)
    await vc.disconnect()

def generate_embed(problema):
    source_should_be_separate = False
    embed=discord.Embed(title=f"{problema.nume}#{problema.cod}", url=problema.url , description=problema.description , color=0x6394e3)
    embed.add_field(name="Cerinta", value=problema.markdownify(problema.cerinta), inline=False)
    if problema.date_intrare:
        embed.add_field(name="Date de intrare", value=problema.markdownify(problema.date_intrare), inline=False)
    if problema.date_iesire:
        embed.add_field(name="Date de iesire", value=problema.markdownify(problema.date_iesire), inline=False)
    if problema.restrictii:
        embed.add_field(name="Restrictii si precizari", value=problema.markdownify(problema.restrictii), inline=False)
    if problema.important:
        embed.add_field(name="Important", value=problema.markdownify(problema.important), inline=False)
    for index , exemplu in enumerate(problema.exemple):
        embed.add_field(name=f"Exemplul {index+1}", value=exemplu.markdownify_continut(), inline=False)
        if exemplu.explicatie:
            embed.add_field(name=f"Explicatie", value=exemplu.markdownify_explicatie(), inline=False)
    if problema.sursa:
        rezolvare = problema.sursa.discord_ready_embed()
        if len(rezolvare) > 1024:
            source_should_be_separate = True
        else:
            embed.add_field(name="Rezolvare Cod Sursa", value=rezolvare, inline=False)
    else:
        embed.add_field(name="Rezolvare Cod Sursa", value="Nu am gasit o rezolvare pentru aceasta problema.", inline=False)
    return embed , source_should_be_separate
