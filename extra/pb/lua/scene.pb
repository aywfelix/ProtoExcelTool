
¿
scene.proto"a
RoleJumpReq
dir (Rdir
pos_x (RposX
pos_y (RposY
height (Rheight"x
RoleJumpAck
obj_id (RobjId
dir (Rdir
pos_x (RposX
pos_y (RposY
height (Rheight"i
RoleReAliveNotify
obj_id (RobjId
pos_x (RposX
pos_y (RposY
pos_z (RposZ"ç
ChannelChatReq!
content_type (RcontentType
	from_type (RfromType!
channel_type (RchannelType
content (	Rcontent"÷
ChannelChatAck
from_uid (RfromUid
username (	Rusername
sex (Rsex!
content_type (RcontentType!
channel_type (RchannelType
	from_type (RfromType
content (	Rcontent"u
ActivityReadyNotify

activityId (R
activityId

count_down (R	countDown
switch_type (R
switchType"Ò
ActivityStartNotify

activityId (R
activityId
switch_type (R
switchType
Ip (	RIp
port (Rport
	maze_seed (RmazeSeed

town_pos_x (RtownPosX

town_pos_y (RtownPosY

town_pos_z (RtownPosZ"R
JoinActivityReq

activityId (R
activityId
join_status (R
joinStatus"M
JoinActivityAck

activityId (R
activityId
errocode (Rerrocode"
MazeGetGemReq"g
AreaInitNotify
errCode (RerrCode
count (Rcount%
areaItem (2	.AreaItemRareaItem"Y
AreaItem
area_id (	RareaId
role_id (RroleId
	user_uuid (	RuserUuid"`
AreaTradeNotify
area_id (	RareaId
role_id (RroleId
	user_uuid (	RuserUuid"
ServerTimeReq"ª
ServerTimeAck
server_time (R
serverTime3
server_real_start_time (RserverRealStartTime
	open_days (RopenDays7
server_real_combine_time (RserverRealCombineTime"7
TransportReq'
transport_index (RtransportIndex"+
SwitchSceneReq
scene_id (RsceneIdbproto3