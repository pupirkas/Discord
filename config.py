responce = ['Конечно',
			'Да',
			'Нет',
			'Ни за что',
			'Возможно']

TOKEN = 'Nzc5Mzg3Nzc0MjkzOTAxNDIy.X7fzbQ.V3p4Gdpf-5j2bXSLuWN6sPeASyQ'

ydl_opts = {
	'format': 'beataudio/best',
	'postprocessors': [{
		'key':'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
}]
}