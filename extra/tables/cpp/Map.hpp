#pragma once

#include <memory>
#include <vector>
#include <string>
#include <unordered_map>

#include "json.h"
#include "JsonConfig.h"
#include "LogUtil.h"

class MapRow
{
public:
	int id;                                           // 主键id 地图默认id
	int map_length;                                   // 名字 
	int map_width;                                    // 地图资源路径 
	float pos_x;                                      // 长度 
	float pos_z;                                      // 宽度 
	float pos_y;                                      // 默认出生点x 
	float pos_v;                                      // 默认出生点z 
	
};

class MapTable
{
	typedef std::shared_ptr<MapRow> ptr_row_type;
	typedef std::unordered_map<int, ptr_row_type> map_table_type;
	typedef std::vector<int> vec_type;	
private:
	vec_type m_keys;
	map_table_type	m_table;
public:
	static MapTable* Instance()
	{
		static MapTable instance;
		return &instance;
	}

	const MapRow* GetRow(int key)
	{
		map_table_type::iterator it = m_table.find(key);
		if (it == m_table.end())
		{
			return nullptr;
		}
		return it->second.get();
	}

	bool HasRow(int key)
	{
		return m_table.find(key) != m_table.end();
	}

	const vec_type& Keys() const
	{
		return m_keys;
	}

	const map_table_type& table() const
	{
		return m_table;
	}

	bool Load()
	{
		return LoadJson("Map.json");
	}

	bool ReLoad()
	{
		return ReLoadJson("Map.json");
	}

	bool LoadJson(const std::string& jsonFile)
	{
		std::string loadfile = std::string(TABLE_PATH).append(jsonFile.c_str());
		if (!g_pConfig->Load(loadfile.c_str()))
		{
			CLOG_ERR << "load table Map error" << CLOG_END;
			return false;
		}

		for (auto it = g_pConfig->m_Root.begin(); it != g_pConfig->m_Root.end(); ++it)
		{
			try
			{
				auto& r = (*it);
				ptr_row_type pRow(new MapRow);
				MapRow& row = *pRow;
                row.id = r["id"].asInt();
                row.map_length = r["map_length"].asInt();
                row.map_width = r["map_width"].asInt();
                row.pos_x = r["pos_x"].asFloat();
                row.pos_z = r["pos_z"].asFloat();
                row.pos_y = r["pos_y"].asFloat();
                row.pos_v = r["pos_v"].asFloat();

				m_table.emplace(row.id, pRow);
				m_keys.emplace_back(row.id);
			}
			catch (std::exception const& e)
			{
				CLOG_ERR << "read table Map error," << e.what() << ":" << (*it)["id"].asInt() << CLOG_END;
				return false;
			}
		}
		return true;
	}

	bool ReLoadJson(const std::string& jsonFile)
	{
		m_keys.clear();
		m_table.clear();
		return LoadJson(jsonFile);
	}

};