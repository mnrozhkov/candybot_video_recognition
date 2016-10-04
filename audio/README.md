1. Install python3 requirements (see requirements.txt)

2. Install SphinxBase:
	$sudo apt-get install sphinxbase-utils

3. Download desired dictionary and acoustic model (here - Russian):
	https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Russian/
	choose cmusphinx-ru-5.2.tar.gz

4. Create binary dictionary:

	$tar -xvf cmusphinx-ru-5.2.tar.gz
	
	$cd cmusphinx-ru-5.2
	
	$sphinx_lm_convert -i ru.lm -o ru.lm.bin
	
	now you have to copy file to python dist-packages folder:
	
		copy into /usr/local/lib/python3.5/dist-packages/pocketsphinx/model:
			ru.dic (better rename it to ru.dict), 
			ru.lm.bin
			
			create here folder ru-ru

		copy into /usr/local/lib/python3.5/dist-packages/pocketsphinx/model/ru-ru:
			feat.params
			feature_transform
			mdef
			means
			mixture_weights
			noisedict
			README
			transition_matrices
			variances

5. Install rhvoice - speech synthesizer:

	1) install it as client-server:
		$sudo apt-get install rhvoice rhvoice-russian
		
	2) install it as speech-dispatcher module:
		$sudo apt-get install speech-dispatcher-rhvoice rhvoice-russian [rhvoice-english]
	
	verify your installation (example for speech-dispatcher):
		$echo "Проверка синтезатора речи" | spd-say -o rhvoice -l ru -e -t female1
	
	for more details see $man spd-say

6. Install ROS and cofigure ROS:
	http://wiki.ros.org/ROS/Installation
	
