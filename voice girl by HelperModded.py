# meta developer: dark
from telethon.tl.functions.channels import JoinChannelRequest
from .. import loader

@loader.tds
class voiceGirlsByHelperModded(loader.Module):
    """Голосовые сообщения девушки"""

    strings = {"name": "voiceGirlsByHelperModded"}

    async def прcmd(self, message):
        """| Привет"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/335",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def привcmd(self, message):
        """| Приветик"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/17",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def нормcmd(self, message):
        """| Все нормально"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/12",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def нуиcmd(self, message):
        """| Ну и что"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/14",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def хорошоcmd(self, message):
        """| Хорошо"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/22",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def Викаcmd(self, message):
        """| Я Вика"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/2",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def мне17cmd(self, message):
        """| Мне 17 лет"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/10",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def хзcmd(self, message):
        """| не знаю"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/24",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def непонcmd(self, message):
        """| Не поняла"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/11",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def гоcmd(self, message):
        """| Ну давай"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/3",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def даcmd(self, message):
        """| Да"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/4",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def нудаcmd(self, message):
        """| Ну да"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/25",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def чтоcmd(self, message):
        """| Что?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/23",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def кудаcmd(self, message):
        """| Куда?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/8",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def спокcmd(self, message):
        """| Спокойной ночи"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/20",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def кнcmd(self, message):
        """| Как настроение?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/7",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def добрcmd(self, message):
        """| Доброе утро"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/5",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def покаcmd(self, message):
        """| Пока"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/16",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def прощайcmd(self, message):
        """| Прощай"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/18",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def сладкихcmd(self, message):
        """| Сладких снов"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/19",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ланcmd(self, message):
        """| Ну ладно"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/9",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def пжcmd(self, message):
        """| Ну пожалуйста"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/15",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def дядяcmd(self, message):
        """| Дядя не надо"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/358",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def хмcmd(self, message):
        """| хмммм"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/359",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
        async def кдcmd(self, message):
        """| Как дела?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/voicegirlbyhelpgirl/6",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return