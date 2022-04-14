// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: game.proto

#ifndef GOOGLE_PROTOBUF_INCLUDED_game_2eproto
#define GOOGLE_PROTOBUF_INCLUDED_game_2eproto

#include <limits>
#include <string>

#include <google/protobuf/port_def.inc>
#if PROTOBUF_VERSION < 3018000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers. Please update
#error your headers.
#endif
#if 3018001 < PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers. Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/port_undef.inc>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_bases.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/metadata_lite.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/generated_enum_reflection.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
#define PROTOBUF_INTERNAL_EXPORT_game_2eproto
PROTOBUF_NAMESPACE_OPEN
namespace internal {
class AnyMetadata;
}  // namespace internal
PROTOBUF_NAMESPACE_CLOSE

// Internal implementation detail -- do not use these members.
struct TableStruct_game_2eproto {
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTableField entries[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::AuxiliaryParseTableField aux[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTable schema[2]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::FieldMetadata field_metadata[];
  static const ::PROTOBUF_NAMESPACE_ID::internal::SerializationTable serialization_table[];
  static const ::PROTOBUF_NAMESPACE_ID::uint32 offsets[];
};
extern const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_game_2eproto;
class EnterGameAck;
struct EnterGameAckDefaultTypeInternal;
extern EnterGameAckDefaultTypeInternal _EnterGameAck_default_instance_;
class EnterGameReq;
struct EnterGameReqDefaultTypeInternal;
extern EnterGameReqDefaultTypeInternal _EnterGameReq_default_instance_;
PROTOBUF_NAMESPACE_OPEN
template<> ::EnterGameAck* Arena::CreateMaybeMessage<::EnterGameAck>(Arena*);
template<> ::EnterGameReq* Arena::CreateMaybeMessage<::EnterGameReq>(Arena*);
PROTOBUF_NAMESPACE_CLOSE

enum GameMsgId : int {
  MSG_ID = 0,
  GAME_ENTERGAMEREQ_REQ = 2001,
  GAME_ENTERGAMEACK_ACK = 2002,
  GameMsgId_INT_MIN_SENTINEL_DO_NOT_USE_ = std::numeric_limits<::PROTOBUF_NAMESPACE_ID::int32>::min(),
  GameMsgId_INT_MAX_SENTINEL_DO_NOT_USE_ = std::numeric_limits<::PROTOBUF_NAMESPACE_ID::int32>::max()
};
bool GameMsgId_IsValid(int value);
constexpr GameMsgId GameMsgId_MIN = MSG_ID;
constexpr GameMsgId GameMsgId_MAX = GAME_ENTERGAMEACK_ACK;
constexpr int GameMsgId_ARRAYSIZE = GameMsgId_MAX + 1;

const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor* GameMsgId_descriptor();
template<typename T>
inline const std::string& GameMsgId_Name(T enum_t_value) {
  static_assert(::std::is_same<T, GameMsgId>::value ||
    ::std::is_integral<T>::value,
    "Incorrect type passed to function GameMsgId_Name.");
  return ::PROTOBUF_NAMESPACE_ID::internal::NameOfEnum(
    GameMsgId_descriptor(), enum_t_value);
}
inline bool GameMsgId_Parse(
    ::PROTOBUF_NAMESPACE_ID::ConstStringParam name, GameMsgId* value) {
  return ::PROTOBUF_NAMESPACE_ID::internal::ParseNamedEnum<GameMsgId>(
    GameMsgId_descriptor(), name, value);
}
// ===================================================================

class EnterGameReq final :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:EnterGameReq) */ {
 public:
  inline EnterGameReq() : EnterGameReq(nullptr) {}
  ~EnterGameReq() override;
  explicit constexpr EnterGameReq(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized);

  EnterGameReq(const EnterGameReq& from);
  EnterGameReq(EnterGameReq&& from) noexcept
    : EnterGameReq() {
    *this = ::std::move(from);
  }

