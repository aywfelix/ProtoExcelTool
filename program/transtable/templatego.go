package Table

import (
	"encoding/json"
	"io/ioutil"
	"fmt"
)

type activityRow struct {
	Id int
	Open_in_week []int
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
