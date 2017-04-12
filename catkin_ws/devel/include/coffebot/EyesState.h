// Generated by gencpp from file coffebot/EyesState.msg
// DO NOT EDIT!


#ifndef COFFEBOT_MESSAGE_EYESSTATE_H
#define COFFEBOT_MESSAGE_EYESSTATE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace coffebot
{
template <class ContainerAllocator>
struct EyesState_
{
  typedef EyesState_<ContainerAllocator> Type;

  EyesState_()
    : x(0)
    , y(0)
    , emotion()  {
    }
  EyesState_(const ContainerAllocator& _alloc)
    : x(0)
    , y(0)
    , emotion(_alloc)  {
  (void)_alloc;
    }



   typedef int8_t _x_type;
  _x_type x;

   typedef int8_t _y_type;
  _y_type y;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _emotion_type;
  _emotion_type emotion;




  typedef boost::shared_ptr< ::coffebot::EyesState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::coffebot::EyesState_<ContainerAllocator> const> ConstPtr;

}; // struct EyesState_

typedef ::coffebot::EyesState_<std::allocator<void> > EyesState;

typedef boost::shared_ptr< ::coffebot::EyesState > EyesStatePtr;
typedef boost::shared_ptr< ::coffebot::EyesState const> EyesStateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::coffebot::EyesState_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::coffebot::EyesState_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace coffebot

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'coffebot': ['/home/alex/catkin_ws/src/coffebot/msg', '/home/alex/catkin_ws/devel/share/coffebot/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::coffebot::EyesState_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::coffebot::EyesState_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::coffebot::EyesState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::coffebot::EyesState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::coffebot::EyesState_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::coffebot::EyesState_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::coffebot::EyesState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bcfd694b6a681b718890867e9439c098";
  }

  static const char* value(const ::coffebot::EyesState_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbcfd694b6a681b71ULL;
  static const uint64_t static_value2 = 0x8890867e9439c098ULL;
};

template<class ContainerAllocator>
struct DataType< ::coffebot::EyesState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "coffebot/EyesState";
  }

  static const char* value(const ::coffebot::EyesState_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::coffebot::EyesState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int8 x #0.0 <= x <= 128\n\
int8 y #0.0 <= y <= 128\n\
string emotion\n\
";
  }

  static const char* value(const ::coffebot::EyesState_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::coffebot::EyesState_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.emotion);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct EyesState_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::coffebot::EyesState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::coffebot::EyesState_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<int8_t>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<int8_t>::stream(s, indent + "  ", v.y);
    s << indent << "emotion: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.emotion);
  }
};

} // namespace message_operations
} // namespace ros

#endif // COFFEBOT_MESSAGE_EYESSTATE_H