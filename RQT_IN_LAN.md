To run rqt to listen topics from another machine:

  1. connect to another machine (by ssh, for example)

  2. do command:
     export ROS_MASTER_URI=<another_machine_ip_address>:11311

  3. run rqt:
      rqt

  4. for more details: see http://wiki.ros.org/ROS/Tutorials/MultipleMachines