  inline EnterGameReq& operator=(const EnterGameReq& from) {
    CopyFrom(from);
    return *this;
  }
  inline EnterGameReq& operator=(EnterGameReq&& from) noexcept {
    if (this == &from) return *this;
    if (GetOwningArena() == from.GetOwningArena()
  #ifdef PROTOBUF_FORCE_COPY_IN_MOVE
        && GetOwningArena() != nullptr
  #endif  // !PROTOBUF_FORCE_COPY_IN_MOVE
    ) {
      InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return default_instance().GetMetadata().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return default_instance().GetMetadata().reflection;
  }
  static const EnterGameReq& default_instance() {
    return *internal_default_instance();
  }
  static inline const EnterGameReq* internal_default_instance() {
    return reinterpret_cast<const EnterGameReq*>(
               &_EnterGameReq_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  friend void swap(EnterGameReq& a, EnterGameReq& b) {
    a.Swap(&b);
  }
  inline void Swap(EnterGameReq* other) {
    if (other == this) return;
    if (GetOwningArena() == other->GetOwningArena()) {
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(EnterGameReq* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetOwningArena() == other->GetOwningArena());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline EnterGameReq* New() const final {
    return new EnterGameReq();
  }

  EnterGameReq* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<EnterGameReq>(arena);
  }
  using ::PROTOBUF_NAMESPACE_ID::Message::CopyFrom;
  void CopyFrom(const EnterGameReq& from);
  using ::PROTOBUF_NAMESPACE_ID::Message::MergeFrom;
  void MergeFrom(const EnterGameReq& from);
  private:
  static void MergeImpl(::PROTOBUF_NAMESPACE_ID::Message* to, const ::PROTOBUF_NAMESPACE_ID::Message& from);
  public:
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  ::PROTOBUF_NAMESPACE_ID::uint8* _InternalSerialize(
      ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(EnterGameReq* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "EnterGameReq";
  }
  protected:
  explicit EnterGameReq(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                       bool is_message_owned = false);
  private:
  static void ArenaDtor(void* object);
  inline void RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  public:

  static const ClassData _class_data_;
  const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*GetClassData() const final;

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kUserIdFieldNumber = 1,
    kRoleIdFieldNumber = 2,
  };
  // int64 UserId = 1;
  void clear_userid();
  ::PROTOBUF_NAMESPACE_ID::int64 userid() const;
  void set_userid(::PROTOBUF_NAMESPACE_ID::int64 value);
  private:
  ::PROTOBUF_NAMESPACE_ID::int64 _internal_userid() const;
  void _internal_set_userid(::PROTOBUF_NAMESPACE_ID::int64 value);
  public:

  // int32 RoleId = 2;
  void clear_roleid();
  ::PROTOBUF_NAMESPACE_ID::int32 roleid() const;
  void set_roleid(::PROTOBUF_NAMESPACE_ID::int32 value);
  private:
  ::PROTOBUF_NAMESPACE_ID::int32 _internal_roleid() const;
  void _internal_set_roleid(::PROTOBUF_NAMESPACE_ID::int32 value);
  public:

  // @@protoc_insertion_point(class_scope:EnterGameReq)
 private:
  class _Internal;

  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  ::PROTOBUF_NAMESPACE_ID::int64 userid_;
  ::PROTOBUF_NAMESPACE_ID::int32 roleid_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_game_2eproto;
};
// -------------------------------------------------------------------

class EnterGameAck final :
    public ::PROTOBUF_NAMESPACE_ID::internal::ZeroFieldsBase /* @@protoc_insertion_point(class_definition:EnterGameAck) */ {
 public:
  inline EnterGameAck() : EnterGameAck(nullptr) {}
  explicit constexpr EnterGameAck(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized);

  EnterGameAck(const EnterGameAck& from);
  EnterGameAck(EnterGameAck&& from) noexcept
    : EnterGameAck() {
    *this = ::std::move(from);
  }

  inline EnterGameAck& operator=(const EnterGameAck& from) {
    CopyFrom(from);
    return *this;
  }
  inline EnterGameAck& operator=(EnterGameAck&& from) noexcept {
    if (this == &from) return *this;
    if (GetOwningArena() == from.GetOwningArena()
  #ifdef PROTOBUF_FORCE_COPY_IN_MOVE
        && GetOwningArena() != nullptr
  #endif  // !PROTOBUF_FORCE_COPY_IN_MOVE
    ) {
      InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return default_instance().GetMetadata().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return default_instance().GetMetadata().reflection;
  }
  static const EnterGameAck& default_instance() {
    return *internal_default_instance();
  }
  static inline const EnterGameAck* internal_default_instance() {
    return reinterpret_cast<const EnterGameAck*>(
               &_EnterGameAck_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    1;

  friend void swap(EnterGameAck& a, EnterGameAck& b) {
    a.Swap(&b);
  }
  inline void Swap(EnterGameAck* other) {
    if (other == this) return;
    if (GetOwningArena() == other->GetOwningArena()) {
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(EnterGameAck* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetOwningArena() == other->GetOwningArena());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline EnterGameAck* New() const final {
    return new EnterGameAck();
  }

  EnterGameAck* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<EnterGameAck>(arena);
  }
  using ::PROTOBUF_NAMESPACE_ID::internal::ZeroFieldsBase::CopyFrom;
  inline void CopyFrom(const EnterGameAck& from) {
    ::PROTOBUF_NAMESPACE_ID::internal::ZeroFieldsBase::CopyImpl(this, from);
  }
  using ::PROTOBUF_NAMESPACE_ID::internal::ZeroFieldsBase::MergeFrom;
  void MergeFrom(const EnterGameAck& from) {
    ::PROTOBUF_NAMESPACE_ID::internal::ZeroFieldsBase::MergeImpl(this, from);
  }
  public:
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "EnterGameAck";
  }
  protected:
  explicit EnterGameAck(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                       bool is_message_owned = false);
  private:
  public:

  static const ClassData _class_data_;
  const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*GetClassData() const final;

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // @@protoc_insertion_point(class_scope:EnterGameAck)
 private:
  class _Internal;

  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_game_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// EnterGameReq

// int64 UserId = 1;
inline void EnterGameReq::clear_userid() {
  userid_ = int64_t{0};
}
inline ::PROTOBUF_NAMESPACE_ID::int64 EnterGameReq::_internal_userid() const {
  return userid_;
}
inline ::PROTOBUF_NAMESPACE_ID::int64 EnterGameReq::userid() const {
  // @@protoc_insertion_point(field_get:EnterGameReq.UserId)
  return _internal_userid();
}
inline void EnterGameReq::_internal_set_userid(::PROTOBUF_NAMESPACE_ID::int64 value) {
  
  userid_ = value;
}
inline void EnterGameReq::set_userid(::PROTOBUF_NAMESPACE_ID::int64 value) {
  _internal_set_userid(value);
  // @@protoc_insertion_point(field_set:EnterGameReq.UserId)
}

// int32 RoleId = 2;
inline void EnterGameReq::clear_roleid() {
  roleid_ = 0;
}
inline ::PROTOBUF_NAMESPACE_ID::int32 EnterGameReq::_internal_roleid() const {
  return roleid_;
}
inline ::PROTOBUF_NAMESPACE_ID::int32 EnterGameReq::roleid() const {
  // @@protoc_insertion_point(field_get:EnterGameReq.RoleId)
  return _internal_roleid();
}
inline void EnterGameReq::_internal_set_roleid(::PROTOBUF_NAMESPACE_ID::int32 value) {
  
  roleid_ = value;
}
inline void EnterGameReq::set_roleid(::PROTOBUF_NAMESPACE_ID::int32 value) {
  _internal_set_roleid(value);
  // @@protoc_insertion_point(field_set:EnterGameReq.RoleId)
}

// -------------------------------------------------------------------

// EnterGameAck

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)


PROTOBUF_NAMESPACE_OPEN

template <> struct is_proto_enum< ::GameMsgId> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::GameMsgId>() {
  return ::GameMsgId_descriptor();
}

PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // GOOGLE_PROTOBUF_INCLUDED_GOOGLE_PROTOBUF_INCLUDED_game_2eproto
