// Code generated by protoc-gen-go. DO NOT EDIT.
// source: login.proto

package login

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type LoginMsgId int32

const (
	LoginMsgId_Login_MSG_ID            LoginMsgId = 0
	LoginMsgId_LOGIN_CREATEACCOUNT_REQ LoginMsgId = 1101
	LoginMsgId_LOGIN_SELECTROLE_ACK    LoginMsgId = 1108
	LoginMsgId_LOGIN_DELETEROLE_ACK    LoginMsgId = 1110
	LoginMsgId_LOGIN_LOGINAPP_ACK      LoginMsgId = 1104
	LoginMsgId_LOGIN_CREATEACCOUNT_ACK LoginMsgId = 1102
	LoginMsgId_LOGIN_LOGINAPP_REQ      LoginMsgId = 1103
	LoginMsgId_LOGIN_CREATEROLE_REQ    LoginMsgId = 1105
	LoginMsgId_LOGIN_SELECTROLE_REQ    LoginMsgId = 1107
	LoginMsgId_LOGIN_DELETEROLE_REQ    LoginMsgId = 1109
	LoginMsgId_LOGIN_CREATEROLE_ACK    LoginMsgId = 1106
)

var LoginMsgId_name = map[int32]string{
	0:    "Login_MSG_ID",
	1101: "LOGIN_CREATEACCOUNT_REQ",
	1108: "LOGIN_SELECTROLE_ACK",
	1110: "LOGIN_DELETEROLE_ACK",
	1104: "LOGIN_LOGINAPP_ACK",
	1102: "LOGIN_CREATEACCOUNT_ACK",
	1103: "LOGIN_LOGINAPP_REQ",
	1105: "LOGIN_CREATEROLE_REQ",
	1107: "LOGIN_SELECTROLE_REQ",
	1109: "LOGIN_DELETEROLE_REQ",
	1106: "LOGIN_CREATEROLE_ACK",
}

var LoginMsgId_value = map[string]int32{
	"Login_MSG_ID":            0,
	"LOGIN_CREATEACCOUNT_REQ": 1101,
	"LOGIN_SELECTROLE_ACK":    1108,
	"LOGIN_DELETEROLE_ACK":    1110,
	"LOGIN_LOGINAPP_ACK":      1104,
	"LOGIN_CREATEACCOUNT_ACK": 1102,
	"LOGIN_LOGINAPP_REQ":      1103,
	"LOGIN_CREATEROLE_REQ":    1105,
	"LOGIN_SELECTROLE_REQ":    1107,
	"LOGIN_DELETEROLE_REQ":    1109,
	"LOGIN_CREATEROLE_ACK":    1106,
}

func (x LoginMsgId) String() string {
	return proto.EnumName(LoginMsgId_name, int32(x))
}

func (LoginMsgId) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_67c21677aa7f4e4f, []int{0}
}

