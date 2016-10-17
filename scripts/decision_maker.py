#!/usr/bin/env python3
'''Meke decision by recieved data'''

import rospy
from std_msgs.msg import String
from candybot_vr.msg import VisionMessage
from candybot_vr.network.encyclopedia import Encyclopedia
from candybot_vr.network.anekdots import Anekdot
from candybot_vr.network.weather import Weather
from candybot_vr.util import rus_ascii_filter

import subprocess

#states set
states_set = ('ready', 'ready_to_photo')
#current state
state = 'ready'
#try parse anekdots in advance
anekdot = Anekdot()


def say(text):
    '''Says text
    Args:
        text: text to say
    '''
    
    echo_proc = subprocess.Popen(['echo', text],
                                         stdout=subprocess.PIPE)
    rhvoice_proc = subprocess.call(['spd-say', '-w', '-o', 'rhvoice',
                                    '-l', 'ru', '-e', '-t', 'male1'],
                                   stdin=echo_proc.stdout)

def make_photo():
    print('photo!')
    
def run_sensors():
    '''Resumes viewing and listening'''
    
    rospy.set_param('listening', True)
    rospy.set_param('viewing', True)


def stop_sensors():
    '''Stops viewing and listening'''

    rospy.set_param('listening', False)
    rospy.set_param('viewing', False)

    
def callback_listen(data):
    '''Listening callback function.
    Args:
        data: listen data, ROS String type
    '''
    global state
    
    #stop sensors while decision and event make
    stop_sensors()
    
    phrase = data.data.lower()
    
    if state == 'ready':
        
        if phrase.find('привет') > -1:
            say('привет')
        else: 
            if  phrase.find('расскажи') > -1:
                if phrase.find('анекдот') > -1:
                    anekdot_text = anekdot.random_anekdot()
                    if not anekdot_text is None:
                        say(rus_ascii_filter(anekdot_text))
                elif phrase.find('погода') > -1:
                    weather = Weather()
                    say(weather.get_weather())
                else:
                    new_phrase = phrase[phrase.find('расскажи') + len('расскажи'):len(phrase)].strip()
                    encyclopedia = Encyclopedia(new_phrase)
                    short_article = encyclopedia.get_summary()
                    if not short_article is None:
                        say(rus_ascii_filter(short_article))
                    else:
                        say('Не могу прочитать статью')
                        
            elif phrase.find('сделай') > -1:
                if phrase.find('фото') > -1:
                    state = 'ready_to_photo'
                    say('Я готов к фото')
                    
            else:
                pass
    
    elif state == 'ready_to_photo':
        if phrase.find('фото') > -1:
            make_photo()
            state = 'ready'
        
    #run sensors after event mdde    
    run_sensors()

    
def callback_view(data):
    '''Listening callback function.
    Args:
        data: listen data, VisionMessage type, see msg/VisionMessage.msg
    '''
    
    if rospy.get_param('viewing'):
        
        stop_sensors()
        
        face_count = data.face_count
        smile_exists = data.smile
        
        if face_count > 6:
            say('Как вас много!')

        if smile_exists:
            say('Улыбка!')

        run_sensors()
    

def recieve():
	'''Recieves messages from listener and viewer
	'''
	print('I ready to recieve messages')
	rospy.init_node('decision_maker', anonymous=True)
	rospy.Subscriber('audio_decision', String, callback_listen)
	rospy.Subscriber('vision_decision', VisionMessage, callback_view)
	rospy.spin()

def main():
	'''Main function'''
	
	recieve()


if __name__ == '__main__':
    main()
