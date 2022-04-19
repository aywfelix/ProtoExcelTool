package table

import (
	"encoding/json"
	"io/ioutil"
	"fmt"
)

type MapRow struct {
	Id int                                            // 主键id 地图默认id
	Map_length int                                    // 名字 
	Map_width int                                     // 地图资源路径 
	Pos_x float32                                     // 长度 
	Pos_z float32                                     // 宽度 
	Pos_y float32                                     // 默认出生点x 
	Pos_v float32                                     // 默认出生点z 
	
}

type mapTable struct {
	keys  []int
	table map[int]*MapRow
}

var MapTable *mapTable

func (t *mapTable) GetRow(id int) *MapRow {
	row, ok := t.table[id]
	if !ok {
		return nil
	}
	return row
}

func (t *mapTable) HasRow(id int) bool {
	_, ok := t.table[id]
	return ok
}

func (t *mapTable) Keys() []int {
	return t.keys
}

func (t *mapTable) Table() map[int]*MapRow {
	return t.table
}

func (t *mapTable) Load() {
	data, err := ioutil.ReadFile("./Map.json")
	if err != nil {
		fmt.Println("read table Map error, ", err.Error())
		return
	}
	err = json.Unmarshal(data, &t.table)
	if err != nil {
		fmt.Println("json parse table Map error, ", err.Error())
		return
	}
	for k, _ := range t.table {
		t.keys = append(t.keys, k)
	}
}

func (t *mapTable) Reload() {
	t.keys = make([]int, 0)
	t.table = make(map[int]*MapRow)
	t.Load()
}

func init() {
	MapTable = new(mapTable)
	MapTable.Load()
}
