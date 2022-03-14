using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;
using Newtonsoft.Json;

namespace DataTables
{
    public class ActivityRow
    {
        public int Id { get; set; }                                           
        public string Comment { get; set; }
        public int[] TestArray{ get; set; }
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
