I. Запуск всей системы:
  a) в RPi (Raspbian):
    cd ~/scripts
    ./candybot_vr.sh enter_package

  c) запуск одного определенного нода:
    - в данном терминале:
      roslaunch candybot_v2 <node_name>.launch

    - в номом терминале:
        II. a)
        source devel/setup.bash
        roslaunch candybot_v2 <node_name>.launch


  b) в докер-контейнере candybot_vr:
    source devel/setup.bash
    roslaunch candybot_v2 run1.launch


II. Использование скрипта тестирования и калибровки:
  в новом терминале выполнить

  a) в RPi (Raspbian):
    cd ~/scripts
    ./candybot_vr.sh attach #подключение к запущенному контейнеру

  b) в докер-контейнере candybot_vr:
    source devel/setup.bash
    cd scripts
    python3 test_servos2.py

    в данном скрипте нужно выбрать пункт для переключения на управление определенной частью робота
    для управления частями робота используются клавиши WASD, для выхода из управления и возврата в главное меню q