// 客户端请求创建账号
type CreateAccountReq struct {
	Account              string   `protobuf:"bytes,1,opt,name=Account,proto3" json:"Account,omitempty"`
	Password             string   `protobuf:"bytes,2,opt,name=Password,proto3" json:"Password,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *CreateAccountReq) Reset()         { *m = CreateAccountReq{} }
func (m *CreateAccountReq) String() string { return proto.CompactTextString(m) }
func (*CreateAccountReq) ProtoMessage()    {}
func (*CreateAccountReq) Descriptor() ([]byte, []int) {
	return fileDescriptor_67c21677aa7f4e4f, []int{0}
}

func (m *CreateAccountReq) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_CreateAccountReq.Unmarshal(m, b)
}
func (m *CreateAccountReq) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_CreateAccountReq.Marshal(b, m, deterministic)
}
func (m *CreateAccountReq) XXX_Merge(src proto.Message) {
	xxx_messageInfo_CreateAccountReq.Merge(m, src)
}
func (m *CreateAccountReq) XXX_Size() int {
	return xxx_messageInfo_CreateAccountReq.Size(m)
}
func (m *CreateAccountReq) XXX_DiscardUnknown() {
	xxx_messageInfo_CreateAccountReq.DiscardUnknown(m)
}

var xxx_messageInfo_CreateAccountReq proto.InternalMessageInfo

func (m *CreateAccountReq) GetAccount() string {
	if m != nil {
		return m.Account
	}
	return ""
}

func (m *CreateAccountReq) GetPassword() string {
	if m != nil {
		return m.Password
	}
	return ""
}

// 选择角色返回
type SelectRoleAck struct {
	ErrCode              int32    `protobuf:"varint,1,opt,name=ErrCode,proto3" json:"ErrCode,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *SelectRoleAck) Reset()         { *m = SelectRoleAck{} }
func (m *SelectRoleAck) String() string { return proto.CompactTextString(m) }
func (*SelectRoleAck) ProtoMessage()    {}
func (*SelectRoleAck) Descriptor() ([]byte, []int) {
	return fileDescriptor_67c21677aa7f4e4f, []int{1}
}

func (m *SelectRoleAck) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_SelectRoleAck.Unmarshal(m, b)
}
func (m *SelectRoleAck) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_SelectRoleAck.Marshal(b, m, deterministic)
}
func (m *SelectRoleAck) XXX_Merge(src proto.Message) {
	xxx_messageInfo_SelectRoleAck.Merge(m, src)
}
func (m *SelectRoleAck) XXX_Size() int {
	return xxx_messageInfo_SelectRoleAck.Size(m)
}
func (m *SelectRoleAck) XXX_DiscardUnknown() {
	xxx_messageInfo_SelectRoleAck.DiscardUnknown(m)
}

var xxx_messageInfo_SelectRoleAck proto.InternalMessageInfo

func (m *SelectRoleAck) GetErrCode() int32 {
	if m != nil {
		return m.ErrCode
	}
	return 0
}

// 删除角色返回
type DeleteRoleAck struct {
	ErrCode              int32    `protobuf:"varint,1,opt,name=ErrCode,proto3" json:"ErrCode,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *DeleteRoleAck) Reset()         { *m = DeleteRoleAck{} }
func (m *DeleteRoleAck) String() string { return proto.CompactTextString(m) }
func (*DeleteRoleAck) ProtoMessage()    {}
func (*DeleteRoleAck) Descriptor() ([]byte, []int) {
	return fileDescriptor_67c21677aa7f4e4f, []int{2}
}

func (m *DeleteRoleAck) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DeleteRoleAck.Unmarshal(m, b)
}
func (m *DeleteRoleAck) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DeleteRoleAck.Marshal(b, m, deterministic)
}
func (m *DeleteRoleAck) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DeleteRoleAck.Merge(m, src)
}
func (m *DeleteRoleAck) XXX_Size() int {
	return xxx_messageInfo_DeleteRoleAck.Size(m)
}
func (m *DeleteRoleAck) XXX_DiscardUnknown() {
	xxx_messageInfo_DeleteRoleAck.DiscardUnknown(m)
}

var xxx_messageInfo_DeleteRoleAck proto.InternalMessageInfo

func (m *DeleteRoleAck) GetErrCode() int32 {
	if m != nil {
		return m.ErrCode
	}
	return 0
}

// 服务器返回请求登录信息
type LoginAppAck struct {
	ErrCode              int32       `protobuf:"varint,1,opt,name=ErrCode,proto3" json:"ErrCode,omitempty"`
	RoleList             []*RoleInfo `protobuf:"bytes,2,rep,name=RoleList,proto3" json:"RoleList,omitempty"`
	XXX_NoUnkeyedLiteral struct{}    `json:"-"`
	XXX_unrecognized     []byte      `json:"-"`
	XXX_sizecache        int32       `json:"-"`
}

func (m *LoginAppAck) Reset()         { *m = LoginAppAck{} }
func (m *LoginAppAck) String() string { return proto.CompactTextString(m) }
func (*LoginAppAck) ProtoMessage()    {}
func (*LoginAppAck) Descriptor() ([]byte, []int) {
	return fileDescriptor_67c21677aa7f4e4f, []int{3}
}

func (m *LoginAppAck) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_LoginAppAck.Unmarshal(m, b)
}
func (m *LoginAppAck) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_LoginAppAck.Marshal(b, m, deterministic)
}
func (m *LoginAppAck) XXX_Merge(src proto.Message) {
	xxx_messageInfo_LoginAppAck.Merge(m, src)
}
func (m *LoginAppAck) XXX_Size() int {
	return xxx_messageInfo_LoginAppAck.Size(m)
}
func (m *LoginAppAck) XXX_DiscardUnknown() {
	xxx_messageInfo_LoginAppAck.DiscardUnknown(m)
}

var xxx_messageInfo_LoginAppAck proto.InternalMessageInfo

func (m *LoginAppAck) GetErrCode() int32 {
	if m != nil {
		return m.ErrCode
	}
	return 0
}

func (m *LoginAppAck) GetRoleList() []*RoleInfo {
	if m != nil {
		return m.RoleList
	}
	return nil
}

// 创建账号返回
type CreateAccountAck struct {
	Token                string   `protobuf:"bytes,1,opt,name=Token,proto3" json:"Token,omitempty"`
	AccountId            int64    `protobuf:"varint,2,opt,name=AccountId,proto3" json:"AccountId,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *CreateAccountAck) Reset()         { *m = CreateAccountAck{} }
func (m *CreateAccountAck) String() string { return proto.CompactTextString(m) }
func (*CreateAccountAck) ProtoMessage()    {}
func (*CreateAccountAck) Descriptor() ([]byte, []int) {
	return fileDescriptor_67c21677aa7f4e4f, []int{4}
}

func (m *CreateAccountAck) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_CreateAccountAck.Unmarshal(m, b)
}
func (m *CreateAccountAck) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_CreateAccountAck.Marshal(b, m, deterministic)
}
func (m *CreateAccountAck) XXX_Merge(src proto.Message) {
	xxx_messageInfo_CreateAccountAck.Merge(m, src)
}
func (m *CreateAccountAck) XXX_Size() int {
	return xxx_messageInfo_CreateAccountAck.Size(m)
}
func (m *CreateAccountAck) XXX_DiscardUnknown() {
	xxx_messageInfo_CreateAccountAck.DiscardUnknown(m)
}

