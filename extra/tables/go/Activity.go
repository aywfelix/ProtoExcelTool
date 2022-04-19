package table

import (
	"encoding/json"
	"io/ioutil"
	"fmt"
)

type ActivityRow struct {
	Id int                                            // 主键id 活动id
	Tab_id int                                        // 注释 
	Open_in_week []int                                // 标签编号 活动所属标签
	
}

type activityTable struct {
	keys  []int
	table map[int]*ActivityRow
}

var ActivityTable *activityTable

func (t *activityTable) GetRow(id int) *ActivityRow {
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

func (t *activityTable) Table() map[int]*ActivityRow {
	return t.table
}

func (t *activityTable) Load() {
	data, err := ioutil.ReadFile("./Activity.json")
	if err != nil {
		fmt.Println("read table Activity error, ", err.Error())
		return
	}
	err = json.Unmarshal(data, &t.table)
	if err != nil {
		fmt.Println("json parse table Activity error, ", err.Error())
		return
	}
	for k, _ := range t.table {
		t.keys = append(t.keys, k)
	}
}

func (t *activityTable) Reload() {
	t.keys = make([]int, 0)
	t.table = make(map[int]*ActivityRow)
	t.Load()
}

func init() {
	ActivityTable = new(activityTable)
	ActivityTable.Load()
}
