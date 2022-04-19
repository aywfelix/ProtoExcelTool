DataTable = DataTable or {}
local DataTable = DataTable

DataTable.Map = DataTable.Map or {}
local Map = DataTable.Map

Map.Table = {}
Map.Keys = {}

local cjson = require 'cjson'

local TABLE_PATH = "../tablejson/"

function Map.LoadJson(jsonFile)
    local file = io.open(TABLE_PATH .. jsonFile)
    local content = file:read("*a")
    Map.Table = cjson.decode(content)
    for key, _ in pairs(Map.Table) do
        Map.Keys[key] = true
    end
end

function Map.Load()
    Map.LoadJson("Map.json")
end

function Map.GetTable()
    return Map.Table
end

function Map.GetRow(key)
    return Map.Table[key]
end

function Map.HasRow(key)
    return Map.Keys[key]
end

function Map.Keys()
    return Map.Keys
end

--------------------------------------------------------------
return Map