var xxx_messageInfo_CreateAccountAck proto.InternalMessageInfo

func (m *CreateAccountAck) GetToken() string {
	if m != nil {
		return m.Token
	}
	return ""
}

func (m *CreateAccountAck) GetAccountId() int64 {
	if m != nil {
		return m.AccountId
	}
	return 0
}

// 客户端登录请求
type LoginAppReq struct {
	Token                string   `protobuf:"bytes,1,opt,name=Token,proto3" json:"Token,omitempty"`
	AccountId            int64    `protobuf:"varint,2,opt,name=AccountId,proto3" json:"AccountId,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *LoginAppReq) Reset()         { *m = LoginAppReq{} }
func (m *LoginAppReq) String() string { return proto.CompactTextString(m) }
func (*LoginAppReq) ProtoMessage()    {}
func (*LoginAppReq) Descriptor() ([]byte, []int) {
	return fileDescriptor_67c21677aa7f4e4f, []int{5}
}

func (m *LoginAppReq) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_LoginAppReq.Unmarshal(m, b)
}
func (m *LoginAppReq) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_LoginAppReq.Marshal(b, m, deterministic)
}
func (m *LoginAppReq) XXX_Merge(src proto.Message) {
	xxx_messageInfo_LoginAppReq.Merge(m, src)
}
func (m *LoginAppReq) XXX_Size() int {
	return xxx_messageInfo_LoginAppReq.Size(m)
}
func (m *LoginAppReq) XXX_DiscardUnknown() {
	xxx_messageInfo_LoginAppReq.DiscardUnknown(m)
}

var xxx_messageInfo_LoginAppReq proto.InternalMessageInfo

func (m *LoginAppReq) GetToken() string {
	if m != nil {
		return m.Token
	}
	return ""
}

func (m *LoginAppReq) GetAccountId() int64 {
	if m != nil {
		return m.AccountId
	}
	return 0
}

// 创建角色请求
type CreateRoleReq struct {
	AccountId            int64    `protobuf:"varint,1,opt,name=AccountId,proto3" json:"AccountId,omitempty"`
	RoleConfId           int32    `protobuf:"varint,2,opt,name=RoleConfId,proto3" json:"RoleConfId,omitempty"`
	RoleName             string   `protobuf:"bytes,3,opt,name=RoleName,proto3" json:"RoleName,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *CreateRoleReq) Reset()         { *m = CreateRoleReq{} }
func (m *CreateRoleReq) String() string { return proto.CompactTextString(m) }
func (*CreateRoleReq) ProtoMessage()    {}
func (*CreateRoleReq) Descriptor() ([]byte, []int) {
	return fileDescriptor_67c21677aa7f4e4f, []int{6}
}

func (m *CreateRoleReq) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_CreateRoleReq.Unmarshal(m, b)
}
func (m *CreateRoleReq) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_CreateRoleReq.Marshal(b, m, deterministic)
}
func (m *CreateRoleReq) XXX_Merge(src proto.Message) {
	xxx_messageInfo_CreateRoleReq.Merge(m, src)
}
func (m *CreateRoleReq) XXX_Size() int {
	return xxx_messageInfo_CreateRoleReq.Size(m)
}
func (m *CreateRoleReq) XXX_DiscardUnknown() {
	xxx_messageInfo_CreateRoleReq.DiscardUnknown(m)
}

