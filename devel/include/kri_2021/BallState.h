// Generated by gencpp from file kri_2021/BallState.msg
// DO NOT EDIT!


#ifndef KRI_2021_MESSAGE_BALLSTATE_H
#define KRI_2021_MESSAGE_BALLSTATE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace kri_2021
{
template <class ContainerAllocator>
struct BallState_
{
  typedef BallState_<ContainerAllocator> Type;

  BallState_()
    : bola_state(false)
    , bola_inFrame_Pos()
    , last_bola_inFrame_Pos()  {
    }
  BallState_(const ContainerAllocator& _alloc)
    : bola_state(false)
    , bola_inFrame_Pos(_alloc)
    , last_bola_inFrame_Pos(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _bola_state_type;
  _bola_state_type bola_state;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _bola_inFrame_Pos_type;
  _bola_inFrame_Pos_type bola_inFrame_Pos;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _last_bola_inFrame_Pos_type;
  _last_bola_inFrame_Pos_type last_bola_inFrame_Pos;





  typedef boost::shared_ptr< ::kri_2021::BallState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::kri_2021::BallState_<ContainerAllocator> const> ConstPtr;

}; // struct BallState_

typedef ::kri_2021::BallState_<std::allocator<void> > BallState;

typedef boost::shared_ptr< ::kri_2021::BallState > BallStatePtr;
typedef boost::shared_ptr< ::kri_2021::BallState const> BallStateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::kri_2021::BallState_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::kri_2021::BallState_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace kri_2021

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'kri_2021': ['/home/robotis/RobotisSoccer/src/kri_2021/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::kri_2021::BallState_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::kri_2021::BallState_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::kri_2021::BallState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::kri_2021::BallState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::kri_2021::BallState_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::kri_2021::BallState_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::kri_2021::BallState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "de7a3afd02c72a42be761a1cf03a491c";
  }

  static const char* value(const ::kri_2021::BallState_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xde7a3afd02c72a42ULL;
  static const uint64_t static_value2 = 0xbe761a1cf03a491cULL;
};

template<class ContainerAllocator>
struct DataType< ::kri_2021::BallState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "kri_2021/BallState";
  }

  static const char* value(const ::kri_2021::BallState_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::kri_2021::BallState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool bola_state\n\
string bola_inFrame_Pos\n\
string last_bola_inFrame_Pos\n\
";
  }

  static const char* value(const ::kri_2021::BallState_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::kri_2021::BallState_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.bola_state);
      stream.next(m.bola_inFrame_Pos);
      stream.next(m.last_bola_inFrame_Pos);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct BallState_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::kri_2021::BallState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::kri_2021::BallState_<ContainerAllocator>& v)
  {
    s << indent << "bola_state: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.bola_state);
    s << indent << "bola_inFrame_Pos: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.bola_inFrame_Pos);
    s << indent << "last_bola_inFrame_Pos: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.last_bola_inFrame_Pos);
  }
};

} // namespace message_operations
} // namespace ros

#endif // KRI_2021_MESSAGE_BALLSTATE_H
