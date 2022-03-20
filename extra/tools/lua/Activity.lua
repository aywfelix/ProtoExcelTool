DataTable = DataTable or {}
local DataTable = DataTable

DataTable.Activity = DataTable.Activity or {}
local Activity = DataTable.Activity

Activity.Table = {}
Activity.Keys = {}

local cjson = require 'cjson'

local TABLE_PATH = "../tablejson/"

function Activity.LoadJson(jsonFile)
    local file = io.open(TABLE_PATH .. jsonFile)
    local content = file:read("*a")
    Activity.Table = cjson.decode(content)
    for key, _ in pairs(Activity.Table) do
        Activity.Keys[key] = true
    end
end

function Activity.Load()
    Activity.LoadJson("Activity.json")
end

function Activity.GetTable()
    return Activity.Table
end

function Activity.GetRow(key)
    return Activity.Table[key]
end

function Activity.HasRow(key)
    return Activity.Keys[key]
end

function Activity.Keys()
    return Activity.Keys
end

--------------------------------------------------------------
return Activity