var xxx_messageInfo_CreateRoleReq proto.InternalMessageInfo

func (m *CreateRoleReq) GetAccountId() int64 {
	if m != nil {
		return m.AccountId
	}
	return 0
}

func (m *CreateRoleReq) GetRoleConfId() int32 {
	if m != nil {
		return m.RoleConfId
	}
	return 0
}

func (m *CreateRoleReq) GetRoleName() string {
	if m != nil {
		return m.RoleName
	}
	return ""
}

// 角色信息
type RoleInfo struct {
	UserId               int64    `protobuf:"varint,1,opt,name=UserId,proto3" json:"UserId,omitempty"`
	RoleImageId          int32    `protobuf:"varint,2,opt,name=RoleImageId,proto3" json:"RoleImageId,omitempty"`
	RoleName             string   `protobuf:"bytes,3,opt,name=RoleName,proto3" json:"RoleName,omitempty"`
	RoleLevel            int32    `protobuf:"varint,4,opt,name=RoleLevel,proto3" json:"RoleLevel,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *RoleInfo) Reset()         { *m = RoleInfo{} }
func (m *RoleInfo) String() string { return proto.CompactTextString(m) }
func (*RoleInfo) ProtoMessage()    {}
func (*RoleInfo) Descriptor() ([]byte, []int) {
	return fileDescriptor_67c21677aa7f4e4f, []int{7}
}

func (m *RoleInfo) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_RoleInfo.Unmarshal(m, b)
}
func (m *RoleInfo) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_RoleInfo.Marshal(b, m, deterministic)
}
func (m *RoleInfo) XXX_Merge(src proto.Message) {
	xxx_messageInfo_RoleInfo.Merge(m, src)
}
func (m *RoleInfo) XXX_Size() int {
	return xxx_messageInfo_RoleInfo.Size(m)
}
func (m *RoleInfo) XXX_DiscardUnknown() {
	xxx_messageInfo_RoleInfo.DiscardUnknown(m)
}

var xxx_messageInfo_RoleInfo proto.InternalMessageInfo

func (m *RoleInfo) GetUserId() int64 {
	if m != nil {
		return m.UserId
	}
	return 0
}

func (m *RoleInfo) GetRoleImageId() int32 {
	if m != nil {
		return m.RoleImageId
	}
	return 0
}

func (m *RoleInfo) GetRoleName() string {
	if m != nil {
		return m.RoleName
	}
	return ""
}

func (m *RoleInfo) GetRoleLevel() int32 {
	if m != nil {
		return m.RoleLevel
	}
	return 0
}

// 角色选择请求
type SelectRoleReq struct {
	RoleId               int64    `protobuf:"varint,1,opt,name=RoleId,proto3" json:"RoleId,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *SelectRoleReq) Reset()         { *m = SelectRoleReq{} }
func (m *SelectRoleReq) String() string { return proto.CompactTextString(m) }
func (*SelectRoleReq) ProtoMessage()    {}
func (*SelectRoleReq) Descriptor() ([]byte, []int) {
	return fileDescriptor_67c21677aa7f4e4f, []int{8}
}

func (m *SelectRoleReq) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_SelectRoleReq.Unmarshal(m, b)
}
func (m *SelectRoleReq) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_SelectRoleReq.Marshal(b, m, deterministic)
}
func (m *SelectRoleReq) XXX_Merge(src proto.Message) {
	xxx_messageInfo_SelectRoleReq.Merge(m, src)
}
func (m *SelectRoleReq) XXX_Size() int {
	return xxx_messageInfo_SelectRoleReq.Size(m)
}
func (m *SelectRoleReq) XXX_DiscardUnknown() {
	xxx_messageInfo_SelectRoleReq.DiscardUnknown(m)
}

