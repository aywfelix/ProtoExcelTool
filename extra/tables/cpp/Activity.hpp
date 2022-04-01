#pragma once

#include <memory>
#include <vector>
#include <string>
#include <unordered_map>

#include "json.h"
#include "JsonConfig.h"
#include "LogUtil.h"

class ActivityRow
{
public:
	int id;                                           // 主键id 活动id
	int tab_id;                                       // 注释 
	std::vector<int> open_in_week;                    // 标签编号 活动所属标签
	
};

class ActivityTable
{
	typedef std::shared_ptr<ActivityRow> ptr_row_type;
	typedef std::unordered_map<int, ptr_row_type> map_table_type;
	typedef std::vector<int> vec_type;	
private:
	vec_type m_keys;
	map_table_type	m_table;
public:
	static ActivityTable* Instance()
	{
		static ActivityTable instance;
		return &instance;
	}

	const ActivityRow* GetRow(int key)
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
		return LoadJson("Activity.json");
	}

	bool ReLoad()
	{
		return ReLoadJson("Activity.json");
	}

	bool LoadJson(const std::string& jsonFile)
	{
		std::string loadfile = std::string(TABLE_PATH).append(jsonFile.c_str());
		if (!g_pConfig->Load(loadfile.c_str()))
		{
			CLOG_ERR << "load table Activity error" << CLOG_END;
			return false;
		}

		for (auto it = g_pConfig->m_Root.begin(); it != g_pConfig->m_Root.end(); ++it)
		{
			try
			{
				auto& r = (*it);
				ptr_row_type pRow(new ActivityRow);
				ActivityRow& row = *pRow;
                row.id = r["id"].asInt();
                row.tab_id = r["tab_id"].asInt();

                auto end_open_in_week = r["open_in_week"].end();
				auto begin_open_in_week = r["open_in_week"].end();
				for (auto it = begin_open_in_week; it != end_open_in_week; ++it)
				{
					row.open_in_week.emplace_back(it->asInt());
				}
            
				m_table.emplace(row.id, pRow);
				m_keys.emplace_back(row.id);
			}
			catch (std::exception const& e)
			{
				CLOG_ERR << "read table Activity error," << e.what() << ":" << (*it)["id"].asInt() << CLOG_END;
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