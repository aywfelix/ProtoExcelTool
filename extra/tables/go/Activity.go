package Table

import (
	"encoding/json"
	"io/ioutil"
	"fmt"
)

type activityRow struct {
	Id int                                            // 主键id 活动id
	Comment []rune                                    // 注释 
	Tab_id int                                        // 标签编号 活动所属标签
	Weight int                                        // 权重 标签列表内的显示权重
	Name_id int                                       // 名称id 活动名称id
	Describe_id int                                   // 描述文本id 
	Race_id int                                       // 是否相关种族 是否需要判断玩家种族来显示对话按钮,0表示否，1表示是
	Main_icon []rune                                  // 主图名称 
	Sub_icon []rune                                   // 副图名称 
	Function_on int                                   // 是否开启 0 不开启 1 开启
	Recommend int                                     // 是否开启推荐 0 不开启 1 开启
	Call int                                          // 支持开启弹窗提醒 0 不开启 1 开启
	Push int                                          // 支持开启推送提醒 0 不开启 1 开启
	Open_type int                                     // 时间类型 1 全天开放 2 限时开放
	Open_in_week []int                                // 开放周次 限时开放时使用 （例）2|4
	Open_in_day []int                                 // 开放时间 限时开放时使用 （例 00:00 - 23:59） 0|0|23|59
	Reset_type int                                    // 重置次数类型 1 每天 2 每周
	Level_min int                                     // 最低等级限制 
	Player_min int                                    // 最低组队玩家数量 
	Active_value int                                  // 活跃度奖励 完成每轮任务奖励的活跃度
	Rounds_max int                                    // 轮次数上限 
	Times_max int                                     // 环次数上限 总=环×轮
	Drop_rounds []int                                 // 每轮掉落奖励 计算方式|掉落包id （掉落计算：0概率；1权值）
	Drop_times []int                                  // 每环掉落奖励 计算方式|掉落包id （掉落计算：0概率；1权值）
	Drop_display []int                                // 奖励显示 
	Scene_id []int                                    // 场景id 活动涉及的所有场景id
	Quest_id int                                      // 记录任务id 记录活跃度的任务id
	
}

type activityTable struct {
	keys  []int
	table map[int]*activityRow
}

var ActivityTable *activityTable

func (t *activityTable) GetRow(id int) *activityRow {
	row, ok := t.table[id]
	if !ok {
		return nil
	}
	return row
}

func (t *activityTable) HasRow(id int) bool {
	_, ok := t.table[id]
	return ok
}

func (t *activityTable) Keys() []int {
	return t.keys
}

func (t *activityTable) Table() map[int]*activityRow {
	return t.table
}

func (t *activityTable) Load() {
	data, err := ioutil.ReadFile("./Activity.json")
	if err != nil {
		return
	}
	err = json.Unmarshal(data, &t.table)
	if err != nil {
		fmt.Println("read table Activity error, ", err.Error())
		return
	}
	for k, _ := range t.table {
		t.keys = append(t.keys, k)
	}
}

func (t *activityTable) Reload() {
	t.keys = make([]int, 0)
	t.table = make(map[int]*activityRow)
	t.Load()
}

func init() {
	ActivityTable = new(activityTable)
	ActivityTable.Load()
}