var xxx_messageInfo_SelectRoleReq proto.InternalMessageInfo

func (m *SelectRoleReq) GetRoleId() int64 {
	if m != nil {
		return m.RoleId
	}
	return 0
}

// 删除角色
type DeleteRoleReq struct {
	RoleId               int64    `protobuf:"varint,1,opt,name=RoleId,proto3" json:"RoleId,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *DeleteRoleReq) Reset()         { *m = DeleteRoleReq{} }
func (m *DeleteRoleReq) String() string { return proto.CompactTextString(m) }
func (*DeleteRoleReq) ProtoMessage()    {}
func (*DeleteRoleReq) Descriptor() ([]byte, []int) {
	return fileDescriptor_67c21677aa7f4e4f, []int{9}
}

func (m *DeleteRoleReq) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DeleteRoleReq.Unmarshal(m, b)
}
func (m *DeleteRoleReq) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DeleteRoleReq.Marshal(b, m, deterministic)
}
func (m *DeleteRoleReq) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DeleteRoleReq.Merge(m, src)
}
func (m *DeleteRoleReq) XXX_Size() int {
	return xxx_messageInfo_DeleteRoleReq.Size(m)
}
func (m *DeleteRoleReq) XXX_DiscardUnknown() {
	xxx_messageInfo_DeleteRoleReq.DiscardUnknown(m)
}

var xxx_messageInfo_DeleteRoleReq proto.InternalMessageInfo

func (m *DeleteRoleReq) GetRoleId() int64 {
	if m != nil {
		return m.RoleId
	}
	return 0
}

// 创建角色返回
type CreateRoleAck struct {
	ErrCode              int32    `protobuf:"varint,1,opt,name=ErrCode,proto3" json:"ErrCode,omitempty"`
	RoleId               int64    `protobuf:"varint,2,opt,name=RoleId,proto3" json:"RoleId,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *CreateRoleAck) Reset()         { *m = CreateRoleAck{} }
func (m *CreateRoleAck) String() string { return proto.CompactTextString(m) }
func (*CreateRoleAck) ProtoMessage()    {}
func (*CreateRoleAck) Descriptor() ([]byte, []int) {
	return fileDescriptor_67c21677aa7f4e4f, []int{10}
}

func (m *CreateRoleAck) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_CreateRoleAck.Unmarshal(m, b)
}
func (m *CreateRoleAck) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_CreateRoleAck.Marshal(b, m, deterministic)
}
func (m *CreateRoleAck) XXX_Merge(src proto.Message) {
	xxx_messageInfo_CreateRoleAck.Merge(m, src)
}
func (m *CreateRoleAck) XXX_Size() int {
	return xxx_messageInfo_CreateRoleAck.Size(m)
}
func (m *CreateRoleAck) XXX_DiscardUnknown() {
	xxx_messageInfo_CreateRoleAck.DiscardUnknown(m)
}

