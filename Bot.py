from viberbot import Api
fom viberbot.api.bot_configuration import BotConfiguration

bot_configuration=BotConfiguration(
	name='СтройДом',
	avatar='',
	auth_token='4d02d6919227d132-d8c3abc3a9b85284-a640d402b8352c6d'
	)
viber=Api(bot_configuration)