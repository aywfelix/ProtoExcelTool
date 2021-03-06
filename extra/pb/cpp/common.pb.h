// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: common.proto

#ifndef GOOGLE_PROTOBUF_INCLUDED_common_2eproto
#define GOOGLE_PROTOBUF_INCLUDED_common_2eproto

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
#define PROTOBUF_INTERNAL_EXPORT_common_2eproto
PROTOBUF_NAMESPACE_OPEN
namespace internal {
class AnyMetadata;
}  // namespace internal
PROTOBUF_NAMESPACE_CLOSE

// Internal implementation detail -- do not use these members.
struct TableStruct_common_2eproto {
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTableField entries[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::AuxiliaryParseTableField aux[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTable schema[1]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::FieldMetadata field_metadata[];
  static const ::PROTOBUF_NAMESPACE_ID::internal::SerializationTable serialization_table[];
  static const ::PROTOBUF_NAMESPACE_ID::uint32 offsets[];
};
extern const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_common_2eproto;
class Assets;
struct AssetsDefaultTypeInternal;
extern AssetsDefaultTypeInternal _Assets_default_instance_;
PROTOBUF_NAMESPACE_OPEN
template<> ::Assets* Arena::CreateMaybeMessage<::Assets>(Arena*);
PROTOBUF_NAMESPACE_CLOSE

enum CommonMsgId : int {
  Common_MSG_ID = 0,
  CommonMsgId_INT_MIN_SENTINEL_DO_NOT_USE_ = std::numeric_limits<::PROTOBUF_NAMESPACE_ID::int32>::min(),
  CommonMsgId_INT_MAX_SENTINEL_DO_NOT_USE_ = std::numeric_limits<::PROTOBUF_NAMESPACE_ID::int32>::max()
};
bool CommonMsgId_IsValid(int value);
constexpr CommonMsgId CommonMsgId_MIN = Common_MSG_ID;
constexpr CommonMsgId CommonMsgId_MAX = Common_MSG_ID;
constexpr int CommonMsgId_ARRAYSIZE = CommonMsgId_MAX + 1;

const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor* CommonMsgId_descriptor();
template<typename T>
inline const std::string& CommonMsgId_Name(T enum_t_value) {
  static_assert(::std::is_same<T, CommonMsgId>::value ||
    ::std::is_integral<T>::value,
    "Incorrect type passed to function CommonMsgId_Name.");
  return ::PROTOBUF_NAMESPACE_ID::internal::NameOfEnum(
    CommonMsgId_descriptor(), enum_t_value);
}
inline bool CommonMsgId_Parse(
    ::PROTOBUF_NAMESPACE_ID::ConstStringParam name, CommonMsgId* value) {
  return ::PROTOBUF_NAMESPACE_ID::internal::ParseNamedEnum<CommonMsgId>(
    CommonMsgId_descriptor(), name, value);
}
// ===================================================================

class Assets final :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:Assets) */ {
 public:
  inline Assets() : Assets(nullptr) {}
  ~Assets() override;
  explicit constexpr Assets(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized);

  Assets(const Assets& from);
  Assets(Assets&& from) noexcept
    : Assets() {
    *this = ::std::move(from);
  }

  inline Assets& operator=(const Assets& from) {
    CopyFrom(from);
    return *this;
  }
  inline Assets& operator=(Assets&& from) noexcept {
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
  static const Assets& default_instance() {
    return *internal_default_instance();
  }
  static inline const Assets* internal_default_instance() {
    return reinterpret_cast<const Assets*>(
               &_Assets_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  friend void swap(Assets& a, Assets& b) {
    a.Swap(&b);
  }
  inline void Swap(Assets* other) {
    if (other == this) return;
    if (GetOwningArena() == other->GetOwningArena()) {
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(Assets* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetOwningArena() == other->GetOwningArena());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline Assets* New() const final {
    return new Assets();
  }

  Assets* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<Assets>(arena);
  }
  using ::PROTOBUF_NAMESPACE_ID::Message::CopyFrom;
  void CopyFrom(const Assets& from);
  using ::PROTOBUF_NAMESPACE_ID::Message::MergeFrom;
  void MergeFrom(const Assets& from);
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
  void InternalSwap(Assets* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "Assets";
  }
  protected:
  explicit Assets(::PROTOBUF_NAMESPACE_ID::Arena* arena,
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
    kPathFieldNumber = 1,
  };
  // string path = 1;
  void clear_path();
  const std::string& path() const;
  template <typename ArgT0 = const std::string&, typename... ArgT>
  void set_path(ArgT0&& arg0, ArgT... args);
  std::string* mutable_path();
  PROTOBUF_MUST_USE_RESULT std::string* release_path();
  void set_allocated_path(std::string* path);
  private:
  const std::string& _internal_path() const;
  inline PROTOBUF_ALWAYS_INLINE void _internal_set_path(const std::string& value);
  std::string* _internal_mutable_path();
  public:

  // @@protoc_insertion_point(class_scope:Assets)
 private:
  class _Internal;

  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr path_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_common_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// Assets

// string path = 1;
inline void Assets::clear_path() {
  path_.ClearToEmpty();
}
inline const std::string& Assets::path() const {
  // @@protoc_insertion_point(field_get:Assets.path)
  return _internal_path();
}
template <typename ArgT0, typename... ArgT>
inline PROTOBUF_ALWAYS_INLINE
void Assets::set_path(ArgT0&& arg0, ArgT... args) {
 
 path_.Set(::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr::EmptyDefault{}, static_cast<ArgT0 &&>(arg0), args..., GetArenaForAllocation());
  // @@protoc_insertion_point(field_set:Assets.path)
}
inline std::string* Assets::mutable_path() {
  std::string* _s = _internal_mutable_path();
  // @@protoc_insertion_point(field_mutable:Assets.path)
  return _s;
}
inline const std::string& Assets::_internal_path() const {
  return path_.Get();
}
inline void Assets::_internal_set_path(const std::string& value) {
  
  path_.Set(::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr::EmptyDefault{}, value, GetArenaForAllocation());
}
inline std::string* Assets::_internal_mutable_path() {
  
  return path_.Mutable(::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr::EmptyDefault{}, GetArenaForAllocation());
}
inline std::string* Assets::release_path() {
  // @@protoc_insertion_point(field_release:Assets.path)
  return path_.Release(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), GetArenaForAllocation());
}
inline void Assets::set_allocated_path(std::string* path) {
  if (path != nullptr) {
    
  } else {
    
  }
  path_.SetAllocated(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), path,
      GetArenaForAllocation());
  // @@protoc_insertion_point(field_set_allocated:Assets.path)
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__

// @@protoc_insertion_point(namespace_scope)


PROTOBUF_NAMESPACE_OPEN

template <> struct is_proto_enum< ::CommonMsgId> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::CommonMsgId>() {
  return ::CommonMsgId_descriptor();
}

PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // GOOGLE_PROTOBUF_INCLUDED_GOOGLE_PROTOBUF_INCLUDED_common_2eproto