var xxx_messageInfo_CreateRoleAck proto.InternalMessageInfo

func (m *CreateRoleAck) GetErrCode() int32 {
	if m != nil {
		return m.ErrCode
	}
	return 0
}

func (m *CreateRoleAck) GetRoleId() int64 {
	if m != nil {
		return m.RoleId
	}
	return 0
}

func init() {
	proto.RegisterEnum("LoginMsgId", LoginMsgId_name, LoginMsgId_value)
	proto.RegisterType((*CreateAccountReq)(nil), "CreateAccountReq")
	proto.RegisterType((*SelectRoleAck)(nil), "SelectRoleAck")
	proto.RegisterType((*DeleteRoleAck)(nil), "DeleteRoleAck")
	proto.RegisterType((*LoginAppAck)(nil), "LoginAppAck")
	proto.RegisterType((*CreateAccountAck)(nil), "CreateAccountAck")
	proto.RegisterType((*LoginAppReq)(nil), "LoginAppReq")
	proto.RegisterType((*CreateRoleReq)(nil), "CreateRoleReq")
	proto.RegisterType((*RoleInfo)(nil), "RoleInfo")
	proto.RegisterType((*SelectRoleReq)(nil), "SelectRoleReq")
	proto.RegisterType((*DeleteRoleReq)(nil), "DeleteRoleReq")
	proto.RegisterType((*CreateRoleAck)(nil), "CreateRoleAck")
}

func init() { proto.RegisterFile("login.proto", fileDescriptor_67c21677aa7f4e4f) }

