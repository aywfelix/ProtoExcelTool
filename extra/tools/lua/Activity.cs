using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;
using Newtonsoft.Json;

namespace DataTables
{
    public class ActivityRow
    {
	int id;                                           // 主键id 活动id
	string comment;                                   // 注释 
	int tab_id;                                       // 标签编号 活动所属标签
	int weight;                                       // 权重 标签列表内的显示权重
	int name_id;                                      // 名称id 活动名称id
	int describe_id;                                  // 描述文本id 
	int race_id;                                      // 是否相关种族 是否需要判断玩家种族来显示对话按钮,0表示否，1表示是
	string main_icon;                                 // 主图名称 
	string sub_icon;                                  // 副图名称 
	int function_on;                                  // 是否开启 0 不开启 1 开启
	int recommend;                                    // 是否开启推荐 0 不开启 1 开启
	int call;                                         // 支持开启弹窗提醒 0 不开启 1 开启
	int push;                                         // 支持开启推送提醒 0 不开启 1 开启
	int open_type;                                    // 时间类型 1 全天开放 2 限时开放
	List<int> open_in_week;                           // 开放周次 限时开放时使用 （例）2|4
	List<int> open_in_day;                            // 开放时间 限时开放时使用 （例 00:00 - 23:59） 0|0|23|59
	int reset_type;                                   // 重置次数类型 1 每天 2 每周
	int level_min;                                    // 最低等级限制 
	int player_min;                                   // 最低组队玩家数量 
	int active_value;                                 // 活跃度奖励 完成每轮任务奖励的活跃度
	int rounds_max;                                   // 轮次数上限 
	int times_max;                                    // 环次数上限 总=环×轮
	List<int> drop_rounds;                            // 每轮掉落奖励 计算方式|掉落包id （掉落计算：0概率；1权值）
	List<int> drop_times;                             // 每环掉落奖励 计算方式|掉落包id （掉落计算：0概率；1权值）
	List<int> drop_display;                           // 奖励显示 
	List<int> scene_id;                               // 场景id 活动涉及的所有场景id
	int quest_id;                                     // 记录任务id 记录活跃度的任务id
	
    };

    class ActivityTable
    {
        private Dictionary<int, ActivityRow> tableDic = new Dictionary<int, ActivityRow>();
        private ArrayList tableKeys = new ArrayList();

        const string TABLE_PATH = ".\\";

        private static ActivityTable instance = new ActivityTable();
        public static ActivityTable Instance()
        {
            return instance;
        }

        private string GetJson(string jsonFile)
        {
            using FileStream fsRead = new FileStream(jsonFile, FileMode.Open);
            int fsLen = (int)fsRead.Length;
            byte[] heByte = new byte[fsLen];
            fsRead.Read(heByte, 0, heByte.Length);
            return System.Text.Encoding.UTF8.GetString(heByte);
        }

        public bool GetRow(int key, out ActivityRow row)
        {
            return tableDic.TryGetValue(key, out row);
        }

        public bool HasRow(int key)
        {
            return tableDic.ContainsKey(key);
        }

        public ArrayList Keys()
        {
            return tableKeys;
        }

        public Dictionary<int, ActivityRow> Table()
        {
            return tableDic;
        }

        public bool Load()
        {
            return LoadJson("Activity.json");
        }

        public bool ReLoad()
        {
            return ReLoadJson("Activity.json");
        }

        private bool LoadJson(string jsonFile)
        {
            try
            {
                string loadFile = TABLE_PATH + jsonFile;
                string json = GetJson(loadFile);
                var tableRows = JsonConvert.DeserializeObject<List<ActivityRow>>(json);
                foreach (var row in tableRows)
                {
                    tableDic.Add(row.Id, row);
                    tableKeys.Add(row.Id);
                }
            }
            catch(Exception e)
            {
                Console.WriteLine("{0} First exception.", e.Message);
                return false;
            }
            return true;
        }

        private bool ReLoadJson(string jsonFile)
        {
            tableDic.Clear();
            tableKeys.Clear();
            return LoadJson(jsonFile);
        }
    }
}
