Coffebot:

	1. To run:
		
		at this folder in terminal type:
		
			python3 run_coffebot.py
			
	2. Work algorithm:
		
		2.1. listener.py listens speech and send recognized text to Subscriber 'audio_decision' in decision.py, callback function - callback_listen()
		
		2.2. in callback_listen() : recognized text is sent to bot - object of class APIAIBot (module BotClient)
		
		2.3. method request() of class class APIAIBot makes request to api.ai and returns some value from response (intent object): bot answer text and actions information
		
		2.4. in method callback_listen(): text is translated to speech and if action was information about it is displayed
		
		