var fileDescriptor_67c21677aa7f4e4f = []byte{
	// 466 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x9c, 0x54, 0xdb, 0x6e, 0xd3, 0x40,
	0x10, 0x25, 0x09, 0x09, 0xce, 0x84, 0x4a, 0xd6, 0xaa, 0x6a, 0x0d, 0xaa, 0x50, 0x64, 0x09, 0x51,
	0x78, 0xe8, 0x03, 0x7c, 0xc1, 0xca, 0x59, 0x8a, 0x85, 0x9b, 0x84, 0x8d, 0xfb, 0x6c, 0x85, 0x64,
	0x1a, 0x45, 0x75, 0xbd, 0xc1, 0x36, 0xf0, 0xc6, 0x27, 0xf1, 0x27, 0xdc, 0x2f, 0xdf, 0x83, 0x66,
	0xd7, 0xb1, 0x4d, 0x15, 0x8c, 0xd4, 0x17, 0x4b, 0x67, 0xce, 0xd9, 0x33, 0x67, 0x66, 0x57, 0x86,
	0x41, 0xac, 0x56, 0xeb, 0xe4, 0x64, 0x93, 0xaa, 0x5c, 0xb9, 0x2f, 0xc0, 0xf6, 0x52, 0x9c, 0xe7,
	0xc8, 0x17, 0x0b, 0xf5, 0x36, 0xc9, 0x25, 0xbe, 0x61, 0x0e, 0xdc, 0x29, 0x90, 0xd3, 0x1a, 0xb6,
	0x8e, 0xfb, 0x72, 0x0b, 0xd9, 0x7d, 0xb0, 0xa6, 0xf3, 0x2c, 0x7b, 0xaf, 0xd2, 0xa5, 0xd3, 0xd6,
	0x54, 0x89, 0xdd, 0xc7, 0xb0, 0x37, 0xc3, 0x18, 0x17, 0xb9, 0x54, 0x31, 0xf2, 0xc5, 0x25, 0xd9,
	0x88, 0x34, 0xf5, 0xd4, 0x12, 0xb5, 0x4d, 0x57, 0x6e, 0x21, 0x49, 0x47, 0x18, 0x63, 0x8e, 0xff,
	0x97, 0x8e, 0x61, 0x10, 0x50, 0x5c, 0xbe, 0xd9, 0x34, 0x0a, 0xd9, 0x43, 0xb0, 0xc8, 0x2d, 0x58,
	0x67, 0xb9, 0xd3, 0x1e, 0x76, 0x8e, 0x07, 0x4f, 0xfb, 0x27, 0x54, 0xf0, 0x93, 0x0b, 0x25, 0x4b,
	0xca, 0x7d, 0x7e, 0x6d, 0x5e, 0x32, 0xdd, 0x87, 0x6e, 0xa8, 0x2e, 0x31, 0x29, 0xa6, 0x35, 0x80,
	0x1d, 0x41, 0xbf, 0xd0, 0xf8, 0x66, 0xd8, 0x8e, 0xac, 0x0a, 0x2e, 0xaf, 0x72, 0xd1, 0xca, 0x6e,
	0x62, 0xb1, 0x86, 0x3d, 0x13, 0x85, 0xc2, 0x91, 0xc9, 0x5f, 0xf2, 0xd6, 0x35, 0x39, 0x7b, 0x00,
	0x40, 0x42, 0x4f, 0x25, 0x17, 0x85, 0x5b, 0x57, 0xd6, 0x2a, 0x74, 0x37, 0x84, 0xc6, 0xf3, 0x2b,
	0x74, 0x3a, 0xe6, 0x6e, 0xb6, 0xd8, 0xfd, 0x60, 0x38, 0xda, 0x05, 0x3b, 0x80, 0xde, 0x79, 0x86,
	0x69, 0xd9, 0xa2, 0x40, 0x6c, 0x08, 0x03, 0xad, 0xb9, 0x9a, 0xaf, 0xb0, 0x6c, 0x50, 0x2f, 0x35,
	0x75, 0xa0, 0xec, 0x7a, 0xc7, 0xf8, 0x0e, 0x63, 0xe7, 0xb6, 0x3e, 0x5b, 0x15, 0xdc, 0x47, 0xf5,
	0xb7, 0x41, 0xa3, 0x1e, 0x40, 0x4f, 0x3b, 0x97, 0x21, 0x0c, 0x22, 0x61, 0xf5, 0x32, 0x9a, 0x84,
	0xbc, 0xbe, 0xbc, 0xe6, 0x97, 0x51, 0x59, 0xb4, 0xeb, 0x16, 0x4f, 0x3e, 0xb6, 0x01, 0xf4, 0x1d,
	0x9e, 0x65, 0x2b, 0x7f, 0xc9, 0x6c, 0xb8, 0xab, 0x51, 0x74, 0x36, 0x3b, 0x8d, 0xfc, 0x91, 0x7d,
	0x8b, 0x1d, 0xc1, 0x61, 0x30, 0x39, 0xf5, 0xc7, 0x91, 0x27, 0x05, 0x0f, 0x05, 0xf7, 0xbc, 0xc9,
	0xf9, 0x38, 0x8c, 0xa4, 0x78, 0x65, 0x7f, 0xb2, 0xd8, 0x3d, 0xd8, 0x37, 0xec, 0x4c, 0x04, 0xc2,
	0x0b, 0xe5, 0x24, 0x10, 0x11, 0xf7, 0x5e, 0xda, 0x3f, 0x6b, 0xd4, 0x48, 0x04, 0x22, 0x14, 0x25,
	0xf5, 0xdb, 0x62, 0x87, 0xc0, 0x0c, 0xa5, 0xbf, 0x7c, 0x3a, 0xd5, 0xc4, 0x57, 0xeb, 0x5f, 0xcd,
	0x88, 0xfd, 0xbc, 0xeb, 0x18, 0xa5, 0xf8, 0x52, 0x6b, 0x65, 0x8e, 0xe9, 0x56, 0x44, 0x7d, 0xdb,
	0x1d, 0x90, 0xa8, 0x1f, 0xbb, 0x03, 0x12, 0xf5, 0x6b, 0xb7, 0x21, 0x85, 0xf8, 0x6e, 0xbd, 0xee,
	0xe9, 0x5f, 0xc6, 0xb3, 0x3f, 0x01, 0x00, 0x00, 0xff, 0xff, 0x6d, 0x2d, 0xea, 0x06, 0x41, 0x04,
	0x00, 0x00,
}
